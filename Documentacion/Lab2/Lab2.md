Nuestro equipo tuvo éxito generando señales cuadradas, triangulares y senoidales utilizando un generador de funciones y visualizándolas correctamente en un osciloscopio. Sin embargo, al intentar leer estas señales con un Arduino Nano 33 IoT y enviar los datos a una laptop, surgieron problemas al leer la señal.
Para obtener las señales

###Algunas posibles fuentes de error fueron:

  *Frecuencia Inadecuada: 
  <p align="justify">Si la frecuencia de muestreo del Arduino es demasiado baja en comparación con la frecuencia de la señal, se puede producir aliasing. El aliasing ocurre cuando las frecuencias de alta frecuencia se interpretan incorrectamente como frecuencias más bajas debido a una frecuencia de muestreo insuficiente. Esto puede distorsionar la forma de onda y dificultar la reconstrucción precisa de la señal original. 

  *Resolución de ADC Insuficiente: 
  <p align="justify">Los microcontroladores, como el Arduino Nano 33 IoT, tienen un Convertidor Analógico-Digital (ADC) que convierte la señal analógica en valores digitales. Si la resolución del ADC es insuficiente en comparación con la amplitud de la señal, se pueden perder detalles finos de la señal y obtener mediciones incorrectas.

  *Ruido y Perturbaciones: 
  <p align="justify">Los microcontroladores están sujetos a ruido eléctrico y perturbaciones en el entorno. Esto puede introducir errores en las mediciones y afectar la precisión de las señales capturadas.

  *Problemas de Conexión: 
  <p align="justify">Las conexiones eléctricas entre el generador de funciones y el Arduino pueden causar problemas si no están aseguradas adecuadamente. Conexiones flojas o inestables pueden llevar a mediciones inconsistentes o incorrectas.

Uno de los resultados obtenidos fueron los siguientes:

https://github.com/jaamiila/IntroSe-ales/assets/142609599/e2c74fa3-972b-4326-a5a9-5550a7ac4fb7

https://github.com/jaamiila/IntroSe-ales/assets/142609599/ebf175bf-82b3-4e12-8122-4b3cf93f4553

Donde se puede observar como las ondas tienden a las formas queridas, pero no llega a ser la querida, 
