from common import *
import poses as P
from block_a import HB, HL, blk, plank_on, bridge_on

ROUT_HEAD = ["Bloque", "Tiempo", "Ejercicios", "Dosificación", "Blocks"]
ROUT_W = [1.05, 0.7, 2.1, 1.35, 1.3]
HAND_BLK = [blk("HdN", to=True, w=0.8)]
BLK_HANDS = [blk("HdN", center=True, w=0.5, h=0.85, ox=0, oy=0)]

# =====================================================================
# MÓDULO 5
# =====================================================================
core = [
    EX("Hundred con block entre tobillos", en="Hundred with block", level="Intermedio",
       frames=[F(P.crunch(legs="hover", arms="floor", lift=22, uaN=95, faN=95), "Bombeo", [blk("AN", center=True, w=0.4, h=0.7, ox=-0.1, oy=0.1)])],
       prim=["ra", "ta", "adu"], sec=["obl", "fc"],
       obj="The Hundred clásico con squeeze de aductores para encender el centro.",
       start="Boca arriba, block bajo entre los tobillos o las pantorrillas, piernas en mesa o a 45°.",
       steps=["Eleva cabeza y hombros.", "Aprieta el block.", "Bombea los brazos: 5 inhalaciones, 5 exhalaciones."],
       breath="5/5.", errors=["Soltar el block.", "Cuello tenso."], regress=["Piernas en mesa, block entre rodillas."], progress=["Piernas más bajas."],
       dose="100 bombeos.", cue="«Block vivo, abdomen largo.»"),
    EX("Roll up con block", en="Roll up with block", level="Intermedio",
       frames=[F(P.supine("straight", arms="overhead"), "Inicio", [blk("HdN", center=True, w=0.5, h=0.8)]), F(P.seated(legs="straight", arms="front", lean=40, head=150, uaN=95, faN=95), "Final", [blk("HdN", center=True, w=0.5, h=0.8)])],
       prim=["ra"], sec=["ta", "obl", "fc", "delA"],
       obj="Articular la columna de acostada a sentada con una palanca larga (brazos con block).",
       start="Boca arriba, piernas extendidas, block sostenido con brazos sobre la cabeza.",
       steps=["Lleva los brazos al techo.", "Exhala y enrolla la columna hasta sentarte en C.", "Alarga hacia los pies.", "Regresa vértebra a vértebra."],
       breath="Inhala para preparar, exhala para subir.", errors=["Subir en bloque con impulso.", "Pies que se levantan."], regress=["Roll down parcial con rodillas flexionadas."], progress=["Más lento."],
       dose="6–8.", cue="«Despega una vértebra a la vez.»"),
    EX("Toe taps con block entre rodillas", en="Toe taps with block", frames=[F(P.supine("table"), "Mesa", [blk("KN", center=True, w=0.5, h=0.7)]), F(P.supine("table", thN=145, shN=55, thF=145, shF=55), "Toque doble", [blk("KN", center=True, w=0.5, h=0.7)])],
       prim=["ta", "ra", "adu"], sec=["fc"],
       obj="Control lumbar con squeeze; ambas piernas bajan juntas.",
       start="Piernas en mesa con un block entre las rodillas.", steps=["Baja ambos pies a tocar el suelo.", "Regresa a mesa sin soltar el block."],
       breath="Exhala al bajar.", errors=["Arquear la espalda baja."], regress=["Rango corto."], progress=["Cabeza elevada."],
       dose="2 × 10–12.", cue="«Pelvis quieta, piernas como una sola.»"),
    EX("Giro ruso pasando el block", en="Russian twist block pass", level="Intermedio", frames=[F(P.russian(uaN=60, faN=100), "Giro", [blk("HdN", center=True, w=0.8, h=0.5)])],
       prim=["obl"], sec=["ra", "fc", "ta"],
       obj="Rotación con carga ligera y coordinación.",
       start="Sentada en V con rodillas flexionadas, block en las manos.", steps=["Gira y apoya el block junto a la cadera.", "Pásalo al otro lado por delante."],
       breath="Exhala al girar.", errors=["Espalda redonda colapsada."], regress=["Pies apoyados."], progress=["Pies elevados."],
       dose="2 × 10 por lado.", cue="«Gira el esternón.»"),
    EX("Plancha con manos sobre blocks", en="Plank on blocks", frames=[F(plank_on(HB), "Isométrico", HAND_BLK)],
       prim=["ta", "ra"], sec=["delA", "ser", "pec", "glmax"],
       obj="Plancha alta con apoyo elevado (más fácil) o inestable (más control).",
       start="Manos sobre dos blocks bajo los hombros.", steps=["Línea de cabeza a talones.", "Empuja los blocks hacia el suelo."],
       breath="Continua.", errors=["Cadera hundida."], regress=["Block alto (más inclinación)."], progress=["Pies sobre blocks.", "Shoulder taps."],
       dose="3 × 30–45 s.", cue="«Empuja los blocks lejos.»"),
    EX("Plancha lateral con antebrazo sobre block", en="Side plank on block", level="Intermedio", frames=[F(P.side_plank("forearm", top_arm="up"), "Antebrazo elevado")],
       prim=["obl", "glmed"], sec=["ta", "delM"],
       obj="Plancha lateral con el antebrazo sobre un block (mayor rango de cadera para los descensos).",
       start="Antebrazo sobre un block bajo, piernas apiladas.", steps=["Eleva la cadera.", "Opcional: descensos de cadera por debajo de la línea."],
       breath="Continua.", errors=["Hombro hundido."], regress=["Rodillas apoyadas."], progress=["Elevar la pierna de arriba."],
       dose="20–40 s por lado.", cue="«Crece desde el block hacia el techo.»"),
    EX("Teaser con block", en="Teaser with block", level="Avanzado", frames=[F(P.seated(legs="v", arms="front", lean=-30, head=200, uaN=130, faN=130, uaF=130, faF=130), "V", [blk("HdN", center=True, w=0.5, h=0.8)])],
       prim=["ra", "fc"], sec=["ta", "obl", "adu"],
       obj="Ejercicio clásico de equilibrio sobre el coxis con block en manos o entre tobillos.",
       start="Sentada en V con piernas elevadas y brazos paralelos a las piernas.", steps=["Rueda hacia atrás y vuelve a la V.", "Mantén el block alineado con las piernas."],
       breath="Exhala al subir.", errors=["Hundir el pecho.", "Usar impulso."], regress=["Una pierna apoyada.", "Rodillas flexionadas."], progress=["Brazos y piernas bajan y suben a la vez."],
       dose="4–6.", cue="«Flota sobre los isquiones.»"),
    EX("Hollow con pase de block", en="Hollow block pass", level="Avanzado",
       frames=[F(P.crunch(legs="up", arms="up", lift=22), "Pase", [blk("HdN", center=True, w=0.5, h=0.7)]), F(P.crunch(legs="hover", arms="overhead", lift=22), "Extensión", [blk("AN", center=True, w=0.4, h=0.7)])],
       prim=["ra", "ta"], sec=["obl", "fc", "adu"],
       obj="Coordinación y anti-extensión pasando el block de manos a pies.",
       start="Hollow con el block en las manos.", steps=["Lleva brazos y piernas al techo y pasa el block a los pies.", "Extiende a hollow.", "Regresa y devuelve el block."],
       breath="Exhala al cerrar.", errors=["Espalda baja despegada."], regress=["Rodillas flexionadas."], progress=["Más lento."],
       dose="6–10 pases.", cue="«Abre y cierra como un libro.»"),
]

