Nuestro equipo tuvo éxito generando señales cuadradas, triangulares y senoidales utilizando un generador de funciones y visualizándolas correctamente en un osciloscopio. Sin embargo, al intentar leer estas señales con un Arduino Nano 33 IoT y enviar los datos a una laptop, surgieron problemas.

Algunas posibles fuentes de error fueron:

Frecuencia de Muestreo Inadecuada: Las señales de interés (cuadradas, triangulares y senoidales) pueden tener componentes de alta frecuencia. Si la frecuencia de muestreo del Arduino no es lo suficientemente alta, podría perder detalles importantes de la señal. Esto puede llevar a mediciones inexactas y a la incapacidad de capturar correctamente la forma de onda deseada.

Aliasing: Si la frecuencia de muestreo del Arduino es demasiado baja en comparación con la frecuencia de la señal, se puede producir aliasing. El aliasing ocurre cuando las frecuencias de alta frecuencia se interpretan incorrectamente como frecuencias más bajas debido a una frecuencia de muestreo insuficiente. Esto puede distorsionar la forma de onda y dificultar la reconstrucción precisa de la señal original.

Resolución de ADC Insuficiente: Los microcontroladores, como el Arduino Nano 33 IoT, tienen un Convertidor Analógico-Digital (ADC) que convierte la señal analógica en valores digitales. Si la resolución del ADC es insuficiente en comparación con la amplitud de la señal, se pueden perder detalles finos de la señal y obtener mediciones incorrectas.

Ruido y Perturbaciones: Los microcontroladores están sujetos a ruido eléctrico y perturbaciones en el entorno. Esto puede introducir errores en las mediciones y afectar la precisión de las señales capturadas.

Problemas de Conexión: Las conexiones eléctricas entre el generador de funciones y el Arduino pueden causar problemas si no están aseguradas adecuadamente. Conexiones flojas o inestables pueden llevar a mediciones inconsistentes o incorrectas.

Sobrecarga de Procesamiento: Si el código en el Arduino consume demasiados recursos de procesamiento, podría afectar la capacidad del dispositivo para tomar lecturas precisas a intervalos regulares.
