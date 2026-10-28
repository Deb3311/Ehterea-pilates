import math
from common import *
import poses as P
from engine import L

HB = 0.85  # altura de un block en posición media (≈ 15 cm) en unidades de figura
HL = 0.5   # posición baja


def blk(at, **kw):
    d = {"k": "block", "at": at}
    d.update(kw)
    return d


def bridge_on(hb=HB, top=True, single=False):
    hip_h = 2.0 if top else 0.3
    trunk = -(90 - math.degrees(math.asin(min(hip_h / 3.0, 0.95))))
    th = 105 if top else 128
    knee_y = hip_h + L["thigh"] * (-math.cos(math.radians(th)))
    drop = knee_y - (hb + 0.05)
    sh = math.degrees(math.acos(max(min(drop / L["shin"], 1), -1)))
    p = dict(trunk=trunk, head=-90, thN=th, shN=sh, ftN=90, thF=th, shF=sh, ftF=90,
             uaN=trunk + 180, faN=trunk + 180, uaF=trunk + 180, faF=trunk + 180)
    if single:
        p.update(thN=th, shN=th, ftN=th + 95)
    return P.pose(**p)


def plank_on(hb=HB, kind="high", **kw):
    if kind == "high":
        hs = L["uarm"] + L["farm"] + L["hand"] * 0.6 + hb
        p = dict(uaN=0, faN=0)
    else:
        hs = L["uarm"] * math.cos(math.radians(55)) + L["farm"] + L["hand"] * 0.6 + hb
        p = dict(uaN=55, faN=0)
    th = P._incline(hs)
    p.update(trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=90 - th, ftN=-15)
    p.update(kw)
    return P.pose(**p)


HANDS_ON = [blk("HdN", to=True, w=0.9)]