upper1 = [
    EX("Push up con manos sobre blocks", en="Deficit push up on blocks", level="Intermedio", frames=[F(plank_on(HL), "Arriba", HAND_BLK), F(plank_on(HL, "bottom"), "Abajo (déficit)", HAND_BLK)],
       prim=["pec", "tri"], sec=["delA", "ser", "ta"],
       obj="Aumentar el rango del push up permitiendo que el pecho baje entre los blocks.",
       start="Manos sobre blocks bajos (posición baja), cuerpo en plancha o rodillas.",
       steps=["Baja el pecho por debajo del nivel de las manos si el hombro lo permite.", "Empuja."],
       breath="Exhala al empujar.", errors=["Bajar más de lo que el hombro tolera.", "Codos a 90°."], regress=["En rodillas."], progress=["Pies sobre block."],
       dose="3 × 6–12.", cue="«Pecho entre los blocks, codos en flecha.»"),
    EX("Plancha con pase de block", en="Plank block pass", level="Intermedio", frames=[F(P.plank("high", uaF=-120, faF=-110), "Pase lateral")],
       prim=["ta", "obl"], sec=["delA", "ser"],
       obj="Anti-rotación arrastrando o pasando el block de un lado a otro.",
       start="Plancha alta con un block al lado de una mano.", steps=["Con la mano contraria, arrastra el block por debajo del cuerpo al otro lado.", "Alterna."],
       breath="Exhala al pasar.", errors=["Girar la cadera."], regress=["En rodillas."], progress=["Pies juntos."],
       dose="2 × 10.", cue="«Cadera cuadrada al suelo.»"),
    EX("Fondos de tríceps con manos sobre blocks", en="Triceps dips on blocks", frames=[F(P.reverse_plank(thN=40, shN=-10, thF=40, shF=-10, ftN=90, ftF=90), "Arriba", HAND_BLK)],
       prim=["tri"], sec=["delA", "pec"],
       obj="Más rango de fondos gracias a la elevación.",
       start="Sentada delante de dos blocks, manos sobre ellos detrás de la cadera.", steps=["Eleva la cadera.", "Flexiona los codos hacia atrás.", "Extiende."],
       breath="Exhala al subir.", errors=["Codos abiertos.", "Hombros a las orejas."], regress=["Rango corto."], progress=["Piernas extendidas."],
       dose="3 × 8–12.", cue="«Codos atrás, pecho abierto.»"),
    EX("Shoulder taps con manos en blocks", en="Shoulder taps on blocks", level="Intermedio", frames=[F(plank_on(HB, uaF=-150, faF=-160), "Toque", HAND_BLK)],
       prim=["ta", "obl"], sec=["delA", "pec", "ser"],
       obj="Anti-rotación sobre apoyo inestable.", start="Plancha con manos sobre blocks.", steps=["Toca el hombro contrario.", "Alterna sin balancear."],
       breath="Exhala en cada toque.", errors=["Balanceo."], regress=["En el suelo."], progress=["Pies juntos."],
       dose="2 × 16 toques.", cue="«Hombro sobre el block como un pilar.»"),
    EX("Plancha a pike con manos en blocks", en="Pike on blocks", level="Avanzado", frames=[F(plank_on(HB), "Plancha", HAND_BLK), F(P.pike(), "Pike")],
       prim=["ra", "delA"], sec=["ta", "ser", "tri"],
       obj="Flexión de cadera con apoyo elevado en hombros.", start="Plancha con manos en blocks.", steps=["Eleva la cadera en V.", "Vuelve con control."],
       breath="Exhala al subir.", errors=["Hombros colapsados."], regress=["Rodillas flexionadas."], progress=["Pies en deslizadores."],
       dose="2 × 8.", cue="«Empuja los blocks y sube el ombligo.»"),
]

