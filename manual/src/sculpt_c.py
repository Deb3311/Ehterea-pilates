from common import *
import poses as P

ROUT_HEAD = ["Bloque", "Tiempo", "Ejercicio", "Dosificación", "Notas / cues"]
ROUT_W = [1.05, 0.65, 1.75, 1.25, 1.8]

# =====================================================================
# MÓDULO 7
# =====================================================================
m7 = module(7, "Conceptos para la creación de rutina · Práctica tren superior · Teoría · Adaptación", [
    "Aplicar los principios del entrenamiento al diseño de una clase.",
    "Construir paso a paso una rutina de tren superior.",
    "Estructurar una clase completa con fases, bloques y tiempos.",
    "Adaptar rutinas por objetivo, nivel y duración.",
], [
    topic("Conceptos para la creación de rutina",
        T("Una buena rutina no es una lista de ejercicios: es una **experiencia con lógica** que calienta, desafía, permite "
          "recuperar y cierra. Estos conceptos son las herramientas para construirla."),
        H("Principios del entrenamiento", 4),
        TBL(["Principio", "Significado", "Aplicación en clase"], [
            ["Sobrecarga progresiva", "El cuerpo se adapta si el estímulo aumenta gradualmente", "Subir peso, reps, tiempo o complejidad cada 2–4 semanas"],
            ["Especificidad", "Te adaptas a lo que entrenas", "Si el objetivo es fuerza de piernas, prioriza patrones de pierna"],
            ["Individualidad", "Cada persona responde distinto", "Ofrecer regresiones y progresiones"],
            ["Variedad", "Cambiar estímulos evita estancamiento y aburrimiento", "Rotar formatos, no todo cada clase"],
            ["Recuperación", "La adaptación ocurre en el descanso", "No repetir el mismo grupo intenso en días consecutivos"],
            ["Reversibilidad", "Lo que no se usa se pierde", "Constancia: mínimo 2 sesiones semanales"],
        ], widths=[1.5, 2.4, 2.6]),
        H("FITT-VP", 4),
        TBL(["Letra", "Variable", "Ejemplo"], [
            ["F", "Frecuencia", "3 clases por semana"], ["I", "Intensidad", "RPE 7–8 al final de cada bloque"],
            ["T", "Tiempo", "45 minutos"], ["T", "Tipo", "Fuerza con mancuernas + cardio de bajo impacto"],
            ["V", "Volumen", "≈ 12 series por grupo muscular a la semana"], ["P", "Progresión", "+1 ronda o +5 s por intervalo cada 2 semanas"],
        ], widths=[0.7, 1.6, 4.2]),
        H("Calentamiento RAMP", 4),
        TBL(["Fase", "Objetivo", "Ejemplo (5–8 min)"], [
            ["R – Raise (elevar)", "Temperatura y pulso", "Marcha, step touch, jacks suaves"],
            ["A – Activate (activar)", "Encender músculos clave", "Puente de glúteo, retracción escapular"],
            ["M – Mobilize (movilizar)", "Rango en articulaciones a usar", "Círculos de cadera, cat-cow de pie, rotaciones torácicas"],
            ["P – Potentiate (potenciar)", "Preparar para la intensidad", "Sentadillas a ritmo, push ups inclinados"],
        ], widths=[1.8, 1.8, 2.9]),
        H("Orden de los ejercicios", 4),
        UL("**Multiarticulares antes que aislamientos:** la sentadilla antes que la patada de glúteo.",
           "**Grandes antes que pequeños:** espalda antes que bíceps.",
           "**Alterna** empuje/tracción o tren inferior/superior para recuperar mientras sigues trabajando.",
           "**Cambia poco de nivel:** agrupa los ejercicios de pie, luego de rodillas, luego en suelo.",
           "**Prepara los props al inicio** para no detener la clase."),
        H("Densidad, volumen y relación trabajo:descanso", 4),
        TBL(["Relación", "Ejemplo", "Efecto"], [
            ["1:1", "30 s / 30 s", "Fuerza y técnica; principiantes"],
            ["2:1", "40 s / 20 s", "Estándar de circuito; equilibrio fuerza-cardio"],
            ["3:1", "45 s / 15 s", "Más estrés metabólico"],
            ["Continuo", "Bloques de 3–4 min sin pausa", "Resistencia muscular"],
        ], widths=[1.2, 2.2, 3.1]),
        BOX("tip", "Equilibrio muscular", "Cuenta los ejercicios por patrón en tu rutina. Si tienes 4 empujes y 1 tracción, añade tracciones. "
            "Si todo el core es flexión (crunch), añade anti-extensión (plancha) y anti-rotación (Pallof)."),
    ),
    topic("Creación de rutina práctica tren superior",
        T("Construiremos juntas una rutina de tren superior de 45 minutos, explicando cada decisión."),
        H("Paso 1 · Define el objetivo y el público", 4),
        T("Objetivo: resistencia muscular e hipertrofia ligera de brazos, hombros y espalda. Público: nivel mixto. Equipo: "
          "mancuernas ligeras (1–3 kg) y medias (3–6 kg), mat."),
        H("Paso 2 · Elige patrones y reparte", 4),
        TBL(["Patrón", "Ejercicios elegidos"], [
            ["Empuje vertical", "Press de hombros"], ["Empuje horizontal", "Push up (con regresiones), press en suelo"],
            ["Tracción horizontal", "Remo inclinado, pájaros"], ["Brazos", "Curl, extensión de tríceps sobre la cabeza"],
            ["Hombro aislado", "Elevaciones laterales"], ["Core", "Plancha y variaciones"],
        ], widths=[2.2, 4.3]),
        H("Paso 3 · Agrupa en bloques y ordena", 4),
        T("Se forman tres bloques con superseries empuje + tracción, de pie primero y suelo al final."),
        H("Paso 4 · Asigna tiempos y formatos", 4),
        TBL(ROUT_HEAD, [
            ["Calentamiento", "6 min", "Marcha, círculos de brazos, retracción escapular, push up en pared", "Continuo", "Elevar pulso y movilizar hombros"],
            ["Bloque 1", "10 min", "Press de hombros + remo inclinado", "3 rondas: 12 + 12, 45 s pausa", "Superserie empuje/tracción"],
            ["", "", "Elevación lateral (finisher)", "16 lentas + 16 pulsos", "Estrés metabólico"],
            ["Bloque 2", "10 min", "Curl + extensión de tríceps", "3 rondas 40/20", "Peso medio"],
            ["", "", "Pájaros", "2 × 15", "Postura"],
            ["Cardio", "3 min", "Jacks / step jacks + mountain climbers", "30/15 × 4", "Ofrecer bajo impacto"],
            ["Bloque 3 (suelo)", "10 min", "Push up (nivel propio) + press en suelo", "Escalera 2-4-6-8", "Nivel personal"],
            ["", "", "Shoulder taps + plancha de antebrazos", "2 × 30 s", "Core"],
            ["Enfriamiento", "6 min", "Estiramientos de pecho, tríceps, espalda", "20–30 s c/u", "Respiración"],
        ], widths=ROUT_W, small=True),
        H("Paso 5 · Revisa el equilibrio", 4),
        UL("Empujes: press de hombros, push up, press en suelo, extensión de tríceps → 4.",
           "Tracciones: remo, pájaros (+ curl como flexión de codo) → 3. Aceptable; podría añadirse un remo a una mano.",
           "Core: anti-extensión (planchas) y anti-rotación (shoulder taps)."),
    ),
    topic("Creación de rutinas teoría",
        T("Toda clase de fuerza grupal puede describirse con una curva de intensidad: sube, ondula con bloques y cardio, y baja."),
        FIG("d_curve_sculpt", "Figura. Curva de intensidad de una clase de Sculpt & Burn de 45–50 min (ejemplo didáctico)."),
        H("Fases y porcentaje de tiempo", 4),
        TBL(["Fase", "% de la clase", "Contenido"], [
            ["Calentamiento", "10–15 %", "RAMP"], ["Bloques de fuerza", "50–60 %", "2–4 bloques"],
            ["Cardio", "10–15 %", "Ráfagas entre bloques o bloque propio"], ["Core", "10–15 %", "Integrado o bloque final"],
            ["Enfriamiento", "8–12 %", "Bajada, estiramientos, cierre"],
        ], widths=[1.8, 1.4, 3.3]),
        H("Anatomía de un bloque", 4),
        OL("**Introducción:** demostración breve y regresiones/progresiones.", "**Construcción:** el ejercicio base con ritmo controlado.",
           "**Intensificación:** pulsos, isométrico, tempo o combo.", "**Pico:** ráfaga de cardio o finisher.",
           "**Recuperación activa:** estiramiento breve del grupo trabajado o transición."),
        H("Formatos de bloque", 4),
        TBL(["Formato", "Estructura", "Ventaja"], [
            ["Superserie", "A + B sin pausa, × 3", "Eficiencia; alterna grupos"], ["Circuito por tiempo", "4–6 ejercicios 40/20, × 2–3", "Fácil de seguir con música"],
            ["Escalera", "2-4-6-8 o 10-8-6-4", "Progresión visible"], ["Capas (layering)", "Base → pulsos → isométrico → combo", "Muy usado en sculpt y barre"],
            ["EMOM", "Tarea al inicio de cada minuto", "Autorregulación"],
        ], widths=[1.6, 2.5, 2.4]),
        BOX("practica", "Plantilla en blanco", "Usa la plantilla de rutina del Apéndice C para escribir tus clases."),
    ),
    topic("Adaptación de rutinas de acuerdo a objetivos y duración",
        H("Por objetivo", 4),
        TBL(["Objetivo", "Carga", "Reps / tiempo", "Descanso", "Herramientas"], [
            ["Hipertrofia / «tonificar»", "Media", "8–15 reps o 40–45 s cerca del fallo", "45–90 s", "Tempo, 1½, pausa"],
            ["Resistencia muscular", "Ligera", "15–25 reps o 45–60 s", "15–30 s", "Pulsos, isométricos, capas"],
            ["Acondicionamiento / gasto calórico", "Ligera-media", "Intervalos 30–45 s", "15–20 s", "Circuitos, cardio intercalado"],
            ["Fuerza", "Más alta", "6–10 reps", "60–120 s", "Ejercicios grandes, menos variedad"],
            ["Movilidad y postura", "Peso corporal", "Lento, rango completo", "Libre", "Bisagra, espalda alta, core"],
        ], widths=[1.6, 0.9, 1.6, 0.9, 1.5], small=True),
        H("Por población (siempre con autorización médica cuando aplique)", 4),
        TBL(["Población", "Adaptaciones clave"], [
            ["Principiantes", "Menos ejercicios, más repetición del patrón, 1:1, enseñar regresiones primero"],
            ["Adultos mayores", "Equilibrio y fuerza de piernas, sentarse-levantarse, evitar cambios bruscos de nivel, bajo impacto"],
            ["Embarazo", "Autorización médica; evitar posiciones boca arriba prolongadas a partir del segundo trimestre, sin impacto si no hay experiencia previa, evitar crunch intenso, prueba del habla"],
            ["Posparto", "Autorización médica; reintroducción gradual del core profundo y suelo pélvico; vigilar diástasis"],
            ["Sobrepeso / articulaciones sensibles", "Bajo impacto, transiciones mínimas al suelo, apoyos"],
        ], widths=[1.8, 4.7]),
        H("Por duración", 4),
        TBL(["Duración", "Calentamiento", "Fuerza", "Cardio", "Core", "Enfriamiento"], [
            ["30 min", "4 min", "16 min (2 bloques)", "3 min", "4 min", "3 min"],
            ["45 min", "6 min", "24 min (3 bloques)", "4 min", "6 min", "5 min"],
            ["50 min", "6 min", "28 min (3 bloques)", "5 min", "6 min", "5 min"],
            ["60 min", "8 min", "32 min (4 bloques)", "6 min", "8 min", "6 min"],
        ], widths=[0.9, 1.1, 1.6, 0.9, 0.9, 1.1]),
        BOX("tip", "Cómo recortar una clase sin perder calidad",
            "Elimina un bloque completo en lugar de acortar todos; conserva calentamiento y enfriamiento; usa superseries."),
    ),
], [
    Q("¿Qué significa la R del calentamiento RAMP?", ["Repetir", "Raise: elevar temperatura y pulso", "Relajar", "Rotar"], 1, ""),
    Q("¿Qué orden es generalmente recomendado?", ["Aislamientos antes que multiarticulares", "Multiarticulares antes que aislamientos", "Core siempre primero", "No importa"], 1, ""),
    Q("Una relación 2:1 equivale, por ejemplo, a 40 s de trabajo y 20 s de descanso.", None, "V", ""),
    Q("Para recortar una clase de 60 a 45 min lo ideal es eliminar el calentamiento.", None, "F", "Mejor eliminar un bloque y conservar calentamiento y enfriamiento."),
    Q("En embarazo, a partir del segundo trimestre, ¿qué posición conviene evitar de forma prolongada?", ["De pie", "Boca arriba", "Sentada", "Cuadrupedia"], 1, ""),
    Q("Diseña una rutina de 30 minutos de tren superior usando la tabla de duración.", None, "Respuesta abierta: revisa equilibrio empuje/tracción y tiempos por fase.", ""),
])

