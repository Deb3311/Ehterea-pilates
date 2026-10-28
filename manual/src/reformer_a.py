from common import *

# =====================================================================
# PARTE I · FUNDAMENTOS
# =====================================================================
m1 = module(1, "Historia y filosofía del Pilates en reformer", [
    "Conocer la vida y obra de Joseph Pilates y el origen del reformer.",
    "Diferenciar los enfoques clásico y contemporáneo.",
    "Definir el rol y el alcance profesional de una instructora de reformer.",
], [
    topic("Joseph Pilates y la Contrología",
        FIG("d_tl_pilates", "Figura. Hitos en la historia de Joseph Pilates y su método."),
        T("**Joseph Hubertus Pilates** (1883–1967) nació en Mönchengladbach, Alemania. De niño tuvo una salud frágil y se "
          "dedicó a estudiar gimnasia, culturismo, boxeo, defensa personal, yoga y disciplinas orientales. Su idea central "
          "era que la salud depende del **equilibrio entre cuerpo y mente**, logrado mediante un control consciente del "
          "movimiento. Llamó a su método **Contrología** (*Contrology*)."),
        T("En *Return to Life Through Contrology* (1945) escribió que la Contrología busca «el desarrollo uniforme del cuerpo», "
          "la corrección de la postura, la restauración de la vitalidad y la coordinación de cuerpo, mente y espíritu. "
          "También afirmó que la buena forma física es el primer requisito de la felicidad."),
        TBL(["Idea de Joseph Pilates", "Cómo se traduce en el reformer"], [
            ["Control consciente de cada movimiento", "Ningún ejercicio se hace por inercia; el carro nunca «golpea» el tope"],
            ["Fuerza desde el centro (powerhouse)", "Abdomen, zona lumbar, glúteos y suelo pélvico dirigen cada ejercicio"],
            ["Respiración completa", "Inhalaciones y exhalaciones acompañan las fases del movimiento"],
            ["Fluidez y ritmo", "Transiciones como parte del ejercicio; pocas pausas"],
            ["Pocas repeticiones, máxima calidad", "Típicamente 3–10 repeticiones por ejercicio"],
        ], widths=[2.6, 3.9]),
    ),
    topic("Origen del reformer",
        T("Durante la Primera Guerra Mundial, Joseph Pilates fue internado en Inglaterra. Según la historia transmitida por sus "
          "alumnos, allí trabajó con personas convalecientes y empezó a usar **resortes** para asistir y resistir el "
          "movimiento, idea que dio origen a sus aparatos."),
        T("Ya en Nueva York, a partir de 1926, con su esposa **Clara**, desarrolló y perfeccionó su equipo. El más conocido es "
          "el **Universal Reformer**, una cama con un carro deslizante unido a resortes, con barra para los pies y correas. "
          "Diseñó además el Cadillac (Trapeze Table), la Wunda Chair, el Ladder Barrel y el Spine Corrector, entre otros."),
        TBL(["Aparato", "Descripción breve"], [
            ["Universal Reformer", "Carro deslizante con resortes, footbar, correas y caja; el aparato más versátil"],
            ["Cadillac (Trapeze Table)", "Camilla elevada con estructura, barras y resortes colgantes"],
            ["Wunda Chair", "Asiento con pedal accionado por resortes; muy exigente en equilibrio"],
            ["Ladder Barrel / Spine Corrector", "Barriles para movilidad y extensión de columna"],
        ], widths=[2.2, 4.3]),
    ),
    topic("Linajes: clásico y contemporáneo",
        T("Los alumnos directos de Joseph y Clara Pilates —conocidos como **«elders»**: Romana Kryzanowska, Kathy Grant, "
          "Lolita San Miguel, Ron Fletcher, Carola Trier, Eve Gentry, Bob Seed, Mary Bowen, entre otros— transmitieron el "
          "método con matices propios. De ahí surgen los **linajes**."),
        TBL(["Aspecto", "Enfoque clásico", "Enfoque contemporáneo"], [
            ["Repertorio", "Ejercicios y orden originales", "Repertorio original más variaciones"],
            ["Orden", "Secuencia fija que fluye", "Flexible según objetivos"],
            ["Columna", "Espalda baja hacia el carro en el trabajo abdominal", "Neutra o imprint según el caso"],
            ["Resortes", "Configuraciones tradicionales", "Ajustes según la persona"],
            ["Escuelas de referencia", "Linajes de los elders (p. ej., Romana's Pilates)", "STOTT PILATES, BASI, Polestar, Balanced Body, etc."],
        ], widths=[1.5, 2.5, 2.5]),
        BOX("escuela", "Sobre este libro",
            "Este manual sigue el **repertorio clásico de Joseph Pilates** y su orden de referencia. Los nombres, el orden exacto y "
            "las configuraciones de resortes varían ligeramente entre linajes y fabricantes. Cuando eso ocurre verás este recuadro."),
    ),
    topic("El rol de la instructora de reformer",
        UL("**Observar** la alineación y el patrón de movimiento antes de corregir.",
           "**Elegir resortes y montaje** seguros para cada cuerpo.",
           "**Guiar** con voz, demostración y, con consentimiento, contacto táctil.",
           "**Adaptar** con regresiones, progresiones y modificaciones.",
           "**Derivar** a profesionales de la salud ante dolor, lesión o condición médica."),
        BOX("seguridad", "Antes de la primera sesión",
            "Aplica un cuestionario de salud (por ejemplo, PAR-Q+) y pregunta por lesiones, cirugías, embarazo, osteoporosis, "
            "hipertensión y dolor actual. La primera clase en reformer debería ser privada o semiprivada siempre que sea posible."),
    ),
], [
    Q("¿Qué nombre dio Joseph Pilates a su método?", ["Reformer", "Contrología", "Powerhouse", "Body conditioning"], 1, ""),
    Q("¿Cómo se llama el reformer original diseñado por Joseph Pilates?", ["Cadillac", "Universal Reformer", "Wunda Chair", "Spine Corrector"], 1, ""),
    Q("Los «elders» fueron alumnos directos de Joseph y Clara Pilates.", None, "V", ""),
    Q("El enfoque contemporáneo prohíbe el repertorio clásico.", None, "F", "Lo conserva y añade variaciones."),
    Q("¿En qué año aproximado abrió Joseph Pilates su estudio en Nueva York?", ["1883", "1914", "1926", "1967"], 2, ""),
    Q("Menciona tres funciones de la instructora de reformer.", None, "Observar, elegir resortes y montaje, guiar, adaptar, derivar.", ""),
])

