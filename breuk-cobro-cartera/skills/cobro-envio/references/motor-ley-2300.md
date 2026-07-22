# Motor de cumplimiento — Ley 2300 de 2023 ("Dejen de Fregar")

Verificado contra el texto vigente (art. 3, funcionpublica.gov.co) el 28 de julio de 2026. Aplica a las cuatro etapas por igual, incluida la comunicacion del requerimiento formal ya aprobada por el contacto de escalamiento — la aprobacion legal no exime del cumplimiento de frecuencia y horario.

## Reglas deterministas

1. **Consentimiento por canal**: cada deudor tiene banderas independientes `autoriza_email`, `autoriza_whatsapp`, `autoriza_sms`. Si el canal elegido para una comunicacion no esta autorizado, bloquea el envio por ese canal y desvia automaticamente al canal alternativo que si tenga autorizacion, dejando registro del desvio en el historial.

2. **Maximo un contacto al dia**: si ya hubo un envio a ese deudor en la fecha actual (sin importar el canal), reprograma cualquier otro envio para el siguiente dia habil.

3. **Un solo canal por semana tras contacto exitoso**: si hubo un contacto exitoso por un canal, los demas canales quedan bloqueados para ese deudor hasta la semana calendario siguiente. Mantén el registro cruzado de canal + fecha por deudor (numeral 5.5 de la Especificacion Funcional) para hacer cumplir esto.

4. **Horario legal**: envios permitidos lunes a viernes 7:00 a.m.-7:00 p.m., sabados 8:00 a.m.-3:00 p.m. Domingos y festivos, bloqueo total. Cualquier envio fuera de esa ventana se encola para el siguiente bloque habil, nunca se fuerza.

5. **Prohibicion de indagar el motivo del impago**: ninguna plantilla puede preguntar por que el deudor no ha pagado. Solo se informa el estado de la obligacion y se ofrecen alternativas de pago.

## Por que es un motor y no una sugerencia

Estas cinco reglas se verificaron de forma independiente contra el texto de la ley durante la sesion de diseno del 28 de julio de 2026 (ver Anexo de auditoria cruzada, Especificacion Funcional v3) y se determino que eran una laguna real de la primera version del plugin — no una precaucion adicional, sino una obligacion legal directa sobre cualquier gestion de cobranza automatizada en Colombia.
