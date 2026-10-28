"""Diagramas específicos del manual de reformer."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon, Ellipse, FancyArrowPatch
from engine import NAVY, NAVY_L, GOLD, MAIN, SEC, EDGE, SKIN, WOOD, WOOD_D, PAD, PAD_D, METAL, draw_figure
from diagrams import _save, _clean, _foot, TEAL, SAND
import rf_poses as R


def reformer_parts(path):
    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    a, b, rail = 0.0, 14.0, 1.2
    for x in (0.4, 6.5, 13.6):
        ax.plot([x, x], [0, rail - 0.2], color=WOOD_D, lw=4)
    ax.add_patch(Rectangle((a, rail - 0.35), b - a, 0.35, fc=WOOD, ec=WOOD_D))
    # plataforma de pie (cabecera) y risers
    ax.add_patch(Rectangle((0.0, rail), 1.6, 0.35, fc=WOOD, ec=WOOD_D))
    ax.plot([0.3, 0.3], [rail, 4.2], color=WOOD_D, lw=4)
    ax.add_patch(Circle((0.3, 4.2), 0.2, fc=METAL, ec="#555"))
    # carro
    ax.add_patch(FancyBboxPatch((2.0, rail + 0.05), 4.6, 0.5, boxstyle="round,pad=0.04", fc=PAD, ec=PAD_D))
    ax.add_patch(Rectangle((2.3, rail + 0.6), 0.25, 0.6, fc=PAD_D))
    ax.add_patch(Rectangle((2.0, rail + 0.55), 0.25, 0.25, fc=PAD_D))
    ax.add_patch(Polygon([(1.9, rail + 0.6), (1.2, rail + 1.1), (1.25, rail + 1.2), (2.0, rail + 0.75)], fc=PAD, ec=PAD_D))
    # cuerdas y correas
    ax.plot([0.3, 3.0], [4.2, rail + 0.75], color="#5A4A3A", lw=1.2)
    ax.add_patch(Ellipse((3.15, rail + 0.75), 0.5, 0.3, fc="none", ec="#5A4A3A", lw=1.5))
    # resortes y gear bar
    zx = np.linspace(6.6, 12.6, 40)
    ax.plot(zx, [rail + 0.15 + (0.08 if i % 2 else -0.08) for i in range(40)], color=METAL, lw=1.2)
    ax.plot([12.7, 12.7], [rail - 0.1, rail + 0.4], color="#444", lw=3)
    # footbar
    ax.plot([13.3, 12.6], [rail, 3.3], color=METAL, lw=3)
    ax.add_patch(Circle((12.6, 3.3), 0.22, fc="#C9C9C9", ec="#555"))
    # caja corta (fantasma)
    ax.add_patch(Rectangle((7.5, 3.8), 2.6, 0.9, fc=WOOD, ec=WOOD_D, alpha=0.5, ls="--"))
    lbl = [((0.3, 4.2), (1.6, 5.0), "Poleas / risers"), ((0.9, rail + 0.2), (1.6, -0.4), "Plataforma"),
           ((1.5, rail + 1.0), (0.6, 2.7), "Reposacabezas"), ((2.42, rail + 1.1), (3.0, 3.4), "Hombreras"),
           ((3.15, rail + 0.75), (4.3, 2.6), "Correas (loops) y cuerdas"), ((4.5, rail + 0.3), (4.8, 0.2), "Carro"),
           ((9.5, rail + 0.15), (9.0, 0.2), "Resortes"), ((12.7, rail + 0.3), (11.2, 0.2), "Gear bar (tensión)"),
           ((12.6, 3.3), (11.2, 4.0), "Footbar (barra de pies)"), ((8.8, 4.7), (8.8, 5.25), "Caja (long box / short box)"),
           ((7.0, rail - 0.2), (7.0, -0.4), "Estructura y rieles")]
    for p, t, s in lbl:
        ax.annotate(s, xy=p, xytext=t, fontsize=7.3, color=NAVY, ha="center",
                    arrowprops=dict(arrowstyle="-", color=GOLD, lw=0.7))
    ax.set_xlim(-0.5, 14.5)
    ax.set_ylim(-0.8, 5.6)
    _clean(ax)
    _save(fig, path)


def footbar_positions(path):
    fig, axs = plt.subplots(1, 4, figsize=(7.2, 1.9))
    data = [("Pilates V (puntas)", 128, "TN", (0.18, -0.1)), ("Arcos", 150, "AN", (0.32, 0.12)),
            ("Talones", 178, "HlN", (0.2, 0.0)), ("Tendon stretch", 112, "TN", (0.15, -0.12))]
    for ax, (t, ft, key, off) in zip(axs, data):
        p = R.pose(trunk=-90, head=-90, thN=120, shN=60, ftN=ft, uaN=90, faN=90, lift=0)
        _, _, _, pts = draw_figure(ax, p, props=None)
        fx, fy = pts[key]
        ax.add_patch(Circle((fx + off[0], fy + off[1]), 0.2, fc="#C9C9C9", ec="#555", zorder=10))
        a = pts["AN"]
        ax.set_xlim(a[0] - 1.8, a[0] + 1.3)
        ax.set_ylim(a[1] - 0.8, a[1] + 1.2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(t, fontsize=8.5, color=NAVY, weight="bold")
    fig.text(0.5, 0.02, "Detalle del pie sobre la footbar (vista lateral). En Pilates V los talones se juntan y las puntas se separan.",
             ha="center", fontsize=6.8, color=NAVY, style="italic")
    _save(fig, path)


def pilates_stance(path):
    fig, axs = plt.subplots(1, 3, figsize=(6.4, 2.4))
    data = [("Paralela", [(-0.45, 0, 0), (0.45, 0, 0)], "Pies a la anchura de la cadera"),
            ("Pilates V", [(-0.42, 0, 28), (0.42, 0, -28)], "Talones juntos, puntas separadas\n(rotación externa ligera desde la cadera)"),
            ("Separada (V amplia)", [(-0.9, 0, 28), (0.9, 0, -28)], "Talones separados a lo ancho\nde la barra")]
    for ax, (t, feet, d) in zip(axs, data):
        for x, y, a in feet:
            _foot(ax, x, y, a)
        ax.text(0, 1.2, t, ha="center", fontsize=9, weight="bold", color=NAVY)
        ax.text(0, -0.9, d, ha="center", va="top", fontsize=6.6, color=NAVY)
        ax.set_xlim(-1.7, 1.7)
        ax.set_ylim(-1.9, 1.5)
        _clean(ax)
    _save(fig, path)


def springs_chart(path):
    rows = [("Footwork", 3.5), ("Running / Pelvic lift", 3.5), ("Hundred / Coordination", 2.5), ("Feet in straps", 2.5),
            ("Stomach massage", 2.5), ("Elephant / Knee stretches", 2), ("Long stretch / Down stretch", 2),
            ("Rowing / Chest expansion", 1), ("Pulling straps / Backstroke", 1), ("Thigh stretch / Arm circles", 1),
            ("Tendon stretch / Star", 1), ("Short box", 4)]
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    for i, (n, v) in enumerate(rows):
        col = MAIN if v >= 3 else GOLD if v >= 2 else TEAL
        ax.barh(i, v, color=col, alpha=0.8, height=0.6)
        ax.text(v + 0.08, i, {4: "Todos / carro fijo", 3.5: "Pesado", 2.5: "Medio-pesado", 2: "Medio", 1: "Ligero"}[v], va="center", fontsize=7, color=NAVY)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=7.4, color=NAVY)
    ax.invert_yaxis()
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(["ligero", "medio", "pesado", "máx."], fontsize=7)
    ax.set_xlim(0, 5.2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.set_title("Resistencia de resortes orientativa por grupo de ejercicios", fontsize=9, color=NAVY, weight="bold")
    _save(fig, path)


def chain_diagram(path):
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.4))
    for ax, (t, d, foot_fixed) in zip(axs, (("Cadena cerrada", "El extremo empuja una superficie fija\n(footwork: pies en la barra)", True),
                                            ("Cadena abierta", "El extremo se mueve libre\n(feet in straps: pies en correas)", False))):
        p = R.pose(trunk=-90, head=-90, thN=125, shN=55, ftN=130, uaN=90, faN=90, lift=1.6)
        props = R.rf(fb="TN", fb_off=(0.18, -0.1), blocks="C", blocks_dx=0.6) if foot_fixed else R.rf(straps=["AN"])
        if not foot_fixed:
            p = R.straps_supine(140, 130, 210)
        x0, x1, top, _ = draw_figure(ax, p, props=props)
        ax.set_title(t, fontsize=9, color=NAVY, weight="bold")
        ax.text((x0 + x1) / 2, -0.4, d, ha="center", va="top", fontsize=6.8, color=NAVY)
        ax.set_xlim(x0 - 0.3, x1 + 0.3)
        ax.set_ylim(-1.6, max(top, 5.5))
        _clean(ax)
    _save(fig, path)