m2 = module(2, "El reformer: partes, resortes y seguridad", [
    "Identificar cada parte del reformer y su función.",
    "Comprender cómo los resortes asisten o resisten el movimiento.",
    "Montar, ajustar y usar el aparato con seguridad.",
], [
    topic("Anatomía del reformer",
        FIG("d_reformer", "Figura. Partes principales del reformer (vista lateral esquemática)."),
        TBL(["Parte", "Función"], [
            ["Estructura y rieles", "Base sobre la que se desliza el carro"],
            ["Carro (carriage)", "Plataforma acolchada que se desliza; aquí se acuesta, sienta, arrodilla o para la persona"],
            ["Resortes", "Unen el carro a la estructura; generan la resistencia o asistencia"],
            ["Gear bar / engranaje", "Cambia la posición de partida del carro y la tensión inicial de los resortes"],
            ["Footbar (barra de pies)", "Apoyo para pies o manos; suele tener varias alturas"],
            ["Hombreras (shoulder blocks)", "Evitan que el cuerpo se deslice; apoyo para pies o manos en algunos ejercicios"],
            ["Reposacabezas (headrest)", "Ajusta la posición del cuello; se baja en ejercicios con cabeza elevada o en extensión"],
            ["Poleas, cuerdas y correas", "Permiten trabajar con brazos o piernas en cadena abierta"],
            ["Plataforma", "Superficie fija en un extremo; apoyo para pies en splits y ejercicios de pie"],
            ["Caja (box)", "Se coloca sobre el carro: a lo largo (long box) o a lo ancho (short box)"],
        ], widths=[2.0, 4.5]),
    ),
    topic("Resortes y resistencia",
        T("Los resortes son el corazón del reformer. Un principio clave del método: **más resorte no siempre es más difícil**."),
        TBL(["Situación", "Efecto de más resorte", "Ejemplo"], [
            ["Empujar con las piernas (cadena cerrada)", "Más resistencia → más trabajo de piernas", "Footwork"],
            ["Ejercicios de estabilidad/control del carro", "Más estabilidad → más fácil", "Short box (carro casi fijo)"],
            ["Plancha o apoyo sobre el carro", "Un resorte ligero hace más inestable el carro → más difícil", "Long stretch, tendon stretch"],
            ["Ejercicios de brazos con correas", "Más resistencia → más trabajo de brazos", "Rowing, chest expansion"],
        ], widths=[2.4, 2.3, 1.8]),
        FIG("d_springs", "Figura. Resistencia orientativa por grupo de ejercicios (ajústala al equipo y a la persona)."),
        BOX("escuela", "Colores y número de resortes",
            "Cada fabricante usa colores y tensiones distintos (por ejemplo, rojo = pesado, azul = medio, amarillo = ligero en "
            "muchas marcas). Los reformers clásicos suelen tener resortes de igual tensión. En este libro la resistencia se "
            "expresa como **ligero, medio, medio-pesado o pesado** con un número orientativo de resortes. Consulta siempre la "
            "tabla de tu equipo."),
        FIG("d_chain", "Figura. Cadena cinética cerrada y abierta en el reformer."),
    ),
    topic("Montaje, ajustes y transiciones",
        TBL(["Ajuste", "Cuándo cambiarlo", "Regla práctica"], [
            ["Footbar alta / media / baja", "Según longitud de piernas y ejercicio", "En footwork la rodilla no debe quedar por encima de la cadera más allá de lo cómodo"],
            ["Reposacabezas", "Arriba en supino neutro; abajo con cabeza elevada (Hundred) y en ejercicios de rodar", "Cuello largo, sin compresión"],
            ["Gear bar", "Personas altas o con poca movilidad", "Que el carro no toque el tope en reposo con tensión"],
            ["Correas", "Longitud igual en ambos lados", "Revisa ganchos y desgaste"],
            ["Caja", "Long box a lo largo; short box a lo ancho delante de las hombreras", "Siempre bien asentada en el carro"],
        ], widths=[1.6, 2.4, 2.5]),
        H("Subir y bajar del reformer", 4),
        OL("Comprueba los resortes **antes** de subir.", "Siéntate en el carro de lado, cerca de las hombreras, y gira para acostarte.",
           "Para bajar, vuelve el carro a reposo con control, siéntate y sal por el lado.",
           "Nunca subas pisando el carro en movimiento ni sueltes el carro de golpe."),
        BOX("tip", "Transiciones clásicas", "En el estilo clásico los cambios de resorte, footbar y correas se integran a la clase sin pausas "
            "largas: la persona aprende a hacerlos ella misma de forma segura."),
    ),
    topic("Seguridad y mantenimiento",
        BOX("seguridad", "Checklist antes de cada clase",
            UL("Resortes enganchados por completo y sin deformaciones.", "Footbar bloqueada en su posición.", "Correas, cuerdas y ganchos sin desgaste.",
               "Ruedas y rieles limpios; el carro se desliza sin trabas.", "Espacio libre alrededor del aparato.")),
        UL("Desinfecta carro, correas y footbar después de cada uso.", "Revisa resortes según el calendario del fabricante (muchos recomiendan cambiarlos cada 1–2 años con uso intenso).",
           "Nunca cambies resortes con alguien sobre el carro en movimiento.", "Los ejercicios de pie sobre el carro requieren supervisión y nivel adecuado."),
    ),
], [
    Q("¿Para qué sirve el gear bar?", ["Para sujetar las correas", "Para cambiar la posición inicial del carro y la tensión de los resortes", "Para apoyar la cabeza", "Para fijar la caja"], 1, ""),
    Q("En ejercicios de plancha sobre el carro, un resorte ligero suele hacer el ejercicio…", ["Más fácil", "Más difícil", "Igual", "Imposible"], 1, "El carro es más inestable."),
    Q("Más resorte siempre significa más dificultad.", None, "F", ""),
    Q("El footwork es un ejemplo de cadena cinética cerrada.", None, "V", ""),
    Q("¿Dónde se coloca la short box?", ["A lo largo del carro", "A lo ancho, delante de las hombreras", "Sobre la plataforma", "Colgada de las poleas"], 1, ""),
    Q("Enumera cuatro puntos del checklist de seguridad antes de la clase.", None, "Resortes, footbar, correas/ganchos, rieles, espacio libre.", ""),
])

