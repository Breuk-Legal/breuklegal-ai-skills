# Connectors

## How tool references work

This plugin's skills describe the email-sending step in terms of the `~~correo`
category rather than a specific product, because different clients use
different email providers. Connect whichever one your company already uses —
the plugin works the same way either way.

## Important: reading email and sending email are different connectors

Testing this plugin (July 2026) showed that the native Gmail read connector
(search/inspect messages) does **not** include a send action. Actually sending
requires a separate write action — confirmed working via the Gmail "Send
Email" action enabled through Zapier (`gmail_send_email`). If your workspace
uses Outlook/Microsoft 365 instead, the equivalent send action must be enabled
the same way. `cobro-setup` checks for this specifically before treating the
email channel as ready for automation, and sends a real test message before
closing the configuration.

## Connectors for this plugin

| Category | Placeholder | Options |
|---|---|---|
| Spreadsheet / files | (fixed) | Google Sheets and Google Drive — used to read your cartera and to store your policy and communication history next to it. |
| Email — reading | `~~correo` | Gmail, Microsoft 365 / Outlook |
| Email — sending (required for automation) | (fixed action, varies by provider) | Gmail: "Send Email" action via Zapier. Outlook/Microsoft 365: the equivalent send action for your provider. |
| Messaging (optional) | (fixed) | WhatsApp Business API — only needed if you want to send the early friendly reminder by WhatsApp. |

Connect Google Sheets/Drive and the send action for your email provider before
running `cobro-setup` — or let `cobro-setup` walk you through connecting them,
since it checks and surfaces the "Connect" prompt directly in the conversation
if something is missing. WhatsApp Business API is optional and only required
if your collection policy uses it as a channel.
