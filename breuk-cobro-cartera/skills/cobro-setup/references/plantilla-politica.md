# Plantilla de la politica de cobro: manual operativo + configuracion tecnica

Este skill produce dos archivos por cliente, no uno. Usa esta referencia para construir ambos.

## 1. El manual operativo (`Politica de Cobro - [Cliente].docx` + `.pdf`)

Documento redactado con la skill `docx`, pensado para que lo lea una persona del equipo del cliente (no solo el asistente). Estructura sugerida, en este orden:

1. **Portada** — nombre del cliente y fecha de configuracion/actualizacion, unicamente. Sin mencion de Breuk.
2. **Proposito** — un parrafo explicando que este documento define como la empresa gestiona su cartera vencida, y que aplica junto al Asistente de Gestion de Cobro o de forma manual por cualquier persona del equipo.
3. **Las cuatro etapas del cobro** — preventiva (recordatorio antes del vencimiento), persuasiva/administrativa (recordatorio, estado de cuenta, y la carta formal de cobro como paso mas fuerte, todo sin abogado), prejuridica (requerimiento formal de pago, ya interviene un abogado, es instancia legal), y judicial (ultima instancia). Aclarar que la carta formal de cobro y el requerimiento formal de pago son documentos distintos, con distinto responsable.
4. **Segmentacion de la cartera** — los rangos de dias de mora que el cliente eligio.
5. **Transiciones entre etapas** — para cada transicion (0→1a, 1a→1b, 1b→1c, 1c→2), el valor que quedo configurado y, si la empresa se desvio del estandar recomendado, el motivo que dio. El umbral de prejuridico a judicial es siempre el estandar fijo de 10 dias habiles, con la nota de que refleja un criterio legal de razonabilidad, no una preferencia de negocio.
6. **Canales y tono de comunicacion** — los canales habilitados, y una descripcion del tono/estilo que la empresa definio (y si aporto ejemplos propios, una mencion de que se uso como referencia).
7. **Quien interviene en prejuridico y judicial** — explica que, apenas un caso real llegue a esa etapa, el asistente pausa y pregunta (o confirma) quien debe revisar y aprobar esa comunicacion: el abogado o firma que instalo este plugin, un abogado interno de la empresa, u otro asesor externo que el cliente prefiera designar en ese momento. No hay un contacto por defecto predefinido en esta skill.
8. **Excepciones caso por caso** — cualquier caso individual puede manejarse distinto si el usuario lo pide expresamente; queda registrado junto a ese deudor especifico, sin cambiar el estandar general.
9. **Marco normativo aplicable** — mencion breve de la Ley 2300 de 2023 y la Circular Externa 048 de 2008, sin el detalle tecnico que ya vive en `cobro-consulta-normativa`.
10. **Organizacion de la carpeta de trabajo** — donde vive cada cosa (politica, cartera, facturas soporte, registro de comunicaciones).
11. **Anexo — configuracion vigente** — tabla legible con los mismos valores del archivo tecnico (seccion 2).

**Sobre marca en este documento:** el manual no debe mencionar "Breuk" en ninguna parte — ni portada, ni proposito, ni pie de pagina, ni el punto 7 de contacto de escalamiento. El documento es de la empresa cliente, no un producto de marca de quien instalo el plugin. Si quien instala el plugin es una firma con nombre propio y quiere ofrecerse como contacto de escalamiento por defecto, puede personalizar esa seccion con su propio nombre — pero el contenido de esta plantilla, tal como se distribuye, no trae ninguna marca precargada. La unica referencia de marca que persiste en todo el plugin es el prefijo tecnico `breuk-` en el nombre del plugin y sus skills.

## 2. El archivo de configuracion tecnica (`politica-cobro-[cliente].json`)

Version maquina-legible que `cobro-ingesta-clasificacion`, `cobro-mensajes` y `cobro-envio` leen para operar. Valores de ejemplo del caso piloto (I.M.C Ingenieria y Soluciones S.A.S.) — no copiar literalmente.