upper2 = [
    EX("Press sobre la cabeza apretando el block", en="Overhead block squeeze press", frames=[F(P.stand("press0"), "Inicio", BLK_HANDS), F(P.stand("press"), "Final", BLK_HANDS)],
       prim=["delA", "delM"], sec=["pec", "tri", "ta"],
       obj="Empuje vertical con isometría de pecho al apretar el block entre las palmas.",
       start="De pie o arrodillada, block entre las palmas a la altura del pecho.", steps=["Aprieta el block.", "Empuja hacia arriba sin arquear la espalda.", "Baja con control."],
       breath="Exhala al subir.", errors=["Costillas abiertas."], regress=["Rango corto."], progress=["Pulsos arriba."],
       dose="2 × 12–16.", cue="«Aprieta, alarga, empuja.»"),
    EX("Squeeze de pecho con block", en="Chest squeeze", frames=[F(P.stand("front"), "Brazos al frente", BLK_HANDS)],
       prim=["pec"], sec=["delA", "ser"],
       obj="Isométrico de aducción horizontal.", start="Block entre las palmas con brazos al frente.", steps=["Aprieta 2 s y suelta sin dejarlo caer.", "Añade pulsos arriba-abajo."],
       breath="Exhala al apretar.", errors=["Hombros arriba."], regress=["Codos flexionados."], progress=["Brazos extendidos más tiempo."],
       dose="30–45 s.", cue="«Aplasta el block.»"),
    EX("Swimming sosteniendo el block", en="Swimming with block", level="Intermedio", frames=[F(P.prone(trunk=-97, head=-102, thN=85, shN=85, thF=95, shF=95), "Extensión", [blk("HdN", center=True, w=0.5, h=0.6)])],
       prim=["ere", "glmax"], sec=["delP", "trap", "isq"],
       obj="Extensión de columna y cadera (Swimming clásico) con un objetivo en las manos.",
       start="Boca abajo, brazos al frente con el block.", steps=["Eleva block, pecho y piernas.", "Aletea las piernas en un rango corto.", "Respira 5 tiempos cada fase."],
       breath="Inhala 5, exhala 5.", errors=["Cuello en extensión.", "Zona lumbar comprimida."], regress=["Solo piernas o solo brazos."], progress=["Más tiempo."],
       dose="20–30 s.", cue="«Alarga antes de elevar.»"),
    EX("Swan con manos sobre blocks", en="Swan on blocks", frames=[F(P.swan(1), "Swan", [blk("HdN", to=True, w=0.8)])],
       prim=["ere"], sec=["glmax", "trap", "rom", "tri"],
       obj="Extensión torácica asistida con apoyo elevado.", start="Boca abajo, manos sobre blocks bajos a la altura del pecho.", steps=["Presiona los blocks y eleva el pecho.", "Mantén el cuello largo.", "Baja con control."],
       breath="Inhala al elevar.", errors=["Extender solo la zona lumbar."], regress=["Sin blocks."], progress=["Swan dive."],
       dose="6–8.", cue="«Corona hacia delante y arriba.»"),
    EX("Plancha invertida con manos sobre blocks", en="Reverse plank on blocks", level="Intermedio", frames=[F(P.reverse_plank(hb=HB), "Isométrico", HAND_BLK)],
       prim=["glmax", "delP", "isq"], sec=["tri", "ere"],
       obj="Cadena posterior y apertura de pecho (Leg-Pull clásico).", start="Sentada, manos sobre blocks detrás de la cadera.", steps=["Eleva la cadera en línea.", "Opcional: eleva una pierna."],
       breath="Continua.", errors=["Cadera caída."], regress=["Mesa invertida."], progress=["Leg-pull (patada)."],
       dose="20–30 s.", cue="«Pecho al techo.»"),
]