# =====================================================================
# MÓDULO 1
# =====================================================================
m1 = module(1, "Bienvenida · ¿Qué es Block Burn Pilates? · Conceptos aplicados · Beneficios", [
    "Definir Block Burn Pilates y su relación con Pilates clásico, Sculpt & Burn y Barre.",
    "Explicar los conceptos biomecánicos que justifican el uso de blocks.",
    "Describir sus beneficios con lenguaje responsable.",
], [
    topic("Bienvenida",
        T("Bienvenida a Block Burn Pilates, la tercera disciplina de este libro. Aquí reunirás lo aprendido en Sculpt & Burn "
          "(fuerza y estructura de clase) y en Barre (alineación, capas y transiciones) con la base de **Pilates clásico**, "
          "usando los blocks como herramienta principal."),
        H("Requisitos previos recomendados", 4),
        UL("Dominar la pelvis neutra y la respiración costal (Barre, Módulo 2).", "Conocer la plancha y el push up (Sculpt & Burn, Módulos 4 y 5).",
           "Conocer la estructura de una clase (Sculpt & Burn, Módulo 7)."),
        OFICIAL("Bienvenida (Block Burn Pilates)", "Mensaje de bienvenida y propósito oficial de la disciplina.", "Requisitos oficiales de la formación."),
    ),
    topic("¿Qué es Block Burn Pilates?",
        BOX("general", "Definición de la disciplina",
            "Block Burn Pilates es una práctica de Pilates Clásico fusionada con elementos de Sculpt & Burn y Barre, en la que los "
            "blocks funcionan como herramienta principal. Al trabajar sobre una superficie inestable, se incrementa la "
            "activación muscular y se amplían los rangos de movimiento en los que normalmente entrenas. El resultado es una "
            "disciplina que fortalece, tonifica y reta al cuerpo de una forma distinta, mientras desarrolla mayor control, "
            "estabilidad y conciencia corporal."),
        TBL(["Componente", "Qué aporta"], [
            ["Pilates clásico", "Principios, repertorio de mat, control del centro, respiración y precisión"],
            ["Sculpt & Burn", "Fuerza, patrones funcionales, intervalos y estructura de bloques"],
            ["Barre", "Alineación, micromovimientos, capas y transiciones coreográficas"],
            ["Blocks", "Elevación, apoyo, inestabilidad, squeeze y mayor rango de movimiento"],
        ], widths=[1.8, 4.7]),
    ),
    topic("Conceptos aplicados a Block Burn Pilates",
        T("Estos conceptos de biomecánica general explican **por qué** un block cambia un ejercicio."),
        TBL(["Concepto", "Definición", "Cómo lo aplica el block"], [
            ["Base de sustentación", "Área sobre la que se apoya el cuerpo; más pequeña = menos estable", "Apoyar pies o manos en la superficie reducida del block"],
            ["Superficie inestable", "Superficie que cede o se mueve, exigiendo ajustes constantes", "Los blocks de espuma se comprimen y su base es estrecha"],
            ["Propiocepción", "Percepción de la posición del cuerpo", "Más información sensorial y ajustes de estabilizadores"],
            ["Rango de movimiento (déficit)", "Elevar el apoyo permite descender más", "Push up o zancada con apoyo elevado"],
            ["Palanca", "Distancia entre el eje y la resistencia", "Sostener un block con brazos extendidos alarga la palanca"],
            ["Contracción isométrica de aducción (squeeze)", "Presionar un objeto entre extremidades", "Block entre muslos o tobillos activa aductores y suelo pélvico"],
            ["Elevación (bajar la dificultad)", "Acercar el suelo a la persona", "Manos en blocks en estiramientos o planchas"],
        ], widths=[1.6, 2.4, 2.5], small=True),
        FIG("d_blocks", "Figura. Un block ofrece tres alturas según su orientación."),
        BOX("general", "Inestabilidad: matiz importante",
            "La evidencia indica que las superficies inestables aumentan la activación de los estabilizadores y la exigencia de "
            "control, pero reducen la fuerza máxima que se puede producir. Por eso en Block Burn se usan para **control, "
            "resistencia y rango**, no para cargas pesadas."),
    ),
    topic("Beneficios de Block Burn Pilates",
        TBL(["Beneficio", "Explicación"], [
            ["Mayor activación del centro y estabilizadores", "Por la base reducida y el squeeze"],
            ["Rango de movimiento ampliado", "Trabajo en déficit y elevaciones"],
            ["Fuerza y tonificación", "Elementos de Sculpt & Burn con capas de barre"],
            ["Equilibrio y propiocepción", "Ajustes continuos sobre el block"],
            ["Accesibilidad", "El block también facilita: eleva el suelo en estiramientos y planchas"],
            ["Variedad", "Un solo prop ofrece decenas de variaciones"],
        ], widths=[2.4, 4.1]),
    ),
], [
    Q("¿Cuáles son las tres influencias de Block Burn Pilates?", None, "Pilates clásico, Sculpt & Burn y Barre (con blocks como herramienta principal).", ""),
    Q("Reducir la base de sustentación hace un ejercicio…", ["Más estable", "Menos estable", "Igual", "Más fácil siempre"], 1, ""),
    Q("Las superficies inestables son ideales para levantar cargas máximas.", None, "F", "Reducen la fuerza máxima; se usan para control y rango."),
    Q("El block puede también hacer un ejercicio más fácil.", None, "V", "Por ejemplo, elevando el apoyo en planchas o estiramientos."),
    Q("¿Qué es trabajar en «déficit»?", ["Sin peso", "Con apoyo elevado para aumentar el rango", "Con poco tiempo", "Sin respirar"], 1, ""),
])

