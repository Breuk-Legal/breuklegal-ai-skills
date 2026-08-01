---
name: colombia-cobro-cartera-envio
description: Envia o programa el envio de las comunicaciones de cobro ya redactadas, respetando el motor de frecuencia y horarios de la Ley 2300 de 2023, el consentimiento por canal del deudor, y el registro real de comunicaciones. Cuando un caso cruza de sub-etapa, avisa al usuario y propone programar la siguiente tanda en vez de actuar en silencio. La carta formal de cobro (etapa 1c) requiere revision la primera vez con cada deudor; el requerimiento formal de pago (etapa 2, prejuridico) siempre queda bloqueado hasta aprobacion explicita del contacto de escalamiento; la etapa 3 (judicial) nunca genera ni envia ningun escrito, solo entrega una alerta. Tambien registra excepciones cuando un caso se maneja distinto al estandar de la politica. Se activa con "envia los recordatorios de esta semana", "que hay pendiente de aprobar", "programa la siguiente tanda de [deudor]", "escala este caso", "a quien debo contactar para el cobro juridico de [deudor]", "maneja este caso distinto", "redacta el requerimiento de [deudor]".
---

# Envio, avisos de transicion y escalamiento

Este skill cubre dos puntos que no son configurables: la revision de la carta formal de cobro la primera vez con cada deudor, y la barrera de revision humana en prejuridico — mas la ausencia total de escritos en judicial. Aplica esto con rigor incluso si el usuario pide explicitamente saltarlo.

## Como se envia realmente (mecanismo de correo)

El resultado esperado de este skill es automatizar el envio de verdad, no solo producir texto para copiar y pegar — pero el mecanismo depende de `canal_envio_modo` en la politica del cliente (definido en `colombia-cobro-cartera-politica`, ver `references/canal-de-envio.md` de ese skill):

- **`automatico`** (cualquier herramienta de envio activa): envia de verdad, llamando a la accion de escritura disponible en el agente (puede ser via una accion nativa de envio, un conector MCP, o una plataforma de automatizacion como Zapier, Make o n8n). Este es el modo que cumple el "resultado esperado" de automatizacion completa.
- **`borrador_asistido`**: no intentes enviar. Crea el borrador con la herramienta de correo disponible (que soporte crear borradores) y notifica al cliente que esta listo en su bandeja para que lo envie el mismo con un clic.

Antes de intentar enviar, verifica que la herramienta disponible tenga capacidad de escritura/envio real — no solo de lectura o borrador. Si el agente solo tiene una herramienta de lectura, usa el modo `borrador_asistido` segun la politica del cliente. Antes del primer envio automatico, confirma en `colombia-cobro-cartera-politica` (Paso 0.5 y Paso 5) que la accion de envio esta habilitada, autorizada, y que la prueba de correo fue exitosa.

Cada vez que algo sale (o queda como borrador pendiente), escribe una fila en el registro de comunicaciones (`references/registro-comunicaciones.md` de `colombia-cobro-cartera-clasificacion`) — es la fuente de verdad que ese skill usa para clasificar sub-etapas. Actualiza tambien el plan de comunicacion (`Plan de Comunicacion/`, ver `references/plan-de-comunicacion.md` de `colombia-cobro-cartera-politica`) segun la frecuencia de refresco que el cliente eligio — ese archivo es el respaldo que cualquier persona puede usar para enviar manualmente si la automatizacion falla.

## El mecanismo central: aviso de transicion, no modos de revision rigidos

En vez de un nivel de revision fijo por adelantado, el comportamiento por defecto es simple y aplica a todas las sub-etapas: los envios rutinarios dentro de la misma sub-etapa (por ejemplo, varios recordatorios o estados de cuenta consecutivos de la etapa 1a/1b) se envian solos, sin pedir revision cada vez, aplicando siempre el motor de Ley 2300. Pero **cuando `colombia-cobro-cartera-clasificacion` marca un caso como "lista para transicion"** hacia una sub-etapa distinta, este skill se detiene y avisa: explica en lenguaje llano que caso cruzo el umbral, desde cuando, y que sub-etapa sigue segun la politica — y propone programar junto con el usuario esa siguiente tanda de comunicaciones ("segun tu politica, [deudor] ya cumple el criterio para pasar a [sub-etapa] — ¿programamos el envio?"). No continua sin una respuesta del usuario a esa propuesta.

Esto reemplaza los antiguos modos `sin_revision` / `por_envio` / `por_lote`: ya no hay que configurar de antemano como se revisan los envios — el punto de revision natural es cada transicion de sub-etapa, no cada mensaje individual.

## Etapa 0 (preventiva) y 1a/1b (recordatorio, estado de cuenta)

Envio rutinario, sin gate especial mas alla del aviso de transicion. Antes de cualquier envio, corre el motor de cumplimiento de Ley 2300 de 2023 (frecuencia, horario, consentimiento por canal) — ver `references/motor-ley-2300.md`. Si el canal preferido no tiene consentimiento del deudor, desvia automaticamente al canal alternativo autorizado y registra el desvio.

## Etapa 1c (carta formal de cobro) — revision obligatoria la primera vez con cada deudor