# =====================================================================
# MÓDULO 8
# =====================================================================
m8 = module(8, "Práctica rutina tren inferior · Práctica rutina tren superior", [
    "Dirigir de principio a fin una clase completa de tren inferior y otra de tren superior.",
    "Registrar y autoevaluar tu práctica.",
], [
    topic("Práctica rutina tren inferior",
        BOX("general", "Propuesta didáctica",
            "Las rutinas de este módulo son **ejemplos de práctica** creados con los fundamentos de este libro. No son "
            "coreografías oficiales del método TBM."),
        H("Clase de 50 minutos · Tren inferior y glúteo", 4),
        TBL(ROUT_HEAD, [
            ["Calentamiento", "0:00–6:00", "Marcha + step touch; sentadilla a puntas; puente de glúteo ×10; círculos de cadera", "Continuo", "BPM 115–122"],
            ["Bloque 1 · Sentadilla", "6:00–16:00", "Sentadilla goblet", "12 reps → 8 lentas (3-1-1) → 16 pulsos → isométrico 20 s", "Capas"],
            ["", "", "Peso muerto rumano", "2 × 12", "Alterna anterior/posterior"],
            ["Cardio 1", "16:00–19:00", "Sentadilla con salto / a puntas + skaters / paso lateral", "30/15 × 4", "Ofrecer bajo impacto"],
            ["Bloque 2 · Zancadas", "19:00–29:00", "Zancada atrás (der.) → split pulsos → zancada atrás (izq.) → split pulsos", "10 + 16 por lado × 2", "Pierna por pierna"],
            ["", "", "Zancada lateral", "8 por lado", "Plano frontal"],
            ["Cardio 2", "29:00–31:00", "Rodillas altas / marcha", "45 s × 2", "Recuperar en marcha"],
            ["Bloque 3 · Suelo", "31:00–41:00", "Puente de glúteo → puente a una pierna → patada en cuadrupedia → fire hydrant", "40/20, 2 rondas", "Mini ball opcional en puente"],
            ["Core", "41:00–45:00", "Dead bug + plancha lateral", "40/20 × 2", ""],
            ["Enfriamiento", "45:00–50:00", "Figura 4, flexor de cadera, isquios, niño", "30 s c/u", "BPM 60–90"],
        ], widths=ROUT_W, small=True),
        H("Guion de voz para el bloque 1 (ejemplo)", 4),
        T("«Toma tu mancuerna pesada y colócala frente al pecho. Pies a la anchura de tu sentadilla. En cuatro… bajamos. "
          "Cadera atrás, pecho orgulloso, rodillas hacia tus dedos. ¡Arriba! Dos más… Ahora bajamos en tres tiempos: tres, "
          "dos, uno, pausa… ¡y sube! Quédate abajo: pulsos pequeños… Últimos ocho… Sostén aquí, respira, veinte segundos. "
          "Si arden las piernas, ¡estás exactamente donde tienes que estar!»"),
        H("Registro de práctica", 4),
        TBL(["Fecha", "Duración", "¿Respeté los tiempos?", "Cue que mejor funcionó", "Qué mejorar"], [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]],
            widths=[0.9, 0.9, 1.4, 1.7, 1.6]),
    ),
    topic("Práctica rutina tren superior",
        H("Clase de 45 minutos · Brazos, hombros, espalda y core", 4),
        TBL(ROUT_HEAD, [
            ["Calentamiento", "0:00–6:00", "Marcha con brazos, círculos, Y-T-W de pie, push up en pared ×10", "Continuo", "BPM 115–122"],
            ["Bloque 1 · Hombro", "6:00–15:00", "Press de hombros → elevación lateral → elevación frontal", "10 + 10 + 10 × 3", "Peso ligero en elevaciones"],
            ["", "", "Remo inclinado", "12 × 3 (entre rondas)", "Tracción"],
            ["Cardio 1", "15:00–18:00", "Jacks / step jacks + burpee / con pasos", "30/15 × 4", ""],
            ["Bloque 2 · Brazos", "18:00–27:00", "Curl → curl martillo → patada de tríceps → extensión sobre cabeza", "Escalera 8-10-12", "Peso medio"],
            ["", "", "Pájaros", "15 × 2", "Postura"],
            ["Bloque 3 · Suelo", "27:00–37:00", "Push up (nivel propio) + press en suelo + aperturas", "40/20 × 2", "Regresiones claras"],
            ["Core", "37:00–40:00", "Shoulder taps, plancha a pike, bear plank", "30/15", ""],
            ["Enfriamiento", "40:00–45:00", "Pecho, tríceps, dorsal, cuello", "30 s c/u", "Respiración 4-6"],
        ], widths=ROUT_W, small=True),
        BOX("practica", "Autoevaluación de la clase",
            UL("¿Di la indicación del siguiente ejercicio antes de que terminara el actual?", "¿Ofrecí regresión y progresión en cada bloque?",
               "¿El volumen de empuje y tracción estuvo equilibrado?", "¿Se cumplió la duración planeada (± 2 min)?",
               "¿Mi voz se escuchó por encima de la música sin gritar?")),
    ),
], [
    Q("En la clase de tren inferior propuesta, ¿qué formato se usa en el bloque 1?", ["Tabata", "Capas: reps → tempo → pulsos → isométrico", "EMOM", "AMRAP"], 1, ""),
    Q("¿Por qué se intercala el peso muerto rumano tras la sentadilla goblet?", ["Para descansar los brazos", "Para alternar cadena anterior y posterior", "Porque es cardio", "No hay razón"], 1, ""),
    Q("Las rutinas de práctica de este libro son coreografías oficiales del método TBM.", None, "F", "Son propuestas didácticas."),
    Q("Graba tu clase de práctica de tren superior completa y completa la autoevaluación.", None, "Práctica.", ""),
])

