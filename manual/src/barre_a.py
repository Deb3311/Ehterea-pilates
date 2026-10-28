from common import *
import poses as P

BAR = [{"k": "barre", "at": "HdN"}]
DB = [{"k": "db"}]
HOLD = dict(uaN=70, faN=95, uaF=70, faF=95)


def plie1(d=1.0, arms=(78, 95)):
    return P.front(arms=arms, legs=(10 + 14 * d, -10 * d), foot=115)


def at_barre(**kw):
    p = dict(HOLD)
    p.update(kw)
    return P.pose(**p)


# =====================================================================
# MÓDULO 1
# =====================================================================
m1 = module(1, "¿Qué hace a Barre tan especial? · Beneficios · Bienvenida · Historia · Nuestro método · Props · ¿Qué es Barre?", [
    "Explicar qué es barre, de dónde viene y qué la diferencia de otras disciplinas.",
    "Describir sus beneficios con base en el tipo de trabajo que propone.",
    "Conocer los props y su uso.",
    "Identificar qué aspectos del método requieren el material oficial.",
], [
    topic("¿Qué hace a Barre tan especial?",
        T("Barre ocupa un lugar único entre las disciplinas de fitness porque **une tres tradiciones**: la precisión postural "
          "del ballet, el control del centro de Pilates y la resistencia muscular del body sculpt. El resultado es una clase "
          "de **bajo impacto y alta intensidad** que trabaja en rangos pequeños, con mucha repetición y atención al detalle."),
        TBL(["Rasgo distintivo", "Por qué importa"], [
            ["Micromovimientos (pulsos de 1–3 cm)", "Mantienen el músculo en tensión constante: alto estrés metabólico con poca carga articular"],
            ["Isométricos en posiciones de ballet", "Fuerza y resistencia postural en ángulos específicos"],
            ["Uso de la barra como apoyo", "Permite trabajar equilibrio y rangos que serían inestables sin soporte"],
            ["Elongación entre bloques", "Alterna trabajo y estiramiento del mismo grupo muscular"],
            ["Atención a la alineación", "Herencia directa del ballet y de Pilates"],
            ["Música y fluidez", "Las secuencias se construyen sobre frases musicales"],
        ], widths=[2.4, 4.1]),
        BOX("cue", "La «quemazón» en barre", "El temblor y la quemazón al final de una serie de pulsos son señales normales de fatiga muscular "
            "(estrés metabólico). El dolor articular, en cambio, nunca es parte del método: indica cambiar el rango o la posición."),
    ),
    topic("Beneficios",
        TBL(["Beneficio", "Mecanismo"], [
            ["Fuerza y resistencia muscular", "Series largas de pulsos e isométricos llevan al músculo cerca de la fatiga"],
            ["Tonificación y definición", "Hipertrofia ligera + resistencia; combinada con hábitos que favorezcan la pérdida de grasa"],
            ["Postura", "Trabajo constante de alineación de columna, pelvis y hombros"],
            ["Estabilidad y equilibrio", "Ejercicios sobre una pierna y en relevé, primero con apoyo y luego sin él"],
            ["Movilidad y flexibilidad", "Elongaciones intercaladas y rangos amplios de cadera"],
            ["Bajo impacto", "Apto para muchas personas con articulaciones sensibles"],
            ["Conexión cuerpo-mente", "Concentración en la precisión y la respiración"],
        ], widths=[2.2, 4.3]),
        BOX("tip", "Lenguaje responsable", "Evita prometer «músculos largos de bailarina»: la longitud de un músculo depende de sus inserciones. "
            "Habla de fuerza, postura, control y bienestar."),
    ),
    topic("Bienvenida",
        T("Bienvenida a la sección de Barre. Aquí aprenderás la disciplina desde cero, como alumna y como futura instructora. "
          "Estudiarás primero la **alineación**, después el **vocabulario del ballet**, luego los **ejercicios** y, finalmente, "
          "cómo **unirlos en coreografías** y rutinas completas."),
        H("Cómo avanzar en esta sección", 4),
        OL("Practica cada posición de ballet frente a un espejo antes de agregar movimiento.",
           "Aprende primero cada ejercicio en su forma básica; luego agrega pulsos, isométricos y brazos.",
           "Graba tus transiciones y verifica que no haya pausas largas.",
           "Responde cada evaluación de módulo."),
        OFICIAL("Bienvenida (Barre)", "Mensaje de bienvenida y filosofía oficial de la formación.", "Calendario, requisitos y entregables oficiales."),
    ),
    topic("Historia",
        FIG("d_tl_barre", "Figura. Línea de tiempo de barre (hitos generales)."),
        T("El origen de barre como disciplina de fitness se atribuye a **Lotte Berk** (1913–2003), bailarina alemana que se "
          "estableció en Londres. Tras una lesión de espalda, combinó su formación en danza con ejercicios de rehabilitación "
          "y en **1959** abrió su estudio en Londres, donde el método se volvió muy popular."),
        T("En **1971**, Lydia Bach llevó el método Lotte Berk a Nueva York. Décadas después, varias instructoras formadas en "
          "esa escuela fundaron sus propios estudios y marcas a finales de los años noventa y principios de los 2000 (entre "
          "ellas Pure Barre, The Bar Method, Core Fusion y Physique 57), lo que expandió barre por todo el mundo."),
        T("Con el tiempo, barre incorporó principios de Pilates, entrenamiento funcional, pesos ligeros y props como la mini "
          "ball y las bandas, dando lugar a muchos estilos: clásico (más ballet), atlético (más cardio y fuerza) y fusión."),
        BOX("general", "Nota sobre las fuentes", "Las fechas y nombres anteriores corresponden a la historia general de barre. La historia del método TBM "
            "y su propia versión de barre se estudian en el material oficial."),
    ),
    topic("Nuestro método",
        T("Este tema corresponde a la propuesta específica del método TBM. Para no inventar contenido propietario, este libro "
          "ofrece un **marco para analizar cualquier método de barre** que podrás completar con la información oficial."),
        TBL(["Pregunta para analizar el método", "Tu respuesta (con el material oficial)"], [
            ["¿Cuál es su filosofía y a quién se dirige?", ""], ["¿Qué postura de pelvis enseña (neutra, tuck, ambas)?", ""],
            ["¿Qué estructura de clase utiliza?", ""], ["¿Qué props son oficiales?", ""], ["¿Qué tipo de música y BPM?", ""],
            ["¿Qué lo diferencia de otros métodos de barre?", ""],
        ], widths=[3.3, 3.2]),
        OFICIAL("Nuestro método (Barre)", "Filosofía, pilares y diferenciadores del barre de TBM.", "Postura pélvica oficial y su justificación.",
                "Estructura y nombres oficiales de bloques.", "Secuencias firma.", "Estándares de evaluación."),
    ),
    topic("Props",
        FIG("d_props_barre", "Figura. Props habituales en barre."),
        TBL(["Prop", "Características", "Usos principales"], [
            ["Barra", "Altura aproximada de la cintura; fija o portátil", "Apoyo para equilibrio, fold-over, pliés, estiramientos"],
            ["Mancuernas ligeras", "0.5–2 kg", "Series largas de brazos"],
            ["Mini ball (pelota blanda)", "20–25 cm, parcialmente inflada", "Squeeze de aductores, apoyo en abdominales, inestabilidad"],
            ["Banda de resistencia", "Larga o en loop", "Brazos, abducción de cadera, estiramientos asistidos"],
            ["Mat", "Antideslizante", "Abdominales, trabajo de glúteo en suelo"],
            ["Tobilleras con peso (opcional)", "0.5–1 kg", "Glúteo en fold-over o cuadrupedia"],
        ], widths=[1.6, 2.1, 2.8]),
        BOX("seguridad", "Sin barra en casa", "Una silla firme, una encimera o el respaldo de un sofá estable pueden servir. Comprueba siempre que no se mueva."),
    ),
    topic("¿Qué es Barre?",
        BOX("general", "Definición de la disciplina",
            "Barre es una combinación de ballet, Pilates y body sculpt que integra elongaciones, micromovimientos y ejercicios de "
            "resistencia para fortalecer, tonificar y estilizar los músculos. Su enfoque de bajo impacto y alta intensidad "
            "también ayuda a mejorar la postura, la estabilidad, el control corporal y la conexión con tu cuerpo."),
        TBL(["Aporte", "Del ballet", "De Pilates", "Del body sculpt"], [
            ["Qué toma", "Posiciones de pies y brazos, plié, relevé, extensiones", "Centro (powerhouse), respiración, control", "Pesos ligeros, series de resistencia"],
            ["Para qué", "Postura, línea y gracia", "Estabilidad y precisión", "Fuerza y tonificación"],
        ], widths=[1.1, 1.9, 1.75, 1.75]),
        H("Estructura típica de una clase (general)", 4),
        FIG("d_curve_barre", "Figura. Curva de intensidad de una clase de barre de 50 minutos (ejemplo didáctico)."),
    ),
], [
    Q("¿Quién se considera la creadora del método que dio origen a barre?", ["Joseph Pilates", "Lotte Berk", "Lydia Bach", "Martha Graham"], 1, ""),
    Q("¿En qué año abrió Lotte Berk su estudio en Londres?", ["1926", "1959", "1971", "2001"], 1, ""),
    Q("Barre es una disciplina de alto impacto.", None, "F", "Es de bajo impacto y alta intensidad."),
    Q("Los micromovimientos favorecen principalmente el estrés metabólico.", None, "V", ""),
    Q("¿Qué tamaño aproximado tiene la mini ball?", ["8–10 cm", "20–25 cm", "55–65 cm", "75 cm"], 1, ""),
    Q("Enumera tres aspectos de «Nuestro método» que debes completar con el material oficial.", None,
      "Filosofía, postura pélvica oficial, estructura de clase, secuencias firma, estándares.", ""),
])