cardio = [
    EX("Saltos laterales sobre el block", en="Lateral block hops", level="Avanzado", frames=[F(P.jack(0.15, lift=0.7), "Salto", [{"k": "block", "xy": (0, 0), "w": 1.6, "h": 0.5}])],
       prim=["gem", "cuad"], sec=["glmed", "glmax", "ta"],
       obj="Potencia lateral usando el block (en posición baja) como obstáculo.",
       start="Block bajo a un lado.", steps=["Salta lateralmente por encima del block.", "Aterriza suave y vuelve."],
       breath="Natural.", errors=["Aterrizar rígida.", "Block en orientación alta (riesgo)."], regress=["Paso lateral por encima (bajo impacto)."], progress=["Más ritmo."],
       dose="20–30 s.", cue="«Pies ligeros por encima del block.»"),
    EX("Step taps sobre el block", en="Block step taps", frames=[F(P.stand(thN=50, shN=-10, ftN=90, thF=0, shF=0, ftF=90, uaN=-30, faN=30, uaF=40, faF=120), "Toque", [blk("TN", h=0.75, w=1.2, ox=0.2)])],
       prim=["fc", "cuad"], sec=["gem", "ta"],
       obj="Cardio de bajo impacto alternando toques del pie en el block.",
       start="Frente a un block en posición media.", steps=["Toca el block con la punta de un pie.", "Alterna rápido con brazos de corredora."],
       breath="Natural.", errors=["Mirar hacia abajo todo el tiempo."], regress=["Más lento."], progress=["Ritmo doble.", "Saltito al cambiar."],
       dose="30–45 s.", cue="«Toques ligeros, como un tambor.»"),
    EX("Skater alrededor del block", en="Block skater", level="Intermedio", frames=[F(P.side_lunge(arms=(40, 120)), "Aterrizaje")],
       prim=["glmed", "glmax"], sec=["cuad", "adu"],
       obj="Skater con el block como referencia de distancia o para tocar.", start="Block en el centro.", steps=["Salta (o da un paso) de lado a lado tocando el block con la mano contraria."],
       breath="Natural.", errors=["Rodilla hacia dentro."], regress=["Paso lateral."], progress=["Más distancia."],
       dose="30 s.", cue="«Aterriza en una pierna, toca el block.»"),
    EX("Sentadilla con salto tocando el block", en="Squat jump block touch", level="Intermedio", frames=[F(P.squat(1, uaN=20, faN=10), "Toque", [blk("HdN", to=True, w=0.9)]), F(P.stand("up", relev=True, lift=0.6), "Salto")],
       prim=["cuad", "glmax", "gem"], sec=["isq", "ta"],
       obj="Profundidad constante gracias al block como objetivo.", start="Block alto delante de los pies.", steps=["Baja y toca el block.", "Salta (o sube a puntas)."],
       breath="Exhala al subir.", errors=["Redondear la espalda para tocar."], regress=["Sin salto."], progress=["Block más bajo."],
       dose="30 s.", cue="«Toca, explota, aterriza suave.»"),
]