# =====================================================================
# MÓDULO 9
# =====================================================================
m9 = module(9, "Cueing · Playlist Sculpt", [
    "Dar indicaciones claras, oportunas y motivadoras.",
    "Diseñar una playlist alineada con la estructura de la clase.",
], [
    topic("Cueing",
        T("**Cueing** es el arte de dar indicaciones. Un buen cue es **breve, oportuno y accionable**: la alumna lo entiende y "
          "lo puede ejecutar de inmediato."),
        FIG("d_cueflow", "Figura. Secuencia recomendada de indicaciones."),
        H("Tipos de cues", 4),
        TBL(["Tipo", "Qué es", "Ejemplo"], [
            ["Verbal de posición", "Dónde colocar el cuerpo", "«Pies a la anchura de la cadera»"],
            ["Verbal de acción", "Qué hacer", "«Baja la cadera atrás»"],
            ["Alineación / técnica", "Cómo hacerlo bien", "«Rodillas hacia tus dedos»"],
            ["Respiración", "Cuándo inhalar/exhalar", "«Exhala al subir»"],
            ["Visual", "Demostración o gesto", "Mostrar la profundidad con la mano"],
            ["Táctil", "Contacto físico guiado (con consentimiento)", "Mano en la escápula para indicar dirección"],
            ["Imagen (metáfora)", "Una imagen que provoca el movimiento", "«Cierra una puerta con los glúteos»"],
            ["Motivacional", "Energía y sentido", "«Ocho más: ¡tú puedes!»"],
            ["Seguridad", "Prevenir errores o lesiones", "«Si molesta la rodilla, reduce el rango»"],
        ], widths=[1.6, 2.2, 2.7]),
        H("Foco externo frente a interno", 4),
        T("La investigación sobre aprendizaje motor (Wulf y colaboradores) indica que los cues de **foco externo** (dirigidos "
          "al efecto del movimiento o al entorno: «empuja el suelo») suelen mejorar el rendimiento más que los de foco interno "
          "(«contrae el cuádriceps»). Usa ambos, pero apóyate en los externos y en imágenes."),
        H("Reglas de oro", 4),
        UL("**Anticipa:** da el siguiente ejercicio en los últimos 4–8 tiempos del actual («5-6-7-8»).",
           "**Menos es más:** un cue a la vez; prioriza el error más importante.",
           "**Lenguaje positivo:** «rodillas hacia fuera» en lugar de «no metas las rodillas».",
           "**Verbos de acción:** empuja, alarga, abre, presiona, exhala.",
           "**Cuenta hacia atrás:** el cerebro tolera mejor «ocho, siete, seis…».",
           "**Corrige al grupo, felicita a la persona:** la corrección general evita exponer a alguien.",
           "**Usa nombres** cuando felicites."),
        FIG("d_eight", "Figura. Frase musical de 32 tiempos y el momento de anticipar la indicación."),
        H("Banco de cues por ejercicio", 4),
        TBL(["Ejercicio", "Cue de técnica", "Cue de imagen"], [
            ["Sentadilla", "Peso en todo el pie, rodillas a los dedos", "Siéntate en una silla lejana"],
            ["Peso muerto rumano", "Cadera atrás, espalda larga", "Cierra una puerta con los glúteos"],
            ["Zancada", "Baja vertical, torso alto", "Baja como un elevador"],
            ["Push up", "Codos a 45°, cuerpo en bloque", "Eres una tabla de surf"],
            ["Remo", "Codos a la cadera", "Mete los codos en los bolsillos traseros"],
            ["Plancha", "Empuja el suelo, costillas cerradas", "Alarga del cráneo a los talones"],
            ["Press de hombros", "Costillas abajo, empuja arriba", "Empuja el techo"],
        ], widths=[1.6, 2.4, 2.5]),
        BOX("practica", "Ejercicio de práctica de voz",
            "Pon una canción de 128 BPM. Cuenta en voz alta 4 frases de 8 dando en cada una: posición (frase 1), acción (2), "
            "alineación (3) y motivación + anticipación del siguiente ejercicio (4). Grábate y repite hasta que suene natural."),
    ),
    topic("Playlist Sculpt",
        T("La música marca el ritmo, la energía y la estructura de la clase. Una playlist bien construida es un **guion "
          "sonoro**: cada canción acompaña una fase."),
        FIG("d_bpm_sculpt", "Figura. Rangos orientativos de BPM por fase en una clase de fuerza con música."),
        H("Construir la playlist paso a paso", 4),
        OL("Escribe la rutina con tiempos por bloque.", "Asigna a cada bloque una o dos canciones de duración similar.",
           "Ordena por BPM siguiendo la curva de intensidad.", "Comprueba transiciones: evita silencios largos o cambios bruscos.",
           "Revisa letras explícitas según el público.", "Ensaya la clase con la playlist completa."),
        TBL(["Fase", "BPM", "Carácter de la música", "Duración"], [
            ["Calentamiento", "110–122", "Positiva, ritmo claro", "1–2 canciones"],
            ["Fuerza", "118–130", "Ritmo estable, compás marcado", "2–3 por bloque"],
            ["Cardio", "130–160", "Energía alta", "1 canción"],
            ["Core", "110–125", "Constante, sin picos", "1–2 canciones"],
            ["Enfriamiento", "60–90", "Calmada", "1–2 canciones"],
        ], widths=[1.4, 0.9, 2.6, 1.6]),
        BOX("seguridad", "Volumen y derechos de autor",
            UL("Cuida el volumen: la voz debe escucharse sin gritar; usa micrófono en salas grandes.",
               "Usar música en clases comerciales requiere licencias de ejecución pública o servicios de música con licencia para fitness. "
               "Consulta la normativa de tu país (por ejemplo, la sociedad de autores local).")),
        OFICIAL("Playlist Sculpt", "Playlists oficiales o recomendadas por el método.", "Plataformas o proveedores de música autorizados.",
                "Criterios oficiales de BPM o estructura musical, si existen."),
    ),
], [
    Q("Un cue de foco externo es, por ejemplo…", ["«Contrae el glúteo»", "«Empuja el suelo»", "«Activa el cuádriceps»", "«Relaja el trapecio»"], 1, ""),
    Q("¿En qué momento conviene anticipar el siguiente ejercicio?", ["Al inicio de la frase", "En los tiempos 5-6-7-8 de la última frase", "Cuando ya terminó", "Nunca"], 1, ""),
    Q("«No metas las rodillas» es un ejemplo de lenguaje positivo.", None, "F", "La versión positiva sería «rodillas hacia fuera / hacia tus dedos»."),
    Q("¿Qué rango de BPM es típico para el enfriamiento?", ["60–90", "130–160", "120–130", "170–190"], 0, ""),
    Q("El contacto táctil siempre requiere consentimiento previo.", None, "V", ""),
    Q("Escribe tres cues (técnica, imagen, motivación) para el peso muerto rumano.", None,
      "Ej.: «Cadera atrás, espalda larga»; «Cierra una puerta con los glúteos»; «Cuatro más, ¡fuerte!».", ""),
])