# =====================================================================
# MÓDULO 2
# =====================================================================
m2 = module(2, "Alineación cadera · Alineación columna · Alineación rodilla-pies", [
    "Reconocer y enseñar la pelvis neutra y sus variaciones.",
    "Describir la alineación ideal de la columna en bipedestación.",
    "Alinear rodilla y pie, especialmente con rotación externa (turnout).",
], [
    topic("Alineación cadera",
        T("La pelvis es el puente entre el tronco y las piernas. Su posición condiciona la curva lumbar, la activación del "
          "glúteo y el trabajo abdominal."),
        FIG("d_pelvis", "Figura. Pelvis en anteversión, neutra y retroversión (la «taza» con agua)."),
        TBL(["Posición", "Cómo se reconoce", "Uso en barre"], [
            ["Neutra", "Las espinas ilíacas anterosuperiores (EIAS) y el pubis forman un plano vertical (de pie) u horizontal (boca arriba)", "Posición de referencia en la mayoría de ejercicios"],
            ["Retroversión («tuck»)", "El cóccix se dirige hacia delante y abajo, la curva lumbar se aplana", "Algunos estilos la usan como acción breve para intensificar glúteo y abdomen"],
            ["Anteversión", "Cadera hacia atrás, aumento de la curva lumbar", "Se evita bajo carga; aparece al arquear en fold-over o arabesque"],
        ], widths=[1.5, 2.8, 2.2]),
        H("Encontrar la pelvis neutra", 4),
        OL("De pie, coloca los talones de las manos sobre las EIAS y los dedos sobre el pubis, formando un triángulo.",
           "Inclina la pelvis hacia delante (anteversión) y hacia atrás (retroversión) varias veces.",
           "Detente a medio camino: el triángulo queda vertical. Esa es tu pelvis neutra."),
        BOX("general", "Debate «tuck» frente a neutra",
            "El barre clásico usaba un «tuck» marcado. Muchos enfoques actuales prefieren pelvis neutra con activación profunda, "
            "y usan el tuck como **micromovimiento opcional y breve**, no como postura sostenida. Ambas opciones pueden ser seguras si "
            "se enseñan con control; la elección oficial depende del método."),
        OFICIAL("Alineación de cadera", "Postura pélvica oficial del método y el lenguaje con que se indica."),
    ),
    topic("Alineación columna",
        FIG("d_spine", "Figura. Curvas naturales de la columna.", 3.4),
        H("La línea de la plomada", 4),
        T("De perfil, en una postura erguida eficiente, una línea vertical imaginaria pasa cerca de: **lóbulo de la oreja → "
          "hombro → cadera (trocánter) → ligeramente delante de la rodilla → ligeramente delante del tobillo**."),
        TBL(["Zona", "Alineación", "Cue"], [
            ["Cabeza", "Sobre los hombros, mentón paralelo al suelo", "«Corona hacia el techo»"],
            ["Hombros", "Abajo y abiertos, sin forzar", "«Escápulas al bolsillo trasero»"],
            ["Costillas", "Cerradas sobre la pelvis", "«Costillas abrazan el ombligo»"],
            ["Abdomen", "Activo, sin apnea", "«Ombligo suave hacia la columna»"],
            ["Pelvis", "Neutra", "«Cóccix largo hacia el suelo»"],
        ], widths=[1.3, 2.6, 2.6]),
        TBL(["Desviación postural", "Señales", "Ejercicios de barre que ayudan"], [
            ["Hiperlordosis", "Costillas abiertas, cadera atrás", "Trabajo abdominal, estiramiento de flexores de cadera"],
            ["Hipercifosis / hombros adelantados", "Cabeza adelantada, pecho cerrado", "Brazos en segunda, pájaros, estiramiento de pecho"],
            ["Espalda plana", "Poca curva lumbar", "Movilidad de cadera, conciencia de neutra"],
        ], widths=[1.9, 2.1, 2.5], caption="Observación general; no se diagnostica. Ante dolor o deformidades importantes, derivar."),
        FIG("d_breath", "Figura. Respiración costal lateral.", 4.6),
    ),
    topic("Alineación rodilla-pies",
        FIG("d_knees", "Figura. Alineación de rodilla con el pie."),
        H("El trípode del pie", 4),
        T("El pie se apoya en tres puntos: **talón, base del dedo gordo y base del dedo pequeño**. Repartir el peso en el "
          "trípode evita que el tobillo se venza hacia dentro (pronación) o hacia fuera (supinación)."),
        H("Turnout: rotación desde la cadera", 4),
        T("En ballet, el turnout es la rotación externa de las piernas. Debe nacer en la **articulación de la cadera** "
          "(rotadores profundos y glúteo). Si se fuerza girando los pies más de lo que permite la cadera, la rodilla sufre "
          "torsión."),
        OL("Párate en paralelo, cadera neutra.", "Gira las piernas hacia fuera desde la parte alta del muslo sin mover la pelvis.",
           "Deja que los pies sigan a las rodillas: la apertura que alcances así es tu turnout natural.",
           "Al flexionar (plié), las rodillas apuntan siempre sobre el segundo o tercer dedo."),
        H("Relevé seguro", 4),
        UL("El peso se ubica entre el primer y el segundo dedo.", "Evita la «hoz» (sickling): tobillo vencido hacia fuera con dedos hacia dentro.",
           "Sube y baja con control, sin caer de golpe."),
        BOX("seguridad", "Rodillas", "Nunca empujes las rodillas hacia fuera más allá de los pies ni bloquees (hiperextiendas) las rodillas en "
            "posiciones de pie. Mantén una microflexión."),
    ),
], [
    Q("En la pelvis neutra (de pie), las EIAS y el pubis…", ["Forman un plano vertical", "Forman un plano horizontal", "No se relacionan", "El pubis queda delante"], 0, ""),
    Q("El turnout debe originarse en…", ["Los pies", "Las rodillas", "La cadera", "Los tobillos"], 2, ""),
    Q("El «sickling» es una buena alineación del tobillo en relevé.", None, "F", ""),
    Q("La línea de la plomada pasa cerca del lóbulo de la oreja, hombro y cadera.", None, "V", ""),
    Q("¿Cuáles son los tres puntos del trípode del pie?", None, "Talón, base del dedo gordo y base del dedo pequeño.", ""),
    Q("Describe cómo enseñarías a encontrar la pelvis neutra a una alumna nueva.", None, "Triángulo con las manos sobre EIAS y pubis; balancear y detenerse a medio camino.", ""),
])

