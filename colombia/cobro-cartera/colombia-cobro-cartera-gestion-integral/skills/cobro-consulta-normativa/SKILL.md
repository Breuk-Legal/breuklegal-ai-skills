---
name: cobro-consulta-normativa
description: Responde preguntas informativas sobre el marco legal colombiano de cobranza (Ley 2300 de 2023, Circular Externa 048 de 2008, regimen de habeas data y reporte a centrales de riesgo, cartera publica/B2G) sin ejecutar ni bloquear ninguna accion sobre la cartera del cliente. Se activa con preguntas como "puedo reportar esta deuda a Datacredito", "cuanto puedo cobrar de intereses", "que pasa si mi deudor es una entidad publica", "cada cuanto puedo contactar a un deudor", "que dice la ley sobre cobranza".
---

# Consulta normativa (informativa, no operativa)

Este skill solo responde preguntas. No lee cartera, no redacta comunicaciones, no envia nada y no cambia el estado de ninguna factura — para eso existen los otros cuatro skills de este plugin.

## Como responder

1. Consulta `references/marco-normativo.md` para las normas que si estan activas en el motor del plugin (arts. 1608 CC, 884 C.Co., Ley 1231/2008, arts. 419-422 CGP, art. 28 Ley 962/2005, Ley 2300/2023, Circular 048/2008).

2. Consulta `references/conocimiento-consulta.md` para temas ya verificados pero que **no estan automatizados** en este plugin (reporte a centrales de riesgo bajo la Sentencia C-282 de 2021, y cartera publica/B2G). Responde con lo verificado, y aclara explicitamente que el plugin no ejecuta esa funcion hoy.

3. Cierra siempre con una advertencia breve de que esto es informacion general y no sustituye una evaluacion del caso concreto por un abogado — y si la pregunta sugiere que ya hay una gestion de cobro real en curso, ofrece el contacto de escalamiento configurado en la politica del cliente (o indica que aun debe definirse, si todavia no hay politica configurada).

## Anti-patrones

- Nunca presentes esto como una opinion legal formal y cerrada — es informacion general.
- Nunca cites un plazo o porcentaje de `conocimiento-consulta.md` marcado como "sin confirmar" como si fuera un hecho verificado — dilo explicitamente.
- Nunca actives, actualices o bloquees nada de la cartera del cliente desde este skill — si la pregunta implica accion, remite al skill correspondiente (`cobro-ingesta-clasificacion`, `cobro-mensajes` o `cobro-envio`).
- Nunca uses el "Manual de Cobro de la UAEJPMP" como fuente para cartera publica en general — ver la correccion explicita en `references/conocimiento-consulta.md`.
