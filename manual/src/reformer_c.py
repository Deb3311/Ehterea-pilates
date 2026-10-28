from common import *

RH = ["#", "Ejercicio", "Resortes", "Reps", "Notas de enseñanza"]
RW = [0.35, 2.0, 1.25, 0.6, 2.3]

m10 = module(10, "Observación, cueing y asistencia en el reformer", [
    "Observar el movimiento con un método sistemático.",
    "Dar indicaciones claras y usar el contacto táctil con consentimiento.",
    "Corregir los errores más comunes de cada serie.",
], [
    topic("Observar antes de corregir",
        OL("**Vista general:** ¿el movimiento fluye? ¿el carro se controla?", "**De centro a periferia:** pelvis y columna → caja torácica y escápulas → extremidades.",
           "**Los dos lados:** ¿hay asimetría?", "**Respiración:** ¿contiene el aire?", "**Una corrección a la vez:** la que más impacto tenga."),
        BOX("tip", "Desde dónde mirar", "Para footwork y feet in straps, colócate al pie del reformer para ver rodillas y pelvis. Para planchas y "
            "knee stretches, mira de lado. Para rowing y short box, de frente y de lado."),
    ),
    topic("Cueing en el reformer",
        FIG("d_cueflow", "Figura. Secuencia de indicaciones."),
        TBL(["Tipo de cue", "Ejemplo en el reformer"], [
            ["Montaje", "«Dos resortes medios, footbar media, reposacabezas abajo.»"],
            ["Posición", "«Talones juntos sobre la barra, hombros contra las hombreras.»"],
            ["Acción", "«Empuja el carro hasta estirar las piernas.»"],
            ["Imagen", "«Imprime la columna en el carro como en arena húmeda.»"],
            ["Respiración", "«Exhala al alejar el carro.»"],
            ["Ritmo", "«Fuera en uno, regresa en tres.»"],
            ["Seguridad", "«Controla el regreso: que el carro no golpee.»"],
        ], widths=[1.6, 4.9]),
        BOX("cue", "Foco externo con el aparato", "El reformer facilita los cues de foco externo: «empuja la barra», «aleja el carro», «presiona las hombreras». Úsalos tanto como los anatómicos."),
    ),
    topic("Asistencia táctil (hands-on)",
        UL("Pide **consentimiento** antes de tocar y explica para qué.", "Toca con la mano abierta, en zonas óseas o musculares neutras (sacro, escápulas, costillas laterales).",
           "Indica dirección («hacia aquí»), no fuerces rango.", "Retira la mano en cuanto se logra la corrección.", "Respeta a quien prefiera no ser tocada: usa cues visuales o verbales."),
    ),
    topic("Errores frecuentes por serie",
        TBL(["Serie", "Error frecuente", "Corrección"], [
            ["Footwork", "Pelvis que se balancea", "Menos rango; «cadera pesada en el carro»"],
            ["Hundred", "Tensión de cuello", "Cabeza apoyada o mano bajo la nuca"],
            ["Feet in straps", "Zona lumbar arqueada", "Piernas más altas"],
            ["Stomach massage", "Perder la C", "Resortes más ligeros, rango corto"],
            ["Short box", "Bajar demasiado", "Límite: borde de la caja"],
            ["Elephant / long stretch", "Hombros que colapsan", "«Empuja la barra lejos»"],
            ["Knee stretches", "Mover hombros", "«Solo se mueven los muslos»"],
            ["Rowing", "Hombros arriba", "Resorte más ligero"],
            ["Splits", "Pérdida de control del carro", "Rango corto, supervisión cercana"],
        ], widths=[1.6, 2.2, 2.7]),
    ),
], [
    Q("¿Cuál es el orden recomendado para observar?", ["De la periferia al centro", "Del centro a la periferia", "Solo los pies", "Solo la cabeza"], 1, ""),
    Q("El contacto táctil requiere consentimiento.", None, "V", ""),
    Q("Corrige todos los errores a la vez para ahorrar tiempo.", None, "F", "Una corrección a la vez."),
    Q("Escribe un cue de foco externo para el footwork.", None, "Ej.: «Empuja la barra lejos».", ""),
])

