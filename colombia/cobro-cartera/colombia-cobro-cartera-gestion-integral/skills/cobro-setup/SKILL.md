---
name: cobro-setup
description: Sesion de consultoria que configura o actualiza la politica de cobro de un cliente — explica el estandar de cada etapa y transicion (preventiva, persuasivo/administrativo con sus sub-pasos, prejuridico, judicial) y pregunta si la empresa lo adopta tal cual o necesita plazos distintos, captura el tono de comunicacion (descripcion + ejemplos), organiza la carpeta de trabajo, y deja canales, revision y automatizacion configurados. Se activa con "instalar el asistente de cobro", "configurar mis politicas de cobro", "ayudame a configurar este asistente", "cambiar mis umbrales de mora", "actualizar mi politica de cobro", "quien revisa mis requerimientos". Tambien se invoca automaticamente desde cualquier otro skill de este plugin (cobro-ingesta-clasificacion, cobro-mensajes, cobro-envio) cuando no encuentra un archivo de politica ya configurado para el cliente actual.
---

# Configuracion de la politica de cobro: sesion de consultoria

Este skill es la puerta de entrada del plugin. No es un formulario — es una sesion breve de asesoria: el agente explica el estandar de cada etapa y pregunta si aplica tal cual o si la empresa necesita algo distinto, en vez de simplemente recolectar valores. Es lo primero que corre con un cliente nuevo, y a lo que cualquier otro skill de este plugin redirige si no encuentra politica configurada.

Recomienda al usuario, si no lo ha hecho ya, usar este asistente en un entorno que soporte herramientas de accion (conectores de hojas de calculo, correo y automatizacion), no en un chat de solo texto. La mayoria de las plataformas de IA con MCP, plugins o conectores nativos cumplen este requisito. Menciona esto una vez, sin insistir, en el Paso 0.

## El modelo de etapas que se explica en esta consultoria

- **Etapa 0 — Preventiva** (antes de la mora): recordatorio de vencimiento.
- **Etapa 1 — Persuasivo/administrativo** (mora temprana, sin abogado, lo maneja la empresa): 1a recordatorio amistoso, 1b estado de cuenta, 1c carta formal de cobro (el paso mas fuerte, sin abogado).
- **Etapa 2 — Prejuridico** (instancia legal, con abogado): requerimiento formal de pago.
- **Etapa 3 — Judicial** (instancia legal, ultima instancia): sin escritos, solo alerta de contacto.

La carta formal de cobro (1c) y el requerimiento formal de pago (2) son documentos distintos — no los confundas al hablar con el cliente.

## Paso 0 — Bienvenida y contexto (solo la primera vez, cliente nuevo)

Si no existe ninguna politica para este cliente, abre con una explicacion breve en lenguaje llano, sin jerga tecnica ni nombres de skills o archivos, antes de preguntar nada. Cubre estas ideas en un par de parrafos cortos:

- El cobro de cartera pasa por cuatro momentos: antes de que exista mora (recordar el vencimiento), la gestion propia de la empresa sin abogado (recordatorios, estados de cuenta, y una carta formal de cobro como ultimo paso administrativo), el cobro prejuridico (ya interviene un abogado, es instancia legal), y solo como ultima instancia una accion judicial.
- Esta va a ser una conversacion de asesoria, no un formulario: en cada transicion entre etapas te voy a explicar cual es el estandar recomendado y por que, y vas a decidir si lo dejamos asi o si tu empresa necesita algo distinto.
- Al final queda todo guardado (politica en Word/PDF + el archivo tecnico), probado, y con la carpeta de trabajo organizada.

## Paso 0.5 — Verificar y conectar los conectores necesarios

Antes de la consultoria, confirma que estan conectados: (a) Google Sheets/Drive, y (b) al menos un conector de correo (Gmail u Outlook/Microsoft 365). Si falta alguno, busca el conector en el registro y muestra la tarjeta de "Conectar" directamente en la conversacion (no le pidas al usuario que vaya a buscarla a otro lado).

**El envio real de correos es un tema aparte de solo "tener un conector de correo conectado".** Muchos agentes de IA tienen herramientas de lectura de correo pero no de envio. Antes de configurar cualquier flujo automatizado, verifica que capacidad de envio tiene el agente disponible en el entorno donde corre (ver `references/canal-de-envio.md`). Presenta al cliente las opciones disponibles, empujando activamente hacia la primera si existe capacidad de envio real:

