"""Biblioteca de posturas paramétricas (vista lateral: la figura mira a la derecha
de pie; acostada o en apoyo, la cabeza queda a la izquierda)."""
import math
from engine import pose, L

ARMS = {
    "down": dict(uaN=0, faN=0),
    "front": dict(uaN=90, faN=90),
    "up": dict(uaN=175, faN=178),
    "hips": dict(uaN=-25, faN=70, uaF=-25, faF=70),
    "chest": dict(uaN=20, faN=150),
    "goblet": dict(uaN=15, faN=160),
    "curl": dict(uaN=0, faN=150),
    "press": dict(uaN=160, faN=180),
    "press0": dict(uaN=60, faN=170),
    "back": dict(uaN=-35, faN=-35),
    "cross": dict(uaN=30, faN=140),
    "head": dict(uaN=140, faN=-40),
    "row": dict(uaN=-40, faN=10),
    "tri_up": dict(uaN=170, faN=10),
    "lat": dict(uaN=90, faN=90),
}


def _arms(name):
    a = dict(ARMS[name])
    if "uaF" not in a:
        a["uaF"] = a["uaN"]
        a["faF"] = a["faN"]
    return a


def stand(arms="down", relev=False, **kw):
    p = dict(_arms(arms))
    if relev:
        p.update(ftN=25, ftF=25)
    p.update(kw)
    return pose(**p)


def squat(depth=1.0, arms="front", relev=False, **kw):
    td = 90 * depth
    p = dict(thN=td, shN=-td * 0.38, trunk=180 - td * 0.42, ftN=90)
    p.update(_arms(arms))
    if relev:
        p.update(ftN=25, shN=-td * 0.2)
    p.update(kw)
    return pose(**p)


def lunge(depth=1.0, arms="hips", back=True, **kw):
    td = 88 * depth
    p = dict(thN=td, shN=0, ftN=90, thF=-30 * depth - 8, shF=-30 * depth - 8 - 60 * depth, ftF=10, trunk=180)
    p.update(_arms(arms))
    p.update(kw)
    return pose(**p)


def split(depth=1.0, arms="hips", **kw):
    return lunge(depth, arms, **kw)


def hinge(depth=1.0, arms="down", knee=12, **kw):
    t = 180 - 75 * depth
    p = dict(trunk=t, thN=knee * depth, shN=-6 * depth, ftN=90 - 6 * depth, head=t - 10)
    p.update(_arms(arms))
    p.update(kw)
    return pose(**p)


def sl_hinge(depth=1.0, arms="down", **kw):
    t = 180 - 85 * depth
    p = dict(trunk=t, thN=10 * depth, shN=-5, ftN=88, thF=-80 * depth, shF=-80 * depth, ftF=-80 * depth + 70)
    p.update(_arms(arms))
    p.update(kw)
    return pose(**p)


def bridge(lift=1.0, arms="floor", single=False, march=False, **kw):
    tr = -90 + 25 * lift
    th = 128 - 23 * lift
    sh = 18 - 18 * lift
    p = dict(trunk=tr, head=-90, thN=th, shN=sh, ftN=90 + sh * 0.3, thF=th, shF=sh, ftF=90)
    if arms == "floor":
        p.update(uaN=90 + tr + 90, faN=90 + tr + 90)
    if single:
        p.update(thN=th, shN=th, ftN=th + 95)
    if march:
        p.update(thN=180, shN=90, ftN=170)
    p.update(kw)
    p["uaF"] = p.get("uaF", p.get("uaN", 0))
    p["faF"] = p.get("faF", p.get("faN", 0))
    return pose(**p)


def _incline(hs, foot_h=0.35, body=None):
    body = body or (L["trunk"] + L["thigh"] + L["shin"])
    return math.degrees(math.asin(max(min((hs - foot_h) / body, 0.95), -0.95)))


