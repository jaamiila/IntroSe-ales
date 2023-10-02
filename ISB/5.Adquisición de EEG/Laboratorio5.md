<html>
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
  </head>
  <body class="c23 doc-content">

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)
6. [Discusión](#id5)
7. [Conclusiones](#id6)
8. [Referencias](#id7)

<h2 class="c17"><span class="c5">Introducci&oacute;n:</span></h2><a name="id0"></a>
<p align="justify">
  En el ámbito de la investigación biomédica, la adquisición de señales del tipo Electroencefalograma (EEG) desempeña un papel fundamental en el estudio de la actividad cerebral. En este informe de laboratorio, abordaremos la adquisición de señales EEG utilizando dos métodos distintos: el módulo Bitalino y el ultracortex de OpenGUI. Estos métodos permiten la captura de señales eléctricas cerebrales, brindando información cuantificable de la actividad neural y abriendo nuevas oportunidades para la investigación y el diagnóstico médico.
</p>

<h2 class="c17"><span class="c5">Objetivos:</span></h2><a name="id1"></a>
<body>
    <ul>
        <li>Adquirir señales biomédicas de EEG.</li>
        <li>Hacer un correcto uso del Ultracortex.</li>
        <li>Extraer la información de la señal EEG con ayuda del software OpenSignals y representar la información de forma gráfica.</li>
    </ul>

<h2 class="c17"><span class="c5">Materiales y equipos:</span></h2><a name="id2"></a>
<body>
    <ul>
        <li>1 Kit BiTalino modelo (R)EVOLUTION
        <li>1 Ultracortex	modelo Mark IV	
        <li>1 Laptop o PC

<h2 class="c17"><span class="c5">Procedimiento:</span></h2><a name="id3"></a>

  ### Fotos de conexión usada en el UltraCortex
  foto
  
  ## Ploteo de la señal en OpenBCI GUI
  <p align="justify">
  OpenBCI es una herramienta open-source diseñada enfocada en biosensores y neurociencia, cuyo objetivo es disminuir la barrera existente al mundo de la interfaz     computador cerebro, manteniendo la protección del consumidor de manera ética.[1]
  </p>
  imagen ultra cortex
  
  <p align="justify">
  En nuestro laboratorio se llegó a colocar el Ultra Cortex en uno de los integrantes, pero debido a falta de tiempo y problemas de conexión con la laptop no se      llegó a observar la onda cerebral de nuestro compañero, debido a eso se presentará una idea de lo que se debió obtener en el laboratorio así como nuestra           interpretación.
  </p>
  instalacion

  <p align="justify">
  De las imágenes y videos vistos anteriormente se debió obtener la siguiente gráfica estando en diferentes estados, uno en reposo, el segundo parpadeando y por      último preguntas para realizar esfuerzo mental.
  </p>
  interfaz deseada
  deseada reposo
  deseada parpadeo
  deseada preguntas
  
  <p align="justify">
  Como se observa se usó la misma metodología para ambos casos, pero solo se ploteara la señal obtenida usando el Open Signals debido a los problemas mencionados     anteriormente.
  </p>

  ### Fotos de conexión usada en el EEG
  Foto

  ## Video de señal mostrando el punto 1,2 y 4 del procedimiento
  video
  
  ## Ploteo de la señal en Python
  plot
  
  ## Explicación de la señal ploteada
  <p align="justify">
  *Paso 1*: Registro de la línea base (30 segundos)
  En este paso, se registra una señal de EEG en condiciones de reposo, sin movimiento y con una respiración normal. Esto proporciona una referencia de la actividad   cerebral en un estado de calma. En este período, esperaríamos ver una señal EEG relativamente estable y con poco ruido, con patrones de actividad cerebral          típicos en un estado de reposo.

  *Lo que se espera de este paso*:  En un estado de reposo, la señal EEG típicamente mostraría patrones de actividad cerebral relacionados con un cerebro en calma     y sin una actividad cognitiva o física significativa. Las características comunes de esta señal incluirían:

  Actividad Alfa: Durante los ojos cerrados y en un estado de reposo tranquilo, podríamos esperar ver una actividad alfa prominente en la señal EEG. La actividad     alfa se encuentra típicamente en el rango de frecuencia de 8-13 Hz y es indicativa de un estado relajado de la mente.

  Baja Amplitud: En este estado, la amplitud de la señal EEG sería relativamente baja, lo que significa que las oscilaciones de voltaje en la señal son suaves y no   muy pronunciadas.

  Poca Variabilidad: Habría poca variabilidad en la señal, ya que el cerebro no está involucrado en tareas cognitivas o físicas activas.

  *Lo que se obtuvo en los resultados*: Se puede observar en la imagen el ruido que existe como picos en la amplitud de la señal que se pueden interpretar como       interferencia por el movimiento, mala colocación de los electrodos, de igual forma la amplitud de la señal EEG sería relativamente baja, lo que significa que las   oscilaciones de voltaje en la señal son suaves y no muy pronunciadas.
  </p>
  plot
  
 <p align="justify">
 *Paso 2*: Ciclo de OJOS ABIERTOS - OJOS CERRADOS (5 repeticiones)
En este paso, se alterna entre períodos de ojos abiertos y ojos cerrados durante 5 segundos cada uno. Esto se hace repetidamente cinco veces. Durante la fase de ojos cerrados, es probable que veamos un aumento en la amplitud de la actividad alfa en el EEG, que es una característica típica de los patrones de descanso. Durante la fase de ojos abiertos, es probable que esta actividad alfa disminuya y veamos una mayor variabilidad en la señal debido a la entrada visual.[2][3][4]

*Lo que se espera de este paso*: Cuando parpadeas, es probable que veas una interrupción temporal en la señal EEG. Esto se debe a que el acto de parpadear puede causar un cambio en la impedancia entre los electrodos y la piel, lo que puede generar artefactos en la señal. Estos artefactos se manifestarían como picos o caídas bruscas en la señal EEG durante el parpadeo.[5]

Picos de Artefacto: Verías picos de artefacto en la señal EEG en el momento en que ocurre el parpadeo. Estos picos pueden ser temporales y de corta duración.

Lo que se obtuvo en los resultados: Se puede visualizar efectivamente mayores picos y momentos de amplitud alta constante por instantes de tiempo (Ojos abiertos de 5 seg). Además de los mencionados picos de artefacto en la señal EEG en el momento en que ocurre el parpadeo.


*Paso 3*: Registro de otra línea base de referencia (30 segundos)
Después de completar el ciclo de ojos abiertos y ojos cerrados, se registra nuevamente una línea base similar a la del Paso 1. Esto permite comparar la actividad cerebral después de la estimulación visual de los ojos abiertos con la actividad en reposo.

*Lo que se espera de este paso*: En un estado de reposo, la señal EEG típicamente mostraría patrones de actividad cerebral relacionados con un cerebro en calma y sin una actividad cognitiva o física significativa al igual que en el paso 1.
*Lo que se obtuvo en los resultados*: Resultado similar al paso 1.
foto


  
