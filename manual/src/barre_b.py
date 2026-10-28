from common import *
import poses as P
from barre_a import BAR, HOLD, plie1, at_barre

ROUT_HEAD = ["Bloque", "Tiempo", "Secuencia", "Cuentas / dosificación", "Notas"]
ROUT_W = [1.05, 0.7, 2.0, 1.4, 1.35]


def ball_at(key, off=(0, 0), r=0.42):
    return [{"k": "ball", "at": key, "off": off, "r": r}]


# poses de abdominales Pilates (cabeza a la izquierda)
def hundred(**kw):
    return P.crunch(legs="table", arms="floor", lift=22, uaN=95, faN=95, **kw)


def single_leg(**kw):
    p = dict(thN=200, shN=110, ftN=120, thF=112, shF=112, ftF=200, uaN=150, faN=110)
    p.update(kw)
    return P.crunch(legs="table", arms="floor", lift=25, **p)


# =====================================================================
# MÓDULO 5
# =====================================================================
cardio = [
    EX("Plié jacks", en="Plié jacks", level="Intermedio", frames=[F(P.jack(0), "Cerrado"), F(P.plie2(0.8, arms=(160, -140)), "Plié en 2.ª")],
       prim=["cuad", "adu", "glmax"], sec=["gem", "delM"],
       obj="Cardio con forma de ballet: del paralelo a plié en segunda.",
       start="Pies juntos, brazos en preparatoria.",
       steps=["**Alto impacto:** salta abriendo a plié en segunda con brazos en quinta; salta para cerrar.",
              "**Bajo impacto:** paso lateral a plié en segunda y regreso.", "Aterriza en plié, nunca con rodillas bloqueadas."],
       breath="Natural.", errors=["Rodillas hacia dentro al aterrizar."], regress=["Paso lateral."], progress=["Pausa en plié."],
       dose="20–40 s.", cue="«Aterriza suave en tu segunda.»"),
    EX("Sauté en primera", en="Sauté in first", level="Intermedio", frames=[F(plie1(0.8), "Plié"), F(P.front(arms=(14, -30), legs=(6, 0), foot=115, ftN=30, lift=0.6), "Salto")],
       prim=["gem", "cuad"], sec=["adu", "glmax"],
       obj="Saltos pequeños con turnout para cardio y potencia de pantorrilla.",
       start="Primera posición en demi-plié.",
       steps=["Salta estirando piernas y empeines.", "Aterriza en demi-plié pasando por la media punta.", "Ritmo constante."],
       breath="Natural.", errors=["Aterrizar en talones.", "Perder turnout."], regress=["Relevé-plié sin salto."], progress=["Changement."],
       dose="16–32.", cue="«Rebota como una pelota pequeña.»"),
    EX("Changement", en="Changement", level="Avanzado", frames=[F(P.front(arms=(14, -30), legs=(6, 0), foot=115, ftN=30, lift=0.7), "Cambio en el aire")],
       prim=["gem", "cuad"], sec=["adu", "glmax", "ta"],
       obj="Salto con cambio de pie (de tercera/quinta a tercera/quinta).",
       start="Tercera posición en plié.", steps=["Salta, cambia el pie de delante en el aire.", "Aterriza en plié."],
       breath="Natural.", errors=["Rodillas que giran al aterrizar."], regress=["Sauté.", "Cambio de pies sin salto."], progress=["Más altura."],
       dose="8–16.", cue="«Cambia rápido, aterriza lento.»"),
    EX("Marcha en relevé", en="Relevé march", frames=[F(P.stand(relev=True, thN=60, shN=-20, ftN=20, thF=0, shF=0, ftF=25, uaN=78, faN=95), "Rodilla arriba en relevé")],
       prim=["gem", "fc"], sec=["cuad", "ta"],
       obj="Cardio de bajo impacto con resistencia de pantorrillas.",
       start="Relevé en paralelo.", steps=["Marcha manteniendo talones altos.", "Añade brazos en primera/segunda."],
       breath="Natural.", errors=["Bajar talones.", "Tronco hacia atrás."], regress=["Talones abajo."], progress=["Ritmo doble."],
       dose="30–45 s.", cue="«Camina sobre tacones invisibles.»"),
    EX("Tap back con brazos", en="Tap back", frames=[F(P.stand(arms="down"), "Paralela"), F(P.lunge(0.2, arms="up", trunk=176), "Tap atrás + brazos arriba")],
       prim=["glmax", "delA"], sec=["cuad", "gem"],
       obj="Cardio suave para calentamiento y transiciones.",
       start="De pie.", steps=["Lleva un pie atrás tocando con la punta mientras elevas los brazos.", "Regresa y alterna, al ritmo de la música."],
       breath="Natural.", errors=["Arquear la espalda al subir brazos."], regress=["Brazos más bajos."], progress=["Añadir plié en el lado de apoyo."],
       dose="30–60 s.", cue="«Pie atrás, corazón arriba.»"),
]