# =====================================================================
# MÓDULO 10
# =====================================================================
m10 = module(10, "Conclusión Sculpt n Burn", [
    "Integrar los conocimientos de los nueve módulos anteriores.",
    "Autoevaluar tu preparación para dirigir una clase completa.",
], [
    topic("Conclusión Sculpt n Burn",
        T("Has recorrido el camino completo: desde la anatomía y la fisiología de la hipertrofia hasta el cueing y la música. "
          "Sculpt & Burn se sostiene en tres ideas: **técnica impecable, intensidad inteligente y una experiencia que motive**."),
        H("Resumen por módulos", 4),
        TBL(["Módulo", "Idea clave"], [
            ["1", "Separa fundamentos generales de contenido oficial; domina la terminología anatómica."],
            ["2", "La tensión mecánica cerca del fallo es el motor del cambio; el tempo controla las contracciones."],
            ["3", "Cada cuerpo tiene su sentadilla; los ejercicios unilaterales equilibran."],
            ["4", "La plancha es la base; equilibra empujes y tracciones."],
            ["5", "El push up se construye por escalones."],
            ["6", "Siempre dos opciones de impacto; core en todas sus funciones."],
            ["7", "Una rutina es una curva con lógica, adaptable a objetivo y duración."],
            ["8", "Practica clases completas y regístralas."],
            ["9", "Cues breves, anticipados y positivos; música alineada a la curva."],
        ], widths=[0.9, 5.6]),
        H("Checklist de preparación", 4),
        TBL(["Competencia", "Lo domino", "En proceso", "Debo repasar"], [
            ["Explico la técnica de 20 ejercicios básicos", "", "", ""], ["Ofrezco regresión y progresión de cada ejercicio", "", "", ""],
            ["Diseño una clase de 45 min equilibrada", "", "", ""], ["Doy cues anticipados al ritmo de la música", "", "", ""],
            ["Adapto una clase a principiantes", "", "", ""], ["Identifico señales para detener un ejercicio", "", "", ""],
        ], widths=[3.2, 1.1, 1.1, 1.1]),
        H("Rúbrica de clase práctica (autoevaluación)", 4),
        TBL(["Criterio", "1 · Inicial", "2 · Básico", "3 · Competente", "4 · Experto"], [
            ["Técnica y demostración", "Errores visibles", "Correcta con fallos menores", "Correcta y clara", "Impecable y adaptada"],
            ["Cueing", "Tardío o confuso", "Claro pero tardío", "Anticipado y claro", "Anticipado, variado e inspirador"],
            ["Estructura y tiempos", "Sin estructura", "Fases presentes, tiempos desajustados", "Fases y tiempos correctos", "Curva de intensidad fluida"],
            ["Seguridad y adaptaciones", "No ofrece opciones", "Opciones ocasionales", "Opciones en cada bloque", "Personaliza en tiempo real"],
            ["Música", "Desconectada", "Ritmo irregular", "Alineada a las fases", "Potencia la experiencia"],
        ], widths=[1.6, 1.1, 1.3, 1.25, 1.25], small=True),
        OFICIAL("Conclusión y certificación Sculpt n Burn", "Evaluación final oficial (teórica y práctica).", "Requisitos de horas y entrega de videos.",
                "Uso del nombre del método y renovación de la certificación."),
    ),
], [
    Q("Menciona las tres ideas que sostienen Sculpt & Burn según la conclusión.", None, "Técnica impecable, intensidad inteligente y experiencia motivadora.", ""),
    Q("Evaluación integradora: diseña una clase de 50 minutos de cuerpo completo con calentamiento RAMP, dos bloques de fuerza, cardio con dos opciones de impacto, core en dos funciones distintas y enfriamiento; incluye BPM y tres cues por bloque.", None,
      "Respuesta abierta; usa la rúbrica del tema.", ""),
])

MODULES = [m7, m8, m9, m10]
