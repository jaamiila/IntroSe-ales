# Procesamiento de EEG

## Tabla de contenidos
1. Introduccion
2. Metodologia
3. Discusion de los resultados
4. Referencias

## Introduccion
Un electroencefalograma (EEG) es un herramienta que mide la actividad eléctrica en el cerebro mediante electrodos colocados sobre el cuero cabelludo [1], el tipo de señales que se obtiene cobra especial relevancia en la detección de trastornos, enfermedades o incluso en la detección de patrones relacionados a actividades diarias como lo son el parpadeo, el movimiento muscular, el habla, etc. Para obtener esta información es indispensable el procesamiento y análisis de señales de EEG. No obstante las características que son de utilidad para una aplicación en específico, pueden no serlo para otra.

Por ejemplo, se ha explorado el uso del EEG en la decodificación de imágenes motoras (MI) para interfaces cerebro-computadora, para mejorar la interacción de personas con discapacidades motoras con su entorno, sin embargo, uno de los principales problemas asociados con la clasificación multiclase de EEG  para este fin es la confusión informativa debido a las características no estacionarias de los datos de EEG.  [2]

Otra aplicación donde las señales EEG son cruciales es en la polisomnografía, ya que registra las actividades eléctricas cerebrales y desempeña un papel fundamental en la estadificación del sueño. La práctica clínica, ha destacado su utilidad en la determinación de parámetros clave como el arousal (AR), complejo K (Kc), y huso del sueño (Ss) en la evaluación del sueño[3]. A su vez, la EEG, al ser una señal fisiológica, ha demostrado una objetividad y confiabilidad superiores para identificar emociones en comparación con señales no fisiológicas [4].

Finalmente, se ha destacado en el diagnóstico de trastornos mentales, incluyendo las enfermedades de Alzheimer [5] y Parkinson [6]. En la literatura se pueden encontrar trabajos de investigación donde se busca extraer características específicas, como densidad espectral de potencia relativa (PSD), frecuencia dominante (DF), y variabilidad de la frecuencia dominante (DFV) [6], con el fin de profundizar en la comprensión de las complejidades cerebrales y su relación con enfermedades neurológicas. 


## Metodologia
Para la obtención de parámetros importantes se usó como guía biosignals notebook[7], además de los códigos revisados en clase, estos recursos nos serán útiles para tratar las señales y extraer las características más importantes de las mismas. Para ese fin se decidió seguir los pasos:

1. Se inicia con la importación de bibliotecas clave como numpy para cálculos numéricos, matplotlib.pyplot para visualización, re para trabajar con expresiones regulares, y scipy.signal para el procesamiento de señales.
2. En la primera parte nos centramos en la lectura y visualización de señales EEG, comenzando con la apertura y examinación de archivos de texto que contienen datos EEG.
3. Posteriormente, utilizamos regex para extraer información específica como la frecuencia de muestreo, seguido de la lectura detallada de estos archivos, excluyendo las filas iniciales.
4. Se continua el análisis con la visualización de estas señales EEG y la exploración del dominio de la frecuencia, empleando la transformada rápida de Fourier (FFT) para analizar componentes frecuenciales.
5. Seguimos con el filtrado de señales, crucial para el aislamiento de bandas de frecuencia específicas, utilizando la biblioteca biosignalsnotebooks.
6. Finalmente, detectamos la banda alfa, típicamente asociada con estados de relajación, mediante el método de Welch para estimar la densidad espectral de potencia.


## Discusion de resultados
En el estudio del procesamiento de señales EEG, hemos realizado una comparativa entre señales EEG filtradas y no filtradas bajo distintas condiciones. Al observar las señales EEG no filtradas, se aprecian patrones distintos que reflejan la actividad cerebral inherente a cada estado. Por ejemplo, en estado de reposo, la señal (gráfica roja) muestra una variabilidad significativa con picos y valles que representan la actividad eléctrica del cerebro en calma. Durante el parpadeo (gráfica azul), emergen picos marcados que denotan artefactos típicos del movimiento ocular. La fase de referencia de 30 segundos (gráfica negra) sirve como control, presentando una señal más uniforme, mientras que en el esfuerzo mental (gráfica verde), la señal se torna más errática, posiblemente indicando una actividad cerebral intensificada por el procesamiento cognitivo.
<p align="center"><img src="Imagenes_lab8/lab8_6.png" width=400p /></p>
<p align="center">Figura 6. Distribución impulso cardíaco de Normal y Anormal EKG [8]</p>

Al contrastar con las señales EEG filtradas, se observa cómo el filtrado modifica la amplitud y la claridad de la señal, eliminando artefactos y ruido, lo que permite un análisis más focalizado en las frecuencias de interés (gráficos de espectro de frecuencia). Específicamente, los gráficos de frecuencia muestran diferencias en la magnitud a lo largo de las bandas de frecuencia entre estados de reposo y de actividad, como el parpadeo, lo cual es crucial para identificar las bandas de frecuencia específicas asociadas con distintos procesos cognitivos y estados de alerta.

Esta comparación entre señales filtradas y no filtradas subraya la importancia del procesamiento adecuado en la interpretación de los EEG, resaltando cómo el filtrado puede mejorar la señal para un análisis más preciso. Los gráficos de frecuencia, tanto para las señales filtradas como no filtradas, son fundamentales para identificar los componentes clave de la señal, desde las frecuencias dominantes hasta los artefactos específicos de ciertas actividades, como el parpadeo. Estas observaciones son cruciales para el desarrollo de técnicas de procesamiento de EEG más efectivas y para mejorar nuestra comprensión de la actividad cerebral en distintas condiciones experimentales.


## Referencias
[1] “Electroencefalografía (EEG),” Mayo Clinic, https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875 (accessed Nov. 12, 2023). 

[2]  S. Phadikar, N. Sinha, and R. Ghosh, “Unsupervised feature extraction with autoencoders for EEG based multiclass motor imagery BCI,” Expert Systems with Applications, vol. 213. Elsevier BV, p. 118901, Mar. 2023. doi: 10.1016/j.eswa.2022.118901.

[3] Ş. Yücelbaş, C. Yücelbaş, G. Tezel, S. Özşen, and Ş. Yosunkaya, “Identification of full-night sleep parameters using morphological features of ECG signals: A practical alternative to EEG and EOG signals,” Biomedical Signal Processing and Control, vol. 88. Elsevier BV, p. 105633, Feb. 2024. doi: 10.1016/j.bspc.2023.105633.

[4] F. Li, K. Hao, B. Wei, L. Hao, and L. Ren, “MS-FTSCNN: An EEG emotion recognition method from the combination of multi-domain features,” Biomedical Signal Processing and Control, vol. 88. Elsevier BV, p. 105690, Feb. 2024. doi: 10.1016/j.bspc.2023.105690.

[5] M. Imani, “Alzheimer’s diseases diagnosis using fusion of high informative BiLSTM and CNN features of EEG signal,” Biomedical Signal Processing and Control, vol. 86. Elsevier BV, p. 105298, Sep. 2023. doi: 10.1016/j.bspc.2023.105298.

[6] A. Jaramillo-Jimenez et al., “Spectral features of resting-state EEG in Parkinson’s Disease: A multicenter study using functional data analysis,” Clinical Neurophysiology, vol. 151. Elsevier BV, pp. 28–40, Jul. 2023. doi: 10.1016/j.clinph.2023.03.363.
