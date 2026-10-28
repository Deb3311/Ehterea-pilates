from common import *

GLOSARIO = [
    ("1RM", "Carga máxima que se puede levantar una sola vez con buena técnica."),
    ("Abducción / aducción", "Alejar / acercar una extremidad a la línea media del cuerpo."),
    ("Agonista / antagonista", "Músculo que produce el movimiento / músculo que se opone a él."),
    ("Anteversión / retroversión", "Inclinación de la pelvis hacia delante / hacia atrás."),
    ("Anti-extensión / anti-rotación", "Trabajo de core que impide que la columna se arquee / gire."),
    ("Arabesque", "Pierna extendida hacia atrás (ballet)."),
    ("Attitude", "Pierna elevada con la rodilla flexionada (ballet)."),
    ("BPM", "Pulsaciones por minuto de la música."),
    ("Capas (layering)", "Trabajar un ejercicio en fases: rango completo, pulsos, isométrico, combo, elongación."),
    ("Contrología", "Nombre que Joseph Pilates dio a su método."),
    ("Cue", "Indicación verbal, visual o táctil que guía el movimiento."),
    ("Déficit", "Trabajo con apoyo elevado que aumenta el rango de movimiento."),
    ("DOMS (agujetas)", "Dolor muscular de aparición tardía, 24–72 h tras un esfuerzo nuevo o excéntrico."),
    ("EIAS", "Espinas ilíacas anterosuperiores: los «huesitos» frontales de la pelvis."),
    ("EMOM / AMRAP", "Cada minuto al minuto / tantas rondas o repeticiones como sea posible."),
    ("Estrés metabólico", "Acumulación de metabolitos durante esfuerzos continuos; produce la «quemazón»."),
    ("Excéntrica", "Contracción en la que el músculo se alarga bajo carga."),
    ("Fold-over", "Posición de barre con el tronco inclinado sobre la barra para trabajar glúteo."),
    ("Hipertrofia", "Aumento del tamaño de las fibras musculares."),
    ("Imprint", "Leve retroversión que acerca la zona lumbar al mat."),
    ("Isométrica", "Contracción sin cambio visible de longitud muscular."),
    ("Neutra (columna / pelvis)", "Posición que respeta las curvas naturales de la columna."),
    ("Passé / retiré", "Punta del pie a la altura de la rodilla de apoyo."),
    ("Plié", "Flexión de rodillas (demi = media, grand = profunda)."),
    ("Port de bras", "Movimiento de los brazos entre posiciones de ballet."),
    ("Powerhouse", "El «centro» en Pilates: abdomen, zona lumbar, glúteos y suelo pélvico."),
    ("Propiocepción", "Percepción de la posición y el movimiento del propio cuerpo."),
    ("Pulso", "Movimiento de rango muy corto (1–3 cm) repetido rítmicamente."),
    ("Regresión / progresión", "Versión más fácil / más difícil de un ejercicio."),
    ("Relevé", "Elevación a media punta."),
    ("RIR", "Repeticiones en reserva antes del fallo."),
    ("RPE", "Escala de esfuerzo percibido de 1 a 10."),
    ("Tempo", "Velocidad de cada fase de una repetición (p. ej., 3-1-1-0)."),
    ("Tensión mecánica", "Fuerza que soportan las fibras al contraerse contra resistencia; principal estímulo de hipertrofia."),
    ("Tuck", "Retroversión pélvica activa usada en algunos estilos de barre."),
    ("Turnout", "Rotación externa de las piernas desde la cadera."),
    ("Valgo / varo", "Rodilla que se desvía hacia dentro / hacia fuera."),
]

REFS = [
    "American College of Sports Medicine (ACSM). *ACSM's Guidelines for Exercise Testing and Prescription*. Wolters Kluwer (ediciones recientes).",
    "Haff, G. G. y Triplett, N. T. (eds.). *Essentials of Strength Training and Conditioning* (NSCA). Human Kinetics.",
    "Schoenfeld, B. J. (2010). The mechanisms of muscle hypertrophy and their application to resistance training. *Journal of Strength and Conditioning Research*, 24(10), 2857–2872.",
    "Schoenfeld, B. J. *Science and Development of Muscle Hypertrophy*. Human Kinetics.",
    "Morton, R. W. et al. (2018). A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains. *British Journal of Sports Medicine*, 52, 376–384.",
    "Organización Mundial de la Salud (2020). *Directrices de la OMS sobre actividad física y hábitos sedentarios*.",
    "Wulf, G. (2013). Attentional focus and motor learning: a review of 15 years. *International Review of Sport and Exercise Psychology*, 6(1), 77–104.",
    "Tanaka, H., Monahan, K. D. y Seals, D. R. (2001). Age-predicted maximal heart rate revisited. *Journal of the American College of Cardiology*, 37(1), 153–156.",
    "Behm, D. G. y Anderson, K. G. (2006). The role of instability with resistance training. *Journal of Strength and Conditioning Research*, 20(3), 716–722.",
    "Kendall, F. P. et al. *Músculos: pruebas funcionales, postura y dolor*. Marbán.",
    "Pilates, J. H. y Miller, W. J. (1945). *Return to Life Through Contrology*.",
    "Friedman, P. y Eisen, G. (1980). *The Pilates Method of Physical and Mental Conditioning*.",
    "Isacowitz, R. *Pilates* (2.ª ed.). Human Kinetics.",
    "Berk, L. y Prince, J. (1980). *The Lotte Berk Method of Exercise*.",
    "American College of Obstetricians and Gynecologists (ACOG). Physical Activity and Exercise During Pregnancy and the Postpartum Period (Committee Opinion 804, 2020).",
    "Material oficial del método TBM (manuales, videos y capacitación): fuente obligatoria para los contenidos señalados como «Requiere material oficial TBM».",
]


