# Marco normativo activo del plugin

Verificado contra fuente primaria o secundaria confiable el 21 y 28 de julio de 2026. Estas son las normas que efectivamente condicionan el comportamiento de los otros skills — no solo referencia, sino reglas activas.

| Norma | Para que la usa el asistente |
|---|---|
| Art. 1608, Codigo Civil | Mora del deudor — base de todo requerimiento de pago (`colombia-cobro-cartera-redaccion`). |
| Art. 884, Codigo de Comercio | Interes bancario corriente certificado por la Superintendencia Financiera — tope aplicable a intereses moratorios. |
| Ley 1231 de 2008 (art. 774 C. Co.) | Requisitos para que una factura sea titulo valor: fecha de vencimiento, fecha de recibo identificada, ausencia de reclamo en 3 dias habiles (`colombia-cobro-cartera-clasificacion`). |
| Arts. 419-421, CGP | Proceso monitorio — obligaciones dinerarias, contractuales, determinadas y exigibles, de minima cuantia (tope 40 SMLMV, actualizar cada enero). |
| Art. 422, CGP | Requisitos del titulo ejecutivo — obligacion clara, expresa y exigible. |
| Art. 28, Ley 962 de 2005 | Conservacion de documentos del comerciante — minimo 10 anos. |
| Art. 5, Ley 2213 de 2022 | Poderes especiales por mensaje de datos — conocimiento de referencia solamente; el plugin no genera poderes. |
| Ley 2300 de 2023, art. 3 ("Dejen de Fregar") | Frecuencia maxima de contacto, un canal por semana tras contacto exitoso, horarios permitidos, prohibicion de indagar el motivo del impago — motor activo en `colombia-cobro-cartera-envio`. |
| Circular Externa 048 de 2008, SFC | Prohibicion de cargar gastos de cobranza prejuridica automaticamente por el solo vencimiento, sin gestion real documentada — regla activa en `colombia-cobro-cartera-redaccion`. |

El tope de 40 SMLMV para el proceso monitorio debe actualizarse cada enero con el salario minimo vigente — nunca dejarlo fijo. Cualquier cifra normativa debe verificarse contra fuente primaria (secretariasenado.gov.co, funcionpublica.gov.co) antes de usarse en un documento vinculante real para un caso especifico.
