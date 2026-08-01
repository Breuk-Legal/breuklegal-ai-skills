# Plan de comunicacion (respaldo ante fallas de automatizacion)

Vive en `Plan de Comunicacion/` junto a la cartera del cliente. Es un documento concreto — no una descripcion de reglas — con fecha y mensaje ya redactado por deudor, para que la gestion de cobro no dependa por completo de que la tarea programada del agente este bien configurada o corriendo.

## Que contiene

Para cada factura/deudor activo, una fila con: fecha en que corresponde el proximo envio, sub-etapa (0, 1a, 1b, 1c, 2), canal, y el texto completo del mensaje ya redactado con los datos de esa factura (no una plantilla generica — el mensaje real, listo para copiar y pegar o enviar).

## Para que sirve

Es la consulta tanto del agente como del usuario: si la automatizacion fallo, no esta configurada, o el cliente simplemente prefiere revisar antes de confiar en el automatismo, cualquier persona puede abrir este archivo y enviar manualmente lo que corresponda, sin tener que pedirle al agente que redacte de nuevo cada mensaje. `colombia-cobro-cartera-envio` tambien lo consulta antes de decidir que sigue, en vez de asumir en el vacio.

## Cuando se refresca

Segun lo que el cliente eligio en `colombia-cobro-cartera-politica` (Paso 0.7), guardado en `plan_comunicacion.frecuencia_refresco` de la politica:

- **al_completar_etapa**: se recalcula justo cuando `colombia-cobro-cartera-clasificacion` detecta que un caso transiciono de sub-etapa.
- **semanal** / **mensual**: se recalcula en ese ciclo, independientemente de si hubo transiciones.

En cualquier caso, `colombia-cobro-cartera-envio` actualiza este archivo cada vez que algo se envia de verdad (para que no queden filas de mensajes ya enviados como si siguieran pendientes).

## Anti-patrones

- Nunca dejes plantillas genericas en este archivo — cada fila debe tener el mensaje ya redactado con los datos reales de esa factura.
- Nunca incluyas aqui un requerimiento formal o cualquier documento de prejuridico/judicial sin que ya haya sido pedido explicitamente por el usuario (ver `colombia-cobro-cartera-redaccion`) — este plan no es una forma de saltarse esa regla.
- Nunca dejes desactualizado este archivo despues de un envio real — que alguien lo use para enviar dos veces lo mismo es peor que no tenerlo.