def _answer(q):
    if q["opts"]:
        letter = "abcdefgh"[q["a"]]
        txt = f"**{letter})** {q['opts'][q['a']]}"
    elif q["a"] in ("V", "F"):
        txt = "**Verdadero**" if q["a"] == "V" else "**Falso**"
    else:
        txt = q["a"] or "Respuesta abierta."
    if q.get("why"):
        txt += f" — {q['why']}"
    return txt


def build(book):
    out = []
    out.append({"title": "Apéndice A · Glosario", "blocks": [TBL(["Término", "Definición"], [[a, b] for a, b in GLOSARIO], widths=[1.9, 4.6], small=True)]})
    sol = []
    for part in book["parts"]:
        sol.append(H(part["title"], 3))
        for m in part["modules"]:
            rows = [[str(i + 1), _answer(q)] for i, q in enumerate(m["quiz"])]
            sol.append(H(f"Módulo {m['num']}", 4))
            sol.append(TBL(["#", "Respuesta"], rows, widths=[0.4, 6.1], small=True))
    out.append({"title": "Apéndice B · Solucionario de las evaluaciones", "blocks": sol})
    plant = [
        H("Plantilla de rutina", 3),
        TBL(["Clase:", "", "Duración:", ""], [["Objetivo:", "", "Nivel:", ""], ["Props:", "", "Fecha:", ""]], widths=[1.1, 2.15, 1.1, 2.15]),
        TBL(["Bloque", "Tiempo", "Ejercicio", "Dosificación", "Regresión / progresión", "Cue clave", "BPM"],
            [["Calentamiento", "", "", "", "", "", ""]] + [["", "", "", "", "", "", ""] for _ in range(9)] + [["Enfriamiento", "", "", "", "", "", ""]],
            widths=[1.0, 0.6, 1.3, 0.9, 1.2, 1.0, 0.5], small=True),
        H("Registro de progreso personal", 3),
        TBL(["Semana", "Clases realizadas", "Ejercicio que mejoró", "Carga / nivel", "Notas"], [[str(i), "", "", "", ""] for i in range(1, 9)],
            widths=[0.8, 1.2, 1.8, 1.1, 1.6], small=True),
        H("Plan de estudio sugerido (12 semanas)", 3),
        TBL(["Semanas", "Contenido", "Práctica"], [
            ["1–2", "Sculpt & Burn módulos 1–3", "Sentadilla, zancada y bisagra diarias (10 min)"],
            ["3–4", "Sculpt & Burn módulos 4–6", "Planchas, push up, cardio de bajo/alto impacto"],
            ["5–6", "Sculpt & Burn módulos 7–10", "Dirigir 2 clases completas grabadas"],
            ["7–8", "Barre módulos 1–5", "Posiciones de ballet y ejercicios en barra"],
            ["9", "Barre módulos 6–9", "Coreografías y clase completa"],
            ["10–11", "Block Burn Pilates módulos 1–6", "Repertorio con blocks"],
            ["12", "Block Burn Pilates módulos 7–9", "Clase completa + autoevaluación final"],
        ], widths=[0.9, 2.6, 3.0]),
    ]
    out.append({"title": "Apéndice C · Plantillas", "blocks": plant})
    rub = [TBL(["Criterio", "1 · Inicial", "2 · Básico", "3 · Competente", "4 · Experto"], [
        ["Técnica y demostración", "Errores visibles", "Correcta con fallos menores", "Correcta y clara", "Impecable y adaptada"],
        ["Alineación y seguridad", "No corrige", "Corrige tarde", "Corrige a tiempo", "Previene y personaliza"],
        ["Cueing", "Tardío o confuso", "Claro pero tardío", "Anticipado y claro", "Anticipado, variado e inspirador"],
        ["Estructura y tiempos", "Sin estructura", "Fases presentes", "Fases y tiempos correctos", "Curva fluida"],
        ["Transiciones", "Pausas largas", "Algunas pausas", "Fluidas", "Fluidas y creativas"],
        ["Uso de props", "Interrumpe la clase", "Correcto", "Eficiente", "Aporta valor en cada bloque"],
        ["Música", "Desconectada", "Ritmo irregular", "Alineada a las fases", "Potencia la experiencia"],
    ], widths=[1.6, 1.1, 1.3, 1.25, 1.25], small=True),
        *T("Puntuación: 7–13 inicial · 14–20 en desarrollo · 21–25 competente · 26–28 lista para dirigir clases. "
          "Esta rúbrica es una herramienta de autoevaluación; la evaluación oficial la define el método TBM.")]
    out.append({"title": "Apéndice D · Rúbrica general de clase práctica", "blocks": rub})
    out.append({"title": "Apéndice E · Referencias y lecturas recomendadas", "blocks": [UL(*REFS)]})
    return out
