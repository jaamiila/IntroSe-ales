# Introduccion a Señales Biomedicas - Grupo 4
#### *Unidades del curso*
1. Introducción, adquisición y principios fisiológicos de las señales biomédicas
2. Análisis de ECG, EMG y EEG
3. Introducción al tratamiento digital de señales
4. Informática biomédica e introducción a la inteligencia artificial en señales biomédicas

### ¿Que son las señales biomedicas?
<p align="justify">Son señales electricas, mecanicas, opticas o alguna otra senal que provengan del cuerpo humano y que contenga informacion relacionada a algun proceso biologico, fisiologico o patologico. Son fundamentales para el diagnostico, monitoreo y estudio de las enfermedades.

### Propuesta de proyecto
<p align="justify">Nuestro propuesta de proyecto es un dispositivo de deteccion de convulsiones mediante el uso del electroencefalograma (EEG) para evaluar la actividad electrica en cerebro.

### ¿Quienes somos?
<p align="justify">Somos estudiantes de la carrera de Ingenieria Biomedica de la Universidad Peruana Cayetano Heridia y Pontificia Universidad Catolica del Peru.

### Integrantes:
  * Jamila Vitella 
    <p align="justify"> Estudiante de octavo ciclo de Ingeniería Biomédica. Me considero responsable y creativa. Me gusta mucho la parte tecnológica de mi carrera ya que nos incentiva a ser más críticos e innovar a través de la ciencia. Me gustaria especializarme en el area de Ingenieria de Tejidos y Biomateriales.
  * Diego Romero
    <p align="justify"> Estudiante de octavo ciclo de Ingenieria Biomédica con gran admiración a la gestión de salud y futura especialización en Ingeniería Clínica. Me gustaria mejorar la calidad de vida de los pacientes en el sector público.
  * Claudia Zavaleta
    <p align="justify"> Estudiante de octavo ciclo de Ingeniería Biomédica con especial interés en el campo de Ingeniería de Tejidos y Biomateriales. Me considero una persona responsable y comprometida a mejorar el sistema de salud del país.

  * Eisel Pinado
    <p align="justify"> Estudiante de octavo ciclo de Ingenieria Biomédica con interes particular en el ámbito de Ingenieria Clinica. Me considero una persona enfocada a sus proyectos y de mente abierta a nuevas ideas.

 <img src="Imagenes/fotogrupal.jpeg" height="450">   

### Docentes del curso
- Lewis de la Cruz - umbert.de.la.cruz@upch.pe
- Moises Meza - moises.meza@upch.pe
- José Alonso Cáceres - jo.alonsok@gmail.com
- Avid Roman - avid.roman.g@upch.pe

### Ploteo de señales en Arduino IDE
<p align="justify">Nuestro equipo tuvo éxito generando señales cuadradas, triangulares y senoidales utilizando un generador de funciones y visualizándolas correctamente en un osciloscopio. Sin embargo, al intentar leer estas señales con un Arduino Nano 33 IoT y enviar los datos a una laptop, surgieron algunos inconvenientes al leer la señal.

<p align="justify">Algunas posibles fuentes de error fueron:

<p align="justify">Frecuencia Inadecuada: Pudo suceder que la frecuencia de muestreo del Arduino es demasiado baja en comparación con la frecuencia de la señal, se puede producir aliasing. El aliasing ocurre cuando las frecuencias de alta frecuencia se interpretan incorrectamente como frecuencias más bajas debido a una frecuencia de muestreo insuficiente. Esto puede distorsionar la forma de onda y dificultar la reconstrucción precisa de la señal original. 

<p align="justify">Resolución de ADC Insuficiente: Los microcontroladores, como el Arduino Nano 33 IoT, tienen un Convertidor Analógico-Digital (ADC) que convierte la señal analógica en valores digitales. Si la resolución del ADC es insuficiente en comparación con la amplitud de la señal, se pueden perder detalles finos de la señal y obtener mediciones incorrectas.

<p align="justify">Ruido y Perturbaciones: Los microcontroladores están sujetos a ruido eléctrico y perturbaciones en el entorno. Esto puede introducir errores en las mediciones y afectar la precisión de las señales capturadas.

<p align="justify">Problemas de Conexión: Las conexiones eléctricas entre el generador de funciones y el Arduino pueden causar problemas si no están aseguradas adecuadamente. Conexiones flojas o inestables pueden llevar a mediciones inconsistentes o incorrectas.