stretch_general = GALLERY("g_stretch_bbp", "Figura. Estiramientos generales al final de la clase.", [
    (P.stand(thF=0, shF=-170, ftF=-100, uaF=-20, faF=-60), "Cuádriceps"), (P.seated(arms="front", lean=55, uaN=100, faN=100), "Isquiotibiales"),
    (P.pose(thN=85, shN=0, thF=-40, shF=-90, ftF=-90, uaN=175, faN=178), "Flexor de cadera"), (P.child(), "Niño"),
], per_row=4)

stretch_blocks = GALLERY("g_stretch_blocks", "Figura. Estiramientos con blocks.", [
    (P.bridge(0.45), "Puente restaurativo\n(block bajo el sacro)", [blk("H", h=0.5, w=0.9, ox=0.2)]),
    (P.supine("bent", arms="overhead"), "Apertura de pecho\n(block bajo escápulas)", [blk("S", h=0.45, w=0.9, ox=0.4)]),
    (P.pose(thN=85, shN=0, thF=-40, shF=-90, ftF=-90, trunk=150, uaN=0, faN=0), "Zancada baja con\nmanos en blocks", [blk("HdN", to=True, w=0.8)]),
    (P.seated(arms="front", lean=50, uaN=100, faN=100), "Flexión sentada\nsobre block", [blk("H", h=0.5, w=1.0, ox=-0.2)]),
], per_row=4)

