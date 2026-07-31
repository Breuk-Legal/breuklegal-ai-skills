# Registro de comunicaciones enviadas

Es la fuente de verdad de lo que realmente paso con cada factura/deudor — no una copia de lo que la politica hubiera indicado en teoria. Vive junto a la cartera del cliente (misma carpeta), en una pestaña o archivo separado de la cartera misma (ej. `registro-comunicaciones-[cliente]`).

`cobro-envio` escribe una fila cada vez que algo sale de verdad (o queda como borrador pendiente); `cobro-ingesta-clasificacion` lo lee para clasificar.

## Columnas

| Campo | Contenido |
|---|---|
| `factura` / `deudor` | Identifica el caso. |
| `sub_etapa` | 0, 1a, 1b, 1c, 2 o 3 — la sub-etapa de la comunicacion. |
| `fecha_envio` | Cuando se envio (o se dejo el borrador, si aplica). |
| `canal` | gmail, outlook, whatsapp, etc. |
| `estado` | `enviado`, `borrador_pendiente`, `bloqueado_esperando_aprobacion`. |
| `aprobado_por` | Quien aprobo, si aplica (etapa 1c o 2). |
| `resultado` | Opcional: si hubo respuesta, promesa de pago, o silencio. |

## Por que existe

Antes de este registro, la clasificacion de etapa dependia de asumir que la politica se habia cumplido al pie de la letra. En la practica eso no siempre es cierto — un cliente puede tener meses de mora sin gestion real previa. Este registro permite que el asistente proponga, en el momento en que un caso cruza de sub-etapa, programar junto con el usuario la siguiente tanda de comunicaciones — en vez de asumir que ya se hizo o de enviarla en automatico sin avisar.
