"""Posturas sobre el reformer (cabeza hacia las poleas; footbar en el lado de los pies o de las manos)."""
import math
from engine import pose, L
import poses as P

CH = 1.6  # altura del carro (unidades de figura)

FOOT = {"toes": 128, "arches": 150, "heels": 178, "tendon": 112}
FB_OFF = {"toes": ("TN", (0.18, -0.1)), "arches": ("AN", (0.32, 0.12)), "heels": ("HlN", (0.2, 0.0)), "tendon": ("TN", (0.15, -0.12))}


def rf(fb=None, fb_off=None, straps=None, carr=("C", "H"), box=None, box_span=None, box_h=1.2, blocks=None, pad=0.6, blocks_dx=0.0,
       fb_end="R", box_pad=0.4):
    d = {"k": "reformer", "ch": CH, "carr": carr, "pad": pad, "fb_end": fb_end, "box_pad": box_pad}
    if fb:
        d["fb"] = fb
    if fb_off:
        d["fb_off"] = fb_off
    if straps:
        d["straps"] = straps
    if box:
        d["box"] = True
        d["box_h"] = box_h
        if box_span:
            d["box_span"] = box_span
    if blocks:
        d["blocks"] = blocks
        d["blocks_dx"] = blocks_dx
    return [d]


def footwork(ext=0.0, foot="toes", single=False):
    th = 135 - 42 * ext
    sh = 45 + 48 * ext
    ft = FOOT[foot] + 25 * ext * (1 if foot == "toes" else 0)
    p = dict(trunk=-90, head=-90, thN=th, shN=sh, ftN=ft, uaN=90, faN=90, lift=CH)
    if single:
        p.update(thF=180, shF=95, ftF=150)
    return pose(**p)


def fw_props(foot="toes"):
    key, off = FB_OFF[foot]
    return rf(fb=key, fb_off=off, blocks="C", blocks_dx=0.6)


def hundred():
    return P.crunch(legs="hover", arms="floor", lift=25, uaN=95, faN=95, uaF=95, faF=95)


def lifted(p, extra=0.0):
    d = dict(p)
    d["lift"] = CH + extra
    return d


def straps_supine(th=160, sh=100, ft=150, arms=90):
    return pose(trunk=-90, head=-90, thN=th, shN=sh, ftN=ft, uaN=arms, faN=arms, lift=CH)


def stomach(ext=0.0, lean=25, hands="back"):
    t = 180 - lean
    th = 128 - 36 * ext
    sh = 40 + 52 * ext
    p = dict(trunk=t, head=t - 15, thN=th, shN=sh, ftN=128 + 20 * ext, lift=CH)
    if hands == "back":
        p.update(uaN=-15, faN=-15)
    elif hands == "reach":
        p.update(uaN=160, faN=170)
    else:
        p.update(uaN=110 - 40 * ext, faN=60 - 30 * ext)
    return pose(**p)


def short_box(back=0, flat=False):
    t = 180 + back
    return pose(trunk=t, head=t + (0 if flat else 20), thN=90, shN=90, ftN=165,
                uaN=30 if not flat else 175, faN=150 if not flat else 178, lift=CH + 1.2)


def kneel_bar(push=0.0, arch=False, knees_off=False):
    t = -110 if arch else -112
    return pose(trunk=t, head=t + (25 if arch else -30), thN=22 * push, shN=90, ftN=170, uaN=-58, faN=-58,
                lift=CH + (0.35 if knees_off else 0))


def plank_bar(push=0.0, kind="long"):
    hs = 1.4 + L["uarm"] + L["farm"] + L["hand"] * 0.6
    body = L["trunk"] + L["thigh"] + L["shin"]
    th = math.degrees(math.asin(min((hs - 0.5) / (body + 1.4 * push), 0.95)))
    p = dict(trunk=-(90 + th), head=-(90 + th), thN=90 - th, shN=90 - th, ftN=-30, uaN=-14 * push, faN=-14 * push, lift=CH)
    return pose(**p)


def elephant(push=0.0):
    return pose(trunk=-63, head=-63, thN=20 + 8 * push, shN=20 + 8 * push, ftN=100, uaN=-63, faN=-63, lift=CH)


def bridge_bar(top=True, hb=1.3):
    hip_h = 2.0 if top else 0.3
    trunk = -(90 - math.degrees(math.asin(min(hip_h / 3.0, 0.95))))
    th = 105 if top else 128
    knee_y = hip_h + L["thigh"] * (-math.cos(math.radians(th)))
    drop = knee_y - (hb + 0.05)
    sh = math.degrees(math.acos(max(min(drop / L["shin"], 1), -1)))
    return pose(trunk=trunk, head=-90, thN=th, shN=sh, ftN=150, uaN=trunk + 180, faN=trunk + 180, lift=CH)


def row_seated(phase=0, legs="straight"):
    arms = {0: (60, 150), 1: (90, 90), 2: (-35, -35), 3: (170, 175)}[phase]
    return pose(trunk=178, head=178, thN=90, shN=90, ftN=165, uaN=arms[0], faN=arms[1], lift=CH)


def prone_box(arms="pull", lift_chest=0):
    t = -90 - lift_chest
    a = {"pull": (-90, -90), "back": (60, 90), "swan": (5, -60)}[arms]
    return pose(trunk=t, head=t - 8, thN=90, shN=90, ftN=90, uaN=a[0], faN=a[1], lift=CH + 1.2)


def supine_box(teaser=False):
    if teaser:
        return pose(trunk=215, head=200, thN=135, shN=135, ftN=215, uaN=130, faN=130, lift=CH + 1.2)
    return pose(trunk=-110, head=-120, thN=150, shN=60, ftN=150, uaN=-20, faN=0, lift=CH + 1.2)


def kneel_up(lean=0, arms="down"):
    a = {"down": (0, 0), "back": (-35, -35), "front": (90, 90), "up": (175, 178)}[arms]
    return pose(trunk=180 + lean, head=180 + lean, thN=lean, shN=-90, ftN=-90, uaN=a[0], faN=a[1], lift=CH)


def short_spine(phase=0):
    if phase == 0:
        return pose(trunk=-90, head=-90, thN=150, shN=110, ftN=200, uaN=90, faN=90, lift=CH)
    if phase == 1:
        return pose(trunk=-15, head=-90, thN=-120, shN=-120, ftN=-40, uaN=90, faN=90, lift=CH)
    return pose(trunk=-20, head=-90, thN=-150, shN=-30, ftN=60, uaN=90, faN=90, lift=CH)