# =====================================================================
# MÓDULO 2
# =====================================================================
m2 = module(2, "Principios básicos de Pilates · Bases de Block Burn Pilates · Props", [
    "Explicar los principios de Pilates y aplicarlos al trabajo con blocks.",
    "Conocer los props, sus medidas y su uso seguro.",
], [
    topic("Principios Básicos de Pilates",
        T("Joseph Pilates llamó a su método **Contrología**. Sus alumnos y estudiosos posteriores sintetizaron sus ideas en "
          "principios. La formulación más difundida (Friedman y Eisen, 1980) incluye seis:"),
        FIG("d_wheel", "Figura. Los seis principios clásicos de Pilates.", 4.2),
        TBL(["Principio", "Significado", "Aplicación con blocks"], [
            ["Concentración", "Atención plena al movimiento", "Sentir la presión sobre el block"],
            ["Control", "Ningún movimiento es descuidado", "Evitar que el block se deslice o caiga"],
            ["Centro (powerhouse)", "El movimiento nace del centro: abdomen, zona lumbar, glúteos, suelo pélvico", "Squeeze para encender el centro"],
            ["Fluidez", "Movimiento continuo, sin tirones", "Transiciones con el block sin pausas"],
            ["Precisión", "Cada detalle cuenta", "Ubicación exacta del block"],
            ["Respiración", "Respiración completa que acompaña el movimiento", "Exhalar en el esfuerzo sobre la superficie inestable"],
        ], widths=[1.5, 2.6, 2.4]),
        H("Conceptos de alineación en Pilates", 4),
        TBL(["Concepto", "Descripción"], [
            ["Columna neutra", "Respeta las curvas naturales; se usa en muchos ejercicios contemporáneos"],
            ["Imprint (impronta)", "Leve retroversión que acerca la zona lumbar al mat; da seguridad con palancas largas"],
            ["Estabilización escapular", "Escápulas apoyadas en la caja torácica, sin elevar hombros"],
            ["Articulación de la columna", "Mover vértebra a vértebra (roll up, puente articulado)"],
            ["Oposición / elongación", "Alargarse en dos direcciones opuestas"],
        ], widths=[1.8, 4.7]),
        FIG("d_breath", "Figura. Respiración costal lateral.", 4.4),
    ),
    topic("Bases de Block Burn Pilates",
        T("Las bases propias de Block Burn Pilates dependen del material oficial. A partir de los fundamentos generales, "
          "estas son **reglas prácticas de seguridad y calidad** al trabajar con blocks:"),
        UL("El block se apoya siempre sobre un mat antideslizante y en una superficie seca.", "Antes de cargar peso, presiona el block para comprobar su estabilidad.",
           "Nunca saltes sobre un block ni lo uses como escalón para impacto.", "Elige la orientación (baja, media, alta) según el objetivo y el nivel.",
           "Si la técnica se pierde por la inestabilidad, retira el block o baja su altura.", "Coloca los blocks antes del bloque para no interrumpir el flujo."),
        OFICIAL("Bases de Block Burn Pilates", "Principios propios del método y su terminología.", "Estructura oficial de clase.",
                "Ejercicios y secuencias firma.", "Especificaciones oficiales de los blocks."),
    ),
    topic("Props de Block Burn Pilates",
        FIG("d_blocks", "Figura. Orientaciones del block (referencia: 23 × 15 × 7.5–10 cm)."),
        TBL(["Material", "Característica", "Uso recomendado"], [
            ["Espuma (EVA)", "Ligero, algo compresible y más inestable", "Squeeze, apoyos de mano, inestabilidad suave"],
            ["Corcho", "Firme y pesado, antideslizante", "Apoyos estables, elevación de pies"],
            ["Madera / bambú", "Muy firme, puede resbalar", "Uso limitado; requiere superficie antideslizante"],
        ], widths=[1.5, 2.4, 2.6]),
        TBL(["Prop complementario", "Uso"], [
            ["Mat", "Base de todo el trabajo"], ["Mancuernas ligeras", "Elementos de sculpt"], ["Mini ball", "Squeeze y apoyo"],
            ["Banda", "Resistencia adicional"], ["Toalla", "Apoyo de rodillas o cabeza"],
        ], widths=[2.2, 4.3]),
        BOX("seguridad", "Revisión del block", "Desecha blocks agrietados, deformados o con superficie resbaladiza."),
    ),
], [
    Q("¿Qué nombre dio Joseph Pilates a su método?", ["Pilates", "Contrología", "Powerhouse", "Body sculpt"], 1, ""),
    Q("¿Cuál NO es uno de los seis principios clásicos?", ["Centro", "Fluidez", "Velocidad", "Precisión"], 2, ""),
    Q("El imprint es una leve retroversión que acerca la zona lumbar al mat.", None, "V", ""),
    Q("Está permitido saltar sobre los blocks si son de corcho.", None, "F", ""),
    Q("Explica la diferencia entre un block de espuma y uno de corcho para Block Burn.", None, "Espuma: ligero, compresible, más inestable. Corcho: firme, pesado, más estable.", ""),
])