1. **Envio automatizado (recomendado si esta disponible).** Verifica si el agente tiene una herramienta de escritura/envio activa — puede ser una accion nativa, un conector MCP, o una integracion con una plataforma de automatizacion (Zapier, Make, n8n, u otra disponible). Explica en una frase por que es mejor: permite que el asistente envie de verdad, no solo redacte. Si se requiere una plataforma de automatizacion adicional, guia al cliente para conectarla y habilitar la accion de envio del proveedor de correo (Gmail, Outlook, u otro). Confirma que la accion de envio funciona antes de continuar.
2. **Modo borrador asistido (sin envio automatico).** Si no hay herramienta de envio disponible o el cliente prefiere no activarla, acepta esa decision sin insistir mas de una vez: el asistente va a dejar los borradores listos directamente en la bandeja del cliente y una persona los envia con un clic. Aclarale que en este modo nada se envia solo.

Registra la eleccion en la politica (`canal_envio_modo`). No avances hasta que el cliente haya elegido una de las dos y, si eligio envio automatizado, hasta que la accion de envio quede efectivamente verificada.

## Paso 0.7 — Organizar la carpeta de trabajo

Propone una estructura estandar dentro de la carpeta conectada del cliente, para que todo tenga un lugar predecible:

- `Politica de Cobro/` — el manual (docx + pdf) y el archivo tecnico.
- `Cartera/` — el Excel/Sheet con las facturas.
- `Facturas soporte/` — PDFs u otro respaldo documental de cada factura (acuses de recibo, contratos, etc.), si el cliente los maneja por separado.
- `Registro de Comunicaciones/` — el registro real de lo que se ha enviado (lo usa `cobro-ingesta-clasificacion`, ver ese skill).
- `Plan de Comunicacion/` — el plan concreto de que enviar y cuando, con el mensaje ya redactado por deudor (ver `references/plan-de-comunicacion.md`). Existe para que la gestion de cobro no dependa por completo de que la automatizacion del agente este bien configurada o corriendo: si algo falla, cualquier persona puede abrir este archivo y enviar manualmente lo que corresponda.

Intenta crear estas subcarpetas directamente con el conector de Drive conectado. Si el conector disponible no soporta crear carpetas, no lo fuerces: dile al cliente los cinco nombres sugeridos y pidele que las cree el mismo (o dile donde prefiere ponerlas), y continua sin bloquear el resto de la configuracion. Si el cliente ya tiene su propia organizacion de carpetas, no se la impongas — pregunta donde prefiere que quede cada cosa y usa esa ubicacion en los pasos siguientes.

Pregunta tambien con que cadencia quiere que se refresque el plan de comunicacion: **al completar cada etapa** (se recalcula justo cuando un caso transiciona), **semanal**, o **mensual**. Guarda esto en la politica (`plan_comunicacion.frecuencia_refresco`).

## Paso 1 — Buscar politica existente

Antes de preguntar nada, busca en la carpeta conectada del usuario un archivo llamado `Politica de Cobro - [Cliente].docx` o `politica-cobro-[nombre-cliente].json` (o variaciones razonables, incluyendo dentro de `Politica de Cobro/` si ya existe esa carpeta). Si existe, léelo, resume su contenido en una frase por parametro, y pregunta si el usuario quiere mantenerlo, actualizar un parametro puntual, o rehacerlo desde cero. Nunca sobrescribas una politica existente sin confirmacion explicita.

Si no existe, continua al Paso 2.

## Paso 2 — Sesion de consultoria por transicion

Para cada transicion entre etapas, sigue el mismo patron: explica en una o dos frases el estandar recomendado (y por que, en terminos practicos, no legales) y pregunta si la empresa lo adopta tal cual o necesita un valor distinto. Si elige algo distinto, pregunta brevemente el motivo y guardalo junto con el valor — eso mismo alimenta el manual operativo. Cuando el entorno lo permita, usa el formulario visual de tarjetas/opciones para agrupar preguntas afines; si no esta disponible, cae de vuelta a preguntar una transicion a la vez en texto.