def plank(kind="high", **kw):
    if kind == "high":
        hs = L["uarm"] + L["farm"] + L["hand"] * 0.6
        th = _incline(hs)
        p = dict(uaN=0, faN=0)
    elif kind == "forearm":
        hs = L["uarm"] + 0.15
        th = _incline(hs)
        p = dict(uaN=0, faN=-90)
    elif kind == "bottom":
        hs = L["uarm"] * math.cos(math.radians(55)) + L["farm"] + L["hand"] * 0.6
        th = _incline(hs)
        p = dict(uaN=55, faN=0)
    elif kind == "knees":
        hs = L["uarm"] + L["farm"] + L["hand"] * 0.6
        th = _incline(hs, 0.22, L["trunk"] + L["thigh"])
        p = dict(uaN=0, faN=0)
        p.update(trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=180 - 40, ftN=180)
        p.update(kw)
        return pose(**p)
    elif kind == "knees_bottom":
        hs = L["uarm"] * math.cos(math.radians(55)) + L["farm"] + L["hand"] * 0.6
        th = _incline(hs, 0.22, L["trunk"] + L["thigh"])
        p = dict(uaN=55, faN=0, trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=140, ftN=180)
        p.update(kw)
        return pose(**p)
    elif kind == "incline":
        hs = 4.6
        th = _incline(hs)
        p = dict(uaN=-20, faN=-20)
    p.update(trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=90 - th, ftN=-15)
    p.update(kw)
    return pose(**p)


def pike(**kw):
    p = dict(trunk=-48, head=-40, thN=45, shN=45, ftN=100, uaN=-48, faN=-48)
    p.update(kw)
    return pose(**p)


def quadruped(arms="floor", **kw):
    hs = L["uarm"] + L["farm"] + L["hand"] * 0.6
    hh = L["thigh"] + 0.15
    th = math.degrees(math.asin((hs - hh) / L["trunk"]))
    p = dict(trunk=-(90 + th), head=-(90 + th), thN=0, shN=90, ftN=90, uaN=0, faN=0)
    p.update(kw)
    return pose(**p)


def bear(**kw):
    return quadruped(thN=0, shN=80, ftN=-10, **kw)


def supine(legs="bent", arms="floor", trunk=-90, head=None, **kw):
    p = dict(trunk=trunk, head=head if head is not None else trunk)
    if legs == "bent":
        p.update(thN=130, shN=20, ftN=95)
    elif legs == "table":
        p.update(thN=180, shN=90, ftN=110)
    elif legs == "straight":
        p.update(thN=90, shN=90, ftN=170)
    elif legs == "up":
        p.update(thN=180, shN=180, ftN=260)
    elif legs == "hover":
        p.update(thN=120, shN=120, ftN=210)
    if arms == "floor":
        p.update(uaN=trunk + 180, faN=trunk + 180)
    elif arms == "up":
        p.update(uaN=trunk + 90 if trunk > -90 else 180 - 0, faN=180)
    elif arms == "reach":
        p.update(uaN=trunk + 145, faN=trunk + 160)
    elif arms == "head":
        p.update(uaN=trunk - 30, faN=trunk + 150)
    elif arms == "overhead":
        p.update(uaN=trunk, faN=trunk)
    p.update(kw)
    for a, b in (("thF", "thN"), ("shF", "shN"), ("ftF", "ftN"), ("uaF", "uaN"), ("faF", "faN")):
        p.setdefault(a, p.get(b, 0))
    return pose(**p)


def crunch(legs="bent", arms="head", lift=25, **kw):
    t = -90 - lift
    return supine(legs=legs, arms=arms, trunk=t, head=t - 15, **kw)


def seated(legs="straight", arms="front", lean=0, **kw):
    t = 180 - lean
    p = dict(trunk=t, head=t)
    if legs == "straight":
        p.update(thN=90, shN=90, ftN=170)
    elif legs == "bent":
        p.update(thN=125, shN=20, ftN=95)
    elif legs == "v":
        p.update(thN=135, shN=135, ftN=215)
    p.update(_arms(arms))
    p.update(kw)
    return pose(**p)


def kneel(arms="down", **kw):
    p = dict(thN=0, shN=-90, ftN=-90)
    p.update(_arms(arms))
    p.update(kw)
    return pose(**p)


def child(**kw):
    p = dict(trunk=-65, head=-65, thN=-72, shN=90, ftN=90, uaN=-95, faN=-90)
    p.update(kw)
    return pose(**p)


def prone(arms="overhead", **kw):
    p = dict(trunk=-90, head=-95, thN=90, shN=90, ftN=90)
    if arms == "overhead":
        p.update(uaN=-90, faN=-90)
    elif arms == "side":
        p.update(uaN=90, faN=90)
    p.update(kw)
    return pose(**p)