# =====================================================================
# MÓDULO 3
# =====================================================================
m3 = module(3, "Posición ballet piernas · Posición brazos", [
    "Ejecutar las posiciones de piernas y brazos del ballet aplicadas a barre.",
    "Conocer el vocabulario básico y su pronunciación aproximada.",
], [
    topic("Posición ballet piernas",
        FIG("d_bfeet", "Figura. Posiciones de pies: paralela y de primera a quinta (vista superior)."),
        TBL(["Posición", "Descripción", "Uso en barre"], [
            ["Paralela", "Pies paralelos a la anchura de la cadera o juntos", "Relevé, chair, trabajo de cuádriceps"],
            ["Primera", "Talones juntos, puntas hacia fuera (turnout natural)", "Plié y relevé en primera; aductores y glúteo"],
            ["Segunda", "Pies separados (≈ 1.5 anchos de cadera) con turnout", "Plié amplio, sumo, pulsos"],
            ["Tercera", "Talón de un pie en el arco del otro", "Poco usada; transición"],
            ["Cuarta", "Un pie delante del otro separado un paso, con turnout", "Zancadas de ballet, lunges"],
            ["Quinta", "Pies cruzados, talón con punta del otro", "En barre se suele sustituir por tercera para proteger rodillas"],
        ], widths=[1.1, 2.9, 2.5]),
        H("Vocabulario esencial", 4),
        TBL(["Término", "Pronunciación aprox.", "Significado"], [
            ["Plié", "pli-É", "Flexión de rodillas (demi = media; grand = profunda)"],
            ["Relevé", "rel-e-VÉ", "Elevación a media punta"],
            ["Tendu", "tan-DÚ", "Deslizar el pie hasta estirar el empeine sin despegar la punta"],
            ["Dégagé", "de-ga-YÉ", "Como tendu, pero despegando ligeramente del suelo"],
            ["Passé / retiré", "pa-SÉ / re-ti-RÉ", "Punta del pie a la altura de la rodilla de apoyo"],
            ["Coupé", "cu-PÉ", "Pie a la altura del tobillo de apoyo"],
            ["Développé", "de-ve-lo-PÉ", "Desplegar la pierna desde passé hasta extenderla"],
            ["Arabesque", "a-ra-BESK", "Pierna extendida hacia atrás"],
            ["Attitude", "a-ti-TÚD", "Pierna elevada con la rodilla flexionada"],
            ["Rond de jambe", "ron de YAMB", "Círculo de la pierna"],
            ["Port de bras", "por de BRA", "Movimiento de brazos entre posiciones"],
            ["Sauté", "so-TÉ", "Salto"],
            ["Changement", "shanch-MAN", "Salto cambiando el pie de delante"],
        ], widths=[1.4, 1.6, 3.5]),
        GALLERY("g_ballet_legs", "Figura. Acciones de pierna en barre (vista lateral y frontal).", [
            (at_barre(), "Paralela", BAR), (at_barre(ftN=25, ftF=25), "Relevé", BAR), (at_barre(thF=-20, shF=-20, ftF=-5), "Tendu atrás", BAR),
            (at_barre(thF=40, shF=-60, ftF=20), "Passé (retiré)", BAR), (at_barre(thF=-45, shF=-45, ftF=-25), "Arabesque baja", BAR),
            (at_barre(thF=-60, shF=-150, ftF=-170), "Attitude", BAR), (plie1(1), "Demi-plié en 1.ª"), (P.plie2(1), "Plié en 2.ª"),
        ], per_row=4),
    ),
    topic("Posición brazos",
        FIG("d_barms", "Figura. Posiciones de brazos (esquema frontal)."),
        TBL(["Posición", "Descripción"], [
            ["Preparatoria (bras bas)", "Brazos redondeados abajo, frente a los muslos"],
            ["Primera", "Brazos redondeados al frente a la altura del ombligo o esternón bajo"],
            ["Segunda", "Brazos abiertos a los lados, ligeramente por delante del cuerpo y por debajo de los hombros"],
            ["Tercera*", "Combinación de dos posiciones (varía según la escuela)"],
            ["Cuarta*", "Un brazo arriba y otro en segunda o primera (varía según la escuela)"],
            ["Quinta (en haut)", "Ambos brazos redondeados por encima y ligeramente delante de la cabeza"],
        ], widths=[1.8, 4.7], caption="*Las posiciones tercera y cuarta cambian entre escuelas (francesa, RAD, Cecchetti, Vaganova)."),
        H("Claves de calidad", 4),
        UL("Codos redondeados (no colgados), «como si abrazaras una pelota grande».", "Hombros abajo; el trabajo nace en la espalda.",
           "Manos suaves: dedos largos, pulgar cerca del dedo medio.", "La mirada acompaña el port de bras."),
        BOX("cue", "Brazos que trabajan", "En barre, los brazos no son decoración: sostener la segunda posición 60 s con pulsos es un ejercicio "
            "de resistencia de deltoides. «Brazos largos desde la espalda hasta la punta de los dedos.»"),
    ),
], [
    Q("En la primera posición los talones están…", ["Separados", "Juntos con puntas hacia fuera", "Uno delante del otro", "Cruzados"], 1, ""),
    Q("¿Qué significa relevé?", ["Flexión de rodillas", "Elevación a media punta", "Salto", "Círculo de pierna"], 1, ""),
    Q("La quinta posición de pies suele sustituirse por tercera en barre para proteger las rodillas.", None, "V", ""),
    Q("En segunda posición de brazos, los brazos van por encima de los hombros.", None, "F", "Ligeramente por debajo y por delante."),
    Q("Define passé y arabesque.", None, "Passé: punta a la altura de la rodilla de apoyo. Arabesque: pierna extendida hacia atrás.", ""),
])

