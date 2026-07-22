import csv, json, datetime as dt

BASE = "./"
HOY = dt.date(2026, 7, 21)

politica = json.load(open(BASE + "politica_prueba.json"))

def parse_bool(s): return str(s).strip().upper() == "TRUE"
def parse_date(s): return dt.datetime.strptime(s.strip(), "%Y-%m-%d").date()

cartera = list(csv.DictReader(open(BASE + "cartera_prueba.csv")))
historial = list(csv.DictReader(open(BASE + "historial_contactos.csv")))
abonos_sabana = list(csv.DictReader(open(BASE + "abonos_detalle_sabana.csv")))

print("=" * 78)
print("PASO 1 — cobro-ingesta-clasificacion: validaciones VAL-DATA-01 a 04")
print("=" * 78)

filas_validas = []
for row in cartera:
    nombre = row["deudor_nombre"]
    factura = row["factura_numero"]
    problemas = []

    # VAL-DATA-01: consistencia de saldo
    capital = float(row["monto_capital"]); iva = float(row["monto_iva"]); abonos = float(row["abonos_parciales"])
    saldo_calculado = capital + iva - abonos
    saldo_reportado = float(row["saldo_reportado"])
    if abs(saldo_calculado - saldo_reportado) > 1:
        problemas.append(f"VAL-DATA-01: saldo reportado {saldo_reportado:,.0f} != calculado {saldo_calculado:,.0f}")

    # VAL-DATA-03: coherencia de fechas
    f_emision = parse_date(row["fecha_emision"]); f_venc = parse_date(row["fecha_vencimiento"])
    if not (f_emision <= f_venc <= HOY):
        problemas.append(f"VAL-DATA-03: cronologia invalida (emision {f_emision} / vencimiento {f_venc} / hoy {HOY})")

    # VAL-DATA-02: calificacion de via procesal (titulo valor)
    acuse = parse_bool(row["acuse_recibo"]); entrega = parse_bool(row["constancia_entrega"]); reclamo = parse_bool(row["reclamacion_3_dias"])
    califica_ejecutivo = acuse and entrega and not reclamo

    if problemas:
        print(f"\n[BLOQUEADA] {nombre} / {factura}")
        for p in problemas: print(f"   - {p}")
        print("   -> accion: no se usa para calcular saldo cierto; se pregunta al usuario si usar el valor calculado o corregir el origen.")
        continue

    filas_validas.append({**row, "saldo_calculado": saldo_calculado, "califica_ejecutivo": califica_ejecutivo})
    print(f"\n[OK] {nombre} / {factura} — saldo {saldo_calculado:,.0f} — califica_ejecutivo={califica_ejecutivo}"
          + ("" if not reclamo else "  (reclamo en 3 dias => se sugiere monitorio/declarativo, no ejecutivo)"))

# VAL-DATA-04: patrones sospechosos (pagos "proyectados")
print("\n--- Deteccion de patrones sospechosos de pago (abonos con fecha repetida cada mes) ---")
dias_abono = [parse_date(a["fecha_abono"]).day for a in abonos_sabana]
if len(set(dias_abono)) == 1:
    print(f"[ALERTA] Grupo Sabana SAS: los {len(abonos_sabana)} abonos caen siempre el dia {dias_abono[0]} de cada mes "
          f"-> se marcan como 'proyectado', NO se cuentan como caja confirmada sin verificacion manual.")

print("\n" + "=" * 78)
print("PASO 2 — Clasificacion por antiguedad y por etapa (segun politica del cliente)")
print("=" * 78)

seg = politica["segmentacion_antiguedad_dias"]
def bucket(dias):
    if dias <= seg[0]: return f"0-{seg[0]}"
    if dias <= seg[1]: return f"{seg[0]+1}-{seg[1]}"
    if dias <= seg[2]: return f"{seg[1]+1}-{seg[2]}"
    return f"+{seg[2]}"

def repeticiones_estado_cuenta(nombre):
    return sum(1 for h in historial if h["deudor_nombre"] == nombre and h["tipo_mensaje"] == "estado_cuenta" and parse_bool(h["exitoso"]))

def dias_habiles_desde_requerimiento(nombre):
    reqs = [parse_date(h["fecha"]) for h in historial if h["deudor_nombre"] == nombre and h["tipo_mensaje"] == "requerimiento_formal"]
    if not reqs: return None
    f = max(reqs)
    dias = 0; cur = f
    while cur < HOY:
        cur += dt.timedelta(days=1)
        if cur.weekday() < 5: dias += 1
    return dias

