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

## Referencias
[1] World Health Organization: WHO, “Epilepsia,” Who.int, Jun. 20, 2019. https://www.who.int/es/news-room/fact-sheets/detail/epilepsy (accessed Nov. 19, 2023).

[2] Centers for Disease Control and Prevention, "Types of Seizures | Epilepsy," [En línea]. Disponible en: https://www.cdc.gov/epilepsy/about/types-of-seizures.htm. [Accedido: 19-Nov-2023]​

[3] J. U. Duncombe, “Infrared navigation—Part I: An assessment of feasibility,” IEEE Trans. Electron Devices, vol. ED-11, no. 1, pp. 34–39, Jan. 1959, doi: 10.1109/TED.2016.2628402.

[4] N. M. Sayed, M. T. K. Aldin, S. E. Ali, and A. E. Hendi, “Cognitive functions and epilepsy-related characteristics in patients with generalized tonic–clonic epilepsy: a cross-sectional study,” Middle East Current Psychiatry, vol. 30, no. 1. Springer Science and Business Media LLC, Feb. 03, 2023. doi: 10.1186/s43045-023-00293-6.

[5] B. Francesca Solari, “Crisis epilepticas en la población infantil” Revista Médica Clínica Las Condes, vol. 22, no. 5. Elsevier BV, pp. 647–654, Sep. 2011. doi: 10.1016/s0716-8640(11)70477-1.

[6] L. S. Isabel Margarita Dra., V. E. Ximena Dra., and M. G. Silvia Dra., “Síndromes epilépticos en niños y adolescentes,” Revista Médica Clínica Las Condes, vol. 24, no. 6. Elsevier BV, pp. 915–927, Nov. 2013. doi: 10.1016/s0716-8640(13)70245-1.

[7] J. Freitas et al., “Age-specific periictal electroclinical features of generalized tonic–clonic seizures and potential risk of sudden unexpected death in epilepsy (SUDEP),” Epilepsy &amp; Behavior, vol. 29, no. 2. Elsevier BV, pp. 289–294, Nov. 2013. doi: 10.1016/j.yebeh.2013.08.010.

[8] J. Tellez, R. Nguyen, L. Hernández-Ronquillo. Injuries, accidents and mortality in epilepsy: Injuries, accidents, and mortality in epilepsy: A review of their prevalences, risk factors and prevention. Research Gate. Available at: https://www.researchgate.net/publication/50434829_Injuries_accidents_and_mortality_in_epilepsy_A_review_of_its_prevalence_risk_factors_and_prevention[Accessed: Nov 19, 2023]. 

[9] C. Helmstaedter and J.-A. Witt, “Epilepsy and cognition – A bidirectional relationship?,” Seizure, vol. 49. Elsevier BV, pp. 83–89, Jul. 2017. doi: 10.1016/j.seizure.2017.02.017.
“NeuroSpace,” NeuroPace, Inc., https://www.neuropace.com/ [Accessed: Nov 19, 2023]. 

[10] I. L. Olokodana, S. P. Mohanty, E. Kougianos, and R. S. Sherratt, “EZcap: A novel wearable for real-time automated seizure detection from EEG signals,” IEEE trans. consum. electron., vol. 67, no. 2, pp. 166–175, 2021.

[11] Z. Lasefr, R. R. Reddy, and K. Elleithy, “Smart phone application development for monitoring epilepsy seizure detection based on EEG signal classification,” in 2017 IEEE 8th Annual Ubiquitous Computing, Electronics and Mobile Communication Conference (UEMCON), 2017, pp. 83–87.

[12] J. Birjandtalab, M. Baran Pouyan, D. Cogan, M. Nourani, and J. Harvey, “Automated seizure detection using limited-channel EEG and non-linear dimension reduction,” Comput. Biol. Med., vol. 82, pp. 49–58, 2017.

[13] D. Chen, S. Wan, J. Xiang, and F. S. Bao, “A high-performance seizure detection algorithm based on Discrete Wavelet Transform (DWT) and EEG,” PLOS ONE, vol. 12, no. 3. Public Library of Science (PLoS), p. e0173138, Mar. 09, 2017. doi: 10.1371/journal.pone.0173138.

[14] G. Yogarajan et al., “EEG-based epileptic seizure detection using binary dragonfly algorithm and deep neural network,” Scientific Reports, vol. 13, no. 1. Springer Science and Business Media LLC, Oct. 18, 2023. doi: 10.1038/s41598-023-44318-w.

[15] F. Rosenow, K. M. Klein, and H. M. Hamer, “Non-invasive EEG evaluation in epilepsy diagnosis,” Expert Review of Neurotherapeutics, vol. 15, no. 4. Informa UK Limited, pp. 425–444, Mar. 16, 2015. doi: 10.1586/14737175.2015.1025382.

[16] K. Vandecasteele et al., “Visual seizure annotation and automated seizure detection using behind‐the‐ear electroencephalographic channels,” Epilepsia, vol. 61, no. 4. Wiley, pp. 766–775, Mar. 11, 2020. doi: 10.1111/epi.16470.

[17] M. M. Monge, “Procesamiento y caracterización de bioseñales para su uso en interfaces de control y afectividad.” Unpublished, 2015. doi: 10.13140/RG.2.1.2088.8407.

[18] P. Handa, M. Mathur, and N. Goel, “Open and free EEG datasets for epilepsy diagnosis”, Arxiv.org. [Online]. Available at: http://arxiv.org/abs/2108.01030. [Accessed: Nov 19, 2023].

[19] F. Rosenow, K. M. Klein, y H. M. Hamer, “Non-invasive EEG evaluation in epilepsy diagnosis”, Expert Rev. Neurother., vol. 15, núm. 4, pp. 425–444, 2015.

[20] Sameer, M., Gupta, B. Detection of epileptical seizures based on alpha band statistical features. Wireless Pers Commun 115, 909–925 (2020). https://doi.org/10.1007/s11277-020-07542-5

#
### [Quienes somos?](https://github.com/jaamiila/IntroSe-ales/blob/main/ISB/1.%20Sobre%20Nosotros/Sobre%20nosotros.md#quienes-somos)
#
### Docentes del curso
- Lewis de la Cruz - umbert.de.la.cruz@upch.pe
- Moises Meza - moises.meza@upch.pe
- José Alonso Cáceres - jo.alonsok@gmail.com
- Avid Roman - avid.roman.g@upch.pe