m5 = module(5, "Core · Tren superior I · Tren superior II", [
    "Aplicar los blocks al trabajo de centro inspirado en Pilates clásico.",
    "Ejecutar empujes, planchas y extensiones con blocks.",
], [
    topic("Core", T("El block cumple aquí tres funciones: **squeeze** (aductores y suelo pélvico), **palanca** (sostenido con brazos o piernas) "
                    "y **apoyo inestable** (manos o antebrazos)."), *core),
    topic("Tren Superior Parte I", T("Empujes y planchas con blocks bajo las manos: más rango (déficit), más control y anti-rotación."), *upper1),
    topic("Tren Superior Parte II", T("Empujes verticales, isometría de pecho y extensiones de columna (Swimming, Swan, Leg-Pull) con blocks."), *upper2),
], [
    Q("¿Qué función cumple el block entre los tobillos en el Hundred?", ["Peso extra", "Squeeze de aductores", "Apoyo de manos", "Ninguna"], 1, ""),
    Q("El push up con manos sobre blocks permite…", ["Más rango (déficit)", "Menos trabajo", "Más impacto", "Trabajar piernas"], 0, ""),
    Q("En el swan conviene extender solo la zona lumbar.", None, "F", "Se busca extensión torácica con cuello largo."),
    Q("El Teaser es un ejercicio del repertorio clásico de mat.", None, "V", ""),
    Q("Diseña una mini secuencia de core de 4 ejercicios con blocks indicando la función del block en cada uno.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 6
# =====================================================================
m6 = module(6, "Cardio moves · Stretch · Stretch con blocks", [
    "Incorporar intervalos de cardio con blocks de forma segura.",
    "Guiar estiramientos generales y con blocks.",
], [
    topic("Cardio Moves", BOX("seguridad", "Regla de oro", "En cardio, el block es un objetivo o una referencia en el suelo; **nunca una plataforma para saltar encima**."), *cardio),
    topic("Stretch",
        T("El estiramiento final reduce la intensidad, mejora la sensación de movilidad y cierra la clase. Mantén cada posición "
          "20–30 s (hasta 60 s para objetivos de flexibilidad) con respiración lenta."),
        stretch_general,
        TBL(["Estiramiento", "Zona", "Cue"], [
            ["Cuádriceps de pie", "Muslo anterior", "«Rodillas juntas, cóccix largo»"], ["Isquiotibiales sentada", "Muslo posterior", "«Inclina desde la cadera»"],
            ["Zancada baja", "Flexores de cadera", "«Aprieta el glúteo de atrás»"], ["Niño", "Espalda y dorsal", "«Respira hacia la espalda»"],
        ], widths=[1.9, 1.7, 2.9])),
    topic("Stretch con Blocks",
        T("El block **acerca el suelo** y da soporte, permitiendo relajarse en el estiramiento en lugar de luchar contra la falta de flexibilidad."),
        stretch_blocks,
        TBL(["Estiramiento", "Uso del block", "Indicación"], [
            ["Puente restaurativo", "Block bajo el sacro (posición baja o media)", "«Deja que la pelvis descanse»"],
            ["Apertura de pecho", "Block bajo las escápulas, otro bajo la cabeza", "«Brazos en cactus, respira»"],
            ["Zancada baja", "Manos sobre blocks altos", "«Pecho alto gracias a los blocks»"],
            ["Flexión sentada", "Sentada sobre un block para inclinar la pelvis", "«Pelvis rueda adelante sobre el block»"],
            ["Paloma", "Block bajo la cadera de la pierna flexionada", "«Cadera nivelada sobre el block»"],
        ], widths=[1.7, 2.4, 2.4])),
], [
    Q("En cardio, el block puede usarse como plataforma de salto.", None, "F", ""),
    Q("En el estiramiento sentado, sentarse sobre un block ayuda a…", ["Redondear más la espalda", "Inclinar la pelvis hacia delante", "Aumentar el impacto", "Nada"], 1, ""),
    Q("¿Cuánto tiempo se recomienda mantener un estiramiento en el cierre de clase?", ["2–5 s", "20–30 s", "5 min", "No se mantiene"], 1, ""),
    Q("Describe dos estiramientos con blocks y la función del block en cada uno.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 7
# =====================================================================
m7 = module(7, "Transición coreográfica intro · Tren inferior · Tren superior", [
    "Planear transiciones considerando la logística de los blocks.",
    "Encadenar secuencias fluidas de tren inferior y superior.",
], [
    topic("Transición Coreográfica Intro",
        T("En Block Burn Pilates las transiciones tienen un reto extra: **mover los blocks**. Una buena coreografía planea dónde "
          "está cada block en cada momento."),
        TBL(["Principio", "Aplicación"], [
            ["Colocación previa", "Ambos blocks junto al mat antes de empezar el bloque"],
            ["Mínimos movimientos del block", "Encadenar ejercicios que usan el block en la misma posición"],
            ["Agrupar por nivel", "De pie → suelo; evitar subir y bajar"],
            ["Cambio de orientación en la transición", "Girar el block de bajo a medio durante una elongación"],
            ["Musicalidad", "Cambiar al inicio de una frase de 8; anticipar en 5-6-7-8"],
        ], widths=[2.4, 4.1]),
        FIG("d_eight", "Figura. Frase de 32 tiempos para anticipar transiciones."),
    ),
    topic("Tran. Coreográfica Tren Inferior",
        TBL(["#", "Ejercicio", "Cuentas", "Transición / block"], [
            ["1", "Sentadilla con block entre muslos", "4×8", "Mantener el block"],
            ["2", "Pulsos + isométrico", "2×8 + 8", "Soltar block al suelo delante"],
            ["3", "Peso muerto a una pierna con manos al block (der.)", "4×8", "Mismo block"],
            ["4", "Arabesque con manos en block (der.)", "2×8 pulsos", "Cambiar de pierna"],
            ["5", "Repetir 3–4 lado izquierdo", "6×8", "Bajar al suelo con el block"],
            ["6", "Puente con block entre muslos", "4×8", "Block bajo los pies"],
            ["7", "Puente con pies sobre blocks + marcha", "4×8", "Elongación: figura 4"],
        ], widths=[0.4, 3.0, 0.9, 2.2]),
        GALLERY("g_trans_bbp_lower", "Figura. Flujo de pie a suelo con un solo block.", [
            (P.squat(0.85), "Sentadilla + squeeze", [blk("KN", center=True, w=0.5, h=0.9, ox=-0.45, oy=0.1)]),
            (P.sl_hinge(1), "Bisagra al block", [blk("HdN", to=True, w=0.8)]),
            (P.bridge(1), "Puente + squeeze", [blk("KN", center=True, w=0.45, h=0.8, ox=-0.6, oy=-0.15)]),
            (bridge_on(HB, True), "Pies sobre block", [blk("AN", h=HB, w=1.2, ox=0.1)]),
        ], per_row=4),
    ),
    topic("Tran. Coreográfica Tren Superior",
        TBL(["#", "Ejercicio", "Cuentas", "Transición / block"], [
            ["1", "Press sobre la cabeza apretando el block (de rodillas)", "4×8", "Bajar el block a squeeze de pecho"],
            ["2", "Squeeze de pecho + pulsos", "2×8", "Colocar blocks bajo las manos"],
            ["3", "Plancha sobre blocks", "4×8 tiempos", "Bajar a push up"],
            ["4", "Push up con déficit", "2×8", "Shoulder taps"],
            ["5", "Shoulder taps sobre blocks", "2×8", "Rotar a boca abajo"],
            ["6", "Swan con manos en blocks → Swimming", "4×8", "Niño con manos en blocks"],
        ], widths=[0.4, 3.0, 0.9, 2.2]),
        OFICIAL("Transiciones coreográficas de Block Burn Pilates", "Coreografías oficiales.", "Logística oficial de blocks y cuentas."),
    ),
], [
    Q("¿Qué reto adicional tienen las transiciones en Block Burn Pilates?", None, "Planear la posición y el movimiento de los blocks.", ""),
    Q("Conviene encadenar ejercicios que usan el block en la misma posición.", None, "V", ""),
    Q("Crea una transición de 4 ejercicios de tren superior que mueva el block solo una vez.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 8
# =====================================================================
m8 = module(8, "Estructura de rutina teoría · Estructura de rutina práctica", [
    "Estructurar una clase de Block Burn Pilates integrando Pilates, sculpt y barre.",
    "Escribir una clase completa con logística de blocks.",
], [
    topic("Estructura de Rutina Teoría",
        FIG("d_curve_bbp", "Figura. Curva de intensidad de una clase de 50 minutos (ejemplo didáctico)."),
        TBL(["Fase", "Minutos (50)", "Contenido", "Influencia"], [
            ["Centrado y respiración", "3", "Respiración costal, imprint/neutra", "Pilates"],
            ["Calentamiento", "5", "Movilidad, roll down, sentadillas suaves", "Pilates / sculpt"],
            ["Tren inferior de pie", "10", "Sentadillas, bisagras, arabesque con blocks", "Sculpt / barre"],
            ["Cardio", "4", "Step taps, skaters, sentadilla con toque", "Sculpt"],
            ["Tren inferior en suelo", "8", "Puentes con blocks", "Pilates / sculpt"],
            ["Core clásico", "8", "Hundred, roll up, teaser con block", "Pilates clásico"],
            ["Tren superior", "7", "Planchas, push ups y swan con blocks", "Sculpt / Pilates"],
            ["Stretch con blocks", "5", "Puente restaurativo, apertura de pecho", "—"],
        ], widths=[1.7, 1.0, 2.6, 1.2], small=True),
        BOX("tip", "Regla de la mezcla", "Dentro de cada bloque, alterna un ejercicio de **control** (Pilates) con uno de **fuerza** (sculpt) y termina con **capas** (barre)."),
        OFICIAL("Estructura de rutina de Block Burn Pilates", "Estructura oficial de clase y tiempos.", "Proporción oficial entre Pilates, sculpt y barre."),
    ),
    topic("Estructura de Rutina Práctica",
        H("Plantilla completada (ejemplo)", 4),
        TBL(ROUT_HEAD, [
            ["Centrado", "0–3", "Respiración, imprint, puente articulado", "6 respiraciones", "—"],
            ["Calentamiento", "3–8", "Roll down de pie, sentadillas, círculos", "Continuo", "—"],
            ["Inferior de pie", "8–18", "Sentadilla con squeeze → bisagra a una pierna → arabesque", "Capas", "1 block"],
            ["Cardio", "18–22", "Step taps / skater al block", "30/15 × 4", "1 block"],
            ["Inferior en suelo", "22–30", "Puente squeeze → puente pies en blocks → marcha", "4×8 c/u", "2 blocks"],
            ["Core", "30–38", "Hundred, toe taps, roll up, teaser", "Clásico", "1 block"],
            ["Superior", "38–45", "Plancha en blocks, push up déficit, swan", "40/20", "2 blocks"],
            ["Stretch", "45–50", "Puente restaurativo, pecho, niño", "45 s c/u", "2 blocks"],
        ], widths=ROUT_W, small=True),
        BOX("practica", "Tu turno", "Usa la plantilla del Apéndice C para escribir tu propia clase de 45 min."),
    ),
], [
    Q("¿Qué disciplina aporta principalmente el bloque de core en la estructura propuesta?", ["Pilates clásico", "Barre", "Cardio", "Yoga"], 0, ""),
    Q("La «regla de la mezcla» alterna control, fuerza y capas.", None, "V", ""),
    Q("Escribe una clase de 30 min de Block Burn Pilates con la logística de blocks.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 9
# =====================================================================
m9 = module(9, "Práctica rutina tren inferior · Práctica rutina tren superior", [
    "Dirigir clases completas de práctica de Block Burn Pilates.",
], [
    topic("Práctica Rutina Tren Inferior",
        BOX("general", "Propuesta didáctica", "Rutina de práctica creada con fundamentos generales; no es una coreografía oficial."),
        H("Clase de 45 min · Énfasis tren inferior", 4),
        TBL(ROUT_HEAD, [
            ["Centrado", "0–3", "Respiración + puente articulado", "6 reps", "—"],
            ["Calentamiento", "3–7", "Sentadilla a puntas, bisagra sin peso, círculos de cadera", "Continuo", "—"],
            ["Bloque 1", "7–15", "Sentadilla talones elevados → con squeeze → pulsos → isométrico", "Capas", "1–2"],
            ["Bloque 2", "15–23", "Peso muerto a una pierna al block → arabesque → elevación de talones en déficit", "4×8 por lado", "1"],
            ["Cardio", "23–26", "Step taps + sentadilla con toque", "30/15 × 3", "1"],
            ["Bloque 3", "26–35", "Puente squeeze → pies en blocks → marcha → una pierna", "4×8", "2"],
            ["Core", "35–40", "Hundred con block, toe taps", "", "1"],
            ["Stretch", "40–45", "Restaurativo, paloma con block, isquios", "45 s", "2"],
        ], widths=ROUT_W, small=True),
    ),
    topic("Práctica Rutina Tren Superior",
        H("Clase de 45 min · Énfasis tren superior y core", 4),
        TBL(ROUT_HEAD, [
            ["Centrado", "0–3", "Respiración, imprint, preparación de hundred", "", "—"],
            ["Calentamiento", "3–7", "Círculos de brazos, cat-cow, push up en rodillas", "Continuo", "—"],
            ["Bloque 1", "7–14", "Press apretando block → squeeze de pecho → pulsos", "Capas", "1"],
            ["Bloque 2", "14–22", "Plancha en blocks → push up déficit → shoulder taps", "40/20 × 2", "2"],
            ["Cardio", "22–25", "Skater al block + step taps", "30/15 × 3", "1"],
            ["Bloque 3", "25–32", "Swan en blocks → swimming con block → plancha invertida en blocks", "4×8 / 30 s", "2"],
            ["Core", "32–40", "Roll up con block, giro ruso, teaser, hollow pass", "6–8 c/u", "1"],
            ["Stretch", "40–45", "Apertura de pecho, niño con manos en blocks", "45 s", "2"],
        ], widths=ROUT_W, small=True),
        BOX("practica", "Autoevaluación final", UL("¿Los blocks se movieron un máximo de 3–4 veces por bloque?", "¿Ofreciste versión sin block cuando la técnica se perdió?",
                                                    "¿Incluiste ejercicios del repertorio clásico?", "¿Hubo capas de barre y estructura de sculpt?")),
        OFICIAL("Prácticas de Block Burn Pilates", "Rutinas oficiales de práctica y evaluación.", "Criterios de certificación."),
    ),
], [
    Q("¿Cuántas veces conviene mover los blocks por bloque como máximo, según la autoevaluación?", ["Ilimitadas", "3–4", "10", "Ninguna"], 1, ""),
    Q("Las rutinas de este módulo son coreografías oficiales.", None, "F", ""),
    Q("Evaluación integradora: dirige y graba una clase completa de 45 min de Block Burn Pilates y evalúala con la rúbrica del Apéndice D.", None, "Práctica.", ""),
])

MODULES = [m5, m6, m7, m8, m9]