tol_p = politica["tolerancia_persuasivo_a_prejuridico"]["valor"]
tol_j = politica["tolerancia_prejuridico_a_judicial"]["valor"]

resultados = []
for row in filas_validas:
    nombre = row["deudor_nombre"]; dias = int(row["dias_mora"])
    seg_b = bucket(dias)

    dias_habiles_req = dias_habiles_desde_requerimiento(nombre)
    if dias_habiles_req is not None and dias_habiles_req >= tol_j:
        etapa = "4 - JUDICIAL"
        motivo = f"requerimiento formal enviado hace {dias_habiles_req} dias habiles (tolerancia configurada: {tol_j})"
    elif repeticiones_estado_cuenta(nombre) >= tol_p:
        etapa = "3 - PREJURIDICO (requerimiento formal)"
        motivo = f"{repeticiones_estado_cuenta(nombre)} estados de cuenta enviados sin abono (tolerancia configurada: {tol_p})"
    elif dias <= seg[0]:
        etapa = "1 - PERSUASIVO (recordatorio)"
        motivo = f"{dias} dias de mora, primer contacto"
    else:
        etapa = "2 - PERSUASIVO (estado de cuenta)"
        motivo = f"{dias} dias de mora, segmento {seg_b}"

    resultados.append({"nombre": nombre, "factura": row["factura_numero"], "etapa": etapa, "motivo": motivo, "segmento": seg_b})
    print(f"\n{nombre} / {row['factura_numero']}  [segmento {seg_b}]")
    print(f"  -> Etapa: {etapa}")
    print(f"     Motivo: {motivo}")

print("\n" + "=" * 78)
print("PASO 3 — cobro-envio: motor Ley 2300 (frecuencia/horario/consentimiento) + gate")
print("=" * 78)

def contacto_hoy(nombre):
    return any(h["deudor_nombre"] == nombre and parse_date(h["fecha"]) == HOY for h in historial)

def contacto_exitoso_ultimos_7d(nombre):
    for h in historial:
        if h["deudor_nombre"] == nombre and parse_bool(h["exitoso"]):
            if 0 <= (HOY - parse_date(h["fecha"])).days < 7:
                return h["canal"]
    return None

for row in filas_validas:
    nombre = row["deudor_nombre"]
    autoriza_email = parse_bool(row["autoriza_email"]); autoriza_wa = parse_bool(row["autoriza_whatsapp"])
    print(f"\n{nombre}:")
    if contacto_hoy(nombre):
        print("  [BLOQUEADO] ya hubo un envio hoy para este deudor -> se reprograma para el siguiente dia habil (VAL-2300-02).")
        continue
    canal_reciente = contacto_exitoso_ultimos_7d(nombre)
    if canal_reciente:
        print(f"  [BLOQUEADO otros canales] contacto exitoso via {canal_reciente} en los ultimos 7 dias -> "
              f"se bloquean los demas canales para este deudor hasta la semana siguiente (VAL-2300-01).")
        continue
    canal_deseado = "whatsapp" if autoriza_wa else "email"
    if canal_deseado == "whatsapp" and not autoriza_wa:
        print("  [DESVIO] whatsapp no autorizado -> se desvia a email (si esta autorizado) y se registra el desvio.")
    else:
        print(f"  [OK] se puede enviar por {canal_deseado} respetando horario legal (L-V 7am-7pm, sab 8am-3pm, sin domingos/festivos).")

print("\n--- Gate de aprobacion (etapas 3 y 4) ---")
contacto = politica["contacto_escalamiento"]
for r in resultados:
    if r["etapa"].startswith("3"):
        print(f"\n{r['nombre']} / {r['factura']}: borrador de requerimiento formal generado por cobro-mensajes,")
        print(f"  ESTADO = bloqueado. Requiere aprobacion explicita de: {contacto['nombre']} "
              f"({contacto['correo']}) antes de poder enviarse. No se envia bajo ninguna instruccion sin esa aprobacion.")
    if r["etapa"].startswith("4"):
        print(f"\n{r['nombre']} / {r['factura']}: NO se genera ningun escrito.")
        print(f"  ALERTA -> '{r['nombre']} supero el umbral de tolerancia prejuridico->judicial ({r['motivo']}).")
        print(f"  Se recomienda contactar a: {contacto['nombre']} — Agenda: {contacto['agenda']} — "
              f"Correo: {contacto['correo']} — WhatsApp: {contacto['whatsapp']}'")

print("\n" + "=" * 78)
print("RESUMEN")
print("=" * 78)
for r in resultados:
    print(f"  {r['nombre']:30s} {r['factura']:8s} -> {r['etapa']}")
