# Prueba sintetica de regresion

`simular_plugin.py` implementa en Python las reglas deterministas descritas en
`skills/cobro-ingesta-clasificacion`, `skills/cobro-envio` y sus `references/`
(validaciones VAL-DATA-01 a 04, motor Ley 2300, clasificacion por etapa y gate
de aprobacion) y las corre contra `cartera_prueba.csv`, `historial_contactos.csv`,
`abonos_detalle_sabana.csv` y `politica_prueba.json` — una cartera sintetica con
siete casos, cada uno disenado para disparar una regla especifica:

| Caso | Que prueba |
|---|---|
| Comercial Rio Verde SAS | Flujo limpio, etapa 1, bloqueado por ya haber sido contactado hoy |
| Constructora Alba Ltda | Escalamiento a prejuridico por repeticiones, gate de aprobacion |
| Distribuidora Norte SAS | Reclamo en 3 dias descalifica la via ejecutiva |
| Suministros Pacifico SAS | Inconsistencia de saldo (VAL-DATA-01) — fila bloqueada |
| Taller Andino Ltda | Fechas incoherentes (VAL-DATA-03) — fila bloqueada |
| Grupo Sabana SAS | Abonos "proyectados" + bloqueo por canal usado la misma semana |
| Inversiones del Valle SAS | Escalamiento a judicial — sin generar ningun escrito, solo alerta |

Correr con `python3 simular_plugin.py`. No requiere conectores ni datos reales —
es la prueba a correr antes de conectar la cartera de un cliente real, y sirve
como regresion cada vez que se ajuste una regla de negocio en las `references/`.