miniball = [
    EX("Puente con squeeze de mini ball", en="Bridge with ball squeeze", frames=[F(P.bridge(1), "Puente + squeeze", ball_at("KN", (0.15, -0.05), 0.35))],
       prim=["glmax", "adu"], sec=["isq", "ta"],
       obj="Combinar glúteo y aductores; la ball ayuda a mantener rodillas alineadas.",
       start="Puente con la mini ball entre las rodillas.",
       steps=["Sube a puente.", "Aprieta la pelota en pulsos sin perder la altura.", "Alterna con pequeñas elevaciones de cadera."],
       breath="Exhala al apretar.", errors=["Arquear la zona lumbar."], regress=["Squeeze sin puente."], progress=["Puente a una pierna con ball entre muslo y pantorrilla."],
       dose="32 squeezes + 16 elevaciones.", cue="«Aprieta como si exprimieras una naranja.»"),
    EX("Chair con mini ball entre muslos", en="Chair with ball", level="Intermedio", frames=[F(P.squat(0.5, relev=True, uaN=70, faN=95, uaF=70, faF=95, trunk=176), "Relevé + ball", BAR + ball_at("KN", (-0.55, 0.15), 0.35))],
       prim=["cuad", "adu"], sec=["gem", "ta"],
       obj="Intensificar el thigh work con aducción.",
       start="Relevé en paralelo con la pelota entre los muslos, sobre las rodillas.",
       steps=["Baja en plié con talones altos.", "Aprieta la pelota en cada pulso.", "Isométrico final."],
       breath="Continua.", errors=["Soltar la pelota.", "Talones abajo."], regress=["Talones abajo."], progress=["Sin manos."],
       dose="45–60 s.", cue="«No dejes caer la pelota.»"),
    EX("C-curve con mini ball en la espalda", en="C-curve with ball", frames=[F(P.seated(legs="bent", arms="front", lean=-35, head=200), "C-curve", ball_at("H", (-0.7, 0.9), 0.5))],
       prim=["ra"], sec=["obl", "ta", "fc"],
       obj="Abdominales en flexión con el apoyo de la pelota detrás de la zona lumbar.",
       start="Sentada, rodillas flexionadas, pelota detrás de la zona lumbar.",
       steps=["Redondea la espalda en C apoyándote en la pelota.", "Brazos al frente.", "Pulsos atrás o giros."],
       breath="Exhala profundamente en cada pulso.", errors=["Colapsar sobre la pelota.", "Tensión de cuello."], regress=["Más vertical."], progress=["Pies elevados.", "Giro con brazos."],
       dose="30–60 s.", cue="«Ombligo hacia la pelota.»"),
    EX("Squeeze de aductores sentada", en="Seated inner-thigh squeeze", frames=[F(P.seated(legs="bent", arms="back", uaN=-30, faN=-30), "Ball entre rodillas", ball_at("KN", (-0.1, 0.0), 0.35))],
       prim=["adu"], sec=["ta", "ra"],
       obj="Aductores con pelota; útil como transición.",
       start="Sentada con manos atrás, rodillas flexionadas, pelota entre las rodillas.",
       steps=["Aprieta y suelta en pulsos.", "Sostén 10 s.", "Opcional: inclina el tronco hacia atrás para sumar core."],
       breath="Exhala al apretar.", errors=["Hombros hacia las orejas."], regress=["Squeeze lento."], progress=["Pies elevados (V-sit)."],
       dose="32 + 10 s.", cue="«Rodillas como un imán.»"),
    EX("Hollow con mini ball entre tobillos", en="Hollow with ball", level="Avanzado", frames=[F(P.crunch(legs="hover", arms="overhead", lift=22), "Hollow", ball_at("AN", (-0.1, 0.2), 0.32))],
       prim=["ra", "ta", "adu"], sec=["obl", "fc"],
       obj="Anti-extensión con aducción para todo el centro.",
       start="Boca arriba con la pelota entre los tobillos.",
       steps=["Eleva cabeza, hombros y piernas.", "Aprieta la pelota.", "Sostén o pasa la pelota de pies a manos."],
       breath="Continua.", errors=["Zona lumbar despegada."], regress=["Rodillas flexionadas."], progress=["Pase de pelota manos-pies."],
       dose="20–40 s.", cue="«Espalda baja al suelo, pelota viva.»"),
]