1. **Nombre del cliente y de la empresa** (para nombrar los archivos y personalizar los mensajes).
2. **Segmentacion por antiguedad**: explica que agrupar las facturas por cuanto tiempo llevan vencidas ayuda a decidir que tan urgente es cada caso. Estandar sugerido: 0-30 / 31-60 / 61-90 / +90 dias de mora.
3. **Transicion 0 → 1a (recordatorio preventivo)**: estandar sugerido, avisar 5 y 3 dias antes del vencimiento. Pregunta si la empresa prefiere otros plazos.
4. **Transicion 1a → 1b (recordatorio → estado de cuenta)**: estandar sugerido, pasar a estado de cuenta despues de 2 recordatorios amistosos sin respuesta ni pago.
5. **Transicion 1b → 1c (estado de cuenta → carta formal de cobro)**: estandar sugerido, tras 2 estados de cuenta sin abono nuevo, o al llegar a 30 dias de mora (lo que ocurra primero). Pregunta tambien el `plazo_carta_formal` que la carta le da al deudor para responder (estandar sugerido 10-15 dias calendario) — al vencer ese plazo sin pago ni acuerdo, el caso pasa automaticamente a cobro prejuridico. Aclara que esta transicion (1c → 2) ya no se pregunta por separado: es directamente el vencimiento de este plazo.
6. **Canales**: cuales usa la empresa para hablar con sus deudores (correo, WhatsApp, etc.). Aclara que el requerimiento formal (etapa 2) nunca se envia solo por WhatsApp, siempre debe quedar tambien en un canal que deje constancia formal.
7. **Tono y estilo de comunicacion**: pregunta como describiria la empresa su propio tono al escribirle a un cliente (formal, cercano, directo, etc.), y ofrece la opcion de subir uno o mas ejemplos reales de comunicaciones que ya han usado (correos, plantillas propias). Si sube ejemplos, ademas de alinear el estilo de redaccion a ese tono, revisalos buscando practicas puntuales que valga la pena sumar a la politica (ej. un canal de pago que ya incluyen, una frase que siempre usan, un dato de contacto especifico) y proponselo al cliente antes de incorporarlo — nunca lo agregues sin confirmar.

No avances a la siguiente transicion sin una respuesta clara de la anterior. Si el usuario dice "lo que tú creas mejor", ofrece el valor sugerido por defecto y pide confirmacion explicita antes de guardarlo.

**Lo que ya NO se pregunta aqui, y por que:**

- *El umbral de prejuridico a judicial* no es una decision de negocio del cliente — es un criterio legal. Queda en 10 dias habiles sin respuesta tras el requerimiento formal como estandar recomendado, explicado en el manual. Si el usuario quiere cambiarlo despues, puede pedirlo explicitamente.
- *Quien revisa y lleva los casos de prejuridico/judicial* tampoco se pregunta aqui. No hay un contacto por defecto predefinido; `cobro-envio` lo pregunta y lo confirma dinamicamente la primera vez que un caso real llegue a prejuridico. Si el usuario lo pide directamente aqui, si se actualiza.
- *Un nivel de revision fijo por adelantado* (sin_revision/por_envio/por_lote) ya no existe como pregunta — en su lugar, `cobro-envio` avisa y propone programar la siguiente tanda cada vez que un caso cruza de sub-etapa. Explicaselo al cliente en una frase: "en vez de configurar de antemano como se revisa cada envio, te voy a avisar cada vez que un caso pase a la siguiente etapa, y programamos juntos que sigue."

## Paso 3 — Escribir la politica: manual operativo (docx + pdf) y configuracion tecnica

La politica de cobro es un documento que cualquier persona del equipo del cliente pueda leer y usar, con o sin el asistente. Este paso produce dos archivos, guardados en `Politica de Cobro/` (o la ubicacion que el cliente prefirio en el Paso 0.7):

1. **El manual operativo** (`Politica de Cobro - [Cliente].docx`, y su version `.pdf`): siguiendo `references/plantilla-politica.md` — proposito, marco normativo aplicable, las cuatro etapas y sus sub-pasos con los valores que la empresa eligio (y el motivo, si se desvio del estandar), canales, tono de comunicacion, como se manejan las excepciones caso por caso, y un anexo final con la configuracion en formato de tabla legible. Sin marca de "Breuk" en ninguna parte del documento — es de la empresa cliente, no de quien instalo el plugin.
2. **El archivo de configuracion tecnica** (`politica-cobro-[cliente].json`): los valores estructurados que `cobro-ingesta-clasificacion`, `cobro-mensajes` y `cobro-envio` necesitan para operar. Nunca reemplaza al manual, es su version maquina-legible.

Tambien crea (vacio) el archivo de registro de comunicaciones en `Registro de Comunicaciones/` (ver `references/registro-comunicaciones.md` en `cobro-ingesta-clasificacion`), listo para que `cobro-envio` lo empiece a llenar.

Confirma al usuario que todo quedo guardado y donde. Nunca sobrescribas una politica existente sin mostrar antes que cambia.

## Paso 4 — Automatizar es el resultado esperado por defecto

