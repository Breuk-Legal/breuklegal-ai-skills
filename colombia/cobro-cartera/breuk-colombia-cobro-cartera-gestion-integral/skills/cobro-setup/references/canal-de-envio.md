# Canal de envio: como determinar la capacidad real de envio

## El problema de fondo

Muchos agentes de IA tienen herramientas de lectura de correo pero no de envio. Antes de configurar cualquier flujo automatizado, el agente debe verificar que capacidad tiene disponible en el entorno donde corre.

## Como verificar la capacidad de envio

1. Revisar las herramientas activas disponibles en el entorno (MCP servers, conectores nativos, integraciones de automatizacion).
2. Buscar explicitamente una accion de escritura / send para el proveedor de correo del cliente (Gmail, Outlook/Microsoft 365, u otro).
3. Si se encuentra: confirmar con un correo de prueba antes de continuar.
4. Si no se encuentra: activar el modo `borrador_asistido`.

## Opciones comunes de puente de automatizacion

Si el agente no tiene una accion de envio nativa, plataformas de automatizacion como **Zapier**, **Make**, **n8n**, **Pipedream** o **Composio** pueden actuar como puente y exponer la accion de envio via MCP o webhook. La disponibilidad depende del entorno donde corra el agente — verificar en el directorio de conectores activo.

## Modos registrados en la politica del cliente

- `zapier` (o equivalente): el agente envia de verdad usando la accion de escritura disponible.
- `borrador_asistido`: el agente crea el borrador y notifica al cliente que esta listo para enviarlo con un clic.

`cobro-envio` lee `canal_envio_modo` de la politica y actua en consecuencia.

## Opcion alternativa — modo borrador asistido

Si el cliente prefiere no configurar una plataforma de automatizacion adicional, o si el agente no tiene acceso a una accion de envio, el asistente usa la herramienta de correo disponible (que soporte crear borradores) para dejar cada comunicacion lista en la bandeja del cliente, y una persona la envia con un clic. No requiere ninguna cuenta nueva, pero las etapas 1-2 dejan de enviarse solas — hay que ser honesto con el cliente sobre eso al momento de elegir.

## Regla para el resto del plugin

`cobro-envio` debe leer `canal_envio_modo` de la politica del cliente y comportarse en consecuencia: si es `zapier` (o equivalente), ejecuta el envio real via la accion de escritura habilitada; si es `borrador_asistido`, crea el borrador y notifica al cliente que esta listo para que el lo envie.