# =====================================================================
# MÓDULO 3
# =====================================================================
m3 = module(3, "Pilates clásico · Evolución de Pilates", [
    "Conocer la historia de Joseph Pilates y del repertorio clásico de mat.",
    "Distinguir Pilates clásico de los enfoques contemporáneos y de fusión.",
], [
    topic("Pilates Clásico",
        FIG("d_tl_pilates", "Figura. Hitos de la historia de Pilates."),
        T("**Joseph Hubertus Pilates** (1883–1967) nació en Mönchengladbach, Alemania. Fue un niño de salud frágil que se "
          "dedicó a estudiar gimnasia, culturismo, boxeo, artes marciales y yoga. Durante la Primera Guerra Mundial fue "
          "internado en Inglaterra, donde perfeccionó sus ejercicios y comenzó a usar resortes para asistir a personas "
          "postradas, origen de sus aparatos."),
        T("Hacia **1926** emigró a Estados Unidos y abrió con su esposa **Clara** un estudio en Nueva York, frecuentado por "
          "bailarines. Publicó *Your Health* (1934) y *Return to Life Through Contrology* (1945), donde describe 34 ejercicios "
          "de mat. Sus alumnas y alumnos directos, conocidos como **«elders»** (Romana Kryzanowska, Kathy Grant, Lolita San "
          "Miguel, Ron Fletcher, Carola Trier, Eve Gentry, entre otros), difundieron el método."),
        H("Los 34 ejercicios de Return to Life (orden original)", 4),
        TBL(["#", "Ejercicio", "#", "Ejercicio"], [
            ["1", "The Hundred", "18", "The Shoulder Bridge"],
            ["2", "The Roll Up", "19", "The Spine Twist"],
            ["3", "The Roll-Over with Legs Spread", "20", "The Jack Knife"],
            ["4", "The One Leg Circle", "21", "The Side Kick"],
            ["5", "Rolling Back", "22", "The Teaser"],
            ["6", "The One Leg Stretch", "23", "The Hip Twist with Stretched Arms"],
            ["7", "The Double Leg Stretch", "24", "Swimming"],
            ["8", "The Spine Stretch", "25", "The Leg-Pull Front"],
            ["9", "Rocker with Open Legs", "26", "The Leg-Pull"],
            ["10", "The Cork-Screw", "27", "The Side Kick Kneeling"],
            ["11", "The Saw", "28", "The Side Bend"],
            ["12", "The Swan-Dive", "29", "The Boomerang"],
            ["13", "The One Leg Kick", "30", "The Seal"],
            ["14", "The Double Kick", "31", "The Crab"],
            ["15", "The Neck Pull", "32", "The Rocking"],
            ["16", "The Scissors", "33", "The Control Balance"],
            ["17", "The Bicycle", "34", "The Push Up"],
        ], widths=[0.4, 2.85, 0.4, 2.85], small=True,
            caption="Nombres en inglés como aparecen en el libro de 1945; las traducciones y algunas agrupaciones varían entre ediciones y escuelas."),
        H("Características del enfoque clásico", 4),
        UL("Respeto por el **orden** y el repertorio original.", "Énfasis en el **powerhouse** y en el ritmo/fluidez.",
           "Uso frecuente de una leve retroversión o espalda baja «hacia el mat» en el trabajo abdominal.", "Transiciones como parte del ejercicio."),
    ),
    topic("Evolución de Pilates",
        T("Después de la muerte de Joseph Pilates, el método se diversificó. Hoy conviven el **enfoque clásico** y diversos "
          "**enfoques contemporáneos**, que incorporan conocimientos de biomecánica y rehabilitación."),
        TBL(["Enfoque", "Rasgos", "Ejemplos de escuelas"], [
            ["Clásico", "Repertorio y orden originales", "Linajes de Romana Kryzanowska y otros elders"],
            ["Contemporáneo", "Columna neutra, modificaciones, evidencia científica", "STOTT PILATES, BASI, Polestar, Balanced Body"],
            ["Clínico / rehabilitación", "Uso terapéutico por fisioterapeutas", "Diversos programas clínicos"],
            ["Fusión / fitness", "Combinación con otras disciplinas y props", "Barre, Pilates con pesas, Block Burn Pilates"],
        ], widths=[1.5, 2.5, 2.5]),
        TBL(["Aspecto", "Clásico", "Contemporáneo"], [
            ["Pelvis en abdominales", "Espalda baja hacia el mat", "Neutra o imprint según el caso"],
            ["Orden", "Fijo", "Flexible según objetivo"], ["Modificaciones", "Limitadas", "Amplias"], ["Props", "Aparatos originales", "Gran variedad"],
        ], widths=[1.8, 2.35, 2.35]),
        BOX("general", "Lugar de Block Burn Pilates", "Según su definición, Block Burn Pilates parte de Pilates clásico y lo fusiona con fuerza y barre: "
            "es, por tanto, un enfoque de fusión con raíz clásica. Los detalles de esa fusión son propios del material oficial."),
    ),
], [
    Q("¿En qué año aproximado abrió Joseph Pilates su estudio en Nueva York?", ["1883", "1926", "1945", "1967"], 1, ""),
    Q("¿Cuántos ejercicios de mat describe Return to Life?", ["10", "20", "34", "50"], 2, ""),
    Q("Los «elders» fueron alumnos directos de Joseph Pilates.", None, "V", ""),
    Q("El enfoque contemporáneo nunca usa columna neutra.", None, "F", ""),
    Q("Explica en tres líneas la diferencia entre Pilates clásico y contemporáneo.", None, "Clásico: orden y repertorio originales. Contemporáneo: neutra, modificaciones y evidencia.", ""),
])