pilates_abs = [
    EX("The Hundred", en="The Hundred", level="Intermedio", frames=[F(hundred(), "Bombeo de brazos")],
       prim=["ra", "ta"], sec=["obl", "fc"],
       obj="Ejercicio clásico de Pilates: calentar y conectar respiración con centro.",
       start="Boca arriba, piernas en mesa (o extendidas a 45° si se domina), cabeza y hombros elevados, brazos largos a los lados.",
       steps=["Bombea los brazos arriba y abajo con un rango corto.", "Inhala 5 bombeos, exhala 5 bombeos.", "Completa 10 ciclos (100 bombeos)."],
       breath="5 inhalaciones / 5 exhalaciones.", errors=["Tensión en el cuello.", "Zona lumbar arqueada."], regress=["Cabeza apoyada.", "Pies en el suelo."], progress=["Piernas extendidas a 45°."],
       dose="100 bombeos.", cue="«Brazos como si salpicaras agua.»"),
    EX("Single leg stretch", en="Single leg stretch", level="Intermedio", frames=[F(single_leg(), "Cambio de piernas")],
       prim=["ra", "ta"], sec=["obl", "fc"],
       obj="Coordinación y estabilidad lumbar con cambio de piernas.",
       start="Cabeza y hombros elevados, una rodilla al pecho y otra extendida.",
       steps=["Cambia de pierna manteniendo el tronco quieto.", "Mano exterior al tobillo, mano interior a la rodilla.", "Ritmo constante."],
       breath="Inhala 2 cambios, exhala 2 cambios.", errors=["Mecer el tronco.", "Pierna extendida demasiado baja."], regress=["Pierna extendida más alta."], progress=["Más ritmo."],
       dose="8–10 por lado.", cue="«Tronco quieto como una roca.»"),
    EX("Double leg stretch", en="Double leg stretch", level="Intermedio", frames=[F(single_leg(thF=200, shF=110, ftF=120), "Recogido"), F(P.crunch(legs="hover", arms="overhead", lift=25, thN=125, shN=125, ftN=215), "Extensión")],
       prim=["ra", "ta"], sec=["obl", "fc", "delA"],
       obj="Alargar brazos y piernas desde el centro sin perder la curva alta.",
       start="Rodillas al pecho, manos en las espinillas, cabeza elevada.",
       steps=["Inhala y extiende brazos atrás y piernas al frente.", "Exhala y círculo de brazos regresando las rodillas."],
       breath="Inhala al extender, exhala al recoger.", errors=["Cabeza que cae.", "Espalda arqueada."], regress=["Brazos al frente, piernas altas."], progress=["Piernas más bajas."],
       dose="6–10.", cue="«Alarga en estrella, regresa a la bolita.»"),
    EX("Criss-cross", en="Criss-cross", level="Intermedio", frames=[F(P.crunch(legs="table", arms="head", thF=112, shF=112, lift=30), "Codo a rodilla")],
       prim=["obl"], sec=["ra", "ta"],
       obj="Rotación con estabilidad: versión Pilates de la bicicleta.",
       start="Manos detrás de la cabeza, cabeza elevada, piernas en mesa.",
       steps=["Gira hacia una rodilla mientras la otra pierna se extiende.", "Sostén el giro un tiempo.", "Cambia."],
       breath="Exhala en el giro.", errors=["Jalar el cuello."], regress=["Pies en el suelo."], progress=["Pausa de 3 tiempos en cada lado."],
       dose="6–10 por lado.", cue="«Axila hacia la rodilla contraria.»"),
    EX("Single straight leg (tijeras)", en="Single straight leg stretch", level="Intermedio", frames=[F(P.crunch(legs="hover", arms="floor", lift=28, thN=180, shN=180, ftN=270, thF=115, shF=115, uaN=165, faN=175), "Tijeras")],
       prim=["ra", "isq"], sec=["ta", "fc"],
       obj="Fuerza abdominal con flexibilidad de isquiotibiales.",
       start="Cabeza elevada, una pierna al techo sujeta por el tobillo o pantorrilla, otra extendida baja.",
       steps=["Cambia de pierna como tijeras con dos pulsos.", "Tronco quieto."],
       breath="Inhala 2, exhala 2.", errors=["Redondear en exceso.", "Doblar mucho las rodillas."], regress=["Rodillas suaves."], progress=["Sin manos."],
       dose="8–10 por lado.", cue="«Piernas como tijeras, tronco de piedra.»"),
    EX("Roll down con mini ball", en="Roll down with ball", frames=[F(P.seated(legs="bent", arms="front", lean=0), "Sentada"), F(P.seated(legs="bent", arms="front", lean=-40, head=205), "Roll down")],
       prim=["ra"], sec=["ta", "obl", "fc"],
       obj="Articular la columna en flexión con control (preparación del Roll Up).",
       start="Sentada, rodillas flexionadas, pelota entre las manos al frente o detrás de la zona lumbar.",
       steps=["Exhala y rueda hacia atrás vértebra a vértebra.", "Detente antes de perder el control.", "Inhala y vuelve a sentarte."],
       breath="Exhala al bajar.", errors=["Bajar en bloque.", "Pies que se levantan."], regress=["Medio recorrido."], progress=["Roll up completo."],
       dose="6–8.", cue="«Imprime cada vértebra en el mat.»"),
]

