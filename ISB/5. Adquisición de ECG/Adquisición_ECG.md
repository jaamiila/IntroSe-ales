<html>
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
  </head>
  <body class="c23 doc-content">
    # **LABORATORIO 4: – Uso de BiTalino para ECG**

# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [¿Que es un ECG?](#id3)
5. [Procedimiento](#id4)
6. [Resultados](#id5)
7. [Discucion](#id6)
8. [Conclusiones](#id7)
9. [Referencias](#id8).

    <h2 class="c17"><span class="c5">Introducci&oacute;n:</span></h2><a name="id0"></a>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >El estudio de se&ntilde;ales biom&eacute;dicas, como las se&ntilde;ales
        electromiogr&aacute;ficas (EMG) y electrocardiogr&aacute;ficas (ECG),
        desempe&ntilde;a un papel fundamental en la comprensi&oacute;n de la
        actividad muscular y card&iacute;aca, respectivamente. En esta
        pr&aacute;ctica de laboratorio, nuestro objetivo principal fue adquirir
        y analizar estas se&ntilde;ales utilizando el sistema BiTalino y el
        software OpenSignals (r)evolution. Para lograr esto, configuramos
        adecuadamente el equipo, realizamos conexiones con electrodos en el
        cuerpo de nuestros compa&ntilde;eros estudiantes y registramos las
        se&ntilde;ales EMG y ECG en diferentes condiciones.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">Objetivos espec&iacute;ficos:</span></h2><a name="id1"></a>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >1. Adquirir se&ntilde;ales biom&eacute;dicas de EMG y ECG: Durante la
        pr&aacute;ctica, adquirimos se&ntilde;ales EMG para estudiar la
        actividad muscular y se&ntilde;ales ECG para analizar la actividad
        el&eacute;ctrica del coraz&oacute;n. Estas se&ntilde;ales nos
        proporcionaron informaci&oacute;n valiosa sobre la actividad
        fisiol&oacute;gica de los sujetos.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >2. Hacer una correcta configuraci&oacute;n de BiTalino: La
        configuraci&oacute;n adecuada del dispositivo BiTalino es esencial para
        garantizar la calidad y precisi&oacute;n de las se&ntilde;ales
        registradas. Esto incluy&oacute; la selecci&oacute;n de los canales
        adecuados, la calibraci&oacute;n y la configuraci&oacute;n de la
        frecuencia de muestreo.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >3. Extraer la informaci&oacute;n de las se&ntilde;ales EMG y ECG del
        software OpenSignals (r)evolution: Utilizamos el software OpenSignals
        (r)evolution para adquirir y visualizar las se&ntilde;ales en tiempo
        real. Adem&aacute;s, este software nos permiti&oacute; grabar los datos
        para su posterior an&aacute;lisis y procesamiento.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >4. Fotos de conexi&oacute;n usada (Electrodos-cuerpo, BiTalino-cables):
        Documentamos visualmente las conexiones entre los electrodos y el cuerpo
        de los sujetos, as&iacute; como la conexi&oacute;n de los cables al
        dispositivo BiTalino para tener un registro completo de nuestra
        configuraci&oacute;n experimental.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >5. Video de se&ntilde;al en silencio el&eacute;ctrico o reposo:
        Grabamos un video que mostraba las conexiones de los electrodos al
        cuerpo de los sujetos en estado de reposo, sin actividad muscular
        significativa. Este video servir&aacute; como referencia visual para la
        condici&oacute;n de referencia.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >6. Ploteo de la se&ntilde;al en OpenSignals: Despu&eacute;s de adquirir
        los datos, ploteamos las se&ntilde;ales EMG y ECG en tiempo real en el
        software OpenSignals (r)evolution para observar la actividad muscular y
        card&iacute;aca en funci&oacute;n del tiempo.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >7. Resumen y explicaci&oacute;n de la se&ntilde;al ploteada: Analizamos
        las se&ntilde;ales registradas, identificamos los patrones y
        caracter&iacute;sticas relevantes en las se&ntilde;ales EMG y ECG y
        proporcionamos una explicaci&oacute;n detallada de lo observado.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >8. El archivo de los datos de la se&ntilde;al ploteada: Guardamos los
        datos registrados en un archivo para su posterior an&aacute;lisis y
        procesamiento. Estos datos se utilizar&aacute;n para investigaciones
        posteriores y an&aacute;lisis m&aacute;s detallados.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >9. Ploteo de la se&ntilde;al en Python: Adem&aacute;s de utilizar el
        software OpenSignals, tambi&eacute;n ploteamos las se&ntilde;ales
        biom&eacute;dicas utilizando Python para aprender c&oacute;mo procesar y
        analizar los datos de manera m&aacute;s personalizada.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >En este informe de laboratorio, presentaremos los resultados y
        an&aacute;lisis obtenidos de acuerdo con los objetivos
        espec&iacute;ficos mencionados anteriormente. El estudio de
        se&ntilde;ales biom&eacute;dicas es esencial en la investigaci&oacute;n
        m&eacute;dica y la tecnolog&iacute;a de la salud, y esta pr&aacute;ctica
        nos proporcion&oacute; una valiosa experiencia en la adquisici&oacute;n
        y an&aacute;lisis de estas se&ntilde;ales.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">Materiales y equipo:</span></h2><a name="id2"></a>
    <p class="c8"><span class="c5"></span></p>
    <a id="t.f2a3bc886aaf4bf27e671900f975c113874ee695"></a><a id="t.0"></a>
    <table class="c36">
      <tr class="c29">
        <td class="c34" colspan="2" rowspan="1">
          <p class="c16"><span class="c24 c15">Equipo | Materiales</span></p>
        </td>
        <td class="c7" colspan="1" rowspan="2">
          <p class="c16"><span class="c24 c15">Cantidad</span></p>
        </td>
      </tr>
      <tr class="c29">
        <td class="c33" colspan="1" rowspan="1">
          <p class="c16"><span class="c24 c15">Modelo</span></p>
        </td>
        <td class="c27" colspan="1" rowspan="1">
          <p class="c16"><span class="c24 c15">Descripci&oacute;n</span></p>
        </td>
      </tr>
      <tr class="c29">
        <td class="c33" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">( R )EVOLUTION</span></p>
        </td>
        <td class="c27" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">Kit BITalino &nbsp;</span></p>
        </td>
        <td class="c7" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">1</span></p>
        </td>
      </tr>
      <tr class="c29">
        <td class="c33" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">-</span></p>
        </td>
        <td class="c27" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">Laptop o PC </span></p>
        </td>
        <td class="c7" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">1</span></p>
        </td>
      </tr>
      <tr class="c29">
        <td class="c33" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">-</span></p>
        </td>
        <td class="c27" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">Parches de electrodos</span></p>
        </td>
        <td class="c7" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">6</span></p>
        </td>
      </tr>
      <tr class="c29">
        <td class="c33" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">Fluke Biomedical</span></p>
        </td>
        <td class="c27" colspan="1" rowspan="1">
          <p class="c16">
            <span class="c2">ProSim&trade; 4 Vital Signs Simulator</span>
          </p>
        </td>
        <td class="c7" colspan="1" rowspan="1">
          <p class="c16"><span class="c2">1</span></p>
        </td>
      </tr>
    </table>
    <p class="c8"><span class="c5"></span></p>
    <p class="c17">
      <span class="c2"
        >Adicionalmente cabe mencionar que para el desarrollo del presente
        laboratorio nos basamos en los siguientes documentos:</span
      >
    </p>
    <ul class="c10 lst-kix_53ap384ualt-0 start">
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Gu&iacute;as de pr&aacute;ctica cl&iacute;nica de la Sociedad
          Espa&ntilde;ola de Cardiolog&iacute;a en pruebas de esfuerzo [1]</span
        >
      </li>
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Protocolo del procedimiento de colocaci&oacute;n de derivaciones de
          ECG de Mindray [2]</span
        >
      </li>
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Gu&iacute;a de laboratorio para ECG BITalino (r)evolution [3]</span
        >
      </li>
    </ul>
    <p class="c8 c19"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">&iquest;Qu&eacute; es un ECG?</span></h2><a name="id3"></a>
    <p class="c17">
      <span
        >Un electrocardiograma(ECG) es un procedimiento indoloro y no invasivo
        que ayuda a diagnosticar varios problemas card&iacute;acos usando las
        se&ntilde;ales el&eacute;ctricas que registra del coraz&oacute;n[4].
        Puede detectar </span
      ><span class="c38">&nbsp;afecciones como:</span>
    </p>
    <p class="c8"><span class="c38"></span></p>
    <ul class="c10 lst-kix_bwajciisvt6j-0 start">
      <li class="c19 c25 li-bullet-0"><span class="c1">Arritmia</span></li>
      <li class="c25 c19 li-bullet-0">
        <span class="c1">Cardiomiopat&iacute;a</span>
      </li>
      <li class="c25 c19 li-bullet-0">
        <span class="c1">Enfermedad de las arterias coronarias</span>
      </li>
      <li class="c25 c19 li-bullet-0">
        <span class="c1">Ataque cardiaco</span>
      </li>
      <li class="c25 c19 li-bullet-0">
        <span class="c1">Insuficiencia cardiaca</span>
      </li>
      <li class="c25 c19 li-bullet-0">
        <span class="c1"
          >Enfermedades de las v&aacute;lvulas del coraz&oacute;n</span
        >
      </li>
      <li class="c25 c19 li-bullet-0">
        <span class="c39">Defectos card&iacute;acos cong&eacute;nitos</span>
      </li>
    </ul>
    <h2 class="c17">
      <span class="c5">&iquest;Qu&eacute; se observa en un ECG?</span>
    </h2>
    <p class="c17">
      <span class="c2"
        >El electrocardiograma es un conjunto de ondas llamadas P, Q, R, S, T y
        U de acuerdo con el orden de aparici&oacute;n en el tiempo, en el
        laboratorio nos centraremos en 3 se&ntilde;ales:</span
      >
    </p>
    <ul class="c10 lst-kix_7p60wf74cab1-0 start">
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Onda P: se inscribe como resultado de la activaci&oacute;n
          auricular.</span
        >
      </li>
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Arreglo Q, R y S: integran el complejo ventricular por la
          propagaci&oacute;n de la onda de excitaci&oacute;n a la musculatura de
          ambos ventr&iacute;culos y al tabique interventricular.</span
        >
      </li>
      <li class="c13 li-bullet-0">
        <span class="c2"
          >Onda T: la expresi&oacute;n del restaurador proceso de
          repolarizaci&oacute;n[5]</span
        >
      </li>
    </ul>
    <p class="c8 c19"><span class="c2"></span></p>
    <p class="c26 c19" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 427.42px;
          height: 320.92px;
        "
        ><img
          alt=""
          src="images/image8.png"
          style="
            width: 427.42px;
            height: 320.92px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c26 c19" align="center">
      <span class="c2" align="center">Img.1 Gr&aacute;fica ECG explicada[6]</span>
    </p>
    <p class="c8 c19"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >Los equipos con los que se realiza el electrocardiograma vienen dotados
        de un selector de derivaciones, de modo que &eacute;stas se toman
        siempre en el mismo orden, se tienen 12 derivaciones seis derivaciones
        est&aacute;ndar y seis derivaciones precordiales, las seis precordiales
        son : V1, V2, V3, V4, V5 y V6.</span
      >
    </p>
    <p class="c8"><span class="c5"></span></p>
    <p class="c26" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 275.75px;
          height: 278.91px;
        "
        ><img
          alt=""
          src="images/image5.png"
          style="
            width: 275.75px;
            height: 278.91px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c26" align="center"><span>Img.2 Ubicaci&oacute;n de derivaciones[7]</span></p>
    <p class="c8"><span class="c5"></span></p>
    <h2 class="c17"><span class="c5">Procedimiento:</span></h2><a name="id4"></a>
    <ol class="c10 lst-kix_mnifvcvxdhvy-0 start" start="1">
      <li class="c18 c37 li-bullet-0">
        <span class="c2">Preparaci&oacute;n del paciente</span>
      </li>
    </ol>
    <p class="c22 c19"><span class="c2"></span></p>
    <p class="c18">
      <span class="c2"
        >Antes de hacer cualquier procedimiento de experimentaci&oacute;n es
        necesario preparar adecuadamente al paciente. Esta preparaci&oacute;n
        incluye:
      </span>
    </p>
    <p class="c22 c19"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0 start">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Comunicaci&oacute;n con el paciente: Explicar el procedimiento del
          ECG y asegurar que comprenda lo que se espera de &eacute;l.
        </span>
      </li>
    </ul>
    <p class="c4"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Vestimenta adecuada: Verificar que el paciente lleve ropa que permita
          acceder a las &aacute;reas donde se colocar&aacute;n los electrodos.
        </span>
      </li>
    </ul>
    <p class="c4"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Preparaci&oacute;n de la piel: Limpiar la piel del paciente en las
          &aacute;reas donde se colocar&aacute;n los electrodos.</span
        >
      </li>
    </ul>
    <p class="c22"><span class="c2"></span></p>
    <p class="c4"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Posici&oacute;n y estado del paciente: Indicar al paciente la
          posici&oacute;n en la que debe estar y solicitar que permanezca lo
          m&aacute;s relajado y tranquilo posible, ya que el movimiento y la
          ansiedad pueden afectar los resultados.
        </span>
      </li>
    </ul>
    <p class="c4"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Duraci&oacute;n de la prueba: Informar al paciente sobre la
          duraci&oacute;n estimada de la prueba.</span
        >
      </li>
    </ul>
    <p class="c22"><span class="c2"></span></p>
    <ul class="c10 lst-kix_qkki3vljkzlv-0">
      <li class="c9 li-bullet-0">
        <span class="c2"
          >Paciente con implantes y accesorios met&aacute;licos: Verificar que
          el paciente no cuente con implantes met&aacute;licos, ni tampoco
          accesorios met&aacute;licos que se encuentren cerca de los electrodos
          porque al realizar el ECG, estos pueden interferir con el equipo.
        </span>
      </li>
    </ul>
    <p class="c8 c19"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-0" start="2">
      <li class="c13 li-bullet-0">
        <span class="c2">Realizaci&oacute;n de la prueba</span>
      </li>
    </ol>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1 start" start="1">
      <li class="c17 c21 li-bullet-0"><span class="c2">Protocolo</span></li>
    </ol>
    <p class="c6"><span class="c2"></span></p>
    <a id="t.85bee8d58ecfc0b816cce2e4c88c9acc30b2c9b3"></a><a id="t.1"></a>
    <table class="c12">
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">N&deg; de orden</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">Actividad</span></p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">1</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2"
              >Preparaci&oacute;n y consentimiento del paciente</span
            >
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">2</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2">Colocaci&oacute;n de los electrodos</span>
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">3</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2"
              >Adquisici&oacute;n de datos en estado de reposo</span
            >
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">4</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2"
              >Adquisici&oacute;n de datos al contener la
              respiraci&oacute;n</span
            >
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">5</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2">Prueba de esfuerzo realizada por el paciente</span>
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">6</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2"
              >Adquisici&oacute;n de datos despu&eacute;s del estr&eacute;s
              f&iacute;sico</span
            >
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">7</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2">Desprendimiento de los electrodos</span>
          </p>
        </td>
      </tr>
      <tr class="c14">
        <td class="c20" colspan="1" rowspan="1">
          <p class="c0"><span class="c2">8</span></p>
        </td>
        <td class="c32" colspan="1" rowspan="1">
          <p class="c0">
            <span class="c2"
              >Procesamiento de informaci&oacute;n asegurando anonimato</span
            >
          </p>
        </td>
      </tr>
    </table>
    <p class="c6"><span class="c2"></span></p>
    <p class="c6"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1" start="2">
      <li class="c17 c21 li-bullet-0">
        <span class="c2">Colocaci&oacute;n de los electrodos</span>
      </li>
    </ol>
    <p class="c11" align="center">
      <div align="center">
        <img src="images/image10.png" alt="" width="112.5px" height="148.19px" style="display:inline-block;">
        <img src="images/image7.png" alt="" width="110.5px" height="147.06px" style="display:inline-block;">
        <img src="images/image9.png" alt="" width="109.5px" height="146px" style="display:inline-block;">
        <img src="images/image1.png" alt="" width="111.5px" height="148.83px" style="display:inline-block;">
      </div>
    </p>
    <p class="c8"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1" start="3">
      <li class="c17 c21 li-bullet-0">
        <span class="c2">Adquisici&oacute;n y registro de datos en reposo</span>
      </li>
    </ol>
    <p class="c17 c30">
      <span class="c2"
        >En esta primera situaci&oacute;n, se registr&oacute; el
        electrocardiograma (ECG) del sujeto mientras se encontraba en un estado
        de reposo al estar sentado en una posici&oacute;n c&oacute;moda y no
        estaba sometido a ning&uacute;n tipo de estr&eacute;s o esfuerzo
        f&iacute;sico. Este estado de reposo proporciona una l&iacute;nea de
        base para evaluar la actividad el&eacute;ctrica del coraz&oacute;n en
        condiciones normales.</span
      >
    </p>
    <p class="c6"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1" start="4">
      <li class="c17 c21 li-bullet-0">
        <span class="c2"
          >Adquisici&oacute;n y registro de datos al contener la
          respiraci&oacute;n</span
        >
      </li>
    </ol>
    <p class="c17 c30">
      <span class="c2"
        >En segunda instancia, el paciente fue instruido para contener la
        respiraci&oacute;n durante un per&iacute;odo de tiempo determinado
        mientras se registraba el ECG. Durante este procedimiento, el paciente
        mantuvo una posici&oacute;n similar a la de reposo, pero se le
        pidi&oacute; que detuviera la respiraci&oacute;n voluntariamente. Esto
        puede revelar informaci&oacute;n sobre la respuesta del sistema
        cardiovascular a la hipoxia o la falta de ox&iacute;geno debido a la
        retenci&oacute;n de aire en los pulmones.</span
      >
    </p>
    <p class="c6"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1" start="5">
      <li class="c17 c21 li-bullet-0">
        <span class="c2"
          >Registro de datos despu&eacute;s de realizar actividad
          f&iacute;sica</span
        >
      </li>
    </ol>
    <p class="c17 c30">
      <span class="c2"
        >En la tercera situaci&oacute;n, el paciente realiz&oacute; actividad
        f&iacute;sica espec&iacute;fica, como ejercicio moderado o una caminata,
        antes de que se registrara el ECG. Esta situaci&oacute;n eval&uacute;a
        la respuesta del coraz&oacute;n y del sistema cardiovascular a la
        demanda aumentada de ox&iacute;geno y energ&iacute;a que se produce
        durante la actividad f&iacute;sica. La frecuencia card&iacute;aca, la
        variabilidad del ritmo card&iacute;aco y otros par&aacute;metros del ECG
        pueden cambiar significativamente en comparaci&oacute;n con el estado de
        reposo.</span
      >
    </p>
    <p class="c6"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-1" start="6">
      <li class="c17 c21 li-bullet-0">
        <span class="c2">Desprendimiento de electrodos</span>
      </li>
    </ol>
    <p class="c6"><span class="c2"></span></p>
    <p class="c6"><span class="c2"></span></p>
    <ol class="c10 lst-kix_mnifvcvxdhvy-0" start="3">
      <li class="c13 li-bullet-0">
        <span class="c2">Uso del simulador ProSim4</span>
      </li>
    </ol>
    <p class="c8 c19"><span class="c2"></span></p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c8"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">Resultados:</span></h2><a name="id5"></a>
    <h2 class="c17"><span class="c5">Discusi&oacute;n:</span></h2><a name="id6"></a>
    <ul class="c10 lst-kix_ic9oo7po0cv4-0 start">
      <li class="c13 c28 li-bullet-0"><span class="c2"></span></li>
    </ul>
    <p class="c17" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 205.58px;
          height: 260.5px;
        "
        ><img
          alt=""
          src="images/image6.png"
          style="
            width: 205.58px;
            height: 260.5px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c8"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">Posibles fuentes de error:</span></h2>
    <p class="c17" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 288.84px;
          height: 202.24px;
        "
        ><img
          alt=""
          src="images/image2.png"
          style="
            width: 288.84px;
            height: 202.24px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c17" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 601.7px;
          height: 393.33px;
        "
        ><img
          alt=""
          src="images/image3.png"
          style="
            width: 601.7px;
            height: 393.33px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c17" align="center">
      <span
        style="
          overflow: hidden;
          display: inline-block;
          margin: 0px 0px;
          border: 0px solid #000000;
          transform: rotate(0rad) translateZ(0px);
          -webkit-transform: rotate(0rad) translateZ(0px);
          width: 601.7px;
          height: 325.33px;
        "
        ><img
          alt=""
          src="images/image4.png"
          style="
            width: 601.7px;
            height: 325.33px;
            margin-left: 0px;
            margin-top: 0px;
            transform: rotate(0rad) translateZ(0px);
            -webkit-transform: rotate(0rad) translateZ(0px);
          "
          title=""
      /></span>
    </p>
    <p class="c8"><span class="c5"></span></p>
    <p class="c17">
      <span class="c35" ><b>Aclaraci&oacute;n Importante (Disclaimer) :</b></span>
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >Deseamos informar que, lamentablemente, no fue posible llevar a cabo
        pruebas con el simulador SimPro4 en esta ocasi&oacute;n debido a
        restricciones de tiempo. A pesar de nuestro esfuerzos las circunstancias
        no permitieron completar dicho proceso dentro del plazo
        estipulado.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >Reconocemos la importancia de realizar pruebas exhaustivas y precisas
        con el simulador para obtener resultados confiables. Por lo tanto, nos
        disculpamos por cualquier molestia que haya surgido como
        resultado.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span class="c2"
        >Agradecemos su comprensi&oacute;n y colaboraci&oacute;n en este asunto,
        y estamos comprometidos a tomar las medidas necesarias para garantizar
        que futuros proyectos cuenten con el tiempo y los recursos adecuados
        para llevar a cabo pruebas rigurosas y exhaustivas con el simulador
        SimPro4.</span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17"><span class="c2">Atentamente,</span></p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17"><span class="c2">Grupo 4</span></p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c8"><span class="c2"></span></p>
    <h2 class="c17"><span class="c5">Concluci&oacute;n:</span></h2><a name="id7"></a>
    <h2 class="c17"><span class="c5">Referencias:</span></h2><a name="id8"></a>
    <p class="c17">
      <span>[1] Ar&oacute;s </span><span class="c15">et al.</span
      ><span>&nbsp;(2013) </span
      ><span class="c15"
        >Gu&iacute;as de Pr&aacute;ctica Cl&iacute;nica de la sociedad
        espa&ntilde;ola de cardiolog&iacute;a en pruebas de Esfuerzo</span
      ><span>, </span
      ><span class="c15">Revista Espa&ntilde;ola de Cardiolog&iacute;a</span
      ><span class="c2"
        >. Available at:
        https://www.sciencedirect.com/science/article/abs/pii/S0300893200752109
        (Accessed: 16 September 2023).
      </span>
    </p>
    <p class="c8"><span class="c15 c24"></span></p>
    <p class="c17">
      <span class="c15"
        >[2] ECG lead Placement Proc 7664REVA - Mindray North America</span
      ><span>&nbsp;(no date) </span
      ><span class="c15">Panorama&reg; ECG Lead Placement Procedure </span
      ><span class="c2"
        >. Available at:
        https://www.mindraynorthamerica.com/cmsAdmin/uploads/ecg-lead-placement-proc-7664reva.pdf
        (Accessed: 16 September 2023).
      </span>
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span>[3] </span
      ><span class="c15"
        >Electrocardiography (ECG) Sensor User Manual - Plux Biosignals</span
      ><span>&nbsp;(no date) </span
      ><span class="c15">BITalino (r)evolution Lab Guide</span
      ><span class="c2"
        >. Available at:
        https://support.pluxbiosignals.com/wp-content/uploads/2021/10/biosignalsplux-Electrocardiography-ECG-User-Manual.pdf
        (Accessed: 16 September 2023).
      </span>
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span>[4] </span
      ><span
        >&ldquo;Electrocardiogram (ECG or EKG) - Mayo Clinic&rdquo;. Top-ranked
        Hospital in the Nation &ndash; Mayo Clinic. Accedido el 17 de septiembre
        de 2023. [En l&iacute;nea]. Disponible: </span
      ><span
        ><a
          class="c31"
          href="https://www.google.com/url?q=https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983&amp;sa=D&amp;source=editors&amp;ust=1695004180889169&amp;usg=AOvVaw22Y27ta62xZm2RH_zb59aB"
          >https://www.mayoclinic.org/es/tests-procedures/ekg/about/pac-20384983</a
        ></span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span
        >[5]J. A. Zavala-Villeda, &ldquo;Descripci&oacute;n del
        electrocardiograma normal y lectura del electrocardiograma&rdquo;, </span
      ><span class="c15">Rev. Mex. Anesteciologia</span
      ><span
        >, vol. 40, Supl. 1, pp. 210&ndash;213, 2017. Accedido el 16 de
        septiembre de 2023. [En l&iacute;nea]. Disponible: </span
      ><span
        ><a
          class="c31"
          href="https://www.google.com/url?q=https://www.medigraphic.com/pdfs/rma/cma-2017/cmas171bj.pdf&amp;sa=D&amp;source=editors&amp;ust=1695004180889865&amp;usg=AOvVaw2vA347kJVQJD26PA3NzPDt"
          >https://www.medigraphic.com/pdfs/rma/cma-2017/cmas171bj.pdf</a
        ></span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span>[6]</span
      ><span class="c15"
        >6 claves para aprender a interpretar el electrocardiograma</span
      ><span
        >. Accedido el 17 de septiembre de 2023. [Imagen]. Disponible: </span
      ><span
        ><a
          class="c31"
          href="https://www.google.com/url?q=https://www.elsevier.com/es-es/connect/medicina/6-claves-para-aprender-a-interpretar-el-electrocardiograma&amp;sa=D&amp;source=editors&amp;ust=1695004180890606&amp;usg=AOvVaw3-RfhSUspN_tAt3Ez0R4OT"
          >https://www.elsevier.com/es-es/connect/medicina/6-claves-para-aprender-a-interpretar-el-electrocardiograma</a
        ></span
      >
    </p>
    <p class="c8"><span class="c2"></span></p>
    <p class="c17">
      <span
        >[7]Weiterleitungshinweis. Accedido el 17 de septiembre de 2023.
        [Imagen]. Disponible: </span
      ><span class="c3"
        ><a
          class="c31"
          href="https://www.google.com/url?q=https://www.google.com/url?sa%3Di%26amp;url%3Dhttps://www.elsevier.com/es-es/connect/enfermeria/11-pasos-para-la-obtencion-de-un-electrocardiograma-de-12-derivaciones%26amp;psig%3DAOvVaw14wrdNRsqBPqObFnOgQsPU%26amp;ust%3D1694998394571000%26amp;source%3Dimages%26amp;cd%3Dvfe%26amp;opi%3D89978449%26amp;ved%3D0CBIQjhxqFwoTCJioq563sIEDFQAAAAAdAAAAABAE&amp;sa=D&amp;source=editors&amp;ust=1695004180891289&amp;usg=AOvVaw2CwpX-TJ4ar5OzfBmdhM6K"
          >https://www.google.com/url?sa=i&amp;amp;url=https://www.elsevier.com/es-es/connect/enfermeria/11-pasos-para-la-obtencion-de-un-electrocardiograma-de-12-derivaciones&amp;amp;psig=AOvVaw14wrdNRsqBPqObFnOgQsPU&amp;amp;ust=1694998394571000&amp;amp;source=images&amp;amp;cd=vfe&amp;amp;opi=89978449&amp;amp;ved=0CBIQjhxqFwoTCJioq563sIEDFQAAAAAdAAAAABAE</a
        ></span
      >
    </p>
  </body>
</html>
