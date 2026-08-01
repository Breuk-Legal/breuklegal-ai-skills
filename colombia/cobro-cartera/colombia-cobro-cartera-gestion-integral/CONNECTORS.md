# Connectors

## How tool references work

This plugin's skills describe the email-sending step in terms of the `~~correo`
category rather than a specific product, because different clients use
different email providers. Connect whichever one your company already uses —
the plugin works the same way either way.

## Important: reading email and sending email are different connectors

Testing this plugin (July 2026) showed that a native Gmail read connector
(search/inspect messages) does **not** necessarily include a send action.
Actually sending requires a separate write action — this can be a native send
action of your agent, an MCP connector, or a Gmail "Send Email" write action
exposed through an automation bridge (e.g. Zapier, Make, n8n; the reference
setup was tested with Zapier's `gmail_send_email`). If your workspace uses
Outlook/Microsoft 365 instead, enable the equivalent send action the same way.
`colombia-cobro-cartera-politica` checks for this specifically before treating the email channel as
ready for automation, and sends a real test message before closing the
configuration.

## Connectors for this plugin

| Category | Placeholder | Options |
|---|---|---|
| Spreadsheet / files | `~~archivos` | Google Sheets/Drive, or an Excel/CSV file in equivalent storage — used to read your cartera and to store your policy and communication history next to it. |
| Email — reading | `~~correo` | Gmail, Microsoft 365 / Outlook |
| Email — sending (required for automation) | (write action, varies by provider) | A send/write action for your provider: a native send action, an MCP connector, or a bridge like Zapier / Make / n8n (e.g. Gmail "Send Email", or the Outlook/Microsoft 365 equivalent). |
| Messaging (optional) | (fixed) | WhatsApp Business API — only needed if you want to send the early friendly reminder by WhatsApp. |

Connect your spreadsheet/files storage and the send action for your email provider before
running `colombia-cobro-cartera-politica` — or let `colombia-cobro-cartera-politica` walk you through connecting them,
since it checks and surfaces the "Connect" prompt directly in the conversation
if something is missing. WhatsApp Business API is optional and only required
if your collection policy uses it as a channel.
