# TinyML y elaboracion del Edge Impulse

## Tabla de contenidos
1. Introduccion
2. Metodologia
3. Discusion de los resultados
4. Conclusiones
5. Referencias

## Introduccion
La integración de TinyML en el análisis de señales de electrocardiograma (ECG) y la elaboración de datasets representa un salto significativo en la tecnología médica. Esta metodología combina el procesamiento avanzado de señales ECG con la eficiencia del aprendizaje automático, adaptado para dispositivos con recursos limitados como los microcontroladores. TinyML no solo mejora la eficiencia y rapidez en el análisis de ECG, sino que también facilita la generación de datasets precisos y detallados. Con herramientas como el Arduino Nano 33 BLE Sense y plataformas como Edge Impulse, se facilita el desarrollo de soluciones de Machine Learning y la creación de datasets en dispositivos de baja potencia, abriendo nuevas oportunidades en el monitoreo cardíaco y la detección temprana de afecciones cardíacas [1][2].

## Metodologia
En el campo del análisis de señales biomédicas, como el electrocardiograma (ECG), la importación de librerías y herramientas adecuadas es fundamental. 

1. Elaboracion del dataset

   Se comienza con la importación de librerías esenciales para el manejo de datos, visualización, procesamiento de señales y análisis específico de ECG. Entre estas librerías se encuentran numpy, para operaciones numéricas; matplotlib y seaborn, para visualización de datos; pandas para el manejo de datos en formato de tabla; pywt para la transformada de wavelet, y scipy, que ofrece herramientas adicionales para el procesamiento de señales. Adicionalmente, se emplea biosignalsnotebooks, una librería específica para trabajar con señales biomédicas.
   
   El proceso de análisis inicia con la lectura de la señal de ECG desde un archivo de texto, utilizando la función numpy.genfromtxt. Tras cargar los datos, la señal se convierte a milivoltios (mV), una unidad más adecuada para la representación de señales biológicas. Para visualizar la señal de ECG en su estado original, se utiliza bokeh, una herramienta de visualización interactiva, que permite una mejor interpretación de los datos. El siguiente paso es el filtrado de la señal, donde se aplica un análisis de Transformada Rápida de Fourier (FFT) para identificar los picos de ruido, seguido de la implementación de un filtro digital IIR notch. Este filtro se utiliza para eliminar específicamente los ruidos en frecuencias de 60 y 120 Hz, comunes en señales biomédicas debido a la interferencia eléctrica. La eficacia del filtrado se verifica visualizando el espectro de frecuencia de la señal después de su aplicación.
   
   Posteriormente, se realiza un proceso de filtrado adicional mediante la Transformada de Wavelet Discreta (DWT). Esta técnica descompone la señal en coeficientes de aproximación y detalle, permitiendo un control más refinado sobre los componentes de la señal. Se establece un umbral para retener solo los componentes significativos y se reconstruye la señal, logrando así una reducción efectiva de ruidos y artefactos. El análisis en el dominio de la frecuencia se lleva a cabo de nuevo mediante FFT, pero esta vez en la señal ya filtrada con DWT. Este análisis es crucial para entender el impacto de las etapas de filtrado sobre la señal en términos de frecuencia.
   
   Finalmente, el código se centra en la extracción de características clave de la señal de ECG y la creación de un conjunto de datos (dataset) que contega 2 conjuntos de data cruda correspondientes a 2 actividades diferentes. Estos datos extraídos se almacenan en un archivo CSV, facilitando su análisis y utilización en investigaciones posteriores.

