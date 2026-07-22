# Esquema de datos y validaciones de ingesta

Basado en la matriz de reglas revisada y verificada el 28 de julio de 2026 (ver Especificacion Funcional v3, numeral 5.1 y Anexo de auditoria cruzada).

## Columnas esperadas (acepta sinonimos razonables al mapear)

**Deudor**: tipo de identificacion (CC/NIT/CE/PP), numero de identificacion, nombre o razon social, correo, telefono, y consentimiento por canal (`autoriza_email`, `autoriza_whatsapp`, `autoriza_sms` — booleanos independientes, usados por el skill `cobro-envio` para cumplir la Ley 2300 de 2023).

**Factura**: numero, fecha de emision, fecha de vencimiento, fecha de mora (si esta vacia, se autocalcula como vencimiento + 1 dia), monto capital, IVA, abonos parciales, los tres booleanos de blindaje documental (`acuse_recibo`, `constancia_entrega`, `reclamacion_3_dias`), y un campo `observaciones_excepcion` (texto libre, vacio por defecto) donde `cobro-envio` registra cuando ese caso especifico se maneja distinto al estandar de la politica del cliente — ver seccion "Excepciones caso por caso" en `cobro-envio/SKILL.md`.

## Las cuatro validaciones obligatorias

1. **Consistencia de saldo**: `saldo_insoluto = monto_capital + IVA - abonos_parciales`. Si el valor reportado en el origen no coincide, suspende esa fila y pregunta si usar el saldo calculado o corregir el origen — nunca sigas adelante con un numero que no cuadra.

2. **Coherencia de fechas**: `fecha_emision <= fecha_vencimiento <= fecha_actual`, y `fecha_mora >= fecha_vencimiento` si se reporta. Si falla, excluye la fila y senala el error de cronologia para correccion manual.

3. **Calificacion de via procesal** (Ley 1231 de 2008, art. 774 C. Co.): si `acuse_recibo` y `constancia_entrega` son verdaderos y `reclamacion_3_dias` es falso, la factura califica como titulo valor y habilita la via ejecutiva. Si no, sugiere monitorio o declarativo segun cuantia. Guarda esto como bandera `califica_ejecutivo` por factura — no bloquea la ingesta, solo informa la recomendacion de via judicial que se usaria mas adelante (fuera de este plugin, ya que la etapa judicial no genera escritos — ver skill `cobro-envio`).

4. **Patrones sospechosos**: fechas de abono que se repiten siempre el mismo dia del mes son senal de un plan de pagos proyectado, no de caja confirmada. Marca estas entradas como "proyectado" y excluyelas del saldo cierto hasta que el cliente confirme que ya se recibieron.

## Ver tambien

`references/registro-comunicaciones.md` — el registro real de comunicaciones enviadas, que complementa esta cartera para determinar la sub-etapa exacta de cada factura (0, 1a, 1b, 1c, 2 o 3).

## Por que estas reglas y no otras

Nacen de un caso real (IMC / Ambiente Solar, ver Especificacion Funcional v3) donde un bloque de abonos "proyectados" casi se contabiliza dos veces, y donde la calificacion de titulo valor determino la via procesal recomendada. No son teoricas — cada una previno un error real detectado en ese caso.
