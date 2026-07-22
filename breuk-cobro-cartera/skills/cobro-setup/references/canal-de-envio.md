# Canal de envio real: por que Zapier y como se activa

Verificado contra la documentacion oficial de Claude (soporte.claude.com, julio 2026): los conectores nativos de Google Workspace y Microsoft 365 en Claude son de solo lectura y borrador **por diseno de Anthropic** — "Claude creates drafts in your Gmail account, but cannot send emails on your behalf". Esto aplica siempre, sin importar la cuenta o la configuracion del plugin. No hay forma de activar el envio nativo.

## Opcion recomendada — automatizacion completa via Zapier

Zapier es, hoy, el puente de automatizacion disponible en el directorio de conectores de Claude que si tiene accion de escritura para enviar correo (`gmail_send_email` para Gmail; la accion equivalente para Outlook/Microsoft 365). Se probo de extremo a extremo el 21-22 de julio de 2026 y funciono correctamente.

Pasos para un cliente nuevo:

1. Si no tiene cuenta, crear una gratis en **https://zapier.com/sign-up** (el plan gratuito alcanza para volumenes bajos de cobro).
2. Conectar el conector "Zapier" dentro de Claude — se ofrece como tarjeta de "Conectar" directamente en la conversacion, no hay que salir de Claude para esto.
3. Cuando `cobro-setup` o `cobro-envio` habilite la accion de envio del proveedor de correo del cliente, si Zapier todavia no tiene autorizado ese proveedor, la respuesta incluye un link de autorizacion — hay que compartirselo al cliente y esperar a que confirme que ya autorizo antes de continuar.
4. Confirmar con el correo de prueba del Paso 5 de `cobro-setup`.

Otras plataformas de automatizacion similares (Make, n8n, Composio, Pipedream) se revisaron en el directorio de conectores el 22 de julio de 2026 y no estaban disponibles ahi — si eso cambia en el futuro, son alternativas validas al mismo rol que cumple Zapier aqui.

## Opcion alternativa — modo borrador asistido (sin Zapier)

Si el cliente prefiere no crear una cuenta adicional, el asistente usa el conector nativo (que si puede crear borradores) para dejar cada comunicacion lista en el Gmail/Outlook del cliente, y una persona la envia con un clic. No requiere ninguna cuenta nueva, pero las etapas 1-2 dejan de enviarse solas — el "resultado esperado" de automatizacion total (numeral 2.6 de la Especificacion Funcional) no se cumple del todo en este modo, y hay que ser honesto con el cliente sobre eso al momento de elegir.

## Regla para el resto del plugin

`cobro-envio` debe leer `canal_envio_modo` de la politica del cliente y comportarse en consecuencia: si es `zapier`, ejecuta el envio real via la accion de escritura habilitada; si es `borrador_asistido`, crea el borrador con el conector nativo y notifica al cliente que esta listo para que el lo envie.
