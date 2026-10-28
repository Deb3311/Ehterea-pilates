"""Diagramas conceptuales del manual."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (Ellipse, Polygon, Circle, Rectangle, FancyArrowPatch,
                                FancyBboxPatch, Arc, Wedge)
from engine import (NAVY, NAVY_L, GOLD, MAIN, SEC, BASE, SKIN, EDGE, FLOOR, BLOCK,
                    draw_figure, draw_floor)
import poses as P

DPI = 200
TEAL = "#5E8C8A"
SAND = "#EDE6DA"


def _save(fig, path):
    fig.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def _clean(ax):
    ax.set_aspect("equal")
    ax.axis("off")


# ------------------------------------------------------------------ planos
def planes(path):
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 3.3))
    data = [
        ("Plano sagital", "Divide derecha / izquierda\nMovimientos: flexión y extensión\nEj.: sentadilla, curl, zancada", "front", "v"),
        ("Plano frontal", "Divide anterior / posterior\nMovimientos: abducción y aducción\nEj.: elevación lateral, jacks", "side", "v"),
        ("Plano transversal", "Divide superior / inferior\nMovimientos: rotaciones\nEj.: giro ruso, woodchop", "front", "h"),
    ]
    for ax, (t, desc, view, orient) in zip(axs, data):
        p = P.front() if view == "front" else P.stand()
        draw_figure(ax, p, x0=0)
        if orient == "v":
            ax.add_patch(Polygon([(-0.25, -0.3), (0.25, 0.3), (0.25, 9.6), (-0.25, 9.0)], fc=GOLD, alpha=0.35, ec=GOLD))
        else:
            ax.add_patch(Polygon([(-2.6, 4.3), (2.0, 4.3), (2.6, 4.9), (-2.0, 4.9)], fc=GOLD, alpha=0.4, ec=GOLD))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3.6, 10)
        ax.text(0, 9.9, t, ha="center", fontsize=9, weight="bold", color=NAVY)
        ax.text(0, -0.5, desc, ha="center", va="top", fontsize=6.6, color=NAVY, linespacing=1.4)
        _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ columna
def spine(path):
    fig, ax = plt.subplots(figsize=(4.6, 5.6))
    regions = [("Cervical", 7, "lordosis", "#7FA7C9", 0.55), ("Torácica", 12, "cifosis", "#B9A27A", 0.42),
               ("Lumbar", 5, "lordosis", "#C77B5E", 0.75)]
    y = 0
    pts = []
    total = 24
    ys = np.linspace(0, 10, total)
    xs = []
    for yy in ys:
        # curva en S invertida (vista lateral, anterior a la derecha)
        if yy < 2.9:
            x = 0.45 * math.sin(math.pi * yy / 2.9)
        elif yy < 8.0:
            x = -0.8 * math.sin(math.pi * (yy - 2.9) / 5.1)
        else:
            x = 0.6 * math.sin(math.pi * (yy - 8.0) / 2.6)
        xs.append(x)
    i = 0
    cols = []
    for name, n, curve, col, w in regions:
        for k in range(n):
            cols.append((col, w))
    for (x, yy), (col, w) in zip(zip(xs, ys[::-1] * 0 + ys), cols[::-1]):
        pass
    # dibujar desde arriba (cervical) hacia abajo
    yvals = list(np.linspace(10, 2.2, total))
    xs_top = []
    for yy in yvals:
        t = 10 - yy
        if t < 2.1:
            x = 0.38 * math.sin(math.pi * t / 2.1)
        elif t < 6.0:
            x = -0.7 * math.sin(math.pi * (t - 2.1) / 3.9)
        else:
            x = 0.55 * math.sin(math.pi * (t - 6.0) / 2.0)
        xs_top.append(x)
    idx = 0
    for name, n, curve, col, w in regions:
        ymid = []
        for k in range(n):
            x, yy = xs_top[idx], yvals[idx]
            ax.add_patch(FancyBboxPatch((x - w / 2, yy - 0.13), w, 0.26, boxstyle="round,pad=0.02",
                                        fc=col, ec=EDGE, lw=0.6))
            ymid.append(yy)
            idx += 1
        ym = sum(ymid) / len(ymid)
        ax.text(1.3, ym, f"{name} ({n} vértebras)\nCurva: {curve}", va="center", fontsize=8, color=NAVY)
        ax.plot([1.2, 1.2], [min(ymid) - 0.1, max(ymid) + 0.1], color=col, lw=3)
    # sacro y cóccix
    ax.add_patch(Polygon([(0.15, 2.0), (0.75, 1.9), (0.65, 0.9), (0.35, 0.55)], fc="#9C8A74", ec=EDGE))
    ax.text(1.3, 1.4, "Sacro (5 fusionadas)\ny cóccix", va="center", fontsize=8, color=NAVY)
    ax.plot([1.2, 1.2], [0.6, 2.0], color="#9C8A74", lw=3)
    ax.annotate("", xy=(-1.6, 9.5), xytext=(-1.6, 1.0), arrowprops=dict(arrowstyle="<->", color=GOLD))
    ax.text(-1.75, 5.2, "Vista lateral · anterior →", rotation=90, va="center", ha="right", fontsize=7.5, color=NAVY)
    ax.set_xlim(-2.4, 4.6)
    ax.set_ylim(0.2, 10.6)
    _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ pelvis
def pelvis(path):
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 3.2))
    data = [("Anteversión", 18, "Aumenta la curva lumbar\n(hiperlordosis)"),
            ("Neutra", 0, "EIAS y pubis en el mismo\nplano vertical"),
            ("Retroversión", -18, "Aplana la curva lumbar\n(imprint / tuck)")]
    for ax, (t, ang, desc) in zip(axs, data):
        a = math.radians(ang)
        R = lambda x, y: (x * math.cos(a) + y * math.sin(a), -x * math.sin(a) + y * math.cos(a))
        bowl = [R(x, y) for x, y in [(-1.6, 1.2), (1.6, 1.2), (1.1, -0.6), (0.4, -1.1), (-0.4, -1.1), (-1.1, -0.6)]]
        ax.add_patch(Polygon(bowl, fc=SAND, ec=NAVY, lw=1.5))
        wl = [R(-1.45, 0.75), R(1.45, 0.75)]
        # agua: siempre horizontal
        ax.add_patch(Polygon([(-1.3, 0.75), (1.3, 0.75), (0.9, -0.4), (-0.9, -0.4)], fc="#9EC3D9", alpha=0.6, ec="none"))
        asis = R(1.55, 1.15)
        pub = R(0.55, -1.05)
        ax.plot(*asis, "o", color=MAIN)
        ax.plot(*pub, "o", color=MAIN)
        ax.plot([asis[0], pub[0]], [asis[1], pub[1]], color=MAIN, ls="--", lw=1)
        ax.text(asis[0] + 0.12, asis[1] + 0.1, "EIAS", fontsize=6.5, color=MAIN)
        ax.text(pub[0] + 0.12, pub[1] - 0.2, "Pubis", fontsize=6.5, color=MAIN)
        # columna lumbar
        base = R(-1.0, 1.2)
        curv = 0.55 + ang / 30.0
        ys = np.linspace(0, 2.6, 30)
        xs = base[0] + curv * np.sin(np.pi * ys / 2.6) * 0.8 - ys * math.sin(a) * 0.3
        ax.plot(xs, base[1] + ys, color=NAVY, lw=4, solid_capstyle="round")
        if ang:
            ax.annotate("", xy=(1.9, 0.1 - 0.8 * np.sign(ang)), xytext=(1.9, 0.1 + 0.8 * np.sign(ang)),
                        arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.5, connectionstyle="arc3,rad=-0.4"))
        ax.text(0, 4.3, t, ha="center", fontsize=9.5, weight="bold", color=NAVY)
        ax.text(0, -1.6, desc, ha="center", va="top", fontsize=7, color=NAVY)
        ax.text(-2.2, 4.0, "← posterior", fontsize=6, color=EDGE)
        ax.text(2.2, 4.0, "anterior →", fontsize=6, color=EDGE, ha="right")
        ax.set_xlim(-2.4, 2.6)
        ax.set_ylim(-2.6, 4.7)
        _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ rodilla-pie
def knees(path):
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 3.4))
    data = [("Correcta", 0, "Rodilla alineada con el\n2.º–3.er dedo del pie", "#3C7A5A"),
            ("Valgo (rodillas hacia dentro)", 0.55, "Colapso medial: carga\nexcesiva en ligamentos", MAIN),
            ("Varo (rodillas hacia fuera)", -0.45, "Peso en el borde externo\ndel pie", "#C38A2E")]
    for ax, (t, k, desc, col) in zip(axs, data):
        for s in (1, -1):
            hip = (s * 0.9, 6)
            ank = (s * 1.05, 1.0)
            knee = (s * (1.0 - k), 3.5)
            ax.plot([hip[0], knee[0], ank[0]], [hip[1], knee[1], ank[1]], color=NAVY, lw=7, solid_capstyle="round")
            ax.add_patch(Circle(knee, 0.32, fc=SKIN, ec=col, lw=2, zorder=5))
            foot = Ellipse((s * 1.35, 0.55), 0.7, 1.3, angle=-s * 20, fc=SAND, ec=NAVY, lw=1.2)
            ax.add_patch(foot)
            ax.plot([s * 1.05, s * 1.55], [1.0, -0.1], color=col, ls=":", lw=1.4)
            ax.plot([hip[0], s * 1.55], [hip[1], -0.1], color=GOLD, ls="--", lw=0.8)
        ax.add_patch(FancyBboxPatch((-1.4, 5.8), 2.8, 0.9, boxstyle="round,pad=0.05", fc=SKIN, ec=NAVY))
        ax.text(0, 7.2, t, ha="center", fontsize=8.2, weight="bold", color=col)
        ax.text(0, -0.6, desc, ha="center", va="top", fontsize=7, color=NAVY)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2.2, 7.7)
        _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ pies
def _foot(ax, x, y, ang, col=SAND, scale=1.0, label=None):
    """ang: grados de rotación del pie (0 = apuntando hacia arriba en la imagen)."""
    a = math.radians(ang)
    pts = [(-0.28, -0.5), (0.28, -0.5), (0.34, 0.15), (0.3, 0.55), (0.0, 0.7), (-0.3, 0.55), (-0.34, 0.1)]
    R = [(x + scale * (px * math.cos(a) - py * math.sin(a)), y + scale * (px * math.sin(a) + py * math.cos(a))) for px, py in pts]
    ax.add_patch(Polygon(R, closed=True, fc=col, ec=NAVY, lw=1.2, joinstyle="round"))
    hx, hy = x + scale * (0.4 * math.sin(a)), y - scale * (0.4 * math.cos(a))
    ax.add_patch(Circle((hx, hy), 0.08 * scale, fc=NAVY))


def ballet_feet(path):
    fig, axs = plt.subplots(1, 6, figsize=(7.2, 2.2))
    T = 40  # rotación externa didáctica (no 90°)
    data = [
        ("Paralela", [(-0.4, 0, 0), (0.4, 0, 0)]),
        ("1.ª", [(-0.3, 0, T), (0.3, 0, -T)]),
        ("2.ª", [(-1.0, 0, T), (1.0, 0, -T)]),
        ("3.ª", [(-0.25, 0.25, T), (0.15, -0.05, -T)]),
        ("4.ª", [(-0.35, 0.75, T), (0.2, -0.55, -T)]),
        ("5.ª", [(-0.2, 0.3, T), (0.2, -0.25, -T)]),
    ]
    for ax, (t, feet) in zip(axs, data):
        for x, y, a in feet:
            _foot(ax, x, y, a)
        ax.text(0, 1.55, t, ha="center", fontsize=10, weight="bold", color=NAVY)
        ax.set_xlim(-1.7, 1.7)
        ax.set_ylim(-1.5, 1.9)
        _clean(ax)
    fig.text(0.5, -0.02, "Vista superior. La rotación externa se muestra moderada: en barre se usa la rotación natural de la cadera, nunca forzada desde rodillas o pies.",
             ha="center", fontsize=6.8, color=NAVY, style="italic")
    _save(fig, path)


def ballet_arms(path):
    fig, axs = plt.subplots(1, 6, figsize=(7.4, 2.7))
    for ax, (name, kw) in zip(axs, P.BALLET_ARMS.items()):
        draw_figure(ax, P.front(**kw), x0=0)
        ax.set_xlim(-3.2, 3.2)
        ax.set_ylim(-1.6, 10.5)
        ax.text(0, -0.4, name, ha="center", va="top", fontsize=6.8, color=NAVY, wrap=True)
        _clean(ax)
    fig.text(0.5, -0.02, "*Tercera y cuarta varían según la escuela (francesa, RAD, Cecchetti, Vaganova).",
             ha="center", fontsize=6.8, color=NAVY, style="italic")
    _save(fig, path)


def squat_stances(path):
    fig, axs = plt.subplots(1, 4, figsize=(7.2, 2.4))
    data = [("Estrecha", 0.35, 5, "Más cuádriceps,\nexige más tobillo"),
            ("Ancho de cadera", 0.6, 12, "Punto de partida\nuniversal"),
            ("Ancho de hombros", 0.9, 20, "La más común para\nfemur largo"),
            ("Amplia / sumo", 1.45, 40, "Más aductores y\nglúteo; tronco erguido")]
    for ax, (t, w, a, d) in zip(axs, data):
        _foot(ax, -w, 0, a)
        _foot(ax, w, 0, -a)
        ax.plot([-w, w], [-0.45, -0.45], color=GOLD, lw=1)
        ax.text(0, 1.25, t, ha="center", fontsize=8.5, weight="bold", color=NAVY)
        ax.text(0, -0.75, f"Puntas ≈ {a}°\n{d}", ha="center", va="top", fontsize=6.6, color=NAVY)
        ax.set_xlim(-2.1, 2.1)
        ax.set_ylim(-2.1, 1.6)
        _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ contracciones
def contractions(path):
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.6))
    t = np.linspace(0, 3, 100)
    data = [("Concéntrica", 1 - 0.35 * t / 3, "El músculo se acorta\nEj.: subir la mancuerna en el curl", MAIN),
            ("Isométrica", np.ones_like(t) * 0.82, "Longitud constante\nEj.: plancha, wall sit, sostener", TEAL),
            ("Excéntrica", 0.65 + 0.35 * t / 3, "Se alarga bajo carga\nEj.: bajar despacio en la sentadilla", GOLD)]
    for ax, (n, y, d, c) in zip(axs, data):
        ax.plot(t, y, color=c, lw=3)
        ax.set_ylim(0.4, 1.15)
        ax.set_xlim(0, 3)
        ax.set_title(n, fontsize=9.5, color=NAVY, weight="bold")
        ax.set_xlabel("tiempo", fontsize=7, color=NAVY)
        ax.set_ylabel("longitud del músculo", fontsize=7, color=NAVY)
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.text(1.5, 0.45, d, ha="center", va="bottom", fontsize=6.6, color=NAVY)
    fig.tight_layout()
    _save(fig, path)


def hypertrophy(path):
    fig, ax = plt.subplots(figsize=(6.8, 3.0))
    items = [((1.1, 2.0), 1.0, "Tensión\nmecánica", "Estímulo principal:\ncarga + rango completo\n+ cerca del fallo", MAIN),
             ((3.6, 2.0), 0.8, "Estrés\nmetabólico", "Metabolitos, «quemazón»,\npausas cortas, pulsos", GOLD),
             ((5.8, 2.0), 0.7, "Daño\nmuscular", "Microlesiones; papel\nsecundario y discutido", TEAL)]
    for (x, y), r, t, d, c in items:
        ax.add_patch(Circle((x, y), r, fc=c, alpha=0.18, ec=c, lw=2))
        ax.text(x, y, t, ha="center", va="center", fontsize=8.5, weight="bold", color=NAVY)
        ax.text(x, y - r - 0.15, d, ha="center", va="top", fontsize=6.6, color=NAVY)
        ax.add_patch(FancyArrowPatch((x, y + r), (8.1, 2.55), arrowstyle="-|>", mutation_scale=12,
                                     color=EDGE, lw=1.1, connectionstyle="arc3,rad=-0.25"))
    ax.add_patch(FancyBboxPatch((7.4, 1.6), 2.0, 0.9, boxstyle="round,pad=0.1", fc=NAVY, ec=NAVY))
    ax.text(8.4, 2.05, "HIPERTROFIA", ha="center", va="center", color="white", fontsize=9, weight="bold")
    ax.text(8.4, 1.3, "+ proteína suficiente\n+ descanso y sueño\n+ progresión", ha="center", va="top", fontsize=6.6, color=NAVY)
    ax.set_xlim(0, 9.7)
    ax.set_ylim(-0.3, 4.3)
    _clean(ax)
    _save(fig, path)


def energy_systems(path):
    fig, ax = plt.subplots(figsize=(6.8, 2.8))
    t = np.logspace(0, 3.6, 300)
    pc = np.exp(-((np.log10(t) - 0.6) ** 2) / 0.12)
    gl = np.exp(-((np.log10(t) - 1.7) ** 2) / 0.25)
    ox = 1 / (1 + np.exp(-(np.log10(t) - 2.2) * 4))
    for y, c, n in ((pc, MAIN, "ATP-PC (fosfágenos)\n0–10 s · máxima potencia"),
                    (gl, GOLD, "Glucolítico\n10 s–2 min · alta intensidad"),
                    (ox, TEAL, "Oxidativo (aeróbico)\n> 2 min · resistencia")):
        ax.plot(t, y, color=c, lw=2.5, label=n)
        ax.fill_between(t, y, alpha=0.08, color=c)
    ax.set_xscale("log")
    ax.set_xticks([1, 10, 60, 120, 600, 3600])
    ax.set_xticklabels(["1 s", "10 s", "1 min", "2 min", "10 min", "60 min"], fontsize=7)
    ax.set_yticks([])
    ax.set_ylabel("contribución relativa", fontsize=7.5, color=NAVY)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(fontsize=6.8, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=3)
    ax.text(3600, 1.05, "Los tres sistemas funcionan siempre a la vez;\nlo que cambia es cuál predomina.", ha="right", fontsize=6.8, color=NAVY, style="italic")
    _save(fig, path)


# ------------------------------------------------------------------ curvas de clase
def class_curve(path, phases, title=None):
    """phases: lista de (nombre, minutos, intensidad_inicio, intensidad_fin, color)."""
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    t0 = 0
    for name, dur, i0, i1, col in phases:
        xs = np.linspace(t0, t0 + dur, 20)
        ys = np.linspace(i0, i1, 20)
        ax.fill_between(xs, ys, color=col, alpha=0.35, lw=0)
        ax.plot(xs, ys, color=col, lw=2)
        ax.text(t0 + dur / 2, max(i0, i1) + 0.4, name, ha="center", va="bottom", fontsize=6.4, color=NAVY,
                rotation=0 if dur >= 6 else 90)
        t0 += dur
    ax.set_xlim(0, t0)
    ax.set_ylim(0, 11.5)
    ax.set_xlabel("minutos", fontsize=7.5, color=NAVY)
    ax.set_ylabel("intensidad (RPE 1–10)", fontsize=7.5, color=NAVY)
    ax.tick_params(labelsize=7)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if title:
        ax.set_title(title, fontsize=9, color=NAVY, weight="bold")
    _save(fig, path)


def tempo(path):
    fig, ax = plt.subplots(figsize=(6.6, 2.2))
    segs = [("3", "Excéntrica\n(bajar)", GOLD, 3), ("1", "Pausa\nabajo", TEAL, 1.4), ("1", "Concéntrica\n(subir)", MAIN, 1.4), ("0", "Pausa\narriba", EDGE, 1.0)]
    x = 0
    for n, t, c, w in segs:
        ax.add_patch(FancyBboxPatch((x, 0), w * 1.2, 1, boxstyle="round,pad=0.02", fc=c, alpha=0.8, ec="white"))
        ax.text(x + w * 0.6, 0.5, n, ha="center", va="center", fontsize=15, color="white", weight="bold")
        ax.text(x + w * 0.6, -0.15, t, ha="center", va="top", fontsize=7, color=NAVY)
        x += w * 1.2 + 0.1
    ax.text(x / 2, 1.35, "Tempo 3-1-1-0 en una sentadilla", ha="center", fontsize=9, weight="bold", color=NAVY)
    ax.set_xlim(-0.1, x)
    ax.set_ylim(-1.2, 1.7)
    _clean(ax)
    _save(fig, path)


def tree(path, root, branches, w=7.2, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h))
    n = len(branches)
    ax.add_patch(FancyBboxPatch((n / 2 - 1.3, 4.3), 2.6, 0.7, boxstyle="round,pad=0.06", fc=NAVY, ec=NAVY))
    ax.text(n / 2, 4.65, root, ha="center", va="center", color="white", fontsize=9, weight="bold")
    for i, (title, items) in enumerate(branches):
        cx = i + 0.5
        ax.plot([n / 2, cx], [4.3, 3.55], color=EDGE, lw=1)
        ax.add_patch(FancyBboxPatch((cx - 0.46, 3.0), 0.92, 0.55, boxstyle="round,pad=0.04", fc=GOLD, ec=GOLD))
        ax.text(cx, 3.27, title, ha="center", va="center", color="white", fontsize=6.6, weight="bold")
        ax.text(cx, 2.85, "\n".join("· " + it for it in items), ha="center", va="top", fontsize=6.0, color=NAVY, linespacing=1.5)
    ax.set_xlim(-0.05, n + 0.05)
    ax.set_ylim(0, 5.2)
    _clean(ax)
    ax.set_aspect("auto")
    _save(fig, path)


def flow(path, steps, title=None, w=7.2, h=1.6, colors=None):
    fig, ax = plt.subplots(figsize=(w, h))
    n = len(steps)
    for i, (t, d) in enumerate(steps):
        c = (colors or [NAVY])[i % len(colors or [NAVY])]
        ax.add_patch(FancyBboxPatch((i * 2.2, 0.35), 1.8, 0.9, boxstyle="round,pad=0.06", fc=c, ec=c))
        ax.text(i * 2.2 + 0.9, 0.8, t, ha="center", va="center", fontsize=7.6, color="white", weight="bold")
        ax.text(i * 2.2 + 0.9, 0.15, d, ha="center", va="top", fontsize=6.3, color=NAVY)
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((i * 2.2 + 1.9, 0.8), (i * 2.2 + 2.15, 0.8), arrowstyle="-|>", mutation_scale=10, color=GOLD))
    if title:
        ax.text(n * 1.1 - 0.2, 1.5, title, ha="center", fontsize=8.5, weight="bold", color=NAVY)
    ax.set_xlim(-0.15, n * 2.2 - 0.25)
    ax.set_ylim(-0.75, 1.75)
    _clean(ax)
    _save(fig, path)


def wheel(path, center, items):
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.add_patch(Circle((0, 0), 1.0, fc=NAVY))
    ax.text(0, 0, center, ha="center", va="center", color="white", fontsize=9, weight="bold")
    n = len(items)
    for i, (t, d) in enumerate(items):
        a = math.pi / 2 - 2 * math.pi * i / n
        x, y = 2.35 * math.cos(a), 2.35 * math.sin(a)
        ax.plot([0.95 * math.cos(a), 1.6 * math.cos(a)], [0.95 * math.sin(a), 1.6 * math.sin(a)], color=EDGE)
        ax.add_patch(Circle((x, y), 0.78, fc=GOLD if i % 2 == 0 else TEAL, alpha=0.9))
        ax.text(x, y + 0.12, t, ha="center", va="center", color="white", fontsize=6.6 if len(t) > 10 else 7.8, weight="bold")
        ax.text(x, y - 0.25, d, ha="center", va="center", color="white", fontsize=5.6)
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-3.2, 3.2)
    _clean(ax)
    _save(fig, path)


def timeline(path, events, title=None, w=7.2):
    fig, ax = plt.subplots(figsize=(w, 2.5))
    years = [e[0] for e in events]
    y0, y1 = min(years) - 3, max(years) + 3
    ax.plot([y0, y1], [0, 0], color=NAVY, lw=2)
    for i, (yr, txt) in enumerate(events):
        up = 1 if i % 2 == 0 else -1
        ax.plot([yr, yr], [0, 0.55 * up], color=GOLD, lw=1)
        ax.plot(yr, 0, "o", color=GOLD, ms=6)
        ax.text(yr, 0.62 * up, f"{yr}\n{txt}" if up > 0 else f"{txt}\n{yr}", ha="center",
                va="bottom" if up > 0 else "top", fontsize=6.2, color=NAVY)
    if title:
        ax.set_title(title, fontsize=9, color=NAVY, weight="bold")
    ax.set_xlim(y0 - 4, y1 + 4)
    ax.set_ylim(-1.9, 1.9)
    ax.axis("off")
    _save(fig, path)


def core_cylinder(path):
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.add_patch(Ellipse((0, 3.2), 3.2, 0.9, fc="#9EC3D9", ec=NAVY, lw=1.4))
    ax.add_patch(Rectangle((-1.6, 0.4), 3.2, 2.8, fc=SAND, ec="none"))
    ax.plot([-1.6, -1.6], [0.4, 3.2], color=NAVY, lw=1.4)
    ax.plot([1.6, 1.6], [0.4, 3.2], color=NAVY, lw=1.4)
    ax.add_patch(Ellipse((0, 0.4), 3.2, 0.9, fc="#E3B7A0", ec=NAVY, lw=1.4))
    for y in (1.0, 1.6, 2.2, 2.8):
        ax.add_patch(Arc((0, y), 3.2, 0.7, theta1=180, theta2=360, ec=MAIN, lw=0.8, ls="--"))
    ax.add_patch(Rectangle((1.25, 0.6), 0.3, 2.5, fc=TEAL, alpha=0.8, ec="none"))
    lbl = [((1.7, 3.3), "Diafragma (techo)"), ((1.7, 0.3), "Suelo pélvico (base)"),
           ((-1.7, 1.8), "Transverso del abdomen\n(pared envolvente)"), ((1.7, 1.9), "Multífidos\n(pared posterior)")]
    for (x, y), t in lbl:
        ax.text(x + (0.15 if x > 0 else -0.15), y, t, ha="left" if x > 0 else "right", va="center", fontsize=7.6, color=NAVY)
    ax.text(0, 4.1, "El «cilindro» del core profundo", ha="center", fontsize=9.5, weight="bold", color=NAVY)
    ax.text(0, -0.55, "Trabajan juntos para regular la presión intraabdominal y estabilizar columna y pelvis.",
            ha="center", fontsize=6.8, color=NAVY, style="italic")
    ax.set_xlim(-4.6, 4.6)
    ax.set_ylim(-0.9, 4.4)
    _clean(ax)
    _save(fig, path)


def breathing(path):
    fig, axs = plt.subplots(1, 2, figsize=(6.2, 2.8))
    for ax, (t, w, arrows) in zip(axs, (("Inhala", 2.5, True), ("Exhala", 2.0, False))):
        ax.add_patch(Ellipse((0, 1.4), w, 2.6, fc=SAND, ec=NAVY, lw=1.5))
        for y in (0.6, 1.1, 1.6, 2.1):
            ax.add_patch(Arc((0, y + 0.3), w * 0.9, 0.7, theta1=200, theta2=340, ec=EDGE, lw=1))
        if arrows:
            for s in (1, -1):
                ax.add_patch(FancyArrowPatch((s * w / 2, 1.4), (s * (w / 2 + 0.7), 1.4), arrowstyle="-|>", mutation_scale=12, color=GOLD, lw=1.6))
        else:
            for s in (1, -1):
                ax.add_patch(FancyArrowPatch((s * (w / 2 + 0.7), 1.4), (s * w / 2, 1.4), arrowstyle="-|>", mutation_scale=12, color=TEAL, lw=1.6))
        ax.text(0, 3.0, t, ha="center", fontsize=10, weight="bold", color=NAVY)
        desc = ("Costillas se expanden hacia los\nlados y atrás; abdomen sin empujar" if arrows
                else "Costillas se cierran; ombligo hacia la\ncolumna, suelo pélvico se eleva")
        ax.text(0, -0.15, desc, ha="center", va="top", fontsize=6.8, color=NAVY)
        ax.set_xlim(-2.4, 2.4)
        ax.set_ylim(-1.2, 3.3)
        _clean(ax)
    _save(fig, path)


# ------------------------------------------------------------------ blocks
def _box3d(ax, x, y, w, h, d, col=BLOCK):
    dx, dy = d * 0.6, d * 0.4
    ax.add_patch(Polygon([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], fc=col, ec="#7A5E2E"))
    ax.add_patch(Polygon([(x, y + h), (x + w, y + h), (x + w + dx, y + h + dy), (x + dx, y + h + dy)], fc="#DCC08A", ec="#7A5E2E"))
    ax.add_patch(Polygon([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + h + dy), (x + w, y + h)], fc="#B08F52", ec="#7A5E2E"))


def blocks(path):
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    W, H, D = 2.3, 1.5, 0.75   # proporción típica 23 x 15 x 7.5 cm
    data = [("Bajo", (W, D, H), "≈ 7.5–10 cm"), ("Medio", (W, H, D), "≈ 15 cm"), ("Alto", (D, W, H), "≈ 23 cm")]
    x = 0
    for t, (w, h, d), hh in data:
        _box3d(ax, x, 0, w, h, d)
        ax.text(x + w / 2, -0.35, f"{t}\n{hh}", ha="center", va="top", fontsize=8, color=NAVY)
        x += w + 1.6
    ax.plot([-0.3, x], [0, 0], color=FLOOR, lw=1.2)
    ax.text(x / 2 - 0.5, 3.1, "Tres alturas de un mismo block (medidas de referencia de un block de yoga estándar)",
            ha="center", fontsize=7.6, color=NAVY, style="italic")
    ax.set_xlim(-0.5, x)
    ax.set_ylim(-1.4, 3.4)
    _clean(ax)
    _save(fig, path)


def feet_on_blocks(path):
    fig, axs = plt.subplots(1, 5, figsize=(7.4, 2.6))
    def blk(ax, x, y, w=0.9, h=1.5):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.03", fc=BLOCK, ec="#7A5E2E", alpha=0.9))
    data = [
        ("Un pie por block\n(paralelo)", lambda ax: (blk(ax, -0.7, 0), blk(ax, 0.7, 0), _foot(ax, -0.7, 0, 0), _foot(ax, 0.7, 0, 0))),
        ("Talones elevados\n(block bajo los talones)", lambda ax: (blk(ax, 0, -0.45, 2.4, 0.6), _foot(ax, -0.55, 0, 0), _foot(ax, 0.55, 0, 0))),
        ("Antepié sobre el\nborde (talón libre)", lambda ax: (blk(ax, 0, 0.35, 2.4, 0.7), _foot(ax, -0.55, 0, 0), _foot(ax, 0.55, 0, 0))),
        ("Escalonado\n(un pie elevado)", lambda ax: (blk(ax, 0.6, 0.5), _foot(ax, 0.6, 0.5, 0), _foot(ax, -0.6, -0.6, 0))),
        ("Block entre muslos\n(squeeze)", lambda ax: (blk(ax, 0, 0.9, 0.5, 0.9), _foot(ax, -0.5, -0.5, 0), _foot(ax, 0.5, -0.5, 0))),
    ]
    for ax, (t, fn) in zip(axs, data):
        fn(ax)
        ax.text(0, -1.45, t, ha="center", va="top", fontsize=6.8, color=NAVY)
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-2.4, 1.8)
        _clean(ax)
    _save(fig, path)


def props_sheet(path, items):
    """items: lista de (nombre, dibujador)."""
    fig, axs = plt.subplots(1, len(items), figsize=(7.2, 1.9))
    for ax, (t, d, fn) in zip(axs, items):
        fn(ax)
        ax.text(0, -1.25, t, ha="center", va="top", fontsize=7.8, weight="bold", color=NAVY)
        ax.text(0, -1.75, d, ha="center", va="top", fontsize=6.2, color=NAVY)
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-2.6, 1.4)
        _clean(ax)
    _save(fig, path)


def _db(ax):
    ax.add_patch(Rectangle((-0.6, -0.08), 1.2, 0.16, fc="#555"))
    for x in (-0.75, 0.55):
        ax.add_patch(FancyBboxPatch((x, -0.35), 0.2, 0.7, boxstyle="round,pad=0.03", fc="#3D3D3D"))


def _ball(ax):
    ax.add_patch(Circle((0, 0), 0.75, fc="#D9C9A3", ec="#8C7B57", lw=1.5))
    ax.add_patch(Arc((0, 0), 1.5, 0.5, theta1=180, theta2=360, ec="#8C7B57"))


def _band(ax):
    ax.add_patch(Ellipse((0, 0), 2.0, 0.9, fc="none", ec="#C0504D", lw=4))


def _mat(ax):
    ax.add_patch(FancyBboxPatch((-1.1, -0.35), 2.2, 0.7, boxstyle="round,pad=0.05", fc="#9FB8C8", ec=NAVY))
    ax.add_patch(Circle((1.0, 0), 0.3, fc="#7E9CB0", ec=NAVY))


def _barre(ax):
    ax.plot([-1.1, 1.1], [0.6, 0.6], color="#A88C68", lw=5, solid_capstyle="round")
    for x in (-0.8, 0.8):
        ax.plot([x, x], [-0.9, 0.6], color="#7A6A55", lw=3)
        ax.plot([x - 0.3, x + 0.3], [-0.9, -0.9], color="#7A6A55", lw=3)


def _block(ax):
    _box3d(ax, -0.8, -0.6, 1.4, 0.9, 0.6)


def _ankle(ax):
    ax.add_patch(FancyBboxPatch((-0.9, -0.25), 1.8, 0.5, boxstyle="round,pad=0.12", fc="#7E6B8F", ec="#4F4260"))


PROP_DRAW = dict(db=_db, ball=_ball, band=_band, mat=_mat, barre=_barre, block=_block, ankle=_ankle)


def music_bpm(path, rows, title):
    fig, ax = plt.subplots(figsize=(6.8, 2.4))
    for i, (name, lo, hi, col) in enumerate(rows):
        ax.barh(i, hi - lo, left=lo, color=col, alpha=0.8, height=0.55)
        ax.text(lo - 2, i, name, ha="right", va="center", fontsize=7.5, color=NAVY)
        ax.text(hi + 2, i, f"{lo}–{hi} BPM", ha="left", va="center", fontsize=7, color=NAVY)
    ax.set_yticks([])
    ax.set_xlim(40, 185)
    ax.invert_yaxis()
    ax.set_xlabel("pulsaciones por minuto de la música (BPM)", fontsize=7.5, color=NAVY)
    ax.tick_params(labelsize=7)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_title(title, fontsize=9, color=NAVY, weight="bold")
    _save(fig, path)


def eight_counts(path):
    fig, ax = plt.subplots(figsize=(7.0, 2.0))
    for phr in range(4):
        for c in range(8):
            x = phr * 8.6 + c
            col = GOLD if (phr == 3 and c >= 4) else (NAVY if c == 0 else NAVY_L)
            ax.add_patch(FancyBboxPatch((x, 0), 0.82, 0.82, boxstyle="round,pad=0.02", fc=col, ec="white"))
            ax.text(x + 0.41, 0.41, str(c + 1), ha="center", va="center", color="white", fontsize=7.5, weight="bold")
        ax.text(phr * 8.6 + 4, 1.05, f"Frase de 8 n.º {phr + 1}", ha="center", fontsize=7, color=NAVY)
    ax.annotate("Indica el siguiente ejercicio\nen «5-6-7-8»", xy=(3 * 8.6 + 6, 0), xytext=(3 * 8.6 + 6, -1.3),
                fontsize=6.8, color=GOLD, ha="center", va="top", arrowprops=dict(arrowstyle="-|>", color=GOLD))
    ax.text(0, -0.5, "Bloque musical de 32 tiempos (4 × 8). El tiempo 1 (azul oscuro) marca el inicio de cada frase.",
            fontsize=6.8, color=NAVY)
    ax.set_xlim(-0.2, 34.6)
    ax.set_ylim(-2.4, 1.4)
    _clean(ax)
    _save(fig, path)
