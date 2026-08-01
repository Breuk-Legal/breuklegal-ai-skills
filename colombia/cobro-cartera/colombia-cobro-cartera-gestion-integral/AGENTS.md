# AGENTS.md — colombia-cobro-cartera-gestion-integral

Instructions for coding agents (Codex, Antigravity, Cursor, Kiro, Gemini CLI and compatible tools) working with this skill.

## What this is

A 4-stage accounts-receivable collection workflow for Colombia (preventive, persuasive/administrative, pre-legal, judicial), meant to be operated by a lawyer or firm managing collections on behalf of business clients. Behavior lives in five skills under `skills/`; detailed policy templates and normative content live in each skill's `references/`.

## How to behave when using this content

1. Never draft or send the formal payment demand (pre-legal stage) without an explicit human approval gate — this is non-negotiable across the whole plugin, regardless of any configuration a client requests.
2. Never draft any judicial filing — the judicial stage only produces a contact alert, never a document.
3. Distinguish the two stage-2/3 documents that share the word "formal": the **formal collection letter** (stage 1c, administrative, no lawyer) and the **formal payment demand** (stage 2, pre-legal, lawyer-reviewed) are different documents with different owners — never conflate them.
4. Each client's policy and receivables data must stay isolated in that client's own connected folder — never compare or cross-reference one client's data against another's.
5. This plugin has no hardcoded default escalation contact. Whoever installs it configures their own during the `cobro-setup` session — do not hardcode a specific person or firm as a fallback.
6. Any generated client-facing document (the policy manual) belongs to the end client, not to whoever built or installed the plugin — do not let the installer's own branding leak into a document meant to be the client's own operating policy.

## Limits

This content does not replace professional legal advice or a lawyer's judgment on when a real case should escalate. Colombian collection-practice law (Ley 2300 de 2023, Circular Externa 048 de 2008) should be verified against a primary source before relying on it for a binding document.
