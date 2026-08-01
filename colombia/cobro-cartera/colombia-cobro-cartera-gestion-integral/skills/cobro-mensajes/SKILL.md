---
name: cobro-mensajes
description: Redacta el borrador de la comunicacion de cobro correspondiente a la etapa de una factura o deudor especifico (recordatorio de vencimiento, recordatorio amistoso, estado de cuenta, carta formal de cobro, o requerimiento formal de pago), usando plantillas ya verificadas y aplicando las restricciones de la Ley 2300 de 2023 y la Circular Externa 048 de 2008. Se activa con "redacta el recordatorio para [deudor]", "prepara el estado de cuenta de [deudor]", "genera la carta formal de cobro de [deudor]", "genera el requerimiento formal de [factura]", "escribeme el mensaje de cobro para [deudor]".
---

# Redaccion de comunicaciones de cobro

## El modelo de etapas de este plugin

- **Etapa 0 — Preventiva** (antes de la mora): recordatorio de vencimiento.
- **Etapa 1 — Persuasivo/administrativo** (mora temprana, sin abogado): 1a recordatorio amistoso, 1b estado de cuenta, 1c **carta formal de cobro** (el paso mas fuerte de esta etapa, sin abogado).
- **Etapa 2 — Prejuridico** (instancia legal, con abogado): **requerimiento formal de pago**.
- **Etapa 3 — Judicial** (instancia legal, ultima instancia): sin plantilla, solo alerta.

La carta formal de cobro (1c) y el requerimiento formal de pago (2) son documentos distintos — no los confundas. La carta formal la redacta y envia la empresa sola; el requerimiento formal requiere abogado.

## Antes de redactar

Confirma que existe politica del cliente (si no, invoca `cobro-setup`) y que la factura/deudor ya fue clasificado por `cobro-ingesta-clasificacion` en una sub-etapa especifica. Este skill **solo redacta para las etapas 0, 1 y 2**. No existe plantilla de etapa 3 (judicial): si la factura ya esta ahi, no redactes nada — remite al skill `cobro-envio`, que se encarga de la alerta de escalamiento sin generar ningun escrito.

**El requerimiento formal de pago (etapa 2) nunca se redacta de forma proactiva.** Que una factura haya cruzado el umbral hacia prejuridico no es, por si solo, motivo para generar el borrador — eso lo detecta y alerta `cobro-envio`, sin escribir nada todavia. Este skill solo redacta el requerimiento formal cuando el usuario (una persona, no una tarea programada) lo pide explicitamente para ese caso. Cuando lo pida, redacta el borrador con normalidad, pero antes de entregarlo recuerda brevemente que sigue sujeto a revision y aprobacion del contacto de escalamiento antes de poder enviarse, y que la responsabilidad de decidir enviarlo es de quien lo aprueba.

La carta formal de cobro (etapa 1c) si puede redactarse cuando el caso llega a esa sub-etapa (no requiere la misma espera que el requerimiento formal), pero recuerda que `cobro-envio` exige una revision la primera vez que se usa con cada deudor antes de enviarla, aunque no sea revision de un abogado.

## Las plantillas (ver `references/plantillas.md` para el texto base)

0. **Recordatorio de vencimiento** (etapa preventiva): tono suave, informativo, antes de que exista mora. Solo incluye un enlace o canal de pago si el cliente lo definio explicitamente en su politica — nunca inventes uno.

1a. **Recordatorio amistoso** (etapa persuasiva): tono cordial, sin fundamento legal, sin indagar el motivo del impago bajo ninguna circunstancia (Ley 2300 de 2023) — nunca redactes frases como "cuentanos por que no has podido pagar"; limitate a informar el estado y ofrecer alternativas de pago.

1b. **Estado de cuenta** (etapa persuasiva): tono neutral e informativo, por factura individual, nunca solo el saldo consolidado.

1c. **Carta formal de cobro** (etapa administrativa, el paso mas fuerte, sin abogado): ya cita mora (art. 1608 C.C.) e intereses (art. 884 C.Co.), pero la sigue enviando la empresa. Incluye el plazo (`plazo_carta_formal`) que el cliente definio en su politica, y advierte que vencido ese plazo sin pago ni acuerdo se inicia cobro prejuridico.

2. **Requerimiento formal de pago** (etapa prejuridica, con abogado): tono formal, cita explicitamente el art. 1608 del Codigo Civil (mora) y el art. 884 del Codigo de Comercio (interes bancario corriente). No incluyas una reserva de derechos por defecto — si la contraparte necesita pedir una aclaracion o correccion, que lo haga ella; no se ofrece preventivamente en el texto. Antes de incluir cualquier cobro de gastos de cobranza, verifica en la politica del cliente que exista una gestion de cobranza real y documentada (Circular 048 de 2008) — si no existe, redacta el borrador sin ese rubro y señalalo como pendiente.

## Despues de redactar

Todo borrador queda marcado con estado `revisado_y_aprobado: no`. La carta formal de cobro (1c) y el requerimiento formal de pago (2) quedan ademas bloqueados hasta la revision que corresponda (ver skill `cobro-envio`) — esto lo hace cumplir `cobro-envio`, no este skill. Este skill nunca envia nada por si mismo.

## Anti-patrones

- Nunca redactes una plantilla de etapa judicial — esa etapa no genera escritos en este plugin.
- Nunca confundas la carta formal de cobro (administrativa, sin abogado) con el requerimiento formal de pago (prejuridica, con abogado) — son documentos distintos con distinto responsable.
- Nunca redactes el requerimiento formal de forma automatica solo porque una factura cruzo el umbral de prejuridico — espera a que el usuario lo pida expresamente para ese caso.
- Nunca inventes una cita normativa que no este en `references/marco-normativo.md` (skill `cobro-consulta-normativa`).
- Nunca incluyas gastos de cobranza sin la gestion real documentada que exige la Circular 048 de 2008.
- Nunca menciones una reserva de derechos por defecto en ninguna plantilla.
- Nunca inventes un canal o enlace de pago en el recordatorio preventivo — solo si el cliente lo definio en su politica.
- Nunca uses lenguaje amenazante o un tono mas firme del que corresponde a la etapa.