# =====================================================================
# MÓDULO 4
# =====================================================================
lower = [
    EX("Plié en primera con relevé", en="First position plié-relevé", frames=[F(plie1(0), "Primera"), F(plie1(1), "Demi-plié"), F(P.front(arms=(160, -140), legs=(8, 0), foot=115, ftN=40), "Relevé")],
       prim=["cuad", "adu", "glmax"], sec=["gem", "glmed", "ta"],
       obj="Fortalecer piernas y aductores en rotación externa, integrando equilibrio.",
       start="Primera posición de pies con turnout natural, una mano en la barra.",
       steps=["Flexiona las rodillas sobre la línea de los pies (demi-plié) manteniendo talones en el suelo.", "Extiende las piernas apretando la cara interna de los muslos.",
              "Sube a relevé manteniendo los talones juntos.", "Baja con control. Variante: pulsos en plié o en relevé."],
       breath="Inhala al bajar, exhala al subir.", errors=["Rodillas que no siguen la línea de los pies.", "Cadera en anteversión.", "Talones que se separan en el relevé."],
       regress=["Sin relevé.", "Menos turnout."], progress=["Pulsos en plié-relevé (talones altos).", "Sin apoyo en la barra."],
       dose="2–3 series de 16–32 o 60 s.", cue="«Cierra una cremallera desde las rodillas a los muslos.»"),
    EX("Plié en segunda con pulsos", en="Second position plié pulses", frames=[F(P.wide(arms=(78, 95)), "Segunda"), F(P.plie2(1), "Plié + pulsos")],
       prim=["glmax", "adu", "cuad"], sec=["glmed", "ta"],
       obj="Trabajo intenso de glúteo y aductores en posición amplia.",
       start="Segunda posición, torso vertical, brazos en segunda o mano en la barra.",
       steps=["Baja hasta que los muslos se acerquen a la horizontal.", "Realiza pulsos de 2 cm.", "Termina con un isométrico y estira."],
       breath="Respiración continua.", errors=["Inclinar el tronco adelante.", "Rodillas hacia dentro.", "Glúteos que salen hacia atrás."],
       regress=["Menor profundidad."], progress=["Relevé en plié de segunda.", "Mancuernas en segunda."],
       dose="3 series de 30–60 s.", cue="«Desliza la espalda por una pared imaginaria.»"),
    EX("Relevé en paralelo con rodillas flexionadas", en="Parallel high-heel thigh", level="Intermedio", frames=[F(at_barre(), "Paralela", BAR), F(P.squat(0.45, relev=True, uaN=70, faN=95, uaF=70, faF=95, trunk=176), "Talones altos + plié", BAR)],
       prim=["cuad"], sec=["gem", "adu", "ta"],
       obj="Trabajo característico de cuádriceps en barre (thigh work).",
       start="Paralela con pies juntos o a dos dedos, manos en la barra.",
       steps=["Sube a relevé alto.", "Flexiona las rodillas manteniendo talones altos y tronco vertical.", "Pulsos de 1–2 cm hacia abajo.", "Isométrico final."],
       breath="Continua.", errors=["Talones que bajan.", "Hiperlordosis.", "Rodillas que se separan."],
       regress=["Talones bajos.", "Menos flexión."], progress=["Mini ball entre muslos.", "Brazos en segunda sin apoyo."],
       dose="3 series de 45–60 s.", cue="«Talones altos como tacones; rodillas juntas.»"),
    EX("Chair (silla) en paralelo", en="Chair pose / parallel chair", frames=[F(P.squat(0.7, uaN=70, faN=95, uaF=70, faF=95), "Silla", BAR)],
       prim=["cuad", "glmax"], sec=["adu", "ta", "ere"],
       obj="Isométrico de pierna con espalda larga.",
       start="Paralela con pies juntos, manos en la barra.",
       steps=["Siéntate atrás como en una silla manteniendo el pecho largo.", "Rodillas sobre los tobillos o ligeramente delante.", "Pulsos o isométrico."],
       breath="Continua.", errors=["Redondear la espalda.", "Rodillas separadas."], regress=["Más arriba."], progress=["Con relevé.", "Mini ball."],
       dose="30–60 s.", cue="«Cadera atrás, corona adelante.»"),
    EX("Fold-over con elevación de pierna", en="Fold-over leg lift", level="Intermedio",
       frames=[F(P.hinge(1, uaN=88, faN=88, uaF=88, faF=88, thF=-15, shF=-15), "Inicio", BAR), F(P.hinge(1, uaN=88, faN=88, uaF=88, faF=88, thF=-85, shF=-85, ftF=-60), "Elevación", BAR)],
       prim=["glmax"], sec=["isq", "ere", "ta", "glmed"],
       obj="Aislar el glúteo con el tronco apoyado en la barra (flexión de cadera).",
       start="Tronco inclinado al frente, antebrazos o manos en la barra, pierna de apoyo con rodilla suave.",
       steps=["Extiende una pierna hacia atrás con el pie en flex o en punta.", "Eleva la pierna hasta la línea de la cadera sin rotar la pelvis.",
              "Pulsos de 2 cm arriba.", "Variante: flexionar la rodilla y subir el talón al techo."],
       breath="Exhala al elevar.", errors=["Arquear la espalda baja.", "Abrir la cadera de la pierna que trabaja.", "Bloquear la rodilla de apoyo."],
       regress=["Rango menor.", "Tronco más vertical."], progress=["Tobillera.", "Cuentas lentas + pulsos + isométrico."],
       dose="2 rondas de 32–48 por lado.", cue="«Ambas crestas ilíacas miran al suelo.»"),
    EX("Arabesque en barra", en="Arabesque lift", level="Intermedio", frames=[F(at_barre(thF=-20, shF=-20, ftF=-5), "Tendu atrás", BAR), F(at_barre(thF=-45, shF=-45, ftF=-25, trunk=172), "Arabesque", BAR)],
       prim=["glmax"], sec=["isq", "ere", "glmed"],
       obj="Extensión de cadera con tronco erguido y estabilidad de la pierna de apoyo.",
       start="De frente a la barra, pierna de trabajo en tendu atrás con ligero turnout.",
       steps=["Eleva la pierna atrás desde el glúteo, larga.", "El tronco puede inclinarse levemente para mantener la columna larga.", "Pulsos o elevaciones lentas."],
       breath="Exhala al elevar.", errors=["Arquear la zona lumbar para subir más.", "Girar el torso.", "Hundirse en la cadera de apoyo."],
       regress=["Sin turnout, rango corto."], progress=["Sin apoyo de manos.", "Combinar con plié de la pierna de apoyo."],
       dose="32–48 por lado.", cue="«Pierna larga hacia la pared de atrás antes que hacia arriba.»"),
    EX("Attitude", en="Attitude lift", level="Intermedio", frames=[F(at_barre(thF=-60, shF=-150, ftF=-170), "Attitude atrás", BAR)],
       prim=["glmax", "glmed"], sec=["isq", "ere"],
       obj="Trabajar glúteo mayor y medio con la rodilla flexionada (palanca corta).",
       start="De frente a la barra, pierna de trabajo con rodilla flexionada detrás, rodilla ligeramente hacia fuera.",
       steps=["Eleva la rodilla hacia atrás y arriba manteniendo el ángulo.", "Pulsos pequeños.", "Isométrico final."],
       breath="Continua.", errors=["Perder la pelvis.", "Rodilla que cae."], regress=["Más bajo."], progress=["Tobillera."],
       dose="32 por lado.", cue="«Rodilla hacia el techo de atrás.»"),
    EX("Développé / elevación lateral en barra", en="Side développé / leg lift", frames=[F(P.front(arms=(78, 95), armsF=(30, 80)), "Inicio"), F(P.front(arms=(78, 95), armsF=(30, 80), legs=(55, 55), trunk=176), "Elevación lateral")],
       prim=["glmed"], sec=["glmax", "obl", "adu"],
       obj="Abducción de cadera para el glúteo medio y estabilidad pélvica.",
       start="De lado a la barra, mano interna apoyada, pierna externa en tendu lateral.",
       steps=["Eleva la pierna al lado sin inclinar el tronco.", "Rodilla y pie miran al frente o ligeramente arriba.", "Variante développé: passé → extensión lateral."],
       breath="Exhala al elevar.", errors=["Inclinarse hacia la barra.", "Elevar la cadera."], regress=["Rango corto."], progress=["Banda en los tobillos.", "Sin apoyo."],
       dose="16–32 por lado.", cue="«Alarga la pierna antes de levantarla.»"),
    EX("Curtsy en barra", en="Curtsy at the barre", frames=[F(P.front(arms=(70, 95)), "Inicio"), F(P.front(arms=(70, 95), legs=(18, -15), legsF=(-25, -30)), "Curtsy")],
       prim=["glmax", "glmed"], sec=["cuad", "adu"],
       obj="Glúteo y estabilidad de rodilla con patrón cruzado.",
       start="De frente a la barra, pies en paralelo.",
       steps=["Lleva una pierna en diagonal detrás de la otra.", "Baja con cadera al frente.", "Pulsos abajo o regreso a paralela."],
       breath="Inhala al bajar.", errors=["Rotar la pelvis."], regress=["Rango corto."], progress=["Relevé en la pierna de atrás."],
       dose="16–24 por lado.", cue="«Reverencia elegante, cadera de frente.»"),
]