def swan(lift=1.0, **kw):
    t = -90 - 35 * lift
    p = dict(trunk=t, head=t - 10, thN=88, shN=88, ftN=88, uaN=10, faN=-85)
    p.update(kw)
    return pose(**p)


# ---- vista frontal
def front(arms=(0, 0), legs=(0, 0), armsF=None, legsF=None, foot=90, **kw):
    ua, fa = arms
    th, sh = legs
    p = dict(view="front", trunk=180, uaN=ua, faN=fa, thN=th, shN=sh, ftN=foot)
    if armsF:
        p.update(uaF=armsF[0], faF=armsF[1])
    if legsF:
        p.update(thF=legsF[0], shF=legsF[1])
    p.update(kw)
    return pose(**p)


def plie2(depth=1.0, arms=(80, 95), **kw):
    return front(arms=arms, legs=(40 + 25 * depth, -12 * depth + 10), foot=100, **kw)


def wide(arms=(0, 0), **kw):
    return front(arms=arms, legs=(18, 12), foot=100, **kw)


def side_lunge(arms=(10, 60), **kw):
    return front(arms=arms, legs=(62, -8), legsF=(28, 28), foot=95, **kw)


def jack(open_=1.0, **kw):
    return front(arms=(30 + 140 * open_, 30 + 145 * open_), legs=(4 + 14 * open_, 4 + 14 * open_), **kw)


BALLET_ARMS = {
    "Preparatoria\n(bras bas)": dict(arms=(14, -30)),
    "Primera\nposición": dict(arms=(50, -80)),
    "Segunda\nposición": dict(arms=(78, 95)),
    "Tercera\nposición*": dict(arms=(50, -80), armsF=(78, 95)),
    "Cuarta\nposición*": dict(arms=(160, -140), armsF=(78, 95)),
    "Quinta posición\n(en haut)": dict(arms=(160, -140)),
}


def side_plank(kind="hand", top_arm="up", hips=0.0, **kw):
    """Plancha lateral vista de frente (figura rotada). hips: descenso de cadera 0..1."""
    if kind == "hand":
        rot = 69
        p = dict(uaF=70, faF=70)
    else:
        rot = 80
        p = dict(uaF=80, faF=170)
    p.update(uaN=110 if top_arm == "up" else 20, faN=110 if top_arm == "up" else 160)
    p.update(view="front", trunk=180 + 12 * hips, thN=-5.5 - 10 * hips, shN=-5.5, thF=-5.5 + 10 * hips, shF=-5.5, ftN=90, ftF=90, rot=rot)
    p.update(kw)
    return pose(**p)


def reverse_plank(hb=0.0, **kw):
    hs = L["uarm"] + L["farm"] + L["hand"] * 0.6 + hb
    th = _incline(hs, 0.3)
    p = dict(trunk=-(90 + th), head=-(90 + th) + 20, thN=90 - th, shN=90 - th, ftN=180 - th, uaN=10, faN=10)
    p.update(kw)
    return pose(**p)


def incline_push(bottom=False, **kw):
    hs = 2.1 + (L["uarm"] * math.cos(math.radians(55)) if bottom else L["uarm"]) + L["farm"] + L["hand"] * 0.6
    th = _incline(hs)
    p = dict(uaN=55 if bottom else 0, faN=0, trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=90 - th, ftN=-15)
    p.update(kw)
    return pose(**p)


def decline_push(bottom=False, **kw):
    hs = (L["uarm"] * math.cos(math.radians(55)) if bottom else L["uarm"]) + L["farm"] + L["hand"] * 0.6
    th = _incline(hs, 2.2)
    p = dict(uaN=55 if bottom else 0, faN=0, trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=90 - th, ftN=-60)
    p.update(kw)
    return pose(**p)


def russian(**kw):
    p = dict(trunk=220, head=215, thN=128, shN=55, ftN=140, uaN=40, faN=130)
    p.update(kw)
    return pose(**p)


def mod(base, **kw):
    """Copia una postura cambiando solo los segmentos indicados (sin copiar N→F)."""
    d = dict(base)
    d.update(kw)
    return d