# =====================================================================
# MÓDULO 4
# =====================================================================
lower1 = [
    EX("Sentadilla con talones sobre block", en="Heels-elevated squat", frames=[F(P.squat(0, lift=HL), "Inicio", [blk("HlN", h=HL, w=1.4, ox=0.2)]), F(P.squat(1, lift=HL), "Final", [blk("HlN", h=HL, w=1.4, ox=0.2)])],
       prim=["cuad", "glmax"], sec=["adu", "ta", "gem"],
       obj="Aumentar la profundidad y el énfasis en cuádriceps compensando la movilidad de tobillo.",
       start="Talones sobre el block en posición baja, antepié en el suelo o ambos sobre el block, pies a la anchura de la cadera.",
       steps=["Baja con el tronco más vertical que en la sentadilla normal.", "Rodillas avanzan sobre los dedos.", "Sube empujando todo el pie."],
       breath="Inhala al bajar, exhala al subir.", errors=["Peso solo en la punta.", "Rodillas hacia dentro."], regress=["Rango parcial."], progress=["Pulsos.", "Goblet."],
       dose="3 × 12–16.", cue="«Tronco alto, rodillas largas hacia el frente.»"),
    EX("Sentadilla con block entre muslos", en="Squat with block squeeze", frames=[F(P.squat(0.85), "Squeeze", [blk("KN", center=True, w=0.5, h=0.9, ox=-0.45, oy=0.1)])],
       prim=["cuad", "adu"], sec=["glmax", "ta"],
       obj="Activar aductores y alinear rodillas con un squeeze constante.",
       start="Pies a la anchura de la cadera en paralelo, block en orientación media entre los muslos, sobre las rodillas.",
       steps=["Aprieta el block.", "Baja a sentadilla sin soltarlo.", "Sube manteniendo la presión."],
       breath="Exhala al subir.", errors=["Soltar el block.", "Pies muy separados."], regress=["Sentadilla parcial."], progress=["Pulsos + isométrico.", "Relevé."],
       dose="3 × 15 o 45 s.", cue="«El block es un tesoro: no lo dejes caer.»"),
    EX("Elevación de talones desde el borde del block", en="Deficit calf raise", frames=[F(P.stand(lift=HB, ftN=110, ftF=110), "Talones abajo", [blk("TN", h=HB, w=1.0, ox=-0.25)]), F(P.stand(lift=HB, relev=True), "Relevé", [blk("TN", h=HB, w=1.0, ox=-0.25)])],
       prim=["gem"], sec=["tib", "ta"],
       obj="Mayor rango de pantorrilla gracias al déficit.",
       start="Antepié sobre el borde del block, talones libres, apoyo en pared o barra.",
       steps=["Deja bajar los talones por debajo del borde.", "Sube a relevé alto.", "Controla la bajada."],
       breath="Exhala al subir.", errors=["Rebotar.", "Tobillos vencidos."], regress=["Sin déficit."], progress=["A una pierna."],
       dose="3 × 15–20.", cue="«Sube sobre el dedo gordo, baja en tres.»"),
    EX("Peso muerto a una pierna con manos al block", en="Single-leg hinge to block", level="Intermedio", frames=[F(P.sl_hinge(1), "Manos al block", [blk("HdN", to=True, w=0.8)])],
       prim=["isq", "glmax"], sec=["glmed", "ere", "ta"],
       obj="Bisagra a una pierna con un objetivo físico que guía la profundidad.",
       start="Block en orientación alta delante del pie de apoyo.",
       steps=["Bisagra de cadera llevando las manos al block.", "Pierna libre larga atrás.", "Regresa empujando el suelo."],
       breath="Inhala al bajar.", errors=["Abrir la cadera.", "Espalda redonda."], regress=["Block alto, punta del pie trasero apoyada."], progress=["Block bajo.", "Levantar el block y volver."],
       dose="2–3 × 8–10 por lado.", cue="«Cabeza y talón se alejan.»"),
    EX("Sentadilla sumo sosteniendo el block", en="Sumo squat with block", frames=[F(P.wide(arms=(12, -15)), "Inicio", [blk("HdN", center=True, w=0.9, h=0.5, oy=-0.1)]), F(P.plie2(1, arms=(12, -15)), "Final", [blk("HdN", center=True, w=0.9, h=0.5, oy=-0.1)])],
       prim=["glmax", "adu"], sec=["cuad", "delA", "ta"],
       obj="Sumo con el block como carga ligera y referencia de alineación.",
       start="Segunda posición amplia, block sostenido con brazos largos.",
       steps=["Baja verticalmente.", "Opcional: eleva el block al frente al subir (brazos)."],
       breath="Exhala al subir.", errors=["Inclinar el tronco."], regress=["Sin block."], progress=["Pulsos + elevación de talones."],
       dose="3 × 15.", cue="«Desliza la espalda por la pared.»"),
]