upper = [
    EX("Brazos en segunda con pulsos", en="Second position arm pulses", frames=[F(P.front(arms=(78, 95)), "Segunda", DB)],
       prim=["delM"], sec=["delP", "trap", "delA"],
       obj="Resistencia del deltoides con peso muy ligero o sin peso.",
       start="De pie en paralelo, brazos en segunda posición, palmas abajo.",
       steps=["Pulsos de 2 cm hacia arriba.", "Cambia a pulsos hacia atrás.", "Termina con círculos pequeños hacia delante y atrás."],
       breath="Continua.", errors=["Subir los hombros.", "Codos colgados."], regress=["Sin peso.", "Brazos más bajos."], progress=["Mancuernas de 0.5–1 kg."],
       dose="60–90 s por bloque.", cue="«Brazos largos desde la espalda.»"),
    EX("Círculos de brazos", en="Arm circles", frames=[F(P.front(arms=(90, 90)), "Brazos al lado")],
       prim=["delM", "delA"], sec=["delP", "ser"],
       obj="Movilidad y resistencia de hombros.",
       start="Brazos en segunda.", steps=["Círculos pequeños hacia delante (16).", "Hacia atrás (16).", "Círculos grandes lentos (8)."],
       breath="Continua.", errors=["Mover el tronco."], regress=["Más bajos."], progress=["Con peso ligero."], dose="45–60 s.", cue="«Dibuja monedas con las puntas de los dedos.»"),
    EX("Bíceps en barre", en="Barre biceps curl", frames=[F(P.front(arms=(78, 95)), "Segunda", DB), F(P.front(arms=(78, 165)), "Flexión", DB)],
       prim=["bic"], sec=["delM", "ant"],
       obj="Curl de bíceps con brazos abiertos en segunda (variante barre).",
       start="Brazos en segunda, palmas hacia el techo, mancuernas ligeras.",
       steps=["Flexiona los codos hacia las orejas sin bajar los codos.", "Extiende sin bloquear.", "Pulsos a mitad de rango."],
       breath="Exhala al flexionar.", errors=["Codos que caen."], regress=["Brazos más bajos."], progress=["Isométrico a 90°."],
       dose="16–32 + pulsos.", cue="«Los codos son un estante fijo.»"),
    EX("Tríceps press back", en="Triceps press back", frames=[F(P.hinge(0.3, uaN=-25, faN=-25, uaF=-25, faF=-25), "Brazos atrás", DB), F(P.hinge(0.3, uaN=-45, faN=-45, uaF=-45, faF=-45), "Pulso atrás", DB)],
       prim=["tri"], sec=["delP", "dor"],
       obj="Tríceps en extensión de hombro con pulsos.",
       start="Inclina ligeramente el tronco, brazos extendidos atrás junto a la cadera, palmas hacia atrás.",
       steps=["Empuja los brazos hacia atrás y arriba en pulsos pequeños.", "Mantén los codos extendidos.", "Variante: flexión y extensión del codo."],
       breath="Continua.", errors=["Encoger hombros.", "Redondear la espalda."], regress=["Sin peso."], progress=["Mancuernas 1–2 kg."],
       dose="32 pulsos + 16 extensiones.", cue="«Empuja el aire hacia la pared de atrás.»"),
    EX("Press de pecho en primera", en="Chest press", frames=[F(P.stand("chest"), "Codos abiertos", DB), F(P.stand("front"), "Brazos al frente", DB)],
       prim=["pec", "delA"], sec=["tri", "ser"],
       obj="Activar pecho y hombro anterior en una posición de brazos de ballet.",
       start="Brazos en «cactus» o primera abierta a la altura del pecho.",
       steps=["Empuja los brazos al frente juntando las manos.", "Abre de nuevo con control.", "Variante isométrica: apretar las palmas."],
       breath="Exhala al cerrar.", errors=["Hombros hacia las orejas."], regress=["Sin peso."], progress=["Banda alrededor de la espalda."],
       dose="16–32.", cue="«Abraza una pelota gigante.»"),
    EX("Push up en barra", en="Barre push up", frames=[F(P.incline_push(), "Arriba", [{"k": "barre", "at": "HdN", "ox": 0}]), F(P.incline_push(True), "Abajo", [{"k": "barre", "at": "HdN", "ox": 0}])],
       prim=["pec", "tri"], sec=["delA", "ser", "ta"],
       obj="Push up inclinado usando la barra.",
       start="Manos en la barra a la anchura de los hombros, cuerpo en plancha inclinada.",
       steps=["Baja el pecho hacia la barra con codos hacia atrás.", "Empuja.", "Variante: pulsos abajo."],
       breath="Exhala al empujar.", errors=["Cadera hacia atrás.", "Cuello adelantado."], regress=["Pies más cerca."], progress=["Pies más lejos.", "Push up en suelo."],
       dose="12–20.", cue="«Cuerpo de tabla hacia la barra.»"),
    EX("Press de hombros en quinta", en="Fifth position press", frames=[F(P.front(arms=(80, 175)), "Goal post", DB), F(P.front(arms=(165, 190)), "Quinta", DB)],
       prim=["delA", "delM"], sec=["tri", "trap", "ser"],
       obj="Empuje vertical ligero que termina en la quinta posición de brazos.",
       start="Brazos en «goal post» (codos a la altura de los hombros, antebrazos verticales).",
       steps=["Empuja hacia arriba juntando las mancuernas en quinta.", "Baja a goal post.", "Pulsos arriba."],
       breath="Exhala al subir.", errors=["Arquear la espalda.", "Hombros a las orejas."], regress=["Sin peso."], progress=["En relevé."],
       dose="16–24.", cue="«Corona y manos hacia el techo.»"),
]