m5 = module(5, "Barre cardio moves · Mini ball moves · Pilates abs", [
    "Integrar movimientos de cardio con vocabulario de ballet.",
    "Utilizar la mini ball para intensificar y apoyar ejercicios.",
    "Ejecutar los abdominales clásicos de Pilates usados en barre.",
], [
    topic("Barre cardio moves", T("El cardio en barre suele ser breve (30–90 s) y con forma de ballet. Ofrece siempre versión sin salto."), *cardio),
    topic("Mini ball moves", T("La mini ball cumple tres funciones: **intensificar** (squeeze de aductores), **apoyar** (detrás de la espalda o la "
          "cabeza) y **desestabilizar** (bajo pies o manos)."), *miniball),
    topic("Pilates abs", T("Estos ejercicios provienen del repertorio clásico de Pilates en mat («serie de cinco»: Single leg stretch, Double leg "
          "stretch, Single straight leg, Double straight leg y Criss-cross). En barre se usan para el bloque de centro."), *pilates_abs),
], [
    Q("¿Cuál NO es una función de la mini ball?", ["Intensificar", "Apoyar", "Desestabilizar", "Sustituir la barra"], 3, ""),
    Q("The Hundred se respira…", ["1 inhalación y 1 exhalación por bombeo", "5 inhalaciones y 5 exhalaciones por ciclo", "Sin respirar", "Solo exhalando"], 1, ""),
    Q("El criss-cross es la versión Pilates de la bicicleta.", None, "V", ""),
    Q("La versión de bajo impacto de los plié jacks es un paso lateral a plié en segunda.", None, "V", ""),
    Q("Menciona los cinco ejercicios de la «serie de cinco» de Pilates.", None, "Single leg stretch, double leg stretch, single straight leg, double straight leg, criss-cross.", ""),
])

