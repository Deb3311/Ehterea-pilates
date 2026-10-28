"""Genera figuras y build/reformer.json para el manual de Pilates Reformer."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
import engine as E
import build as B
import rf_diagrams as RD
import diagrams as D
from diagrams import TEAL
from appendix import _answer
import reformer_a, reformer_b, reformer_c

B.EX_PREFIX = "rx_"
B.DIAGRAMS.update({
    "d_reformer": RD.reformer_parts, "d_footbar": RD.footbar_positions, "d_stance": RD.pilates_stance,
    "d_springs": RD.springs_chart, "d_chain": RD.chain_diagram,
    "d_curve_reformer": lambda p: D.class_curve(p, [("Footwork", 6, 3, 5, TEAL), ("Hundred", 3, 6, 7, E.NAVY_L), ("Correas", 6, 5, 6, "#7E6B8F"),
                                                    ("Sentada: stomach / short box", 10, 5, 7, E.MAIN), ("Rodillas y de pie", 12, 6, 8, E.GOLD),
                                                    ("Brazos", 6, 5, 6, "#7E6B8F"), ("Running / pelvic lift", 5, 5, 3, TEAL)]),
    "d_cover_reformer": lambda p: E.pose_gallery(p, [
        (__import__("rf_poses").footwork(1), "Footwork", __import__("rf_poses").fw_props()),
        (__import__("rf_poses").elephant(0), "Elephant", __import__("rf_poses").rf(fb="HdN", carr=("TN", "AN"), blocks="AN", blocks_dx=0.4)),
        (__import__("rf_poses").prone_box("back", 15), "Pulling straps", __import__("rf_poses").rf(straps=["HdN"], carr=("S", "H"), box=True)),
    ], per_row=3, cell=(2.6, 2.0)),
})

GLOS = [
    ("Carro (carriage)", "Plataforma deslizante del reformer."), ("Footbar", "Barra de pies; apoyo para pies o manos."),
    ("Hombreras (shoulder blocks)", "Topes acolchados que evitan que el cuerpo se deslice."), ("Gear bar", "Mecanismo que ajusta la posición inicial del carro."),
    ("Long box / short box", "Caja colocada a lo largo / a lo ancho del carro."), ("Correas (straps / loops)", "Asas para manos o pies unidas a las cuerdas."),
    ("Contrología", "Nombre que Joseph Pilates dio a su método."), ("Powerhouse", "Centro de fuerza: abdomen, espalda baja, glúteos, aductores, suelo pélvico."),
    ("Pilates V (Pilates stance)", "Talones juntos, puntas separadas, rotación externa ligera."), ("Imprint", "Leve retroversión que acerca la zona lumbar al carro."),
    ("Columna neutra", "Posición que respeta las curvas naturales."), ("C-curve", "Columna en flexión redondeada."),
    ("Cadena cerrada / abierta", "El extremo empuja una superficie fija / se mueve libre."), ("Elders", "Alumnos directos de Joseph y Clara Pilates."),
    ("Linaje", "Escuela o línea de enseñanza derivada de un elder."), ("Inversión", "Ejercicio con la pelvis por encima de la cabeza (short spine, overhead)."),
    ("Resorte ligero / pesado", "Menor / mayor tensión; no siempre equivale a más fácil / más difícil."),
]

REFS = [
    "Pilates, J. H. y Miller, W. J. (1945). *Return to Life Through Contrology*.",
    "Pilates, J. H. (1934). *Your Health*.",
    "Friedman, P. y Eisen, G. (1980). *The Pilates Method of Physical and Mental Conditioning*.",
    "Gallagher, S. P. y Kryzanowska, R. (1999). *The Pilates Method of Body Conditioning*. BainBridgeBooks.",
    "Isacowitz, R. *Pilates* (2.ª ed.). Human Kinetics.",
    "Isacowitz, R. y Clippinger, K. *Pilates Anatomy*. Human Kinetics.",
    "Siler, B. (2000). *The Pilates Body*. Broadway Books.",
    "Latey, P. (2001). The Pilates method: history and philosophy. *Journal of Bodywork and Movement Therapies*, 5(4), 275–282.",
    "Wells, C., Kolt, G. S. y Bialocerkowski, A. (2012). Defining Pilates exercise: a systematic review. *Complementary Therapies in Medicine*, 20(4), 253–262.",
    "American College of Sports Medicine (ACSM). *ACSM's Guidelines for Exercise Testing and Prescription*.",
    "American College of Obstetricians and Gynecologists (2020). Committee Opinion 804: Physical Activity and Exercise During Pregnancy and the Postpartum Period.",
    "Manual del fabricante de tu reformer (tensiones de resortes, mantenimiento y seguridad).",
]

PARTS = [
    dict(key="fund", title="Fundamentos", box_title="Qué aprenderás en esta parte",
         intro="Historia y filosofía de la Contrología, el reformer y sus resortes, los principios del método y la anatomía aplicada. "
               "Es la base que necesitas antes de enseñar un solo ejercicio.", modules=reformer_a.MODULES),
    dict(key="rep", title="Repertorio clásico", box_title="Qué aprenderás en esta parte",
         intro="El repertorio de reformer de Joseph Pilates organizado por niveles: básico, intermedio y avanzado. Cada ejercicio tiene "
               "ficha técnica con figura sobre el aparato, mapa muscular, resortes y montaje, ejecución, errores, adaptaciones y cue clave.",
         modules=reformer_b.MODULES),
    dict(key="ens", title="Enseñanza", box_title="Qué aprenderás en esta parte",
         intro="Observación, cueing, asistencia táctil, diseño de clases, adaptaciones, contraindicaciones y clases de práctica completas.",
         modules=reformer_c.MODULES),
]

META = {
    "kicker": "MANUAL DE ESTUDIO", "cover_lines": ["Pilates Reformer", "Repertorio clásico"],
    "subtitle": "Guía de estudio para el aprendizaje personal desde cero",
    "tagline": "Historia · el aparato · principios · anatomía · fichas de ejercicios · enseñanza · evaluaciones",
    "cover_image": "d_cover_reformer", "prepared": "Preparado para Ethérea Pilates",
    "footnote": "Basado en el repertorio clásico de Joseph Pilates. Material de estudio; no sustituye una certificación integral.",
    "doc_title": "Manual de estudio: Pilates Reformer — Repertorio clásico", "header": "Pilates Reformer",
    "notices": [
        {"t": "box", "kind": "seguridad", "title": "Salud y seguridad", "body": [
            {"t": "p", "x": "Este libro es educativo. Antes de comenzar, consulta con un profesional de la salud, especialmente si tienes lesiones, embarazo, osteoporosis, problemas cervicales o de hombro, hipertensión u otra condición médica."},
            {"t": "p", "x": "El reformer es un aparato con resortes y partes móviles: aprende cada ejercicio con supervisión de una instructora certificada antes de practicarlo sola."}]},
        {"t": "box", "kind": "escuela", "title": "Repertorio y linajes", "body": [
            {"t": "p", "x": "El manual sigue el **repertorio clásico de Joseph Pilates**. Los nombres, el orden y las configuraciones de resortes varían ligeramente entre linajes (clásico, contemporáneo) y fabricantes; donde ocurre, lo verás señalado. Las resistencias de resortes son **orientativas**."}]},
    ],
    "howto": ["El libro tiene tres partes: Fundamentos (módulos 1–4), Repertorio clásico (módulos 5–9) y Enseñanza (módulos 10–12). "
              "Estudia en orden: el repertorio se entiende mejor después de conocer el aparato y los principios. Cada módulo termina con una evaluación; las respuestas están en el Apéndice B."],
    "legend": [["general", "Fundamento", "Definiciones y bases generales."], ["escuela", "Varía según escuela", "Diferencias entre linajes o fabricantes."],
               ["seguridad", "Seguridad", "Precauciones y contraindicaciones."], ["cue", "Cue clave", "Indicación modelo para enseñar."],
               ["tip", "Dato útil", "Consejos prácticos."], ["practica", "Práctica", "Ejercicios para tu estudio."]],
    "ficha_help": ["**Figura:** la persona sobre el reformer (inicio → final). Verás el carro, los resortes, la footbar, las hombreras, las correas y la caja cuando se usan.",
                   "**Mapa muscular:** rojo = principales; salmón = secundarios/estabilizadores.",
                   "**Tabla:** objetivo, posición inicial, ejecución, respiración, **resortes y montaje**, músculos, errores (✗), regresión (▼), progresión (▲), dosificación y cue clave."],
}


def appendix(book):
    out = [{"title": "Apéndice A · Glosario del reformer", "blocks": [TBL(["Término", "Definición"], [[a, b] for a, b in GLOS], widths=[2.0, 4.5], small=True)]}]
    sol = []
    for part in book["parts"]:
        sol.append(H(part["title"], 3))
        for m in part["modules"]:
            sol.append(H(f"Módulo {m['num']}", 4))
            sol.append(TBL(["#", "Respuesta"], [[str(i + 1), _answer(q)] for i, q in enumerate(m["quiz"])], widths=[0.4, 6.1], small=True))
    out.append({"title": "Apéndice B · Solucionario", "blocks": sol})
    out.append({"title": "Apéndice C · Plantillas", "blocks": [
        H("Tabla de resortes de tu reformer", 3),
        T("Completa con los colores y tensiones de tu equipo para traducir las resistencias orientativas del libro."),
        TBL(["Resistencia del libro", "Combinación en tu reformer", "Notas"], [["Ligero", "", ""], ["Medio", "", ""], ["Medio-pesado", "", ""], ["Pesado", "", ""], ["Todos / carro fijo", "", ""]], widths=[1.8, 2.6, 2.1]),
        H("Plantilla de clase", 3),
        TBL(["#", "Ejercicio", "Resortes", "Footbar / montaje", "Reps", "Cue clave"], [["", "", "", "", "", ""] for _ in range(14)], widths=[0.35, 1.9, 0.9, 1.3, 0.55, 1.5], small=True),
        H("Plan de estudio sugerido (10 semanas)", 3),
        TBL(["Semanas", "Contenido", "Práctica"], [
            ["1–2", "Módulos 1–4", "Conocer el aparato; respiración y postura Pilates"], ["3–4", "Módulo 5", "Footwork, Hundred, correas"],
            ["5", "Módulo 6", "Clase básica completa"], ["6–7", "Módulos 7–8", "Repertorio intermedio"], ["8", "Módulo 9", "Observar el avanzado (con supervisión)"],
            ["9–10", "Módulos 10–12", "Dirigir y grabar clases; rúbrica"]], widths=[0.9, 2.4, 3.2]),
    ]})
    out.append({"title": "Apéndice D · Rúbrica de clase práctica", "blocks": [TBL(["Criterio", "1 · Inicial", "2 · Básico", "3 · Competente", "4 · Experto"], [
        ["Montaje y resortes", "Inseguro", "Correcto con dudas", "Correcto y ágil", "Ajusta a cada persona"],
        ["Técnica y demostración", "Errores visibles", "Fallos menores", "Correcta", "Impecable"],
        ["Observación y corrección", "No corrige", "Corrige tarde", "Corrige a tiempo", "Prioriza y personaliza"],
        ["Cueing", "Confuso", "Claro pero tardío", "Anticipado", "Anticipado e inspirador"],
        ["Orden y fluidez", "Pausas largas", "Algunas pausas", "Fluido", "Transiciones integradas"],
        ["Seguridad y adaptaciones", "No ofrece opciones", "Ocasionales", "Siempre", "Anticipa riesgos"],
    ], widths=[1.6, 1.1, 1.3, 1.25, 1.25], small=True)]})
    out.append({"title": "Apéndice E · Referencias", "blocks": [UL(*REFS)]})
    return out


def main():
    book = {"meta": META, "parts": []}
    n = 0
    for part in PARTS:
        mods = []
        for m in part["modules"]:
            topics = []
            for tp in m["topics"]:
                blocks = B.process(tp["blocks"])
                n += sum(1 for b in blocks if b["t"] == "ex")
                topics.append({"title": tp["title"], "blocks": blocks})
            mods.append({**{k: v for k, v in m.items() if k != "topics"}, "topics": topics})
        book["parts"].append({**{k: v for k, v in part.items() if k != "modules"}, "modules": mods})
    book["appendix"] = appendix(book)
    B.render_diagram("d_cover_reformer")
    with open(os.path.join(B.ROOT, "build", "reformer.json"), "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
    print("ejercicios:", n, "módulos:", sum(len(p["modules"]) for p in book["parts"]))


if __name__ == "__main__":
    main()
