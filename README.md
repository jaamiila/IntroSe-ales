# Deteccion de convulsiones tonico-clonicas en niños con epilepsia
## Detection of tonic-clonic seizures in children with epilepsy


## Resumen
Las convulsiones tónico-clónicas son particularmente significativas en la epilepsia pediátrica; este tipo específico de convulsión necesita mecanismos de detección efectivos debido a sus riesgos inherentes. Nuestro proyecto propone un algoritmo de procesamiento de señales digitales para un dispositivo portátil y ligero para el monitoreo en tiempo real de las convulsiones tónico-clónicas en niños de 6 a 14 años. El algoritmo propuesto extrae las características más relevantes de una señal EEG y es capaz de contar cada episodio de convulsión durante el tiempo de monitoreo. Este proyecto tiene el potencial de mejorar los procesos de toma de decisiones de los profesionales de la salud, influyendo directamente y mejorando la calidad de vida de los pacientes y sus familias.

## Motivacion
La motivación detrás de nuestro proyecto de detección de convulsiones tónico-clónicas en niños con epilepsia surge de la profunda comprensión de la importancia de abordar de manera efectiva y rápida este tipo específico de convulsión en la población pediátrica. Esta enfermedad afecta a aproximadamente 50 millones de personas, convirtiéndola en la cuarta condición neurológica más común y con una manifestación de la epilepsia en niños sonde solo en los Estados Unidos, alrededor de 470,000 niños menores de 14 años sufren de esta enfermedad. 

Reconocemos los riesgos inherentes asociados con las convulsiones tónico-clónicas y cómo su detección temprana puede marcar la diferencia en la calidad de vida de los niños afectados y sus familias. La falta de mecanismos de detección efectivos puede llevar a consecuencias graves, y nuestro proyecto busca llenar ese vacío mediante el desarrollo de un algoritmo innovador basado en procesamiento de señales digitales. Al mejorar la capacidad de monitoreo en tiempo real y contar con un enfoque preciso en la identificación de convulsiones, aspiramos a brindar una herramienta valiosa para los profesionales de la salud, permitiéndoles tomar decisiones informadas y personalizadas en el tratamiento de pacientes pediátricos con epilepsia. Nuestro objetivo es contribuir significativamente a la mejora de la atención médica en este campo, impactando positivamente en la vida de aquellos que enfrentan los desafíos diarios de la epilepsia pediátrica. 

## Principales Hallazgos
* Procesamiento de Datos:
  Se seleccionaron pacientes pediátricos con un alto número de episodios de epilepsia para mejorar la identificación de características en la señal EEG. Se aplicaron FFT y DWT a canales seleccionados, enfocándose en áreas como el lóbulo frontal lateral para obtener una localización más precisa de la actividad epileptogénica.

* Análisis de Frecuencia y Transformada Wavelet: Se utilizó FFT para descomponer la señal EEG en componentes de frecuencia, identificando la banda alfa y otros patrones relevantes. La Transformada Wavelet se aplicó para analizar cómo varían las frecuencias a lo largo del tiempo, ayudando a identificar convulsiones como eventos de alta energía en rangos de frecuencia específicos.

* Detección y Contabilización de Convulsiones: Se implementó un enfoque para contabilizar con precisión las convulsiones, considerando la variación temporal entre picos consecutivos. Esto ayudó a evitar la sobreestimación de episodios convulsivos y permitió una evaluación clínica más informada.

* Desafíos en la Adquisición de Señales EEG: Se enfrentaron obstáculos significativos en la adquisición de señales EEG en tiempo real, principalmente debido a problemas de conectividad y fallas en el hardware. Estas dificultades impactaron la comprobación del sistema de adquisición de señales EEG.

* Contribución al Tratamiento de la Epilepsia Pediátrica: A pesar de los desafíos, se desarrolló un algoritmo exitoso para la detección y contabilización de convulsiones, mejorando la comprensión de la distribución temporal de los episodios convulsivos y contribuyendo significativamente al campo de la epilepsia pediátrica y la medicina personalizada.
#
### Quienes somos?(https://github.com/jaamiila/IntroSe-ales/blob/main/ISB/1.%20Sobre%20Nosotros/Sobre%20nosotros.md#quienes-somos)
#
### Docentes del curso
- Lewis de la Cruz - umbert.de.la.cruz@upch.pe
- Moises Meza - moises.meza@upch.pe
- José Alonso Cáceres - jo.alonsok@gmail.com
- Avid Roman - avid.roman.g@upch.pe