2. Edge Impulse

   Paso 1: Crear una cuenta y proyecto en Edge Impulse
   Nos registramos en sitio web de Edge Impulse (https://www.edgeimpulse.com/) y crea una cuenta y un nuevo proyecto.

   Paso 2: Recopilar y cargar datos
   Recopilamos los datos de señales ECG. Usando el dataset (.csv) creado anteriormente
   Cargamos los datos en Edge Impulse y etiquetamos los segmentos según la clase a la que pertenece.

   Paso 3: Procesamiento de datos
   Edge Impulse proporciona herramientas como filtros y transformadas, nosotros aplicamos un análisis espectral.

   Paso 4: Diseño del modelo y entrenamiento
   Seleccionamos el tipo de modelo en la sección de "Create impulse", elegimos el modelo de clasificación y configuramos la arquitectura del modelo: 200 ciclos de entrenamiento y 0.001 de tasa de aprendizaje

   Paso 5: Entrenamiento del modelo
   Utilizamos los datos cargados previamente para entrenar el modelo. Además, pudimos evaluar el rendimiento del modelo utilizando otros conjuntos de datos que también adquirimos en laboratorios pasados. Se consiguió un nivel de 85% de ACCURACY.

4. Integración de TinyML

   La integración de TinyML con plataformas como Edge Impulse es fundamental para el desarrollo y la implementación de soluciones de Machine Learning en dispositivos de borde. Edge Impulse proporciona herramientas necesarias para recopilar datos, entrenar modelos de Machine Learning, y desplegarlos en dispositivos de baja potencia como el Arduino Nano 33 BLE Sense, lo cual es vital para el análisis de ECG, permitiendo un procesamiento eficiente y en tiempo real de los datos biomédicos.
   
   La configuración para la integración de TinyML en el análisis de ECG incluye la instalación del Arduino IDE y varias librerías específicas, como Arduino Mbed OS Nano Boards y TensorFlow Lite para Arduino. Además, es crucial actualizar el firmware del Arduino Nano 33 BLE Sense para garantizar su compatibilidad y rendimiento óptimo con TinyML.
   
   Una vez configurado, el Arduino Nano 33 BLE Sense se conecta a Edge Impulse mediante comandos específicos para iniciar el análisis de ECG. Se recomienda explorar con los sensores del Arduino Nano 33 BLE Sense, incluyendo la conexión con la cámara, para adquirir una variedad de datos biomédicos. Esta capacidad de TinyML para clasificar y analizar datos de ECG en tiempo real demuestra su potencial en aplicaciones de monitoreo de salud en tiempo real, donde la rapidez y la eficiencia del procesamiento son cruciales. La capacidad de trabajar con modelos de Machine Learning en dispositivos de baja potencia abre nuevas posibilidades para el análisis predictivo y la detección temprana de anomalías cardíacas, destacando el potencial de TinyML para revolucionar el campo del monitoreo y análisis cardíaco.

## Discusion de los resultados


*Disclaimer:* Una de las dificultades principales fue la instalación inadecuada de librerías clave como Chocolatey y Visual Studio, que son esenciales para el correcto funcionamiento de plataformas como Edge Impulse con dispositivos como el Arduino Nano 33 BLE Sense. Esta limitación impidió una conexión efectiva y el aprovechamiento pleno de las capacidades de TinyML. Además, es relevante considerar otros posibles factores que pudieron haber influido en este desafío. Por ejemplo, la compatibilidad entre diferentes versiones de software y hardware puede presentar obstáculos, especialmente en sistemas que requieren una sincronización precisa entre múltiples componentes tecnológicos. También, la curva de aprendizaje asociada con la implementación de tecnologías emergentes como TinyML puede representar una barrera, particularmente en entornos donde la experiencia previa con estas tecnologías es limitada.

## Conclusiones
TinyML es un campo de tecnologías de rápido crecimiento, abarcando hardware, algoritmos y software diseñados para ejecutar tareas de aprendizaje automático en dispositivos con restricciones de tamaño y consumo de energía.

Edge impulse se presenta como un punto de inicio para aquellos que estén interesados en la aplicación de Machine Learning para la resolución de problemas, para el caso del análisis de una señal ECG, es un avance significativo para la creación de datasets y poder entrenar modelos para una detección temprana más rápida y eficiente.

[Diclaimer] Durante el desarrollo de la presente práctica de laboratorio, nos enfrentamos a restricciones de tiempo que impidieron la implementación completa de la integración entre el Arduino 33 BLE Sense y el TinyML. Como resultado, nuestro enfoque se centró exclusivamente en la plataforma Edge Impulse para explorar y comprender las aplicaciones de Machine Learning en dispositivos embebidos. Es importante tener en cuenta que la falta de tiempo para abordar todas las facetas del proyecto podría haber afectado la amplitud y la profundidad de nuestra experiencia.

A pesar de este inconveniente, la concentración en Edge Impulse proporcionó una valiosa introducción a las capacidades de desarrollo de algoritmos de Machine Learning en entornos con recursos limitados. La plataforma se destacó como un recurso integral para la creación de datasets y el entrenamiento eficiente de modelos, lo cual se refleja en nuestras conclusiones.

Esperamos que esta nota aclare cualquier ambigüedad con respecto a la implementación completa del proyecto y reafirme el valor obtenido a través de la exploración de Edge Impulse en el contexto de TinyML.


## Referencias
[1]  Edge Impulse, "The Edge AI Platform" Edge Impulse, 2023. [Online]. Available: https://edgeimpulse.com/. [Accessed: Nov. 21, 2023].
[2] E. Kim, J. Kim, J. Park, H. Ko, and Y. Kyung, "TinyML-Based Classification in an ECG Monitoring Embedded System," in Computers, Materials & Continua, vol. 75, no. 1, pp. 1751-1764, 2023. [Online]. Available: https://doi.org/10.32604/cmc.2023.031663​​​​.


