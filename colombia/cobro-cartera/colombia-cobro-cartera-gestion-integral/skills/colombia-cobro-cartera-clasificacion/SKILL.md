---
name: colombia-cobro-cartera-clasificacion
description: Lee la cartera de facturas del cliente desde su hoja de calculo, archivo CSV/Excel o carpeta conectada, valida la consistencia de los datos (saldos, fechas, soporte de titulo valor), y clasifica cada factura por antiguedad y por sub-etapa exacta de cobro (preventiva, recordatorio, estado de cuenta, carta formal de cobro, prejuridico, judicial) segun la politica ya configurada y el registro real de comunicaciones enviadas. Se activa con "revisa mi cartera", "clasifica las facturas vencidas", "actualiza el estado de mora", "que facturas estan en riesgo", "cuales facturas califican para ejecutivo".
---

# Ingesta, validacion y clasificacion de cartera

## Paso 0 — Verificar politica

Antes de leer ninguna cartera, confirma que existe la politica del cliente (manual + archivo tecnico, ver `colombia-cobro-cartera-politica`). Si no existe, invoca el skill `colombia-cobro-cartera-politica` en su lugar y no continues.

## Paso 1 — Leer la cartera

Lee el archivo de cartera conectado del cliente — puede ser un Google Sheet, un archivo Excel/CSV en Drive o almacenamiento equivalente, u otra fuente estructurada disponible via la herramienta de archivos del agente. Mapea las columnas de forma flexible aceptando sinonimos razonables (ej. "saldo pendiente" = `saldo_insoluto`), pero valida internamente contra el esquema de `references/validaciones-datos.md`.

## Paso 2 — Validar cada fila antes de calcular nada

Ejecuta, para cada factura, las cuatro validaciones documentadas en `references/validaciones-datos.md` (consistencia de saldo, coherencia de fechas, calificacion de via procesal, patrones sospechosos de pago). Si una fila falla una validacion, no la uses para calcular el saldo cierto del deudor — señala el problema en lenguaje natural y pregunta como proceder (usar el valor calculado o pedir correccion en el origen).

## Paso 3 — Leer el registro real de comunicaciones

Antes de clasificar, lee el registro de comunicaciones efectivamente enviadas por factura/deudor (lo mantiene `colombia-cobro-cartera-envio` cada vez que algo sale — ver ese SKILL.md). Este registro es la fuente de verdad de lo que realmente paso, no lo que la politica hubiera indicado en teoria. Si el registro no existe todavia para este cliente, trátalo como vacio (ningun contacto previo) y avisa que se va a crear a partir de ahora.

## Paso 4 — Clasificar por antiguedad y por sub-etapa exacta

Para cada factura individual (nunca solo por el saldo consolidado del deudor):

1. Calcula los dias hasta el vencimiento (si aun no vence) o los dias de mora (si ya vencio).
2. Ubica la factura en el segmento de antiguedad de la politica del cliente.
3. Compara el registro real de comunicaciones contra los umbrales de tolerancia de la politica para determinar la sub-etapa exacta: **0 preventiva** (aun no vence, o vencio hace muy poco), **1a recordatorio**, **1b estado de cuenta**, **1c carta formal de cobro**, **2 prejuridico**, o **3 judicial**.
4. Si una factura acaba de cruzar el umbral hacia una sub-etapa distinta (especialmente hacia 1c, 2 o 3), marcala explicitamente como "lista para transicion" — esto es lo que el skill `colombia-cobro-cartera-envio` usa para avisar al usuario y proponer programar la siguiente tanda de comunicaciones, en vez de actuar en silencio.
5. Si el campo `observaciones_excepcion` de una factura ya tiene una nota registrada por `colombia-cobro-cartera-envio`, respeta esa excepcion — no reclasifiques automaticamente ese caso al estandar general sin confirmar primero con el usuario.

## Paso 5 — Actualizar el registro

Escribe los resultados (dias de mora o dias al vencimiento, sub-etapa exacta, bandera `califica_ejecutivo`, alertas de anomalias) de vuelta en una pestaña o archivo junto a la cartera del cliente — nunca en un almacenamiento separado o centralizado.

## Anti-patrones

- Nunca calcules o comuniques una cifra de saldo sin haber corrido las cuatro validaciones primero.
- Nunca clasifiques solo por el saldo agregado del deudor — cada factura es un titulo valor independiente con su propio requisito de entrega, aceptacion y mora.
- Nunca clasifiques la sub-etapa de un caso solo por dias de mora sin revisar tambien el registro real de comunicaciones — la politica define umbrales, pero lo que realmente paso puede diferir (ej. un caso retomado con una excepcion).
- Nunca trates un pago "proyectado" (fechas repetidas siempre el mismo dia del mes) como caja confirmada sin advertirlo.
- Nunca leas ni compares datos de cartera de un cliente con los de otro.