lower2 = [
    EX("Puente con pies sobre blocks", en="Bridge with feet on blocks", frames=[F(bridge_on(HB, False), "Inicio", [blk("AN", h=HB, w=1.2, ox=0.1)]), F(bridge_on(HB, True), "Final", [blk("AN", h=HB, w=1.2, ox=0.1)])],
       prim=["glmax", "isq"], sec=["ere", "ta"],
       obj="Mayor rango de extensión de cadera y más demanda de isquiotibiales.",
       start="Boca arriba, pies sobre dos blocks (o uno ancho), rodillas flexionadas.",
       steps=["Exhala, presiona los talones contra los blocks.", "Eleva la cadera hasta la línea de rodillas.", "Baja articulando."],
       breath="Exhala al subir.", errors=["Arquear la espalda.", "Blocks que se deslizan."], regress=["Blocks en posición baja."], progress=["Marcha.", "Una pierna."],
       dose="3 × 12–15.", cue="«Imprime los talones en el block.»"),
    EX("Puente con block entre muslos", en="Bridge with block squeeze", frames=[F(P.bridge(1), "Puente + squeeze", [blk("KN", center=True, w=0.45, h=0.8, ox=-0.6, oy=-0.15)])],
       prim=["glmax", "adu"], sec=["isq", "ta"],
       obj="Puente con aducción isométrica para un centro más activo.",
       start="Puente con el block entre los muslos.", steps=["Sube y aprieta el block.", "Pulsos arriba.", "Baja articulando."],
       breath="Exhala al apretar.", errors=["Soltar el block al bajar."], regress=["Squeeze sin puente."], progress=["Pies sobre blocks."],
       dose="3 × 15 + 16 pulsos.", cue="«Aprieta el block y alarga las rodillas.»"),
    EX("Marcha en puente sobre blocks", en="Bridge march on blocks", level="Intermedio", frames=[F(bridge_on(HB, True), "Puente", [blk("AN", h=HB, w=1.2, ox=0.1)]), F(bridge_on(HB, True, single=True), "Marcha", [blk("AF", h=HB, w=1.2, ox=0.1)])],
       prim=["glmax"], sec=["isq", "obl", "ta", "glmed"],
       obj="Anti-rotación de pelvis con apoyo elevado.",
       start="Puente con pies sobre blocks.", steps=["Eleva un pie sin que la cadera caiga.", "Alterna."],
       breath="Exhala al elevar.", errors=["Pelvis que se inclina."], regress=["En el suelo."], progress=["Extender la pierna."],
       dose="2–3 × 10 por lado.", cue="«Cadera como una mesa nivelada.»"),
    EX("Puente a una pierna sobre block", en="Single-leg bridge on block", level="Avanzado", frames=[F(bridge_on(HB, True, single=True), "Una pierna", [blk("AF", h=HB, w=1.0, ox=0.1)])],
       prim=["glmax"], sec=["isq", "glmed", "ta"],
       obj="Máxima carga unilateral de glúteo en suelo.",
       start="Un pie sobre el block, otra pierna extendida.", steps=["Sube y baja la cadera.", "Pelvis nivelada."],
       breath="Exhala al subir.", errors=["Rotar la pelvis."], regress=["Puente a una pierna en el suelo."], progress=["Pulsos arriba."],
       dose="2–3 × 8–12.", cue="«Empuja el block con el talón.»"),
]