m3 = module(3, "Principios y bases del movimiento", [
    "Aplicar los seis principios clásicos en cada ejercicio.",
    "Dominar la postura Pilates, la respiración y la organización de columna, pelvis y escápulas.",
], [
    topic("Los seis principios",
        FIG("d_wheel", "Figura. Principios clásicos de Pilates (Friedman y Eisen, 1980).", 4.2),
        TBL(["Principio", "Qué significa en el reformer"], [
            ["Concentración", "Atención a la sensación del carro, los resortes y el cuerpo"],
            ["Control", "El carro se mueve a la velocidad que tú decides; regresa sin golpear"],
            ["Centro", "Cada movimiento nace del powerhouse"],
            ["Fluidez", "Ritmo continuo, transiciones integradas"],
            ["Precisión", "Ubicación exacta de pies, manos y columna"],
            ["Respiración", "Acompaña y facilita el movimiento"],
        ], widths=[1.8, 4.7]),
    ),
    topic("Powerhouse y respiración",
        T("El **powerhouse** (centro de fuerza) es la zona entre la parte baja de las costillas y la línea de la cadera: "
          "abdominales, músculos de la espalda baja, glúteos, aductores y suelo pélvico. En la tradición clásica se describe "
          "como «ombligo hacia la columna» y «apretar glúteos y cara interna de los muslos»."),
        FIG("d_core", "Figura. El core profundo como un cilindro.", 4.4),
        FIG("d_breath", "Figura. Respiración costal lateral.", 4.4),
        TBL(["Patrón respiratorio", "Uso"], [
            ["Exhalar en el esfuerzo", "Regla general: exhala al empujar o al flexionar la columna"],
            ["Respiración percusiva (5/5)", "The Hundred: 5 inhalaciones y 5 exhalaciones cortas"],
            ["Inhalar para preparar, exhalar para ejecutar", "Ejercicios de rodar (roll up, short spine)"],
            ["Respiración continua", "Isométricos y series rápidas (running)"],
        ], widths=[2.4, 4.1]),
    ),
    topic("Postura Pilates, columna neutra e imprint",
        FIG("d_stance", "Figura. Posiciones de pies: paralela, Pilates V y V amplia."),
        T("La **postura Pilates** (Pilates stance) consiste en talones juntos y puntas ligeramente separadas, con una suave "
          "rotación externa desde la cadera y activación de glúteos y aductores. Es la posición de pies más característica del "
          "repertorio clásico."),
        FIG("d_pelvis", "Figura. Pelvis en anteversión, neutra y retroversión."),
        TBL(["Posición", "Descripción", "Cuándo"], [
            ["Columna neutra", "Curvas naturales; el sacro apoya, la zona lumbar con una pequeña curva", "Footwork, ejercicios con palanca corta (enfoque contemporáneo)"],
            ["Imprint", "Leve retroversión que acerca la zona lumbar al carro", "Palancas largas (piernas extendidas bajas, Hundred)"],
            ["Flexión (C-curve)", "Columna redondeada", "Stomach massage, short box round, rodar"],
            ["Extensión", "Columna arqueada larga", "Swan, pulling straps, up stretch"],
        ], widths=[1.5, 2.9, 2.1]),
    ),
    topic("Escápulas, cuello y el «marco» del cuerpo",
        UL("**Escápulas:** apoyadas en la caja torácica, sin elevarse hacia las orejas.", "**Cuello:** largo; en flexión, la barbilla se acerca levemente al pecho («una manzana bajo la barbilla»).",
           "**El marco (box):** imagina un rectángulo entre hombros y caderas que debe permanecer cuadrado; si un ángulo se deforma, hay compensación.",
           "**Oposición:** alargar en dos direcciones (corona hacia un lado, talones hacia el otro)."),
        BOX("cue", "Cues clásicos", UL("«Ombligo hacia la columna.»", "«Aprieta glúteos y cara interna de los muslos.»", "«Hombros abajo, cuello largo.»",
                                        "«Mantén el marco cuadrado.»", "«Controla el carro: que no te controle a ti.»")),
    ),
], [
    Q("¿Qué es el powerhouse?", None, "La zona entre costillas bajas y cadera: abdomen, espalda baja, glúteos, aductores y suelo pélvico.", ""),
    Q("La postura Pilates consiste en…", ["Pies paralelos separados", "Talones juntos y puntas separadas", "Puntas juntas y talones separados", "Un pie delante del otro"], 1, ""),
    Q("¿En qué ejercicio se usa la respiración 5/5?", ["Footwork", "The Hundred", "Elephant", "Swan"], 1, ""),
    Q("El imprint es útil con palancas largas como las piernas extendidas bajas.", None, "V", ""),
    Q("«El marco» se refiere al rectángulo entre hombros y caderas.", None, "V", ""),
])

