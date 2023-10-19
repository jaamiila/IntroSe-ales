# Filtros IIR y FIR

### Laboratorio 7

#
## Objetivos
* Diseñar un filtro de tipo FIR usando el dataset de ECG obtenido el laboratorio pasado
* Diseñar un filtro de tipo IIR usando el dataset de ECG obtenido el laboratorio pasado 
* Presentar una tabla resumen comparando la señal cruda con la señal filtrada  

#

## Tabla de contenidos

1. Conceptos previos
  * Filtros digitales
      * Filtros FIR
      * Filtros IIR

## Conceptos previos
Este informe tiene como objetivo mostrar el uso de diferentes filtros (FIR, IIR y DWT) en las señales de ECG, EMG y EEG adquiridas en clase. Los filtros son herramientas que permiten modificar una señal para eliminar o resaltar ciertas características de interés. En el caso de las señales bioeléctricas, como el ECG, EMG y EEG, los filtros son utilizados para eliminar el ruido y las interferencias que pueden afectar la calidad de la señal y dificultar su análisis. 

### Filtros digitales
Son una herramienta crucial en el procesamiento digital de señales (PDS). Estos filtros se utilizan para modificar o analizar las señales digitales, permitiendo separar o combinar ciertas frecuencias en una señal. Dentro de este tipo de filtros tenemos tres tipos: Filtros de respuesta infinita al impulso, filtro de respuesta finita al impulso y filtros wavelet.

#### Filtros FIR
Los filtros FIR (Respuesta finita al impulso) son aquellos que tienen una respuesta al impulso de duración finita. Estos filtros son estables porque la sumatoria contiene una cantidad finita de elementos[1]. Los filtros FIR son ampliamente utilizados en el procesamiento de señales debido a su simplicidad y facilidad de implementación[2]. Los filtros FIR se pueden diseñar usando técnicas como la del ventaneo o el método de mínimos cuadrados. Las ventanas que se escogen para diseñar los filtros FIR pueden ayudar a mitigar en mayor o menor medida los efectos del fenómeno de Gibbs.

#### Filtros IIR
Los filtros IIR (respuesta infinita al impulso) son sistemas causales que trabajan en tiempo real y tienen una respuesta de fase no lineal. El diseño de estos filtros se basa en la transformada Z, que permite representar la función de transferencia del filtro en el dominio Z. Los filtros IIR presentan una cantidad infinita de términos cuando se les aplica un impulso, lo que los hace más complejos que los filtros FIR. Los filtros IIR se utilizan en el procesamiento de señales bioeléctricas, como el ECG, EEG y EMG, para eliminar el ruido y las interferencias que pueden afectar la calidad de la señal y dificultar su análisis[3][4].

Los filtros IIR son utilizados en el procesamiento de señales bioeléctricas, como el EMG, para eliminar el ruido y las interferencias que pueden afectar la calidad de la señal y dificultar su análisis. Los tipos de filtros IIR más comunes son Butterworth, Chebyshev, Elliptic, Bessel y Causalidad. [1] El filtro Butterworth es un filtro de respuesta plana en la banda de paso y decae suavemente en la banda de rechazo.[2] El filtro Chebyshev presenta una respuesta de rizado en la banda de paso, pero tiene una pendiente más empinada en la banda de transición que el filtro Butterworth.[3][5] El filtro Elliptic presenta una respuesta de rizado tanto en la banda de paso como en la de rechazo, pero tiene la pendiente más empinada en la banda de transición. El filtro Bessel tiene una respuesta de fase lineal, lo que significa que no introduce distorsión en la señal de salida. El filtro de causalidad es un filtro IIR que solo utiliza valores pasados de la señal de entrada para calcular la salida, lo que lo hace útil en aplicaciones en tiempo real. En general, el tipo de filtro IIR utilizado en el procesamiento de señales bioeléctricas dependerá de las características específicas de la señal y de los requisitos de la aplicación.[4][5]


#### Filtros Wavelet
La transformada wavelet discreta (DWT) es una técnica de procesamiento de señales que permite analizar señales no estacionarias y detectar cambios abruptos en la señal. Las wavelets son señales que tienen una duración limitada y un valor promedio de cero. La DWT se obtiene al discretizar los parámetros de desplazamiento y escalamiento dentro de la transformada wavelet continua. Los coeficientes wavelet nos indican cuánta relación hay entre la señal y la wavelet madre, lo que nos permite conocer los componentes frecuenciales de la señal. La DWT se utiliza en el procesamiento de señales bioeléctricas, como el EMG, para extraer características de la señal y mejorar su análisis[4][5][6].

## Referencias
[1]	EUM, “Introducción a los Filtros Digitales,” Edu.uy. [Online]. Available: https://www.eumus.edu.uy/eme/ensenanza/electivas/dsp/presentaciones/clase10.pdf. [Accessed: 18-Oct-2023].

[2]	D. M. B. D. Torres, “INTRODUCCIÓN A LOS FILTROS DIGITALES UN ENFOQUE TEÓRICO-PRÁCTICO,” Azurewebsites.net, Jan-2018. [Online]. Available: http://diegorenza.azurewebsites.net/books/Introduccion_Filtros_Digitales.pdf. [Accessed: 18-Oct-2023].

[3]	T. de Grado Presentado por, “Acondicionamiento de Señales Bioeléctricas,” Core.ac.uk. [Online]. Available: https://core.ac.uk/download/pdf/71394319.pdf. [Accessed: 18-Oct-2023].

[4]	“Redes neuronales en la caracterización de señales bioeléctricas – acervo para el mejoramiento del aprendizaje de alumnos de ingeniería, en Inteligencia Artificial,” Unam.mx. [Online]. Available: https://virtual.cuautitlan.unam.mx/intar/?page_id=977. [Accessed: 18-Oct-2023].

[5]	Wikipedia contributors, “IIR,” Wikipedia, The Free Encyclopedia. [Online]. Available: https://es.wikipedia.org/w/index.php?title=IIR&oldid=117829344.

[6]	Universidad Tecnológica de Pereira, “CARACTERIZACIÓN DE SEÑALES ELECTROMIOGRÁFICAS PARA LA DISCRIMINACIÓN DE SEIS MOVIMIENTOS DE LA MANO,” Unirioja.es, Agosto de 2009. [Online]. Available: https://dialnet.unirioja.es/descarga/articulo/4706922.pdf. [Accessed: 18-Oct-2023].

[7]	“¿Sabes para qué sirven los filtros y cuáles son los valores recomendados?,” CardioTeca, 05-Jul-2023. [Online]. Available: https://www.cardioteca.com/pildoras-ecg/5017-sabes-para-que-sirven-los-filtros-y-cuales-son-los-valores-recomendados.html. [Accessed: 18-Oct-2023].
