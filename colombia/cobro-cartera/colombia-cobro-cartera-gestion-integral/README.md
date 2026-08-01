# colombia-cobro-cartera-gestion-integral

A skill package that helps a lawyer or law firm run accounts-receivable collection (*cobro de cartera*) as a service for their business clients in Colombia: a consulting-style session builds each client's own collection policy, classifies invoices by stage, drafts communications from verified templates, and automates sending while respecting Colombian consumer-protection collection law (Ley 2300 de 2023).

It runs in any AI agent environment that supports action tools (connectors / MCP) — spreadsheet, email, and automation — for example Claude Cowork/Code, or coding agents that read `AGENTS.md`. It is not tied to a single platform or automation vendor.

**Who this is for:** this plugin's primary user is a lawyer or firm that offers collection management to business clients — not a general-purpose skill for any legal practice area. If that's not your practice model, it likely won't be useful to you as-is.

## The 4-stage model

0. **Preventive** — a reminder before the invoice is even due.
1. **Persuasive/administrative** — friendly reminder, account statement, and, as the strongest step, a **formal collection letter** (already cites default and interest, but sent by the company itself, no lawyer involved).
2. **Pre-legal** (*instancia legal*) — **formal payment demand**, lawyer-reviewed. A different document from the collection letter above.
3. **Judicial** (*instancia legal*, last resort) — no drafting at all, only a contact alert.

## What it does, in short

1. **Builds the client's policy in a consulting session** (once, or whenever it needs adjusting): the assistant explains the recommended standard for each stage transition and asks whether the client adopts it as-is or needs something different, captures the client's communication tone (description or real examples), and organizes the working folder.
2. **Reads the client's receivables** from their own spreadsheet (Google Sheets, an Excel/CSV file in Drive, or equivalent storage), cross-checks them against the real log of what's already been sent, and classifies each invoice into its exact sub-stage.
3. **Drafts the message for each stage**, with the tone and legal grounding that stage requires — never threatening, never inventing figures.
4. **Sends routine communications automatically and flags every transition**: when a case moves to the next stage, it pauses and proposes scheduling the next batch together — instead of requiring a review mode configured upfront.

## What it never does

- Never sends the formal payment demand (pre-legal stage) without a lawyer reviewing and approving it first.
- Never drafts lawsuits or any filing for the judicial stage — only alerts who to contact.
- Never reports debtors to credit bureaus (Datacrédito/CIFIN) — out of scope today.
- Never compares one client's receivables against another's.

## How to use it

If you don't use Claude, see the repository's main README for instructions for ChatGPT, Gemini, and coding agents.

If you use Claude Cowork or Claude Code:

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install colombia-cobro-cartera-gestion-integral@breuklegal-ai-skills
/reload-plugins
```

Or with the skills.sh CLI:

```
# This whole plugin (all 5 cobro skills)
npx skills add Breuk-Legal/breuklegal-ai-skills/colombia/cobro-cartera/colombia-cobro-cartera-gestion-integral

# A single skill by its full name — e.g. only the policy-setup session
npx skills add Breuk-Legal/breuklegal-ai-skills --skill colombia-cobro-cartera-politica

# Everything in the repo (both plugins)
npx skills add Breuk-Legal/breuklegal-ai-skills --all
```

Pass any of this plugin's skill names to `--skill` to install it on its own: `colombia-cobro-cartera-politica`, `colombia-cobro-cartera-clasificacion`, `colombia-cobro-cartera-redaccion`, `colombia-cobro-cartera-envio`, `colombia-cobro-cartera-normativa`.

Once installed, tell Claude something like *"help me set up the collection assistant"* — the plugin recognizes that phrase and starts the guided policy-setup session (`colombia-cobro-cartera-politica`) on its own.

**Important:** use this in an agent environment that can actually take actions (connectors / MCP), not a plain text chat — the spreadsheet, email, and send/automation tools and scheduled-task automation only work where the agent can execute them. In Claude that means Cowork or Claude Code.

## Connectors needed

See `CONNECTORS.md`. In short: you need Google Sheets/Drive connected (where the client's receivables live) and an email connector (Gmail or Microsoft 365/Outlook). WhatsApp Business API is optional.

## Skills included

| Skill | What it does |
|---|---|
| `colombia-cobro-cartera-politica` | Consulting session: builds or updates the client's collection policy, communication tone, and working folder. |
| `colombia-cobro-cartera-clasificacion` | Reads and validates the receivables, cross-checks the real communications log, and classifies each invoice into its exact stage. |
| `colombia-cobro-cartera-redaccion` | Drafts each stage's message (reminder, account statement, formal collection letter, formal payment demand). |
| `colombia-cobro-cartera-envio` | Sends routine communications, flags every stage transition, and enforces the human-review gate before pre-legal/judicial. |
| `colombia-cobro-cartera-normativa` | Answers informational questions about Colombian collection law. |

## Escalation contact

This plugin has no hardcoded default escalation contact. During setup, `colombia-cobro-cartera-politica` asks who should review pre-legal/judicial cases for each client — the lawyer or firm installing the plugin, the client's in-house counsel, or another external advisor the client designates.

## Scope and limitations

Content grounded in Ley 2300 de 2023 (Colombian collection-practice consumer protection law) and Circular Externa 048 de 2008. Verify current validity of any cited article before using it in a binding document. This skill does not replace professional legal advice or a lawyer's judgment on when to escalate a real case.

## License

MIT — see the repository's [LICENSE](../LICENSE).