m11 = module(11, "Diseño de clases, adaptaciones y contraindicaciones", [
    "Estructurar una clase de reformer siguiendo la lógica clásica.",
    "Adaptar ejercicios y resortes a cada persona.",
    "Reconocer contraindicaciones y precauciones.",
], [
    topic("Estructura de la clase clásica",
        T("El orden clásico va de **supino** (footwork, Hundred, correas) a **sentada** (stomach massage, short box), luego a **rodillas y "
          "de pie** (elephant, knee stretches, splits) y vuelve a **supino** para cerrar (running, pelvic lift). Esta progresión "
          "calienta, trabaja la columna en todas direcciones y termina con la persona organizada."),
        FIG("d_curve_reformer", "Figura. Curva de intensidad de una clase de reformer de 50 minutos (ejemplo)."),
        TBL(["Nivel", "Orden de referencia"], [
            ["Básico", "Footwork · Hundred · Frog · Leg circles · Stomach massage (round, hands back) · Short box (round, flat) · Elephant · Knee stretches (round, arched) · Running · Pelvic lift"],
            ["Intermedio", "Footwork · Hundred · Coordination · Rowing · Long box (pulling straps, backstroke, teaser) · Long stretch series · Stomach massage completo · Short box completo · Semi-circle · Chest expansion · Thigh stretch · Arm circles · Knee stretches (con knees off) · Running · Pelvic lift · Side splits · Front splits"],
            ["Avanzado", "Intermedio + Overhead · Short spine · Corkscrew · Tic-toc · Balance control · Long spine · Tendon stretch · Snake/twist · Star · Horseback · Russian splits · Control push up"],
        ], widths=[1.1, 5.4], small=True),
        BOX("escuela", "Orden de referencia", "El orden exacto varía entre linajes (por ejemplo, la ubicación de Frog/Leg circles o de Short spine). Usa esta tabla como guía y respeta el orden de tu escuela."),
    ),
    topic("Clases privadas y grupales",
        TBL(["Aspecto", "Privada", "Grupal"], [
            ["Personalización", "Total", "Por bloques; ofrecer opciones"],
            ["Cambios de resorte", "La instructora los hace", "Se enseñan para que cada alumna los haga"],
            ["Repertorio", "Completo según la persona", "Ejercicios seguros para el grupo; evitar avanzados de alto riesgo"],
            ["Ritmo", "Ajustado", "Fluido, con cues anticipados"],
        ], widths=[1.6, 2.45, 2.45]),
    ),
    topic("Adaptaciones y contraindicaciones",
        TBL(["Condición", "Precauciones", "Alternativas"], [
            ["Osteoporosis / osteopenia", "Evitar flexión con carga, rotación forzada e inversiones", "Footwork neutro, extensión suave, rowing erguida"],
            ["Dolor lumbar inespecífico", "Evitar rangos que provoquen dolor; palancas cortas", "Footwork, pelvic lift corto, knee stretches arched suaves"],
            ["Embarazo (con autorización)", "Evitar supino prolongado desde el 2.º trimestre, inversiones y flexión intensa", "Sentada, de rodillas, lateral; resortes moderados"],
            ["Problemas cervicales", "Evitar Hundred con cabeza elevada e inversiones", "Cabeza apoyada"],
            ["Hombro inestable o doloroso", "Evitar planchas con carro inestable y rangos por encima de la cabeza", "Correas con rango corto"],
            ["Rodilla", "Evitar hiperextensión y flexión profunda con carga", "Footwork con rango corto, footbar más alta"],
            ["Hipermovilidad", "No buscar rangos extremos", "Énfasis en control y fuerza"],
        ], widths=[1.7, 2.5, 2.3], small=True, caption="Información general; no sustituye la valoración de un profesional de la salud."),
    ),
], [
    Q("¿Con qué serie suele iniciar una clase clásica de reformer?", ["Short box", "Footwork", "Splits", "Long box"], 1, ""),
    Q("En osteoporosis conviene evitar…", ["Footwork", "Flexión de columna con carga", "Respirar", "Rowing erguida"], 1, ""),
    Q("En clases grupales conviene enseñar a las alumnas a cambiar sus resortes.", None, "V", ""),
    Q("Las inversiones son recomendables durante el embarazo.", None, "F", ""),
    Q("Escribe el orden básico de referencia.", None, "Footwork, Hundred, Frog, Leg circles, Stomach massage, Short box, Elephant, Knee stretches, Running, Pelvic lift.", ""),
])