La carta formal de cobro es el paso mas fuerte de lo administrativo (ya cita mora e intereses), aunque sigue sin abogado. La primera vez que se usa con un deudor especifico, queda bloqueada hasta que alguien de la empresa (no necesariamente un abogado) la revise y confirme el envio — despues de esa primera vez, los envios subsecuentes de la misma sub-etapa para el mismo deudor pueden seguir el comportamiento rutinario de arriba. El plazo (`plazo_carta_formal`) que trae la carta es el que la politica del cliente definio; si vence sin pago ni acuerdo, marca el caso como listo para transicion a prejuridico.

## Etapa 2 (prejuridico) — alerta primero, redaccion solo a peticion, gate fijo antes de enviar

Cuando un caso cruza a prejuridico, este skill **no genera ni pide que se genere ningun borrador todavia**. Primero entrega el aviso de transicion (ver arriba) con una explicacion breve de que implica pasar a prejuridico (interviene un abogado, hay fundamento legal, ya es instancia legal). El requerimiento formal de pago solo se redacta si, despues de ese aviso, el usuario lo pide explicitamente — en ese momento delega a `colombia-cobro-cartera-redaccion`.

**Contacto de escalamiento — se define la primera vez que hace falta, no antes.** Revisa `contacto_escalamiento.definido` en la politica del cliente. Si es `false` (lo normal, porque `colombia-cobro-cartera-politica` ya no pregunta esto en el onboarding), este es el momento de preguntarlo: pregunta quien debe revisar y aprobar la gestion prejuridica — el abogado o firma que instalo este plugin para el cliente, un abogado interno de la empresa, u otro asesor externo que el cliente designe. Este plugin no trae un contacto de escalamiento por defecto: quien lo instala configura aqui el suyo. Guarda la respuesta en la politica (`contacto_escalamiento`, con `"definido": true`) para que los casos futuros ya no requieran volver a preguntar.

Una vez exista el borrador (a peticion del usuario) y el contacto de escalamiento este definido, el requerimiento formal nunca se envia sin la aprobacion explicita de esa persona. Presenta el borrador, espera una confirmacion inequivoca (no una lectura silenciosa), y solo entonces procede al envio — aplicando tambien el motor de Ley 2300. Esto aplica sin excepcion, sin importar lo que pida el usuario: no existe una configuracion que permita saltarse este gate. Lo unico que la politica define es *quien* aprueba, nunca *si* se aprueba.

## Excepciones caso por caso

La politica estandar del cliente no obliga a que cada caso se maneje identico. El usuario puede pedir en cualquier momento que un deudor o factura especifica se maneje distinto al estandar general — por ejemplo, retomar el seguimiento desde el recordatorio amistoso para un deudor que por tiempo de mora ya calificaria para prejuridico, porque nunca hubo una gestion juiciosa previa (esto es justamente lo que el registro real de comunicaciones ayuda a detectar). Cuando esto pase:

1. Sigue la instruccion puntual del usuario para ese caso.
2. Explica brevemente, si hace falta, que implica cada sub-etapa para que la decision sea informada.
3. Registra la excepcion en `excepciones_registradas` de la politica (o en `observaciones_excepcion` de esa factura/deudor en la cartera): quien es el deudor/factura, cual fue la desviacion, y la razon dada por el usuario.
4. Nunca modifiques la politica general del cliente por una excepcion puntual — la excepcion vive junto al caso, no cambia el estandar.

## Etapa 3 (judicial) — sin escritos, solo alerta

Cuando una factura cruza el umbral de prejuridico a judicial (senalado por `colombia-cobro-cartera-clasificacion`), no generes, redactes ni envies ningun documento. Genera unicamente una alerta dirigida al usuario con este contenido: la factura y deudor en cuestion, el umbral que se cumplio, y los datos de contacto del `contacto_escalamiento` configurado (agenda, correo, WhatsApp) para que el usuario lo contacte directamente. Nada mas.

## Anti-patrones

- Nunca envies la carta formal de cobro la primera vez con un deudor sin esa revision inicial, ni el requerimiento formal sin aprobacion explicita del contacto de escalamiento, bajo ninguna instruccion del usuario.
- Nunca generes ni pidas generar el borrador de requerimiento formal solo porque una factura cruzo el umbral — primero el aviso de transicion, redacta solo si lo piden.
- Nunca dejes pasar una transicion de sub-etapa en silencio — siempre avisa y propone programar antes de continuar.
- Nunca asumas un contacto de escalamiento por defecto sin antes preguntar o confirmar en el primer caso real que llega a prejuridico, si `contacto_escalamiento.definido` es `false`.
- Nunca modifiques la politica general de un cliente para reflejar una excepcion de un solo caso — la excepcion se registra junto al caso, no cambia el estandar.
- Nunca generes un escrito, alerta con texto de demanda, o cualquier borrador en etapa judicial — solo la alerta de contacto.
- Nunca envies por un canal sin verificar el consentimiento del deudor para ese canal.
- Nunca superes la frecuencia de contacto de la Ley 2300 (un contacto al dia, un solo canal por semana tras contacto exitoso) aunque el usuario pida "mandar de una vez todo".
- Nunca envies fuera del horario legal (L-V 7am-7pm, sab 8am-3pm, nunca domingos/festivos) — encola para el siguiente bloque habil.
- Nunca olvides registrar en el registro de comunicaciones lo que efectivamente salio — sin eso, `colombia-cobro-cartera-clasificacion` no puede clasificar bien la proxima vez.