```json
{
  "cliente": "I.M.C Ingenieria y Soluciones S.A.S.",
  "actualizado": "2026-07-22",
  "segmentacion_antiguedad_dias": [30, 60, 90],
  "transiciones": {
    "preventiva_a_recordatorio": { "dias_antes_vencimiento": [5, 3], "origen": "estandar" },
    "recordatorio_a_estado_cuenta": { "criterio": "repeticiones", "valor": 2, "origen": "estandar" },
    "estado_cuenta_a_carta_formal": { "criterio": "repeticiones_o_dias", "valor": 2, "dias_alternativo": 30, "origen": "estandar" },
    "plazo_carta_formal_dias": { "valor": 12, "origen": "estandar" },
    "prejuridico_a_judicial": { "criterio": "dias_habiles", "valor": 10, "origen": "estandar_fijo" }
  },
  "canal_envio_modo": "zapier",
  "canales_habilitados": ["gmail"],
  "combinacion_por_etapa": {
    "recordatorio_preventivo": "gmail",
    "recordatorio": "gmail",
    "estado_cuenta": "gmail",
    "carta_formal_cobro": "gmail",
    "requerimiento_formal": "gmail"
  },
  "tono_comunicacion": {
    "descripcion": null,
    "ejemplos_aportados": false,
    "notas": null
  },
  "contacto_escalamiento": {
    "definido": false,
    "tipo": null,
    "nombre": null,
    "agenda": null,
    "correo": null,
    "whatsapp": null
  },
  "carpetas": {
    "politica": "Politica de Cobro/",
    "cartera": "Cartera/",
    "facturas_soporte": "Facturas soporte/",
    "registro_comunicaciones": "Registro de Comunicaciones/",
    "plan_comunicacion": "Plan de Comunicacion/"
  },
  "plan_comunicacion": { "frecuencia_refresco": "al_completar_etapa" },
  "tarea_programada": { "activa": false, "frecuencia": null, "modo_aprobacion_recomendado": "aprobar_manualmente" },
  "excepciones_registradas": []
}
```

## Notas sobre cada campo

- `transiciones.*`: cada una lleva un `"origen"` que es `"estandar"` si el cliente adopto la recomendacion tal cual, o `"ajustado_por_cliente"` si pidio un valor distinto (guarda el motivo en el manual, no en este archivo tecnico).
- `transiciones.prejuridico_a_judicial`: **no se pregunta** en la consultoria. Queda siempre en 10 dias habiles con `"origen": "estandar_fijo"`, salvo que el cliente pida explicitamente cambiarlo.
- `tono_comunicacion`: si el cliente describio su tono y/o subio ejemplos, resume aqui lo esencial (no el texto completo de los ejemplos) — el detalle vive en el manual.
- `contacto_escalamiento`: queda vacio (`"definido": false`) hasta que un caso real cruce a prejuridico por primera vez — lo llena `cobro-envio` en ese momento.
- `carpetas`: rutas relativas dentro de la carpeta conectada del cliente; si el cliente prefirio otra organizacion, refleja la que realmente se uso.
- `plan_comunicacion.frecuencia_refresco`: `al_completar_etapa` | `semanal` | `mensual` — ver `references/plan-de-comunicacion.md` para que es este archivo y como se mantiene.
- `tarea_programada.modo_aprobacion_recomendado`: sugerido `"aprobar_manualmente"` (la opcion del candado en el menu de modo de la tarea) para la primera corrida de prueba con datos reales de cada cliente, asi la tarea pide aprobar cada accion antes de ejecutarla — ajustable despues a `"aprobar_automaticamente"` u `"omitir_aprobaciones"` segun preferencia del cliente.
- `excepciones_registradas`: lista donde `cobro-envio` anota cada vez que un caso especifico se maneja distinto al estandar — cada entrada incluye el deudor/factura, la desviacion, y la razon.
- Este archivo (y su version docx/pdf) vive siempre junto a la cartera del cliente (misma carpeta de Drive), nunca en un repositorio centralizado de quien instala el plugin.
