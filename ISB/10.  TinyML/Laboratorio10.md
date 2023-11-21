# TinyML y elaboracion del Edge Impulse

## Tabla de contenidos
1. Introduccion
2. Metodologia
3. Discusion de los resultados
4. Referencias

## Introduccion
La integración de TinyML en el análisis de señales de electrocardiograma (ECG) y la elaboración de datasets representa un salto significativo en la tecnología médica. Esta metodología combina el procesamiento avanzado de señales ECG con la eficiencia del aprendizaje automático, adaptado para dispositivos con recursos limitados como los microcontroladores. TinyML no solo mejora la eficiencia y rapidez en el análisis de ECG, sino que también facilita la generación de datasets precisos y detallados. Con herramientas como el Arduino Nano 33 BLE Sense y plataformas como Edge Impulse, se facilita el desarrollo de soluciones de Machine Learning y la creación de datasets en dispositivos de baja potencia, abriendo nuevas oportunidades en el monitoreo cardíaco y la detección temprana de afecciones cardíacas.

## Metodologia
En el campo del análisis de señales biomédicas, como el electrocardiograma (ECG), la importación de librerías y herramientas adecuadas es fundamental. 

1. Elaboracion del dataset
Este proceso comienza con la importación de librerías esenciales para el manejo de datos, visualización, procesamiento de señales y análisis específico de ECG. Entre estas librerías se encuentran numpy, para operaciones numéricas; matplotlib y seaborn, para visualización de datos; pandas para el manejo de datos en formato de tabla; pywt para la transformada de wavelet, y scipy, que ofrece herramientas adicionales para el procesamiento de señales. Adicionalmente, se emplea biosignalsnotebooks, una librería específica para trabajar con señales biomédicas.

El proceso de análisis inicia con la lectura de la señal de ECG desde un archivo de texto, utilizando la función numpy.genfromtxt. Tras cargar los datos, la señal se convierte a milivoltios (mV), una unidad más adecuada para la representación de señales biológicas. Para visualizar la señal de ECG en su estado original, se utiliza bokeh, una herramienta de visualización interactiva, que permite una mejor interpretación de los datos.

El siguiente paso es el filtrado de la señal, donde se aplica un análisis de Transformada Rápida de Fourier (FFT) para identificar los picos de ruido, seguido de la implementación de un filtro digital IIR notch. Este filtro se utiliza para eliminar específicamente los ruidos en frecuencias de 60 y 120 Hz, comunes en señales biomédicas debido a la interferencia eléctrica. La eficacia del filtrado se verifica visualizando el espectro de frecuencia de la señal después de su aplicación.

Posteriormente, se realiza un proceso de filtrado adicional mediante la Transformada de Wavelet Discreta (DWT). Esta técnica descompone la señal en coeficientes de aproximación y detalle, permitiendo un control más refinado sobre los componentes de la señal. Se establece un umbral para retener solo los componentes significativos y se reconstruye la señal, logrando así una reducción efectiva de ruidos y artefactos.

El análisis en el dominio de la frecuencia se lleva a cabo de nuevo mediante FFT, pero esta vez en la señal ya filtrada con DWT. Este análisis es crucial para entender el impacto de las etapas de filtrado sobre la señal en términos de frecuencia.

Finalmente, el código se centra en la extracción de características clave de la señal de ECG y la creación de un conjunto de datos (dataset). La señal filtrada se segmenta en intervalos de 3 segundos para la extracción de características relevantes, como los intervalos RR, la frecuencia cardíaca en latidos por minuto (BPM) y la desviación estándar de los intervalos NN (SDNN), elementos cruciales en estudios de variabilidad de la frecuencia cardíaca. Estos datos extraídos se almacenan en un archivo CSV, facilitando su análisis y utilización en investigaciones posteriores.

2. Integración de TinyML
La integración de TinyML con plataformas como Edge Impulse es fundamental para el desarrollo y la implementación de soluciones de Machine Learning en dispositivos de borde. Edge Impulse proporciona herramientas necesarias para recopilar datos, entrenar modelos de Machine Learning, y desplegarlos en dispositivos de baja potencia como el Arduino Nano 33 BLE Sense, lo cual es vital para el análisis de ECG, permitiendo un procesamiento eficiente y en tiempo real de los datos biomédicos.

La configuración para la integración de TinyML en el análisis de ECG incluye la instalación del Arduino IDE y varias librerías específicas, como Arduino Mbed OS Nano Boards y TensorFlow Lite para Arduino. Además, es crucial actualizar el firmware del Arduino Nano 33 BLE Sense para garantizar su compatibilidad y rendimiento óptimo con TinyML.

Una vez configurado, el Arduino Nano 33 BLE Sense se conecta a Edge Impulse mediante comandos específicos para iniciar el análisis de ECG. Se recomienda explorar con los sensores del Arduino Nano 33 BLE Sense, incluyendo la conexión con la cámara, para adquirir una variedad de datos biomédicos. Esta capacidad de TinyML para clasificar y analizar datos de ECG en tiempo real demuestra su potencial en aplicaciones de monitoreo de salud en tiempo real, donde la rapidez y la eficiencia del procesamiento son cruciales. La capacidad de trabajar con modelos de Machine Learning en dispositivos de baja potencia abre nuevas posibilidades para el análisis predictivo y la detección temprana de anomalías cardíacas, destacando el potencial de TinyML para revolucionar el campo del monitoreo y análisis cardíaco.

## Discusion de los resultados
