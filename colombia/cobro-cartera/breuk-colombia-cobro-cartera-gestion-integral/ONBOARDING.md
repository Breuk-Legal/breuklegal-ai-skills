# Onboarding rapido — Asistente de Gestion de Cobro

Version corta, interna, para que el plugin mismo (o cualquier skill) sepa a donde apuntar. Quien instala este plugin puede armar su propia guia en lenguaje llano para compartir con sus clientes, apoyandose en este documento y en `README.md`.

## Flujo minimo

1. Instalar el plugin en **Cowork** (no en un chat normal) — desde el repositorio de GitHub `breuklegal-ai-skills`, o subiendo el archivo `.plugin` directamente.
2. Decirle a Claude "ayudame a instalar y configurar el asistente de cobro" (o simplemente empezar a hablar de la cartera — cualquier skill sin politica configurada redirige aqui solo).
3. `cobro-setup` corre como una sesion de consultoria (no un formulario): explica el modelo de 4 etapas (preventiva, persuasivo/administrativo con carta formal de cobro, prejuridico con requerimiento formal, judicial) y pregunta, transicion por transicion, si el estandar aplica o si la empresa necesita algo distinto. Tambien verifica conectores (Sheets/Drive + correo), decide entre Zapier o modo borrador, organiza la carpeta de trabajo (Politica de Cobro / Cartera / Facturas soporte / Registro de Comunicaciones), captura el tono de comunicacion (descripcion o ejemplos), escribe la politica en docx+pdf y su version tecnica, ofrece la tarea programada, y termina con una prueba real de envio.
4. Desde ahi, usar las frases de cada skill (`cobro-ingesta-clasificacion`, `cobro-mensajes`, `cobro-envio`, `cobro-consulta-normativa`) segun se necesite. El requerimiento formal (prejuridico) nunca se redacta solo — hay que pedirlo explicitamente. Ya no hay modos de revision configurados de antemano: `cobro-envio` avisa y propone programar la siguiente tanda cada vez que un caso cambia de etapa.

## Donde esta cada cosa

- Detalle de por que Zapier y como conectarlo: `skills/cobro-setup/references/canal-de-envio.md`.
- Estructura de la politica del cliente (manual operativo + configuracion tecnica): `skills/cobro-setup/references/plantilla-politica.md`.
- Plantillas por etapa (incluye la carta formal de cobro y el requerimiento formal como documentos distintos): `skills/cobro-mensajes/references/plantillas.md`.
- Registro real de comunicaciones (fuente de verdad para clasificar sub-etapas): `skills/cobro-ingesta-clasificacion/references/registro-comunicaciones.md`.
- Prueba de regresion (datos sinteticos, sin conectores reales): `tests/`.
- Especificacion funcional completa (diseno y justificacion de cada regla): documento aparte en la carpeta del proyecto, no incluido en el plugin.
