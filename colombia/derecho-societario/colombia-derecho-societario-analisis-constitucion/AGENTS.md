# AGENTS.md — colombia-derecho-societario-analisis-constitucion

Instructions for coding agents (Codex, Antigravity, Cursor, Kiro, Gemini CLI and compatible tools) working with this skill.

## What this is

A methodology for analyzing and recommending the right corporate vehicle in Colombian law (SAS, S.A., Ltda., branch of a foreign company), including the foreign investment regime when applicable. Detailed normative content is in `skills/colombia-derecho-societario-constitucion/references/figuras-societarias-colombia.md`. Expected behavior is in `skills/colombia-derecho-societario-constitucion/SKILL.md`.

## How to behave when using this content

1. Diagnose the real case before answering (number of shareholders, nationality, corporate purpose, whether foreign investment is involved, urgency).
2. Show the comparison of corporate vehicles before recommending one — never assume SAS without justifying why it wins over S.A., Ltda., or a branch for the specific case.
3. Never cite a specific article as verified current text without warning that it must be confirmed against a primary source (secretariasenado.gov.co, funcionpublica.gov.co) before a binding document — Colombian corporate law has had high-impact recent reforms (Ley 2069/2020, Ley 2294/2023).
4. If preparing an advisory session or presentation, follow this order: framing -> comparison -> recommended vehicle in depth -> recent risk to highlight -> foreign investment regime if applicable -> application to the concrete case -> open questions -> closing.

## Limits

This content does not replace professional legal advice. Do not invent normative precision that isn't in `references/` — if something is missing, explicitly flag that it needs verification.
