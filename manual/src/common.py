"""Bloques de contenido del manual (se serializan a JSON para el maquetador)."""
import re
import unicodedata

from engine import MUSCLES


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:60]


def H(text, level=4):
    return {"t": "h", "l": level, "x": text}


def T(*texts):
    return [{"t": "p", "x": t} for t in texts]


def UL(*items):
    return {"t": "ul", "items": list(items)}


def OL(*items):
    return {"t": "ol", "items": list(items)}


def TBL(head, rows, widths=None, caption=None, small=False):
    return {"t": "table", "head": head, "rows": rows, "widths": widths, "caption": caption, "small": small}


def FIG(name, caption, width=6.3):
    return {"t": "fig", "name": name, "caption": caption, "width": width}


def BOX(kind, title, *content):
    """kind: general | oficial | seguridad | cue | tip | practica"""
    body = []
    for c in content:
        body.append(c if isinstance(c, dict) else {"t": "p", "x": c})
    return {"t": "box", "kind": kind, "title": title, "body": body}


def OFICIAL(tema, *items):
    return BOX("oficial", "Requiere material oficial TBM",
               f"Este libro no reproduce ni inventa contenido propietario del método TBM sobre «{tema}». "
               "Completa estos puntos con el manual, los videos o la capacitación oficial:",
               UL(*items))


def EX(name, *, en=None, level="Principiante", frames, prim, sec=(), extra=None, obj, start, steps,
       breath, errors, regress, progress, dose, cue, props=None):
    return {"t": "ex", "name": name, "en": en, "level": level, "frames": frames,
            "prim": list(prim), "sec": list(sec), "extra": extra, "obj": obj, "start": start,
            "steps": steps, "breath": breath, "errors": errors, "regress": regress,
            "progress": progress, "dose": dose, "cue": cue, "props": props,
            "prim_txt": ", ".join(MUSCLES[m] for m in prim),
            "sec_txt": ", ".join([MUSCLES[m] for m in sec] + ([extra] if extra else []))}


def F(p, label="", props=None):
    return {"p": p, "label": label, "props": props or []}


def Q(q, opts=None, a=None, why=""):
    return {"q": q, "opts": opts, "a": a, "why": why}


def topic(title, *blocks):
    out = []
    for b in blocks:
        if isinstance(b, list):
            out.extend(b)
        else:
            out.append(b)
    return {"title": title, "blocks": out}


def module(num, title, objectives, topics, quiz, intro=None):
    return {"num": num, "title": title, "objectives": objectives, "topics": topics, "quiz": quiz, "intro": intro}


def GALLERY(name, caption, items, per_row=4, width=6.3):
    """items: lista de (pose, etiqueta[, props]). Se renderiza como figura."""
    return {"t": "gallery", "name": name, "caption": caption, "items": items, "per_row": per_row, "width": width}
