# breuk-derecho-societario-colombia

Plugin de Claude Cowork / Claude Code con una skill para analizar y recomendar la figura societaria adecuada en derecho colombiano. Compatible tambien con agentes de codigo que leen `AGENTS.md` (Codex, Antigravity, Cursor, Kiro, Gemini CLI) y con `npx skills add` (skills.sh).

## Que incluye

**Skill:** `analisis-constitucion-societaria-colombia`

Ayuda a diagnosticar el caso, comparar figuras societarias (SAS, S.A., Ltda., sucursal de sociedad extranjera), aplicar el régimen de inversión extranjera cuando corresponde, y estructurar una asesoría completa — con recordatorios explícitos de verificar cualquier cita normativa en fuente primaria antes de un documento vinculante.

## Cómo usarlo

Si no usas Claude, mira el README principal del repositorio para instrucciones de ChatGPT, Gemini y agentes de código.

Si usas Claude Cowork o Claude Code:

```
/plugin marketplace add Breuk-Legal/breuklegal-ai-skills
/plugin install breuk-derecho-societario-colombia@breuklegal-ai-skills
/reload-plugins
```

## Alcance y limitaciones

Contenido validado contra fuentes normativas primarias en julio de 2026 (Ley 1258/2008, Ley 2069/2020, Ley 2294/2023, Decreto 1068/2015). El derecho societario colombiano cambia — revisa la vigencia de cualquier artículo citado antes de usarlo en un documento vinculante. Este skill no sustituye asesoría legal profesional.

## Licencia

MIT — ver [LICENSE](../LICENSE) del repositorio.
