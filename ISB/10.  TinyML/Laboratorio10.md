# TinyML y elaboracion del Edge Impulse

## Tabla de contenidos
1. Introduccion
2. Metodologia
3. Discusion de los resultados
4. Referencias

## Introduccion

## Metodologia
En el campo del análisis de señales biomédicas, como el electrocardiograma (ECG), la importación de librerías y herramientas adecuadas es fundamental. Este proceso comienza con la importación de librerías esenciales para el manejo de datos, visualización, procesamiento de señales y análisis específico de ECG. Entre estas librerías se encuentran numpy, para operaciones numéricas; matplotlib y seaborn, para visualización de datos; pandas para el manejo de datos en formato de tabla; pywt para la transformada de wavelet, y scipy, que ofrece herramientas adicionales para el procesamiento de señales. Adicionalmente, se emplea biosignalsnotebooks, una librería específica para trabajar con señales biomédicas.

El proceso de análisis inicia con la lectura de la señal de ECG desde un archivo de texto, utilizando la función numpy.genfromtxt. Tras cargar los datos, la señal se convierte a milivoltios (mV), una unidad más adecuada para la representación de señales biológicas. Para visualizar la señal de ECG en su estado original, se utiliza bokeh, una herramienta de visualización interactiva, que permite una mejor interpretación de los datos.

El siguiente paso es el filtrado de la señal, donde se aplica un análisis de Transformada Rápida de Fourier (FFT) para identificar los picos de ruido, seguido de la implementación de un filtro digital IIR notch. Este filtro se utiliza para eliminar específicamente los ruidos en frecuencias de 60 y 120 Hz, comunes en señales biomédicas debido a la interferencia eléctrica. La eficacia del filtrado se verifica visualizando el espectro de frecuencia de la señal después de su aplicación.

Posteriormente, se realiza un proceso de filtrado adicional mediante la Transformada de Wavelet Discreta (DWT). Esta técnica descompone la señal en coeficientes de aproximación y detalle, permitiendo un control más refinado sobre los componentes de la señal. Se establece un umbral para retener solo los componentes significativos y se reconstruye la señal, logrando así una reducción efectiva de ruidos y artefactos.

El análisis en el dominio de la frecuencia se lleva a cabo de nuevo mediante FFT, pero esta vez en la señal ya filtrada con DWT. Este análisis es crucial para entender el impacto de las etapas de filtrado sobre la señal en términos de frecuencia.

Finalmente, el código se centra en la extracción de características clave de la señal de ECG y la creación de un conjunto de datos (dataset). La señal filtrada se segmenta en intervalos de 3 segundos para la extracción de características relevantes, como los intervalos RR, la frecuencia cardíaca en latidos por minuto (BPM) y la desviación estándar de los intervalos NN (SDNN), elementos cruciales en estudios de variabilidad de la frecuencia cardíaca. Estos datos extraídos se almacenan en un archivo CSV, facilitando su análisis y utilización en investigaciones posteriores.

## Discusion de los resultados