# =====================================================================
# MÓDULO 6
# =====================================================================
m6 = module(6, "Transición coreografía lower · Transición coreografía upper", [
    "Encadenar ejercicios en coreografías fluidas sin pausas innecesarias.",
    "Planear transiciones según posición, nivel y musicalidad.",
], [
    topic("Transición coreografía lower",
        T("Una transición es el puente entre dos ejercicios. En barre, las buenas transiciones mantienen al músculo trabajando "
          "y a la alumna en movimiento, con indicaciones anticipadas."),
        H("Principios de transición", 4),
        TBL(["Principio", "Explicación", "Ejemplo"], [
            ["Posición puente", "Pasar por una posición común a ambos ejercicios", "Plié en 1.ª → relevé en 1.ª → relevé en paralelo"],
            ["Un cambio a la vez", "Cambiar solo pies, o solo brazos, o solo nivel", "De plié en 2.ª a plié en 2.ª en relevé"],
            ["Mismo lado, mismo grupo", "Terminar todo un lado antes de cambiar", "Fold-over → attitude → arabesque (mismo lado)"],
            ["Niveles agrupados", "De pie → barra → suelo", "Evitar subir y bajar del suelo varias veces"],
            ["Frase musical", "Cambiar al inicio de una frase de 8", "Cue en 5-6-7-8"],
            ["Elongación como transición", "Estirar el grupo trabajado", "Tras chair: estiramiento de cuádriceps en la barra"],
        ], widths=[1.6, 2.4, 2.5]),
        FIG("d_eight", "Figura. Frase musical de 32 tiempos."),
        H("Secuencia de ejemplo · Piernas (≈ 6 minutos)", 4),
        TBL(["#", "Ejercicio", "Cuentas", "Transición al siguiente"], [
            ["1", "Plié en 1.ª (rango completo)", "4 × 8", "Quedarse abajo en plié"],
            ["2", "Pulsos en plié en 1.ª", "2 × 8", "Subir talones sin estirar piernas"],
            ["3", "Plié en 1.ª en relevé + pulsos", "2 × 8", "Isométrico 8 tiempos"],
            ["4", "Estirar piernas, cerrar a paralela en relevé", "1 × 8", "Flexionar rodillas en relevé"],
            ["5", "Thigh en paralelo: pulsos", "4 × 8", "Isométrico + mini ball (opcional)"],
            ["6", "Estiramiento de cuádriceps en la barra", "2 × 8 por lado", "Abrir a segunda"],
            ["7", "Plié en 2.ª + pulsos + isométrico", "4 × 8", "Elongación de aductores"],
        ], widths=[0.4, 2.6, 1.0, 2.5]),
        GALLERY("g_trans_lower", "Figura. Ejemplo de flujo: primera → relevé → paralela en relevé → segunda.", [
            (plie1(1), "Plié en 1.ª"), (P.front(arms=(78, 95), legs=(14, -8), foot=115, ftN=40), "Relevé en 1.ª"),
            (at_barre(ftN=25, ftF=25, thN=25, shN=-12, thF=25, shF=-12), "Paralela en relevé", BAR), (P.plie2(1), "Plié en 2.ª"),
        ], per_row=4),
    ),
    topic("Transición coreografía upper",
        T("En los brazos, las transiciones aprovechan las posiciones de ballet como «estaciones»: preparatoria, primera, "
          "segunda y quinta. Cambiar de una a otra mantiene el deltoides en tensión."),
        H("Secuencia de ejemplo · Brazos (≈ 5 minutos)", 4),
        TBL(["#", "Ejercicio", "Cuentas", "Transición"], [
            ["1", "Brazos en 2.ª: pulsos arriba", "4 × 8", "Girar palmas al techo"],
            ["2", "Bíceps en 2.ª (curl abierto)", "4 × 8", "Quedarse a 90° (goal post)"],
            ["3", "Press a quinta", "2 × 8", "Bajar a 2.ª con palmas atrás"],
            ["4", "Pulsos atrás en 2.ª", "2 × 8", "Llevar brazos a primera"],
            ["5", "Press de pecho en primera", "2 × 8", "Inclinar tronco"],
            ["6", "Tríceps press back", "4 × 8", "Estiramiento de pecho en la barra"],
        ], widths=[0.4, 2.6, 1.0, 2.5]),
        GALLERY("g_trans_upper", "Figura. Estaciones de brazos en la secuencia.", [
            (P.front(arms=(78, 95)), "2.ª pulsos", [{"k": "db"}]), (P.front(arms=(78, 165)), "Curl en 2.ª", [{"k": "db"}]),
            (P.front(arms=(165, 190)), "Quinta", [{"k": "db"}]), (P.front(arms=(50, -80)), "Primera", [{"k": "db"}]),
        ], per_row=4),
        BOX("cue", "Lenguaje de transición", "«En los próximos ocho, sin bajar los brazos, gira las palmas al techo… cinco, seis, siete, ocho: ¡curl!»"),
        OFICIAL("Transiciones coreográficas", "Coreografías y transiciones oficiales del método.", "Cuentas oficiales por bloque."),
    ),
], [
    Q("¿Qué es una «posición puente»?", ["Un puente de glúteo", "Una posición común que conecta dos ejercicios", "Un descanso", "Un estiramiento"], 1, ""),
    Q("Es buena práctica cambiar pies, brazos y nivel al mismo tiempo.", None, "F", "Un cambio a la vez."),
    Q("Conviene terminar todo un lado antes de cambiar al otro.", None, "V", ""),
    Q("Crea una transición de 3 ejercicios para brazos usando las posiciones de ballet como estaciones.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 7
# =====================================================================
m7 = module(7, "Creación de rutina teoría · Práctica tren inferior · Adaptación · Práctica tren superior", [
    "Estructurar una clase de barre completa.",
    "Diseñar bloques de tren inferior y superior.",
    "Adaptar la clase por objetivo, nivel y duración.",
], [
    topic("Creación de rutina teoría",
        FIG("d_curve_barre", "Figura. Curva de intensidad de una clase de barre (ejemplo didáctico)."),
        TBL(["Fase", "Duración (50 min)", "Contenido"], [
            ["Calentamiento", "5–7 min", "Movilidad, tap backs, pliés suaves, port de bras"],
            ["Brazos (de pie)", "6–8 min", "Series con peso ligero, sin pausa"],
            ["Piernas en barra", "15–18 min", "2–3 bloques: muslos, glúteo, aductores"],
            ["Cardio barre", "3–5 min", "Intervalos breves (opcional)"],
            ["Centro (mat)", "8–10 min", "Pilates abs, mini ball"],
            ["Glúteo en suelo (opcional)", "4–5 min", "Puentes, cuadrupedia"],
            ["Elongación y cierre", "4–6 min", "Estiramientos y respiración"],
        ], widths=[1.8, 1.4, 3.3]),
        H("Método de capas para cada ejercicio", 4),
        OL("**Rango completo** (8–16 repeticiones) para aprender.", "**Medio rango o pulsos** (16–32).", "**Isométrico** (8–16 tiempos).",
           "**Combo** (por ejemplo, 2 lentos + 4 pulsos).", "**Elongación** del grupo trabajado."),
        BOX("tip", "Equilibrio en barre", "Por cada bloque de cuádriceps (thigh), incluye glúteo y aductores. En brazos, combina deltoides con espalda alta y tríceps."),
    ),
    topic("Creación de rutina práctica tren inferior",
        H("Bloque de piernas paso a paso (18 min)", 4),
        TBL(ROUT_HEAD, [
            ["Thigh 1", "0–6", "Plié en 1.ª → pulsos → relevé → isométrico", "4×8 / 2×8 / 2×8 / 8 tiempos", "Barra"],
            ["Elongación", "6–7", "Cuádriceps en la barra", "2×8 por lado", ""],
            ["Thigh 2", "7–11", "Thigh en paralelo + mini ball", "4×8 pulsos, isométrico", "Mini ball"],
            ["Seat (glúteo)", "11–17", "Fold-over → attitude → arabesque (der. e izq.)", "4×8 cada uno por lado", "Mismo lado completo"],
            ["Elongación", "17–18", "Figura 4 de pie en la barra", "2×8 por lado", ""],
        ], widths=ROUT_W, small=True),
    ),
    topic("Adaptación de rutinas de acuerdo a objetivos y duración",
        TBL(["Objetivo", "Ajustes"], [
            ["Tonificación / resistencia", "Más pulsos e isométricos; pausas mínimas"],
            ["Fuerza", "Más peso en brazos (2–3 kg) y menos repeticiones; ejercicios a una pierna"],
            ["Cardio / gasto calórico", "Intervalos de cardio barre entre bloques"],
            ["Postura y movilidad", "Más tiempo de alineación, port de bras y elongaciones"],
            ["Principiantes", "Rango completo antes que pulsos; más apoyo en la barra; explicar vocabulario"],
            ["Adultos mayores", "Ambas manos en la barra, sin saltos, relevés cortos, evitar suelo prolongado"],
            ["Embarazo (con autorización)", "Sin tuck marcado, sin boca arriba prolongado (2.º y 3.er trimestre), base amplia"],
        ], widths=[2.0, 4.5]),
        TBL(["Duración", "Calentamiento", "Brazos", "Piernas", "Centro", "Cierre"], [
            ["30 min", "4", "5", "12", "5", "4"], ["45 min", "5", "7", "18", "9", "6"], ["50 min", "6", "8", "20", "10", "6"], ["60 min", "7", "9", "24", "12", "8"],
        ], widths=[1.0, 1.15, 0.9, 1.0, 0.9, 0.9], caption="Minutos aproximados por fase."),
    ),
    topic("Creación de rutina práctica tren superior",
        H("Bloque de brazos paso a paso (8 min)", 4),
        TBL(ROUT_HEAD, [
            ["Deltoides", "0–3", "2.ª pulsos arriba → atrás → círculos", "4×8 / 2×8 / 2×8", "0.5–1 kg"],
            ["Bíceps", "3–5", "Curl en 2.ª → pulsos a 90°", "4×8 / 2×8", "Palmas arriba"],
            ["Hombro", "5–6", "Press a quinta", "2×8", ""],
            ["Tríceps", "6–8", "Press back → extensiones", "4×8 / 2×8", "Tronco inclinado"],
            ["Pecho + estiramiento", "8", "Push up en barra + estiramiento de pecho", "8 + 16 tiempos", "Transición a piernas"],
        ], widths=ROUT_W, small=True),
    ),
], [
    Q("¿Qué fase suele ocupar más tiempo en una clase de barre?", ["Calentamiento", "Piernas en barra", "Cierre", "Cardio"], 1, ""),
    Q("Ordena las capas: isométrico, rango completo, pulsos, elongación.", None, "Rango completo → pulsos → isométrico → (combo) → elongación.", ""),
    Q("Para adultos mayores conviene usar ambas manos en la barra.", None, "V", ""),
    Q("Diseña un bloque de glúteo de 6 minutos con tres ejercicios y su elongación.", None, "Respuesta abierta.", ""),
])

# =====================================================================
# MÓDULO 8
# =====================================================================
m8 = module(8, "Práctica rutina tren inferior · Práctica rutina tren superior", [
    "Dirigir clases completas de barre de práctica.",
    "Evaluar la fluidez de las transiciones.",
], [
    topic("Práctica rutina tren inferior",
        BOX("general", "Propuesta didáctica", "Rutina de práctica creada con los fundamentos del libro; no es una coreografía oficial."),
        H("Clase de 50 min con énfasis en piernas", 4),
        TBL(ROUT_HEAD, [
            ["Calentamiento", "0–6", "Tap backs, port de bras, pliés suaves, rodamiento de columna", "Continuo", "BPM 110–120"],
            ["Brazos", "6–12", "Secuencia de brazos del Módulo 6", "≈ 6 min", "0.5–1 kg"],
            ["Thigh", "12–20", "Plié 1.ª → relevé → paralela relevé → mini ball", "Capas", "Barra"],
            ["Seat", "20–30", "Fold-over → attitude → arabesque × lado", "4×8 cada uno", ""],
            ["Cardio", "30–33", "Plié jacks / paso lateral + marcha en relevé", "30/15 × 4", ""],
            ["Plié en 2.ª", "33–37", "Plié 2.ª → pulsos → relevé en 2.ª → isométrico", "Capas", ""],
            ["Centro", "37–45", "Hundred, single leg, double leg, criss-cross, C-curve con ball", "8–10 c/u", "Mat"],
            ["Cierre", "45–50", "Figura 4, isquios, niño, respiración", "30 s c/u", "BPM 60–80"],
        ], widths=ROUT_W, small=True),
    ),
    topic("Práctica rutina tren superior",
        H("Clase de 45 min con énfasis en brazos y postura", 4),
        TBL(ROUT_HEAD, [
            ["Calentamiento", "0–5", "Port de bras, círculos, rotaciones torácicas", "Continuo", ""],
            ["Brazos 1", "5–13", "2.ª pulsos, curl en 2.ª, press a quinta", "Capas", "0.5–1 kg"],
            ["Piernas", "13–25", "Thigh + seat (versión corta)", "Capas", ""],
            ["Brazos 2", "25–31", "Press back, chest press, push up en barra", "4×8 c/u", ""],
            ["Espalda alta", "31–34", "Pájaros ligeros, Y-T-W de pie", "2×8 c/u", "Postura"],
            ["Centro", "34–41", "Pilates abs + hollow con ball", "", ""],
            ["Cierre", "41–45", "Pecho, tríceps, cuello, respiración", "30 s c/u", ""],
        ], widths=ROUT_W, small=True),
        BOX("practica", "Autoevaluación", UL("¿Hubo pausas mayores a 10 s entre ejercicios?", "¿Cada cambio cayó al inicio de una frase musical?",
                                            "¿Equilibraste thigh, seat y aductores?", "¿Diste elongación tras cada bloque?")),
    ),
], [
    Q("En la clase propuesta de piernas, ¿qué ejercicios forman el bloque «seat»?", None, "Fold-over, attitude y arabesque por lado.", ""),
    Q("Las pausas largas entre ejercicios son parte del estilo de barre.", None, "F", "Barre busca fluidez y tensión continua."),
    Q("Graba tu clase de práctica y responde la autoevaluación.", None, "Práctica.", ""),
])

# =====================================================================
# MÓDULO 9
# =====================================================================
m9 = module(9, "Conclusión Barre · Playlist", [
    "Integrar todo lo aprendido en barre.",
    "Construir una playlist alineada con la estructura de barre.",
], [
    topic("Conclusión Barre",
        T("Barre combina precisión, resistencia y musicalidad. Su esencia está en **la alineación, el trabajo en capas y la "
          "fluidez de las transiciones**."),
        TBL(["Competencia", "Lo domino", "En proceso", "Repasar"], [
            ["Explico pelvis neutra y tuck", "", "", ""], ["Uso el vocabulario de ballet correctamente", "", "", ""],
            ["Enseño 15 ejercicios en barra con capas", "", "", ""], ["Encadeno transiciones sin pausas", "", "", ""],
            ["Diseño una clase de 50 min", "", "", ""], ["Adapto para principiantes y adultos mayores", "", "", ""],
        ], widths=[3.2, 1.1, 1.1, 1.1]),
        OFICIAL("Conclusión Barre y certificación", "Evaluación final oficial.", "Requisitos de práctica y certificación."),
    ),
    topic("Playlist",
        FIG("d_bpm_barre", "Figura. Rangos orientativos de BPM en barre."),
        TBL(["Fase", "BPM", "Carácter"], [
            ["Calentamiento", "105–120", "Fluida, positiva"], ["Brazos", "115–125", "Ritmo marcado"], ["Thigh / seat", "120–130", "Constante para pulsos"],
            ["Cardio barre", "128–140", "Energética"], ["Centro", "110–122", "Estable"], ["Elongación", "60–85", "Calmada"],
        ], widths=[1.8, 1.2, 3.5]),
        BOX("tip", "Pulsos y música", "Los pulsos suelen marcarse a tiempo (1 pulso por tiempo) o a medio tiempo (1 pulso cada 2 tiempos). Elige canciones con "
            "pulso claro y compás de 4/4."),
        OFICIAL("Playlist Barre", "Playlists oficiales.", "Proveedores de música autorizados y licencias."),
    ),
], [
    Q("Menciona las tres claves de barre según la conclusión.", None, "Alineación, trabajo en capas y fluidez de transiciones.", ""),
    Q("¿Qué compás conviene para los pulsos?", ["3/4", "4/4", "6/8", "Libre"], 1, ""),
    Q("Evaluación integradora: diseña una clase de barre de 45 min con secuencias, cuentas, transiciones y BPM por fase.", None, "Respuesta abierta.", ""),
])

MODULES = [m5, m6, m7, m8, m9]