El resultado mas esperado de este skill no es solo dejar la politica escrita: es que la gestion de cobro quede corriendo sola, con avisos en cada transicion, y con el plan de comunicacion (Paso 0.7) como respaldo si algo falla. Termina la configuracion proponiendo activamente una tarea programada recurrente usando el mecanismo de planificacion que soporte el agente (schedule, cron, tarea periodica, o equivalente disponible en el entorno) — no la presentes como un extra opcional: "voy a dejar esto corriendo solo [frecuencia] — cada vez que un caso cambie de etapa te aviso y programamos juntos que sigue. ¿confirmamos?". La tarea clasifica la cartera contra el registro de comunicaciones, actualiza el plan de comunicacion, envia lo rutinario de las etapas 0 y 1a/1b, y se detiene a avisar en cualquier transicion hacia 1c, 2 o 3 — nunca redacta ni envia nada de prejuridico o judicial por su cuenta. Solo si el cliente rechaza explicitamente la automatizacion se deja en modo manual puro — confirma igual que puede activarla despues cuando quiera.

**Importante sobre como se comporta esto dentro de una tarea programada:** una tarea programada no tiene a una persona en vivo esperando para responder una pregunta — "avisar y proponer programar" en ese contexto significa que la corrida se detiene y deja el caso pendiente de revision para cuando el cliente entre a revisarlo, no una pregunta conversacional en tiempo real. Explica esto al cliente para que no espere una interaccion instantanea de la tarea. Ademas, recomienda dejar la tarea en modo **"Aprobar manualmente"** (el icono de candado, en el menu de modo de la tarea) durante su primera corrida de prueba con datos reales — en los otros dos modos ("Aprobar automaticamente" y "Omitir todas las aprobaciones"), darle "Run" ejecuta la tarea completa de inmediato (incluyendo cualquier envio real que le corresponda en ese momento), no es una vista previa. Una vez el cliente confirme que el comportamiento es el esperado, puede cambiar el modo segun su preferencia.

## Paso 5 — Prueba breve de verificacion antes de cerrar

Antes de dar la configuracion por completa, confirma que el canal de envio realmente funciona: envia un correo de prueba corto (ej. "Prueba de envio - Asistente de Gestion de Cobro" con un cuerpo de una linea) a traves del conector de correo ya conectado, dirigido al contacto de escalamiento configurado o a una direccion que el cliente indique para la prueba — nunca a un deudor real. Usa la accion de envio real habilitada en el Paso 0.5 (no el conector de solo lectura). Envia unicamente ese mensaje corto de verificacion — nunca uses una plantilla real de mensaje de cobro como parte de esta prueba. Confirma con el cliente que lo recibio antes de cerrar la sesion. Si el envio falla, diagnostica con el cliente (conector no autenticado, accion de envio no habilitada, direccion incorrecta) antes de continuar.

## Anti-patrones

- Nunca conviertas esta consultoria en un formulario ciego — siempre explica el estandar y su porque antes de preguntar si aplica o cambia.
- Nunca inventes un umbral o un canal sin preguntarle al usuario primero — ni siquiera como valor por defecto silencioso (excepto el umbral judicial, que es un estandar fijo y explicado, no una pregunta).
- Nunca preguntes en esta consultoria quien revisa los casos de prejuridico/judicial — eso se resuelve dinamicamente en `cobro-envio`.
- Nunca agregues algo de un ejemplo de comunicacion subido por el cliente a la politica sin proponerselo y confirmar primero.
- Nunca sobrescribas una politica existente sin mostrar antes qué cambia.
- Nunca generes un poder especial de cobro ni ofrezcas hacerlo — esa gestion la hace Wanda caso por caso, fuera de este plugin.
- Nunca guardes la politica de un cliente en un lugar donde otro cliente pueda leerla — cada politica vive junto a la cartera de su propio dueño.
- Nunca generes solo el manual docx/pdf sin el archivo de configuracion tecnica, ni viceversa.
- Nunca fuerces una estructura de carpetas si el cliente ya tiene la suya propia — pregunta y adapta.
- Nunca crees una tarea programada sin confirmacion explicita del cliente, ni la dejes en un modo de aprobacion que pueda enviar algo real sin que el cliente lo sepa en su primera corrida de prueba.
- Nunca dejes que el cliente piense que "Run" en una tarea programada es una vista previa — siempre es una ejecucion real.
- Nunca envies el correo de prueba del Paso 5 a un deudor real, a una direccion no autorizada, ni usando una plantilla real de mensaje de cobro.
- Nunca asumas que un conector de correo esta listo para automatizar solo porque aparece "conectado" — confirma especificamente que la accion de envio (no solo lectura) esta habilitada y autenticada.
