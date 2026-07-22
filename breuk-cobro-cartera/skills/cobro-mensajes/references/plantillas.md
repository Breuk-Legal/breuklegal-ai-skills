# Plantillas verificadas por etapa

Variables entre llaves se llenan con los datos del deudor/factura clasificados por `cobro-ingesta-clasificacion`. El modelo de etapas de este plugin, de menor a mayor formalidad:

- **Etapa 0 — Cobranza preventiva** (antes de que exista mora): recordatorio de vencimiento. Sin abogado.
- **Etapa 1 — Cobro persuasivo o administrativo** (mora temprana, sin abogado, lo maneja la empresa): sub-pasos de formalidad creciente — (1a) recordatorio amistoso, (1b) estado de cuenta, (1c) **carta formal de cobro** (el paso mas fuerte de esta etapa, ya cita mora e intereses, pero sigue sin abogado).
- **Etapa 2 — Cobro prejuridico** (instancia legal, interviene un abogado): **requerimiento formal de pago**.
- **Etapa 3 — Cobro judicial** (instancia legal, ultima instancia): no existe plantilla, solo alerta (ver `cobro-envio`).

No confundir la carta formal de cobro (etapa 1c, administrativa, sin abogado) con el requerimiento formal de pago (etapa 2, prejuridica, con abogado) — son dos documentos distintos, con distinto nivel de formalidad y distinto responsable.

## 0. Recordatorio de vencimiento (etapa preventiva)

```
Asunto: Tu factura {numero_factura} vence pronto — {empresa_cliente}

Hola {nombre_deudor},

Te recordamos que la factura {numero_factura} por {monto_factura} vence el
{fecha_vencimiento}. Si ya programaste el pago, ignora este mensaje.

Un saludo,
{empresa_cliente}
```

Tono suave, informativo, nunca insistente. Se envia antes del vencimiento (por defecto 5 y 3 dias antes, ajustable en la politica). Si la politica del cliente incluye un enlace o canal de pago autorizado, inclúyelo aqui para reducir friccion — solo si el cliente lo definio explicitamente, nunca inventes un canal de pago.

## 1a. Recordatorio amistoso (etapa persuasiva/administrativa)

```
Asunto: Recordatorio de pago pendiente — {empresa_cliente}

Hola {nombre_deudor},

Te escribimos de parte de {empresa_cliente} para recordarte que la factura
{numero_factura} por {monto_pendiente} sigue pendiente de pago.

Si ya realizaste el pago, ignora este mensaje. Si necesitas apoyo para
coordinarlo, cuentanos y vemos como ayudarte.

Un saludo,
{empresa_cliente}
```

No incluir preguntas sobre el motivo del atraso. No incluir fundamento legal. Tono cordial en todo momento.

## 1b. Estado de cuenta (etapa persuasiva/administrativa)

```
Asunto: Estado de cuenta — {empresa_cliente}

Hola {nombre_deudor},

Te compartimos el estado de cuenta actualizado a la fecha:

Factura {numero_factura} — Emitida: {fecha_emision} — Vencida: {fecha_vencimiento}
Valor: {monto_factura} — Abonado: {monto_abonado} — Saldo: {saldo_pendiente}

Quedamos atentos a cualquier duda sobre este detalle.

Un saludo,
{empresa_cliente}
```

Siempre por factura individual — si hay varias facturas pendientes, listarlas todas por separado, nunca solo el saldo consolidado.

## 1c. Carta formal de cobro (etapa persuasiva/administrativa — el paso mas fuerte, sin abogado)

```
Asunto: Carta formal de cobro — {empresa_cliente}

Senores
{nombre_deudor}

Por medio de la presente, {empresa_cliente} le informa formalmente que la
factura {numero_factura}, por valor de {saldo_pendiente}, se encuentra
vencida desde el {fecha_vencimiento} y continua pendiente de pago pese a
los recordatorios previos.

Esta obligacion se encuentra en mora en los terminos del articulo 1608 del
Codigo Civil, lo que puede dar lugar a intereses moratorios conforme al
articulo 884 del Codigo de Comercio.

Le solicitamos regularizar esta obligacion dentro de los {plazo_carta_formal}
dias siguientes al recibo de esta comunicacion. De no recibir el pago o una
propuesta de acuerdo dentro de ese plazo, {empresa_cliente} dara inicio a
la gestion de cobro prejuridico de esta obligacion.

Cordialmente,
{empresa_cliente}
```

Esta carta la redacta y (segun la politica) envia la empresa directamente, sin que intervenga un abogado — es distinta del requerimiento formal de pago de la etapa 2. Requiere revision la primera vez que se usa con cada deudor (ver `cobro-envio`), aunque no sea la revision de un abogado. El `plazo_carta_formal` lo define el usuario en su politica (sugerido 10-15 dias calendario); al vencer sin pago ni acuerdo, el caso pasa a cobro prejuridico.

## 2. Requerimiento formal de pago (etapa prejuridica — instancia legal, con abogado)

```
Asunto: Requerimiento formal de pago — {empresa_cliente}

Senores
{nombre_deudor}

Por medio de la presente, {empresa_cliente} requiere formalmente el pago de
la factura {numero_factura}, por valor de {saldo_pendiente}, vencida desde
el {fecha_vencimiento}.

Este requerimiento se formula con fundamento en el articulo 1608 del Codigo
Civil, que establece la mora del deudor, y en el articulo 884 del Codigo de
Comercio, que regula el interes bancario corriente aplicable en caso de
causarse intereses moratorios.

Se solicita el pago dentro de los diez (10) dias habiles siguientes al
recibo de esta comunicacion. Vencido este plazo sin que se verifique el
pago, se procedera a evaluar las acciones legales correspondientes.

Cordialmente,
{contacto_escalamiento_nombre}
```

Este borrador queda bloqueado hasta la aprobacion del contacto de escalamiento (abogado) configurado en la politica del cliente (ver skill `cobro-envio`). El plazo de 10 dias habiles es el valor sugerido por defecto — ajustable en la politica del cliente si asi lo definio.

## Nota sobre la etapa judicial

No existe una plantilla de etapa 3 (judicial). Cuando una factura cruza el umbral de prejuridico a judicial, el skill `cobro-envio` genera unicamente una alerta de escalamiento — nunca un escrito, demanda o comunicacion redactada por este skill.