m12 = module(12, "Clases de práctica y conclusión", [
    "Dirigir clases completas de nivel básico e intermedio.",
    "Autoevaluar tu práctica con una rúbrica.",
], [
    topic("Clase básica (45 minutos)",
        BOX("general", "Propuesta didáctica", "Configuraciones orientativas; ajusta resortes y repeticiones al equipo y a cada persona."),
        TBL(RH, [
            ["1", "Footwork: V, arcos, talones, tendon stretch", "Pesado", "10 c/u", "Hombros contra hombreras; pelvis quieta"],
            ["2", "Hundred", "Medio", "100", "Piernas en mesa; cabeza apoyada si hay tensión"],
            ["3", "Frog", "Medio-pesado", "10", "Pies en correas con carro en reposo"],
            ["4", "Leg circles", "Medio-pesado", "5 + 5", "Círculos pequeños"],
            ["5", "Stomach massage: round, hands back", "Medio-pesado", "10 c/u", "Mantener la C / crecer"],
            ["6", "Short box: round back, flat back", "Todos", "3–5", "Revisar correa de pies"],
            ["7", "Elephant", "Medio", "5–10", "Solo se mueven las piernas"],
            ["8", "Knee stretches: round, arched", "Medio", "10 c/u", "Hombros quietos"],
            ["9", "Running", "Pesado", "20", "Carro quieto"],
            ["10", "Pelvic lift", "Pesado", "5–10", "Articular la columna"],
        ], widths=RW, small=True),
    ),
    topic("Clase intermedia (55 minutos)",
        TBL(RH, [
            ["1", "Footwork completo", "Pesado", "10 c/u", ""], ["2", "Hundred (piernas a 45°)", "Medio", "100", ""],
            ["3", "Coordination", "Medio", "5", ""], ["4", "Rowing (back y front)", "Ligero", "3–5", "Cambiar resortes con fluidez"],
            ["5", "Long box: pulling straps, backstroke, teaser", "Ligero", "3–5", "Long box contra hombreras"],
            ["6", "Long stretch, down stretch, up stretch, elephant", "Medio", "3–5", ""],
            ["7", "Stomach massage completo", "Medio", "5–10", ""], ["8", "Short box completo", "Todos", "3", ""],
            ["9", "Semi-circle", "Medio", "3 + 3", ""], ["10", "Chest expansion, thigh stretch, arm circles", "Ligero", "3–4", "Arrodilladas frente a poleas"],
            ["11", "Knee stretches + knees off", "Medio", "10 c/u", ""], ["12", "Running, pelvic lift", "Pesado", "20 / 10", ""],
            ["13", "Side splits, front splits", "Ligero", "5 / 3 por lado", "Supervisión"],
        ], widths=RW, small=True),
    ),
    topic("Registro, rúbrica y conclusión",
        TBL(["Fecha", "Nivel", "¿Fluyó el orden?", "Resortes que ajusté", "Qué mejorar"], [["", "", "", "", ""] for _ in range(4)],
            widths=[0.9, 0.9, 1.5, 1.6, 1.6]),
        T("El reformer amplifica todo lo que hace el cuerpo: la buena técnica se vuelve más precisa y los errores se hacen "
          "visibles. Enseñarlo bien exige **conocer el aparato, respetar los principios y observar con atención**. Sigue "
          "practicando el repertorio en tu propio cuerpo; es la mejor escuela de una instructora."),
        BOX("practica", "Siguiente paso", "Busca una certificación integral reconocida (clásica o contemporánea) con horas de observación, práctica supervisada y examen. Este libro es material de estudio y no sustituye esa formación."),
    ),
], [
    Q("En la clase básica propuesta, ¿qué serie cierra la clase?", ["Elephant", "Pelvic lift", "Footwork", "Short box"], 1, ""),
    Q("Este libro sustituye una certificación integral.", None, "F", ""),
    Q("Evaluación integradora: dirige y graba una clase básica completa y evalúala con la rúbrica del Apéndice D.", None, "Práctica.", ""),
])

MODULES = [m10, m11, m12]