m4 = module(4, "Anatomía aplicada al reformer", [
    "Relacionar los grupos musculares con las series del repertorio.",
    "Comprender las acciones de columna, cadera y hombro en el reformer.",
], [
    topic("Mapa muscular",
        FIG("d_anatomy", "Figura. Principales músculos superficiales (esquema didáctico)."),
        TBL(["Grupo muscular", "Acción principal", "Series del reformer que lo trabajan"], [
            ["Cuádriceps", "Extensión de rodilla", "Footwork, running, pelvic lift"],
            ["Glúteos", "Extensión, abducción y rotación externa de cadera", "Footwork en V, pelvic lift, knee stretches, splits"],
            ["Isquiotibiales", "Flexión de rodilla, extensión de cadera", "Pelvic lift, feet in straps, tendon stretch"],
            ["Aductores", "Aducción de cadera", "Pilates V, frog, side splits"],
            ["Recto abdominal y oblicuos", "Flexión y rotación de columna", "Hundred, stomach massage, short box, coordination"],
            ["Transverso y suelo pélvico", "Estabilidad del centro", "Todo el repertorio"],
            ["Erectores espinales", "Extensión de columna", "Swan, pulling straps, up stretch, short box flat back"],
            ["Dorsal ancho", "Extensión y aducción del hombro", "Pulling straps, rowing, hundred"],
            ["Deltoides y manguito rotador", "Movimientos del hombro", "Rowing, arm circles, long stretch"],
            ["Serrato anterior", "Estabiliza las escápulas", "Long stretch, elephant, knee stretches"],
            ["Tríceps / bíceps", "Extensión / flexión del codo", "Down stretch, rowing, chest expansion"],
        ], widths=[1.8, 2.2, 2.5], small=True),
    ),
    topic("La columna en el reformer",
        FIG("d_spine", "Figura. Regiones y curvas de la columna.", 3.4),
        TBL(["Movimiento de columna", "Ejercicios representativos"], [
            ["Flexión", "Stomach massage round, short box round back, knee stretches round"],
            ["Extensión", "Swan / pulling straps, up stretch, knee stretches arched"],
            ["Flexión lateral", "Short box side to side, star"],
            ["Rotación", "Stomach massage twist, short box twist, snake/twist"],
            ["Estabilidad (columna neutra)", "Footwork, long stretch, rowing"],
            ["Articulación vértebra a vértebra", "Pelvic lift, short spine, semi-circle"],
        ], widths=[2.3, 4.2]),
        BOX("seguridad", "Osteoporosis y flexión con carga",
            "En personas con osteoporosis u osteopenia se recomienda evitar la flexión de columna con carga y la rotación forzada. "
            "Ejercicios como stomach massage round, short box round back o short spine requieren adaptación o sustitución."),
    ),
    topic("Cadera, rodilla y hombro",
        FIG("d_knees", "Figura. Alineación de rodilla."),
        UL("**Cadera:** el reformer trabaja flexión, extensión, abducción, aducción y rotaciones con el soporte del carro.",
           "**Rodilla:** en footwork, la rodilla se alinea con el segundo dedo; evita la hiperextensión al final del recorrido.",
           "**Hombro:** en planchas (long stretch) el serrato y el manguito estabilizan; en correas, los hombros se mantienen abajo."),
    ),
], [
    Q("¿Qué serie trabaja principalmente la extensión de columna?", ["Footwork", "Pulling straps / swan", "Stomach massage round", "Running"], 1, ""),
    Q("¿Qué movimiento de columna conviene evitar con carga en osteoporosis?", ["Extensión", "Flexión", "Estabilidad", "Ninguno"], 1, ""),
    Q("El serrato anterior ayuda a estabilizar las escápulas en el long stretch.", None, "V", ""),
    Q("En footwork se busca hiperextender las rodillas al final.", None, "F", ""),
    Q("Relaciona tres grupos musculares con una serie del reformer cada uno.", None, "Ej.: glúteos–pelvic lift; dorsal–pulling straps; oblicuos–short box twist.", ""),
])

MODULES = [m1, m2, m3, m4]
