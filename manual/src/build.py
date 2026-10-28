"""Genera figuras y book.json para el maquetador de Word."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
import engine as E
import diagrams as D
from diagrams import TEAL
import sculpt_a, sculpt_b, sculpt_c, barre_a, barre_b, block_a, block_b

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG = os.path.join(ROOT, "build", "img")
os.makedirs(IMG, exist_ok=True)
FORCE = "--force" in sys.argv

DIAGRAMS = {
    "d_anatomy": E.anatomy_chart,
    "d_planes": D.planes, "d_spine": D.spine, "d_pelvis": D.pelvis, "d_knees": D.knees,
    "d_bfeet": D.ballet_feet, "d_barms": D.ballet_arms, "d_stances": D.squat_stances,
    "d_contr": D.contractions, "d_hyper": D.hypertrophy, "d_energy": D.energy_systems,
    "d_tempo": D.tempo, "d_core": D.core_cylinder, "d_breath": D.breathing,
    "d_blocks": D.blocks, "d_fob": D.feet_on_blocks, "d_eight": D.eight_counts,
    "d_tree": lambda p: D.tree(p, "Entrenamiento", [
        ("Por capacidad", ["Fuerza", "Hipertrofia", "Resistencia", "Potencia", "Movilidad"]),
        ("Por sistema", ["ATP-PC", "Glucolítico", "Oxidativo"]),
        ("Por formato", ["Series", "Circuito", "HIIT / Tabata", "EMOM / AMRAP"]),
        ("Por patrón", ["Sentadilla", "Bisagra", "Zancada", "Empuje", "Tracción", "Core"])]),
    "d_cueflow": lambda p: D.flow(p, [("Posición", "dónde y cómo empiezo"), ("Acción", "qué movimiento"), ("Alineación", "cómo hacerlo bien"),
                                       ("Respiración", "cuándo inhalo/exhalo"), ("Motivación", "para qué / ánimo")], colors=[E.NAVY, E.GOLD, TEAL]),
    "d_wheel": lambda p: D.wheel(p, "Pilates", [("Concentración", "mente"), ("Control", "calidad"), ("Centro", "powerhouse"),
                                                 ("Fluidez", "ritmo"), ("Precisión", "detalle"), ("Respiración", "motor")]),
    "d_tl_barre": lambda p: D.timeline(p, [(1913, "Nace Lotte Berk"), (1959, "Estudio en Londres"), (1971, "Llega a Nueva York"),
                                           (2001, "Expansión de marcas"), (2015, "Estilos de fusión")]),
    "d_tl_pilates": lambda p: D.timeline(p, [(1883, "Nace J. Pilates"), (1914, "Internamiento en\nInglaterra (IGM)"), (1926, "Estudio en\nNueva York"),
                                             (1945, "Return to Life"), (1967, "Muere J. Pilates"), (1980, "Difusión y\nnuevas escuelas")]),
    "d_props_sculpt": lambda p: D.props_sheet(p, [("Mancuernas", "1–10 kg", D._db), ("Mat", "6–8 mm", D._mat), ("Banda", "ligera / media", D._band), ("Block", "opcional", D._block)]),
    "d_props_barre": lambda p: D.props_sheet(p, [("Barra", "a la cintura", D._barre), ("Mancuernas", "0.5–2 kg", D._db), ("Mini ball", "20–25 cm", D._ball),
                                                  ("Banda", "loop / larga", D._band), ("Mat", "", D._mat), ("Tobilleras", "0.5–1 kg", D._ankle)]),
    "d_curve_sculpt": lambda p: D.class_curve(p, [("Calentamiento", 6, 2, 5, TEAL), ("Bloque 1", 10, 6, 8, E.MAIN), ("Cardio", 3, 8, 9, E.GOLD),
                                                  ("Bloque 2", 10, 6, 8, "#7E6B8F"), ("Cardio", 2, 8, 9, E.GOLD), ("Bloque 3", 10, 6, 8, E.MAIN),
                                                  ("Core", 4, 6, 7, E.NAVY_L), ("Enfriamiento", 5, 4, 2, TEAL)]),
    "d_curve_barre": lambda p: D.class_curve(p, [("Calentamiento", 6, 2, 4, TEAL), ("Brazos", 7, 5, 7, "#7E6B8F"), ("Thigh", 8, 6, 8, E.MAIN),
                                                 ("Seat", 9, 6, 8, E.MAIN), ("Cardio", 3, 7, 8.5, E.GOLD), ("Plié 2.ª", 4, 6, 8, E.MAIN),
                                                 ("Centro", 8, 5, 7, E.NAVY_L), ("Elongación", 5, 3, 1.5, TEAL)]),
    "d_curve_bbp": lambda p: D.class_curve(p, [("Centrado", 3, 1.5, 2.5, TEAL), ("Calentamiento", 5, 3, 5, TEAL), ("Inferior de pie", 10, 6, 8, E.MAIN),
                                               ("Cardio", 4, 7.5, 8.5, E.GOLD), ("Inferior suelo", 8, 6, 7.5, E.MAIN), ("Core clásico", 8, 6, 7.5, E.NAVY_L),
                                               ("Superior", 7, 6, 8, "#7E6B8F"), ("Stretch", 5, 3, 1.5, TEAL)]),
    "d_bpm_sculpt": lambda p: D.music_bpm(p, [("Calentamiento", 110, 122, TEAL), ("Fuerza", 118, 130, E.MAIN), ("Cardio", 130, 160, E.GOLD),
                                              ("Core", 110, 125, E.NAVY_L), ("Enfriamiento", 60, 90, TEAL)], "Sculpt & Burn"),
    "d_bpm_barre": lambda p: D.music_bpm(p, [("Calentamiento", 105, 120, TEAL), ("Brazos", 115, 125, "#7E6B8F"), ("Thigh / seat", 120, 130, E.MAIN),
                                             ("Cardio barre", 128, 140, E.GOLD), ("Centro", 110, 122, E.NAVY_L), ("Elongación", 60, 85, TEAL)], "Barre"),
}


def render_diagram(name):
    path = os.path.join(IMG, name + ".png")
    if FORCE or not os.path.exists(path):
        DIAGRAMS[name](path)
    return path


def process(blocks):
    out = []
    for b in blocks:
        t = b["t"]
        if t == "fig":
            render_diagram(b["name"])
            out.append(b)
        elif t == "gallery":
            path = os.path.join(IMG, b["name"] + ".png")
            if FORCE or not os.path.exists(path):
                E.pose_gallery(path, b["items"], per_row=b["per_row"])
            out.append({"t": "fig", "name": b["name"], "caption": b["caption"], "width": b["width"]})
        elif t == "ex":
            name = "ex_" + slug(b["name"])
            path = os.path.join(IMG, name + ".png")
            if FORCE or not os.path.exists(path):
                E.exercise_figure(path, b["frames"], b["prim"], b["sec"])
            c = {k: v for k, v in b.items() if k not in ("frames",)}
            c["img"] = name
            c["img_narrow"] = len(b["frames"]) == 0
            out.append(c)
        elif t == "box":
            out.append(b)
        else:
            out.append(b)
    return out


PARTS = [
    dict(key="sculpt", title="Sculpt & Burn", short="Sculpt & Burn",
         intro="Es una disciplina de fuerza que combina ejercicios específicos y funcionales para desarrollar fuerza, resistencia "
               "muscular y control corporal. Está diseñada para tonificar, moldear e incrementar masa muscular mientras mejoras "
               "tu postura, estabilidad y capacidad física general.",
         modules=sculpt_a.MODULES + sculpt_b.MODULES + sculpt_c.MODULES),
    dict(key="barre", title="Barre", short="Barre",
         intro="Es una combinación de ballet, pilates y body sculpt que integra elongaciones, micromovimientos y ejercicios de "
               "resistencia para fortalecer, tonificar y estilizar los músculos. Su enfoque de bajo impacto y alta intensidad "
               "también ayuda a mejorar la postura, la estabilidad, el control corporal y la conexión con tu cuerpo.",
         modules=barre_a.MODULES + barre_b.MODULES),
    dict(key="block", title="Block Burn Pilates", short="Block Burn Pilates",
         intro="Es una práctica de Pilates Clásico fusionada con elementos de Sculpt & Burn y Barre, en la que los blocks funcionan "
               "como herramienta principal. Al trabajar sobre una superficie inestable, se incrementa la activación muscular y se "
               "amplían los rangos de movimiento en los que normalmente entrenas. El resultado es una disciplina que fortalece, "
               "tonifica y reta al cuerpo de una forma distinta, mientras desarrolla mayor control, estabilidad y conciencia corporal.",
         modules=block_a.MODULES + block_b.MODULES),
]


def main():
    book = {"parts": []}
    n_ex = 0
    for part in PARTS:
        mods = []
        for m in part["modules"]:
            topics = []
            for tp in m["topics"]:
                blocks = process(tp["blocks"])
                n_ex += sum(1 for b in blocks if b["t"] == "ex")
                topics.append({"title": tp["title"], "blocks": blocks})
            mods.append({**{k: v for k, v in m.items() if k != "topics"}, "topics": topics})
        book["parts"].append({**{k: v for k, v in part.items() if k != "modules"}, "modules": mods})
    import appendix
    book["appendix"] = appendix.build(book)
    for b in book["appendix"]:
        for blk in b["blocks"]:
            if blk["t"] == "fig":
                render_diagram(blk["name"])
    with open(os.path.join(ROOT, "build", "book.json"), "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
    print("ejercicios:", n_ex, "módulos:", sum(len(p["modules"]) for p in book["parts"]))


if __name__ == "__main__":
    main()