m4 = module(4, "Ejercicios tren inferior · Ejercicios tren superior", [
    "Ejecutar los ejercicios fundamentales de piernas y glúteos en barra.",
    "Ejecutar las series de brazos características de barre.",
], [
    topic("Ejercicios tren inferior",
        T("En barre, cada ejercicio de pierna suele trabajarse en **capas**: rango completo → pulsos → isométrico → elongación. "
          "Las fichas muestran la forma base; en el Módulo 6 aprenderás a encadenarlos."),
        BOX("tip", "Uso de la barra", "La barra es un apoyo para el equilibrio, no para colgarse. Indica «manos ligeras en la barra» y, cuando se "
            "domina el ejercicio, prueba soltar una mano."),
        *lower),
    topic("Ejercicios tren superior",
        T("Los brazos en barre se trabajan con **peso ligero (0.5–2 kg) y muchas repeticiones**, a menudo sin descanso entre "
          "ejercicios. El objetivo es la resistencia y la postura de hombros."),
        *upper),
], [
    Q("En el fold-over, ¿qué error es más frecuente?", ["Exhalar", "Abrir la cadera de la pierna que trabaja", "Mantener la rodilla de apoyo suave", "Apoyar las manos"], 1, ""),
    Q("¿Qué músculo trabaja principalmente el relevé en paralelo con rodillas flexionadas?", ["Cuádriceps", "Bíceps", "Dorsal", "Recto abdominal"], 0, ""),
    Q("En barre se usan mancuernas de 6–10 kg para los brazos.", None, "F", "Se usan 0.5–2 kg con muchas repeticiones."),
    Q("La elevación lateral de pierna trabaja principalmente el glúteo medio.", None, "V", ""),
    Q("Describe las cuatro capas con las que se suele trabajar un ejercicio de pierna en barre.", None, "Rango completo → pulsos → isométrico → elongación.", ""),
])

MODULES = [m1, m2, m3, m4]