lower3 = [
    EX("Patada de glúteo con block detrás de la rodilla", en="Donkey kick with block", level="Intermedio",
       frames=[F(P.quadruped(thF=95, shF=182, ftF=268), "Patada", [blk("KF", center=True, w=0.7, h=0.45, ox=0.25, oy=0.15)])],
       prim=["glmax", "isq"], sec=["ta", "ere"],
       obj="Mantener la flexión de rodilla activa sosteniendo el block en el hueco poplíteo.",
       start="Cuadrupedia con un block bajo apretado detrás de una rodilla (entre muslo y pantorrilla).",
       steps=["Empuja la planta hacia el techo sin soltar el block.", "Baja sin tocar el suelo."],
       breath="Exhala al subir.", errors=["Arquear la zona lumbar.", "Soltar el block."], regress=["Sin block."], progress=["Pulsos e isométrico arriba."],
       dose="2 × 15–20 por lado.", cue="«Pellizca el block con la rodilla.»"),
    EX("Abducción en cuadrupedia con mano sobre block", en="Fire hydrant on block", level="Intermedio", frames=[],
       prim=["glmed"], sec=["glmax", "obl", "ta"],
       obj="Mayor exigencia de estabilidad al apoyar una mano en un block.",
       start="Cuadrupedia con una mano sobre un block bajo.", steps=["Eleva la pierna lateralmente.", "Tronco nivelado pese a la mano elevada."],
       breath="Exhala al elevar.", errors=["Inclinar el tronco."], regress=["Ambas manos en el suelo."], progress=["Pierna extendida."],
       dose="2 × 12–15 por lado.", cue="«Tronco de mesa, cadera quieta.»"),
    EX("Side kick arrodillada con mano sobre block", en="Kneeling side kick", level="Intermedio", frames=[],
       prim=["glmed", "obl"], sec=["glmax", "ta", "delM"],
       obj="Versión del Side Kick Kneeling de Pilates con apoyo elevado.",
       start="De rodillas, inclina el tronco hacia un lado apoyando la mano en un block alto; la pierna de fuera se extiende a la altura de la cadera.",
       steps=["Patea la pierna al frente y atrás con control.", "El tronco permanece largo."],
       breath="Inhala al frente, exhala atrás.", errors=["Hundir el hombro de apoyo."], regress=["Elevaciones laterales simples."], progress=["Block en posición media."],
       dose="8–10 por lado.", cue="«Larga del cráneo a la punta del pie.»"),
    EX("Clamshell con block entre tobillos", en="Clamshell with block", frames=[],
       prim=["glmed"], sec=["glmax"],
       obj="Rotación externa de cadera con un punto fijo.",
       start="De lado, rodillas flexionadas, un block bajo entre los tobillos.",
       steps=["Abre la rodilla de arriba sin soltar el block.", "La pelvis no rueda hacia atrás."],
       breath="Exhala al abrir.", errors=["Rotar la pelvis."], regress=["Sin block."], progress=["Banda sobre las rodillas."],
       dose="2 × 15–20 por lado.", cue="«Abre como una almeja, cadera apilada.»"),
    EX("Arabesque con manos sobre blocks", en="Arabesque with hands on blocks", level="Intermedio", frames=[F(P.sl_hinge(0.9, uaN=0, faN=0), "Arabesque apoyado", [blk("HdN", to=True, w=0.8)])],
       prim=["glmax", "isq"], sec=["ere", "glmed", "ta"],
       obj="Elevación de pierna con tronco inclinado y apoyo elevado (influencia barre).",
       start="Bisagra de cadera con manos en dos blocks altos.", steps=["Eleva la pierna atrás alineada con el tronco.", "Pulsos.", "Isométrico."],
       breath="Exhala al elevar.", errors=["Abrir la cadera."], regress=["Pierna más baja."], progress=["Una mano."],
       dose="32 pulsos por lado.", cue="«Pierna larga hacia la pared de atrás.»"),
]

