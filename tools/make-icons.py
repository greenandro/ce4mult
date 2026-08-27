#!/usr/bin/env python3
"""Genere les icones PWA de l'application (dossier icons/).

Usage : python tools/make-icons.py    (necessite Pillow)
"""
import os
from PIL import Image, ImageDraw

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RACINE, "icons")
S = 1024                      # rendu haute resolution, reduit ensuite
VIOLET, ROSE = (108, 92, 231), (255, 107, 157)


def degrade(taille):
    """Fond en degrade diagonal violet -> rose."""
    img = Image.new("RGB", (taille, taille))
    px = img.load()
    for y in range(taille):
        for x in range(taille):
            t = (x + y) / (2 * (taille - 1))
            px[x, y] = tuple(round(a + (b - a) * t) for a, b in zip(VIOLET, ROSE))
    return img


def croix(img, epaisseur, longueur):
    """Signe multiplier blanc, centre, avec extremites arrondies."""
    d = ImageDraw.Draw(img)
    c = img.size[0] / 2
    r = epaisseur / 2
    bras = longueur / 2 / (2 ** 0.5)          # projection sur chaque axe
    for dx in (bras, -bras):
        a = (c - dx, c - bras)
        b = (c + dx, c + bras)
        d.line([a, b], fill="white", width=round(epaisseur))
        for p in (a, b):
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="white")


def base(coins, ratio_croix):
    """Icone carree : fond degrade (coins arrondis optionnels) + croix."""
    img = degrade(S).convert("RGBA")
    croix(img, S * 0.10, S * ratio_croix)
    if coins:
        masque = Image.new("L", (S, S), 0)
        ImageDraw.Draw(masque).rounded_rectangle([0, 0, S - 1, S - 1], radius=S * 0.22, fill=255)
        img.putalpha(masque)
    return img


def ecrire(img, nom, taille, alpha=True):
    out = img.resize((taille, taille), Image.LANCZOS)
    if not alpha:
        fond = Image.new("RGB", out.size, VIOLET)
        fond.paste(out, mask=out.split()[3] if out.mode == "RGBA" else None)
        out = fond
    chemin = os.path.join(DEST, nom)
    out.save(chemin, "PNG", optimize=True)
    print(nom, out.size, os.path.getsize(chemin), "octets")


os.makedirs(DEST, exist_ok=True)
arrondie = base(coins=True, ratio_croix=0.52)     # icone classique
pleine = base(coins=False, ratio_croix=0.40)      # maskable : contenu dans la zone sure
ecrire(arrondie, "icon-192.png", 192)
ecrire(arrondie, "icon-512.png", 512)
ecrire(pleine, "icon-maskable-512.png", 512)
ecrire(pleine, "apple-touch-icon.png", 180, alpha=False)
ecrire(arrondie, "favicon-32.png", 32)
