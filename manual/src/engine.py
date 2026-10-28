"""Motor gráfico del manual: mapas musculares y figuras de ejercicios.

Convención de ángulos (grados, absolutos): 0 = hacia abajo, 90 = hacia
adelante (+x), 180 = hacia arriba, -90 = hacia atrás (-x).
"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Circle, Rectangle, FancyArrowPatch, FancyBboxPatch

NAVY = "#1F3A5F"
NAVY_L = "#9AAFC4"
GOLD = "#B08D57"
MAIN = "#B5452F"
SEC = "#E9A77F"
BASE = "#E4DED6"
SKIN = "#F3EFE9"
EDGE = "#8F877D"
FLOOR = "#B9B2A8"
PROP = "#6E8B74"
BLOCK = "#C9A86A"

plt.rcParams["font.family"] = "DejaVu Sans"

# ---------------------------------------------------------------- nombres
MUSCLES = {
    "cuad": "Cuádriceps", "glmax": "Glúteo mayor", "glmed": "Glúteo medio y menor",
    "isq": "Isquiotibiales", "adu": "Aductores", "gem": "Gemelos y sóleo",
    "tib": "Tibial anterior", "fc": "Flexores de cadera (iliopsoas)",
    "ra": "Recto abdominal", "obl": "Oblicuos", "ta": "Transverso del abdomen",
    "ere": "Erectores espinales", "pec": "Pectoral mayor", "delA": "Deltoides anterior",
    "delM": "Deltoides medio", "delP": "Deltoides posterior", "bic": "Bíceps braquial",
    "tri": "Tríceps braquial", "ant": "Flexores/extensores del antebrazo",
    "trap": "Trapecio", "rom": "Romboides", "dor": "Dorsal ancho",
    "ser": "Serrato anterior",
}


def muscle_names(ids):
    return ", ".join(MUSCLES[i] for i in ids)


# ---------------------------------------------------------------- mapa muscular
def _sym(shape_fn, side_shapes):
    out = []
    for s in (1, -1):
        out.append(shape_fn(s))
    return out


def _poly(pts, s):
    return [(s * x, y) for x, y in pts]


def body_silhouette(ax, cx):
    kw = dict(color=SKIN, solid_capstyle="round", zorder=1)
    ax.add_patch(Circle((cx, 16.7), 0.95, fc=SKIN, ec=EDGE, lw=0.8, zorder=1))
    ax.plot([cx, cx], [15.7, 15.2], lw=10, **kw)
    torso = [(-2.55, 14.75), (2.55, 14.75), (1.9, 11.6), (1.75, 10.3), (2.15, 9.1),
             (1.6, 8.2), (0.15, 8.0), (-0.15, 8.0), (-1.6, 8.2), (-2.15, 9.1), (-1.75, 10.3), (-1.9, 11.6)]
    ax.add_patch(Polygon([(cx + x, y) for x, y in torso], closed=True, fc=SKIN, ec=EDGE, lw=0.8, zorder=1))
    for s in (1, -1):
        ax.plot([cx + s * 2.6, cx + s * 2.95, cx + s * 3.25], [14.3, 11.4, 8.9], lw=14, **kw)
        ax.plot([cx + s * 3.25, cx + s * 3.35], [8.9, 8.2], lw=10, **kw)
        ax.plot([cx + s * 1.15, cx + s * 1.15, cx + s * 1.1], [8.6, 4.9, 1.0], lw=22, **kw)
        ax.plot([cx + s * 1.1, cx + s * 1.25], [1.0, 0.45], lw=12, **kw)


def _muscle_shapes(view):
    """Devuelve lista (id, factory(s)->patch_args) para cada vista."""
    E = lambda x, y, w, h, a=0: ("E", (x, y, w, h, a))
    P = lambda pts: ("P", pts)
    if view == "front":
        return [
            ("delA", E(2.55, 14.0, 1.05, 1.55, 15)),
            ("delM", E(3.0, 13.7, 0.5, 1.3, 10)),
            ("pec", P([(0.12, 14.25), (2.15, 14.15), (2.05, 12.75), (1.1, 12.3), (0.12, 12.45)])),
            ("ser", E(1.85, 11.95, 0.45, 1.05, -10)),
            ("bic", E(2.82, 12.75, 0.78, 2.1, 6)),
            ("ant", E(3.12, 10.15, 0.62, 2.05, 6)),
            ("obl", P([(0.75, 12.0), (1.75, 11.6), (1.85, 9.7), (0.75, 9.35)])),
            ("ra", P([(-0.65, 12.25), (0.65, 12.25), (0.62, 9.25), (-0.62, 9.25)])),
            ("fc", P([(0.55, 9.15), (1.45, 9.05), (1.0, 8.15), (0.45, 8.35)])),
            ("cuad", E(1.33, 6.75, 1.25, 3.55, 3)),
            ("adu", P([(0.2, 8.25), (0.75, 8.2), (0.72, 5.9), (0.42, 6.6)])),
            ("tib", E(1.32, 3.0, 0.45, 2.55, 2)),
        ]
    return [
        ("trap", P([(0, 15.55), (2.3, 14.45), (1.2, 13.5), (0.35, 11.0), (0, 10.75)])),
        ("delP", E(2.55, 14.0, 1.05, 1.55, -15)),
        ("delM", E(3.0, 13.7, 0.5, 1.3, -10)),
        ("rom", P([(0.25, 13.95), (1.25, 13.45), (1.0, 12.4), (0.25, 12.0)])),
        ("dor", P([(0.95, 12.35), (2.05, 13.2), (1.85, 10.9), (0.7, 9.85), (0.55, 10.6)])),
        ("tri", E(2.82, 12.75, 0.78, 2.1, -6)),
        ("ant", E(3.12, 10.15, 0.62, 2.05, -6)),
        ("ere", P([(0.12, 12.6), (0.55, 12.6), (0.6, 9.4), (0.12, 9.4)])),
        ("glmed", E(1.55, 9.05, 0.95, 0.9, 20)),
        ("glmax", E(0.98, 8.35, 1.65, 1.55, -8)),
        ("isq", E(1.18, 6.45, 1.1, 3.1, 2)),
        ("adu", P([(0.2, 7.6), (0.6, 7.5), (0.62, 5.9), (0.35, 6.4)])),
        ("gem", E(1.18, 3.55, 0.98, 2.2, 0)),
    ]


def muscle_map(ax, cx, view, prim=(), sec=(), labels=False, title=None):
    body_silhouette(ax, cx)
    placed = {}
    for mid, (kind, args) in _muscle_shapes(view):
        col = MAIN if mid in prim else SEC if mid in sec else BASE
        for s in (1, -1):
            if kind == "E":
                x, y, w, h, a = args
                patch = Ellipse((cx + s * x, y), w, h, angle=s * a, fc=col, ec=EDGE, lw=0.6, zorder=3)
                c = (cx + s * x, y)
            else:
                pts = [(cx + s * x, y) for x, y in args]
                patch = Polygon(pts, closed=True, fc=col, ec=EDGE, lw=0.6, zorder=3)
                c = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
            ax.add_patch(patch)
            placed.setdefault(mid, []).append(c)
    if view == "front":
        for y in (11.5, 10.75, 10.0):
            ax.plot([cx - 0.6, cx + 0.6], [y, y], color=EDGE, lw=0.5, zorder=4)
        ax.plot([cx, cx], [9.3, 12.2], color=EDGE, lw=0.5, zorder=4)
        if "ta" in prim or "ta" in sec:
            col = MAIN if "ta" in prim else SEC
            ax.add_patch(Ellipse((cx, 9.9), 3.3, 1.2, fc="none", ec=col, lw=2.2, ls="--", zorder=5))
    if title:
        ax.text(cx, -0.6, title, ha="center", va="top", fontsize=8, color=NAVY)
    return placed


def anatomy_chart(path):
    fig, ax = plt.subplots(figsize=(7.2, 6.6), dpi=200)
    lf = muscle_map(ax, 0, "front")
    lb = muscle_map(ax, 9, "back")
    front_lbl = [("delA", "Deltoides anterior", -1), ("pec", "Pectoral mayor", -1), ("bic", "Bíceps", -1),
                 ("ser", "Serrato anterior", -1), ("ant", "Antebrazo", -1), ("ra", "Recto abdominal", -1),
                 ("obl", "Oblicuos", -1), ("fc", "Flexores de cadera", -1), ("adu", "Aductores", -1),
                 ("cuad", "Cuádriceps", -1), ("tib", "Tibial anterior", -1)]
    back_lbl = [("trap", "Trapecio", 1), ("delP", "Deltoides posterior", 1), ("rom", "Romboides", 1),
                ("tri", "Tríceps", 1), ("dor", "Dorsal ancho", 1), ("ere", "Erectores espinales", 1),
                ("glmed", "Glúteo medio", 1), ("glmax", "Glúteo mayor", 1), ("isq", "Isquiotibiales", 1),
                ("gem", "Gemelos / sóleo", 1)]
    for placed, lbls, cx in ((lf, front_lbl, 0), (lb, back_lbl, 9)):
        used = {1: [], -1: []}
        for mid, txt, side in lbls:
            pts = placed[mid]
            p = max(pts, key=lambda q: q[0]) if side == 1 else min(pts, key=lambda q: q[0])
            ty = p[1]
            while any(abs(ty - u) < 0.8 for u in used[side]):
                ty -= 0.45
            used[side].append(ty)
            tx = cx + side * 4.6
            ax.annotate(txt, xy=p, xytext=(tx, ty), fontsize=7.2, color=NAVY,
                        ha="left" if side == 1 else "right", va="center",
                        arrowprops=dict(arrowstyle="-", color=GOLD, lw=0.6))
    ax.text(0, 18.3, "VISTA ANTERIOR", ha="center", fontsize=9, weight="bold", color=NAVY)
    ax.text(9, 18.3, "VISTA POSTERIOR", ha="center", fontsize=9, weight="bold", color=NAVY)
    ax.set_xlim(-12, 21)
    ax.set_ylim(-0.5, 19)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


# ---------------------------------------------------------------- figura humana
L = dict(trunk=3.0, neck=0.3, head=0.48, thigh=2.2, shin=2.1, foot=0.75,
         uarm=1.45, farm=1.35, hand=0.25, hipw=0.42, shw=0.85)


def d(a):
    r = math.radians(a)
    return (math.sin(r), -math.cos(r))


def add(p, a, l):
    v = d(a)
    return (p[0] + v[0] * l, p[1] + v[1] * l)


STAND = dict(view="side", trunk=180, head=None, thN=0, shN=0, ftN=90, thF=0, shF=0, ftF=90,
             uaN=0, faN=0, uaF=0, faF=0)


def pose(**kw):
    p = dict(STAND)
    p.update(kw)
    for a, b in (("thF", "thN"), ("shF", "shN"), ("ftF", "ftN"), ("uaF", "uaN"), ("faF", "faN")):
        if a not in kw and b in kw:
            p[a] = kw[b]
    return p


def skeleton(p):
    H = (0.0, 0.0)
    if p["view"] == "side":
        S = add(H, p["trunk"], L["trunk"])
        hd = p["head"] if p["head"] is not None else p["trunk"]
        N = add(S, hd, L["neck"])
        C = add(N, hd, L["head"])
        sides = {}
        for k in ("N", "F"):
            K = add(H, p["th" + k], L["thigh"])
            A = add(K, p["sh" + k], L["shin"])
            T = add(A, p["ft" + k], L["foot"])
            Hl = add(A, p["ft" + k] + 180, 0.22)
            E = add(S, p["ua" + k], L["uarm"])
            W = add(E, p["fa" + k], L["farm"])
            Hd = add(W, p["fa" + k], L["hand"])
            sides[k] = dict(hip=H, K=K, A=A, T=T, Hl=Hl, sh=S, E=E, W=W, Hd=Hd)
        return dict(H=H, S=S, N=N, C=C, sides=sides)
    # vista frontal: N = derecha de la imagen, F = izquierda (espejo)
    S = add(H, p["trunk"], L["trunk"])
    hd = p["head"] if p["head"] is not None else p["trunk"]
    N = add(S, hd, L["neck"])
    C = add(N, hd, L["head"])
    sides = {}
    for k, s in (("N", 1), ("F", -1)):
        hip = (H[0] + s * L["hipw"], H[1])
        sh = (S[0] + s * L["shw"], S[1])
        ang = lambda key: s * p[key + k]
        K = add(hip, ang("th"), L["thigh"])
        A = add(K, ang("sh"), L["shin"])
        T = add(A, ang("ft"), 0.45)
        Hl = A
        E = add(sh, ang("ua"), L["uarm"])
        W = add(E, ang("fa"), L["farm"])
        Hd = add(W, ang("fa"), L["hand"])
        sides[k] = dict(hip=hip, K=K, A=A, T=T, Hl=Hl, sh=sh, E=E, W=W, Hd=Hd)
    return dict(H=H, S=S, N=N, C=C, sides=sides)


def _rotate(sk, deg):
    if not deg:
        return sk
    a = math.radians(deg)
    R = lambda q: (q[0] * math.cos(a) - q[1] * math.sin(a), q[0] * math.sin(a) + q[1] * math.cos(a))
    out = dict(H=R(sk["H"]), S=R(sk["S"]), N=R(sk["N"]), C=R(sk["C"]), sides={})
    for k, v in sk["sides"].items():
        out["sides"][k] = {kk: R(vv) for kk, vv in v.items()}
    return out


def _all_points(sk):
    pts = [sk["H"], sk["S"], (sk["C"][0], sk["C"][1] - L["head"])]
    for s in sk["sides"].values():
        pts += [s["K"], s["A"], s["T"], s["Hl"], s["Hd"], s["E"], s["W"]]
    # tronco
    for i in range(1, 5):
        t = i / 5
        pts.append((sk["H"][0] + (sk["S"][0] - sk["H"][0]) * t, sk["H"][1] + (sk["S"][1] - sk["H"][1]) * t))
    pts.append((sk["C"][0], sk["C"][1] - L["head"]))
    return pts


LW = 0.22  # radio aproximado de los segmentos en unidades


def draw_figure(ax, p, x0=0.0, floor=0.0, props=None, color=NAVY, far=NAVY_L, scale=1.0):
    """Dibuja la figura apoyada en el suelo. props: lista de dicts."""
    props = props or []
    sk = _rotate(skeleton(p), p.get("rot", 0))
    lift = p.get("lift", 0.0)
    miny = min(q[1] for q in _all_points(sk)) - LW
    dx, dy = x0, floor + lift - miny
    T = lambda q: (q[0] + dx, q[1] + dy)
    lw = 5.6 * scale

    def seg(pts, c, w=lw, z=5):
        xs = [T(q)[0] for q in pts]
        ys = [T(q)[1] for q in pts]
        ax.plot(xs, ys, color=c, lw=w, solid_capstyle="round", solid_joinstyle="round", zorder=z)

    order = ("F", "N")
    for k in order:
        s = sk["sides"][k]
        c = far if (k == "F" and p["view"] == "side") else color
        z = 3 if (k == "F" and p["view"] == "side") else 7
        seg([s["hip"], s["K"], s["A"]], c, z=z)
        seg([s["Hl"], s["A"], s["T"]] if p["view"] == "side" else [s["A"], s["T"]], c, w=lw * 0.75, z=z)
    # tronco
    if p["view"] == "side":
        seg([sk["H"], sk["S"]], color, w=lw * 1.65, z=5)
    else:
        hipN, hipF = sk["sides"]["N"]["hip"], sk["sides"]["F"]["hip"]
        shN, shF = sk["sides"]["N"]["sh"], sk["sides"]["F"]["sh"]
        poly = [T(hipF), T(hipN), T(shN), T(shF)]
        ax.add_patch(Polygon(poly, closed=True, fc=color, ec=color, lw=lw * 0.9, joinstyle="round", zorder=5))
    seg([sk["S"], sk["N"]], color, w=lw * 0.8, z=5)
    c = T(sk["C"])
    ax.add_patch(Circle(c, L["head"], fc=color, ec=color, zorder=6))
    for k in order:
        s = sk["sides"][k]
        cc = far if (k == "F" and p["view"] == "side") else color
        z = 4 if (k == "F" and p["view"] == "side") else 8
        seg([s["sh"], s["E"], s["W"], s["Hd"]], cc, w=lw * 0.8, z=z)
    pts = {"C": c}
    for k in ("N", "F"):
        for key, val in sk["sides"][k].items():
            pts[key + k] = T(val)
    pts["H"] = T(sk["H"])
    pts["S"] = T(sk["S"])
    for pr in props:
        draw_prop(ax, pr, pts, floor, color)
    xs = [q[0] for q in pts.values()]
    ys = [q[1] for q in pts.values()]
    return min(xs), max(xs), max(ys), pts


def draw_prop(ax, pr, pts, floor, color):
    kind = pr["k"]
    if kind == "db":
        for key in pr.get("at", ["HdN", "HdF"]):
            x, y = pts[key]
            ax.add_patch(FancyBboxPatch((x - 0.32, y - 0.12), 0.64, 0.24, boxstyle="round,pad=0.04",
                                        fc="#3D3D3D", ec="#3D3D3D", zorder=9 if key.endswith("N") else 4))
    elif kind == "ball":
        x, y = pts[pr["at"]]
        ox, oy = pr.get("off", (0, 0))
        ax.add_patch(Circle((x + ox, y + oy), pr.get("r", 0.42), fc="#D9C9A3", ec="#8C7B57", lw=1, zorder=pr.get("z", 9)))
    elif kind == "block":
        x, y = pr["xy"] if "xy" in pr else pts[pr["at"]]
        w, h = pr.get("w", 1.1), pr.get("h", 0.55)
        ox, oy = pr.get("ox", 0), pr.get("oy", 0)
        if pr.get("center"):
            y0 = y + oy - h / 2
        elif pr.get("to"):
            h = y - floor - pr.get("gap", 0.12)
            y0 = floor
        else:
            y0 = floor if pr.get("ground", True) else y - h
        ax.add_patch(Rectangle((x - w / 2 + ox, y0), w, h, fc=BLOCK, ec="#8C6E3A", lw=1, zorder=pr.get("z", 2)))
    elif kind == "barre":
        x, y = pts[pr.get("at", "HdN")]
        x += pr.get("ox", 0.1)
        ax.plot([x, x], [floor, y - 0.1], color="#7A6A55", lw=3, zorder=1)
        ax.plot([x - 0.35, x + 0.35], [floor, floor], color="#7A6A55", lw=3, zorder=1)
        ax.add_patch(Circle((x, y - 0.05), 0.2, fc="#A88C68", ec="#7A6A55", zorder=2))
    elif kind == "band":
        a, b = pts[pr["a"]], pts[pr["b"]]
        ax.plot([a[0], b[0]], [a[1], b[1]], color="#C0504D", lw=2, zorder=9)
    elif kind == "wall":
        x = pts[pr.get("at", "H")][0] + pr.get("ox", -0.45)
        ax.plot([x, x], [floor, floor + 9.5], color="#9C8A74", lw=4, zorder=1)
    elif kind == "chair":
        if "at" in pr:
            x = pts[pr["at"]][0] + pr.get("ox", 0)
            h = pts[pr["at"]][1] - floor - 0.12
        else:
            x, h = pr["x"], pr.get("h", 2.1)
        w = pr.get("w", 1.6)
        ax.add_patch(Rectangle((x - w / 2, floor + h - 0.18), w, 0.18, fc="#9C8466", ec="#6B5A44", zorder=1))
        for xx in (x - w / 2 + 0.1, x + w / 2 - 0.1):
            ax.plot([xx, xx], [floor, floor + h - 0.18], color="#6B5A44", lw=2.5, zorder=1)
    elif kind == "arrow":
        a = pts[pr["at"]] if isinstance(pr["at"], str) else pr["at"]
        dx, dy = pr["d"]
        ax.add_patch(FancyArrowPatch(a, (a[0] + dx, a[1] + dy), arrowstyle="-|>", mutation_scale=12,
                                     color=GOLD, lw=1.6, zorder=12))


def draw_floor(ax, x0, x1, floor=0.0, mat=True):
    ax.plot([x0, x1], [floor, floor], color=FLOOR, lw=1.5, zorder=0)
    if mat:
        ax.add_patch(Rectangle((x0 + 0.3, floor - 0.12), x1 - x0 - 0.6, 0.12, fc="#D8E1E8", ec="none", zorder=0))


# ---------------------------------------------------------------- ficha de ejercicio
def exercise_figure(path, frames, prim=(), sec=(), dpi=170):
    """frames: lista de dicts {p: pose, props: [...], label: str}."""
    n = len(frames)
    if n == 0:
        fig = plt.figure(figsize=(2.6, 2.35), dpi=dpi)
        axm = fig.add_axes([0, 0, 1, 1])
        _maps(axm, prim, sec)
        fig.savefig(path, bbox_inches="tight", pad_inches=0.04)
        plt.close(fig)
        return
    fig = plt.figure(figsize=(6.6, 2.35), dpi=dpi)
    wpose = 0.66
    axp = fig.add_axes([0.0, 0.02, wpose, 0.96])
    x = 0.0
    labels = []
    allmax = 0
    for i, fr in enumerate(frames):
        # medir
        tmp = plt.figure()
        ta = tmp.add_subplot(111)
        xmin, xmax, top, _ = draw_figure(ta, fr["p"], props=fr.get("props"))
        plt.close(tmp)
        ox = x - xmin + 0.8
        xmin, xmax, top, pts = draw_figure(axp, fr["p"], x0=ox, props=fr.get("props"))
        allmax = max(allmax, top)
        labels.append(((xmin + xmax) / 2, fr.get("label", "")))
        if i < n - 1:
            axp.add_patch(FancyArrowPatch((xmax + 0.45, 2.2), (xmax + 1.65, 2.2), arrowstyle="-|>",
                                          mutation_scale=16, color=GOLD, lw=2, zorder=10))
        x = xmax + 1.3
    draw_floor(axp, -0.2, x + 0.6)
    for cx, t in labels:
        if t:
            axp.text(cx, -0.55, t, ha="center", va="top", fontsize=7.5, color=NAVY, style="italic")
    axp.set_xlim(-0.4, max(x + 0.8, 9))
    top = max(allmax + 0.4, 6.5)
    axp.set_ylim(-1.2, top)
    axp.set_aspect("equal", adjustable="box")
    axp.axis("off")
    axm = fig.add_axes([wpose + 0.01, 0.0, 1 - wpose - 0.01, 1.0])
    _maps(axm, prim, sec)
    fig.savefig(path, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


def _maps(axm, prim, sec):
    muscle_map(axm, 0, "front", prim, sec)
    muscle_map(axm, 8.2, "back", prim, sec)
    axm.text(0, -0.55, "Anterior", ha="center", va="top", fontsize=6.5, color=NAVY)
    axm.text(8.2, -0.55, "Posterior", ha="center", va="top", fontsize=6.5, color=NAVY)
    axm.add_patch(Rectangle((-3.7, 18.1), 0.6, 0.45, fc=MAIN, ec=EDGE, lw=0.4))
    axm.text(-2.95, 18.32, "principal", fontsize=6.2, va="center", color=NAVY)
    axm.add_patch(Rectangle((2.4, 18.1), 0.6, 0.45, fc=SEC, ec=EDGE, lw=0.4))
    axm.text(3.15, 18.32, "secundario / estabilizador", fontsize=6.2, va="center", color=NAVY)
    axm.set_xlim(-4.0, 12.2)
    axm.set_ylim(-1.3, 18.9)
    axm.set_aspect("equal")
    axm.axis("off")


def pose_gallery(path, items, per_row=4, cell=(1.75, 1.55)):
    """items: lista de (pose, etiqueta, props)."""
    import math as _m
    rows = _m.ceil(len(items) / per_row)
    fig, axs = plt.subplots(rows, per_row, figsize=(cell[0] * per_row, cell[1] * rows))
    axs = list(axs.flat) if hasattr(axs, "flat") else [axs]
    for ax in axs:
        ax.axis("off")
    for ax, it in zip(axs, items):
        p, label = it[0], it[1]
        props = it[2] if len(it) > 2 else None
        xmin, xmax, top, _ = draw_figure(ax, p, props=props)
        cx = (xmin + xmax) / 2
        span = max(xmax - xmin, top, 7.5) / 2 + 0.6
        draw_floor(ax, cx - span, cx + span)
        ax.set_xlim(cx - span, cx + span)
        ax.set_ylim(-1.6, max(top + 0.4, 2 * span - 1.6))
        ax.set_aspect("equal")
        ax.text(cx, -0.45, label, ha="center", va="top", fontsize=7.2, color=NAVY)
    fig.tight_layout(pad=0.3)
    fig.savefig(path, dpi=170, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