m4 = module(4, "Posiciones de pies sobre blocks · Tren inferior I · II · III", [
    "Colocar los pies sobre los blocks de forma segura.",
    "Ejecutar ejercicios de tren inferior de pie, en puente y en cuadrupedia con blocks.",
], [
    topic("Posiciones de Pies sobre Blocks",
        FIG("d_fob", "Figura. Posiciones básicas de pies con blocks (vista superior)."),
        TBL(["Posición", "Efecto", "Ejercicios típicos"], [
            ["Un pie por block, paralelo", "Base estrecha, más equilibrio y propiocepción", "Sentadilla, relevé"],
            ["Talones elevados", "Más rango de rodilla, tronco vertical", "Sentadilla, plié"],
            ["Antepié sobre el borde", "Déficit de tobillo", "Elevación de talones"],
            ["Escalonado", "Carga asimétrica, una pierna domina", "Split squat, step taps"],
            ["Block entre muslos o tobillos", "Squeeze de aductores", "Sentadilla, puente, hundred"],
        ], widths=[1.8, 2.5, 2.2]),
        BOX("seguridad", "Antes de subir a un block", UL("Mat antideslizante debajo.", "Presiona primero con el pie.", "Ten una pared o barra cerca al principio.",
                                                         "Usa calcetines antideslizantes o pies descalzos según la superficie.")),
    ),
    topic("Tren Inferior Parte I", T("Ejercicios de pie con blocks como elevación, squeeze o carga ligera."), *lower1),
    topic("Tren Inferior Parte II", T("Puentes: los blocks bajo los pies aumentan el rango; entre los muslos añaden aducción."), *lower2),
    topic("Tren Inferior Parte III", T("Cuadrupedia, decúbito lateral y equilibrio: énfasis en glúteo medio y estabilidad."), *lower3),
], [
    Q("Elevar los talones sobre un block en la sentadilla permite…", ["Más rango con tronco más vertical", "Más impacto", "Menos cuádriceps", "Nada"], 0, ""),
    Q("En el puente con pies sobre blocks aumenta la demanda de…", ["Isquiotibiales", "Bíceps", "Deltoides", "Gemelos solamente"], 0, ""),
    Q("El block entre los tobillos en el clamshell sirve como punto fijo.", None, "V", ""),
    Q("Es buena idea subir a un block sin mat cuando el suelo es de madera.", None, "F", ""),
    Q("Elige tres ejercicios (uno de cada parte) y escribe una regresión y una progresión para cada uno.", None, "Respuesta abierta.", ""),
])

MODULES = [m1, m2, m3, m4]
