# -*- coding: utf-8 -*-
"""Génère le site statique GAZTAK dans /home/claude/site.
Usage : python3 build.py            -> site complet
        python3 build.py --apercu   -> aussi un aperçu monofichier (pages FR/EN/ES)"""
import json, os, re, sys, base64, html
from urllib.parse import quote
from contenu import *

SITE = "/home/claude/site"
MAJ = "2026-10-01"

# ---------------------------------------------------------------- images
IMAGES = {
    "planche": ("planche-fromages-charcuteries-gaztak-agen", [800, 1400, 2000], (2000, 1120)),
    "plateau": ("plateau-fromages-fermiers-gaztak", [700, 1200], (1200, 1200)),
    "raclette": ("raclette-a-volonte-agen-gaztak", [700, 1170], (1170, 1170)),
}
OG = "/assets/img/gaztak-bar-a-fromages-agen-partage.jpg"
LOGO_H = "/assets/logo/gaztak-horizontal.svg"
LOGO_H_BLANC = "/assets/logo/gaztak-horizontal-blanc.svg"
LOGO_MOT = "/assets/logo/gaztak-mot-blanc.svg"
LOGO_H_RATIO = 299.65 / 153.04


def img(cle, alt, sizes, eager=False, classe=""):
    base, largeurs, (w, h) = IMAGES[cle]
    srcset = ", ".join(f"/assets/img/{base}-{l}.webp {l}w" for l in largeurs)
    src = f"/assets/img/{base}-{largeurs[-2] if len(largeurs) > 2 else largeurs[-1]}.webp"
    charge = 'fetchpriority="high"' if eager else 'loading="lazy"'
    cl = f' class="{classe}"' if classe else ""
    return (f'<img{cl} src="{src}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
            f'alt="{html.escape(alt)}" {charge} decoding="async">')


def typo(s):
    """Espaces insécables avant : ; ! ? (typographie française)."""
    for sig in (":", ";", "!", "?"):
        s = s.replace(" " + sig, "\u00a0" + sig)
    return s


def esc(s):
    return typo(html.escape(s, quote=False))


def btn_resa(L, classe, libelle):
    return (f'<a class="{classe}" href="{INFOS["resmio"]}" target="_blank" rel="noopener" data-resa>'
            f'{esc(libelle)}</a>')


ICONES = {
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h-2.5A3.5 3.5 0 0 0 9 6.5V10H6.5v3.5H9V21h3.5v-7.5H15l.5-3.5h-3V7a1 1 0 0 1 1-1H15z"/></svg>',
    "fermer": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>',
}

# ---------------------------------------------------------------- blocs communs

def entete(L, page):
    t = T[L]
    def lien(cle, libelle, href):
        cur = ' aria-current="page"' if page == cle else ""
        return f'<a href="{href}"{cur}>{esc(libelle)}</a>'
    langues = ""
    for l2 in LANGUES:
        href = ROUTES[page][l2] if page in ROUTES else ROUTES["accueil"][l2]
        cur = ' aria-current="true"' if l2 == L else ""
        langues += (f'<li><a href="{href}" hreflang="{l2}" lang="{l2}"{cur} '
                    f'aria-label="{T[l2]["nom_langue"]}">{l2.upper()}</a></li>')
    h = 62
    return f'''<a class="evitement" href="#contenu">{esc(t["evitement"])}</a>
<div class="rayures" aria-hidden="true"></div>
<header class="entete">
  <div class="wrap entete-grille">
    <a class="logo" href="{ROUTES["accueil"][L]}" aria-label="{esc(t["accueil_label"])}"><img src="{LOGO_H}" alt="GAZTAK" width="{round(h*LOGO_H_RATIO)}" height="{h}"></a>
    <nav class="nav" aria-label="{esc(t["nav_label"])}">
      {lien("carte", t["nav_carte"], ROUTES["carte"][L])}
      {lien("raclette", t["nav_raclette"], ROUTES["raclette"][L])}
      <a href="{ROUTES["accueil"][L]}#infos">{esc(t["nav_infos"])}</a>
    </nav>
    <ul class="langues" aria-label="{esc(t["langue_label"])}">{langues}</ul>
    {btn_resa(L, "btn btn-rouge btn-petit btn-entete", t["reserver"])}
  </div>
</header>'''


def pied(L):
    t = T[L]
    h = 56
    return f'''<footer class="pied">
  <div class="rayures" aria-hidden="true"></div>
  <div class="pied-fond">
    <div class="wrap pied-grille">
      <div>
        <img src="{LOGO_H_BLANC}" alt="GAZTAK" width="{round(h*LOGO_H_RATIO)}" height="{h}" loading="lazy">
        <p>{esc(t["pied_tag"])}</p>
      </div>
      <div>
        <h2 class="pied-titre">{esc(t["pied_trouver"])}</h2>
        <p>{INFOS["rue"]}<br>{INFOS["cp"]} {INFOS["ville"]}</p>
        <p><a href="tel:{INFOS["tel"]}">{t["tel_aff"]}</a><br><a href="mailto:{INFOS["email"]}">{INFOS["email"]}</a></p>
      </div>
      <div>
        <h2 class="pied-titre">{esc(t["horaires"])}</h2>
        <p>{esc(t["horaires_court"])}</p>
        <p>{esc(t["ferme_txt"])}</p>
      </div>
      <div>
        <h2 class="pied-titre">{esc(t["pied_suivre"])}</h2>
        <ul class="reseaux">
          <li><a href="{INFOS["instagram"]}" rel="noopener" target="_blank">{ICONES["instagram"]}Instagram</a></li>
          <li><a href="{INFOS["facebook"]}" rel="noopener" target="_blank">{ICONES["facebook"]}Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap pied-bas">
      <nav aria-label="{esc(t["legal_label"])}">
        <a href="/mentions-legales/" hreflang="fr">{esc(t["mentions"])}</a>
        <a href="/confidentialite/" hreflang="fr">{esc(t["confid"])}</a>
      </nav>
      <p>© SARL GAZTAK</p>
    </div>
    <p class="wrap evin" lang="fr">L’abus d’alcool est dangereux pour la santé, à consommer avec modération.</p>
  </div>
</footer>'''


def fenetre_resa(L):
    t = T[L]
    return f'''<dialog class="resa-dialog" id="resa" aria-labelledby="resa-titre">
  <div class="resa-tete">
    <h2 id="resa-titre">{esc(t["resa_titre"])}</h2>
    <button type="button" class="btn-fermer" data-fermer aria-label="{esc(t["fermer"])}">{ICONES["fermer"]}</button>
  </div>
  <iframe title="{esc(t["resa_iframe"])}" data-src="{INFOS["resmio"]}"></iframe>
  <div class="resa-pied">
    <a href="{INFOS["resmio"]}" target="_blank" rel="noopener">{esc(t["resa_secours"])}</a>
    <a href="tel:{INFOS["tel"]}">{esc(t["resa_tel"])}</a>
  </div>
</dialog>'''


def bandeau(L):
    t = T[L]
    return f'''<div class="bandeau">
  <div class="wrap bandeau-grille">
    <div><p class="etiquette">{esc(t["adresse"])}</p><p><a href="{INFOS["maps"]}" target="_blank" rel="noopener">{INFOS["rue"]}, {INFOS["cp"]} {INFOS["ville"]}</a></p></div>
    <div><p class="etiquette">{esc(t["horaires"])}</p><p>{esc(t["horaires_court"])}</p></div>
    <div><p class="etiquette">{esc(t["telephone"])}</p><p><a href="tel:{INFOS["tel"]}">{t["tel_aff"]}</a></p></div>
  </div>
</div>'''


def tableau_horaires(L):
    t = T[L]
    lignes = ""
    for i, jour in enumerate(t["jours"]):
        ouvert = 1 <= i <= 5
        val = t["heures"] if ouvert else t["ferme"]
        cl = "" if ouvert else ' class="ferme"'
        lignes += f'<tr><th scope="row">{jour}</th><td{cl}>{val}</td></tr>'
    return f'<table class="horaires"><tbody>{lignes}</tbody></table>'


def plat_html(p, L, avec_desc=True):
    det = f' <span class="plat-detail">({esc(p["detail"][L])})</span>' if p.get("detail") else ""
    desc = f'<span class="plat-desc">{esc(p["desc"][L])}</span>' if (avec_desc and p.get("desc")) else ""
    return f'<li><span class="plat-nom">{esc(p["nom"])}{det}</span>{desc}</li>'


def bloc_carte(section, L, complet=True):
    tete = f'<h3 class="pastille">{esc(section["titre"][L])}</h3>'
    if "texte" in section:
        corps = f'<p class="carte-intro">{esc(section["texte"][L])}</p>'
    else:
        intro = f'<p class="carte-intro">{esc(section["intro"][L])}</p>' if (complet and section.get("intro")) else ""
        corps = intro + '<ul class="plats">' + "".join(plat_html(p, L, complet) for p in section["plats"]) + "</ul>"
    return f'<article class="carte-bloc">{tete}{corps}</article>'


def formules_html(L):
    return '<ul class="formules">' + "".join(
        f'<li><strong>{esc(f["nom"][L])}</strong><span>{esc(f["cond"][L])}</span></li>' for f in FORMULES) + "</ul>"

# ---------------------------------------------------------------- pages

def page_accueil(L, apercu=False):
    t, c = T[L], ACCUEIL[L]
    sections = {s["id"]: s for s in CARTE}
    if apercu:
        cadre_resa = '<div class="apercu-cadre">Ici s’affichera ton module de réservation resmio (actif sur le site en ligne).</div>'
        plan = '<div class="apercu-cadre apercu-plan">Ici s’affichera le plan OpenStreetMap (actif sur le site en ligne).</div>'
    else:
        cadre_resa = f'<iframe title="{esc(t["resa_iframe"])}" src="{INFOS["resmio"]}" loading="lazy"></iframe>'
        plan = f'<iframe title="{esc(t["map_titre"])}" src="{html.escape(INFOS["osm"])}" loading="lazy" referrerpolicy="no-referrer"></iframe>'
    sujet = quote(c["privat_sujet"])
    return f'''<section class="hero">
  <div class="hero-texte">
    <h1 class="hero-titre"><img src="{LOGO_MOT}" alt="GAZTAK" width="440" height="183"><span>{esc(c["h1"])}</span></h1>
    <p>{esc(c["accroche"])}</p>
    <div class="actions">
      {btn_resa(L, "btn btn-blanc", t["reserver_table"])}
      <a class="btn btn-contour" href="{ROUTES["carte"][L]}">{esc(t["voir_carte"])}</a>
    </div>
  </div>
  <div class="hero-photo">{img("planche", c["alt_planche"], "(max-width: 1060px) 100vw, 50vw", eager=True, classe="cadre-bas")}</div>
</section>
{bandeau(L)}

<section class="section wrap">
  <div class="maison">
    <div class="maison-texte">
      <h2 class="titre-l">{esc(c["maison_h2"])}</h2>
      <p>{esc(c["maison_p"])}</p>
      <p class="mention-guide">{esc(c["guide"])}</p>
    </div>
    <div class="tuile tuile-photo">{img("plateau", c["alt_plateau"], "(max-width: 700px) 100vw, 400px")}</div>
    <div class="tuile tuile-verte">
      <p class="tuile-grand">{esc(c["terrasse"])}</p>
      <p>{esc(c["salle"])}</p>
    </div>
  </div>
</section>

<section class="section wrap">
  <div class="raclette-accueil">
    <div class="raclette-photo">{img("raclette", c["alt_raclette"], "(max-width: 960px) 100vw, 600px")}</div>
    <div class="raclette-texte">
      <h2 class="titre-xl">{esc(c["rac_h2"])}</h2>
      <p class="intro">{esc(c["rac_p"])}</p>
      {formules_html(L)}
      <div class="actions">
        <a class="btn btn-contour" href="{ROUTES["raclette"][L]}">{esc(c["rac_btn"])}</a>
        {btn_resa(L, "btn btn-rouge", t["reserver_table"])}
      </div>
    </div>
  </div>
</section>

<section class="section wrap">
  <div class="titre-ligne">
    <h2 class="titre-xl">{esc(c["carte_h2"])}</h2>
    <a class="btn btn-contour" href="{ROUTES["carte"][L]}">{esc(c["carte_btn"])}</a>
  </div>
  <p class="intro">{esc(c["carte_p"])}</p>
  <div class="cartes-grille">
    {bloc_carte(sections["planches"], L, complet=False)}
    {bloc_carte(sections["hiver"], L, complet=False)}
    {bloc_carte(sections["plaisirs"], L, complet=False)}
  </div>
</section>

<section class="section wrap" id="privatisation">
  <div class="privat">
    <div>
      <h2 class="titre-l">{esc(c["privat_h2"])}</h2>
      <p>{esc(c["privat_p"])}</p>
    </div>
    <div class="actions">
      <a class="btn btn-rouge" href="tel:{INFOS["tel"]}">{esc(c["appeler"])}</a>
      <a class="btn btn-contour" href="mailto:{INFOS["email"]}?subject={sujet}">{esc(c["ecrire"])}</a>
    </div>
  </div>
</section>

<section class="section wrap" id="reserver">
  <div class="resa-infos">
    <div class="bloc-vert">
      <h2 class="titre-xl">{esc(c["resa_h2"])}</h2>
      <p>{esc(c["resa_p"])}</p>
      <div class="resa-cadre">{cadre_resa}</div>
      <p class="petit"><a href="{INFOS["resmio"]}" target="_blank" rel="noopener">{esc(t["resa_secours"])}</a></p>
    </div>
    <div class="bloc-blanc" id="infos">
      <h2 class="titre-l">{esc(c["infos_h2"])}</h2>
      {tableau_horaires(L)}
      <p class="petit discret">{esc(t["cuisine"])}</p>
      <h3>{esc(c["venir_h3"])}</h3>
      <p><strong>{INFOS["rue"]}<br>{INFOS["cp"]} {INFOS["ville"]}</strong></p>
      <p class="discret">{esc(t["acces"])}</p>
      <p><a href="tel:{INFOS["tel"]}">{t["tel_aff"]}</a><br><a href="mailto:{INFOS["email"]}">{INFOS["email"]}</a></p>
    </div>
  </div>
  <div class="plan">
    {plan}
    <a class="btn btn-noir" href="{INFOS["maps"]}" target="_blank" rel="noopener">{esc(t["map_btn"])}</a>
  </div>
</section>'''


def page_carte(L, apercu=False):
    t, c = T[L], PAGE_CARTE[L]
    s = {x["id"]: x for x in CARTE}
    return f'''<section class="page-tete wrap">
  <div class="page-tete-grille">
    <div class="page-tete-texte">
      <h1 class="titre-xl">{esc(c["h1"])}</h1>
      <p class="intro">{esc(c["intro"])}</p>
      <div class="actions">{btn_resa(L, "btn btn-rouge", t["reserver_table"])}</div>
    </div>
    <div class="page-tete-photo">{img("plateau", ACCUEIL[L]["alt_plateau"], "(max-width: 960px) 100vw, 600px", eager=True)}</div>
  </div>
</section>

<section class="section wrap">
  <div class="carte-complete">
    {bloc_carte(s["planches"], L)}
    {bloc_carte(s["hiver"], L)}
    {bloc_carte(s["plaisirs"], L)}
    {bloc_carte(s["planchette"], L)}
    <div class="bloc-rouge">
      <div>
        <h2 class="titre-l">{esc(c["raclette_h2"])}</h2>
        <p>{esc(c["raclette_p"])}</p>
        <div class="actions"><a class="btn btn-blanc" href="{ROUTES["raclette"][L]}">{esc(c["raclette_btn"])}</a></div>
      </div>
      {formules_html(L)}
    </div>
    <div class="bloc-boissons">
      <h2>{esc(c["boissons_h2"])}</h2>
      <p>{esc(c["boissons_p"])}</p>
    </div>
  </div>
  <p class="note">{esc(c["note"])}</p>
</section>'''


def page_raclette(L, apercu=False):
    t, c = T[L], PAGE_RACLETTE[L]
    lien = f'<a href="{ROUTES["carte"][L]}">{esc(c["lien_carte"])}</a>'
    faq = "".join(
        f'<details><summary>{esc(q)}</summary><p>{esc(r).replace("{lien_carte}", lien)}</p></details>'
        for q, r in c["faq"])
    formules = "".join(
        f'<article class="carte-bloc"><h3>{esc(f["nom"][L])}</h3><p class="condition">{esc(f["cond"][L])}</p><p>{esc(f["desc"][L])}</p></article>'
        for f in FORMULES)
    reste = "".join(f"<li>{esc(x)}</li>" for x in RESTE[L])
    return f'''<section class="hero">
  <div class="hero-texte">
    <h1 class="titre-hero">{esc(c["h1"])}</h1>
    <p>{esc(c["intro"])}</p>
    <div class="actions">
      {btn_resa(L, "btn btn-blanc", t["reserver_table"])}
      <a class="btn btn-contour" href="{ROUTES["carte"][L]}">{esc(t["voir_carte"])}</a>
    </div>
  </div>
  <div class="hero-photo">{img("raclette", ACCUEIL[L]["alt_raclette"], "(max-width: 1060px) 100vw, 50vw", eager=True)}</div>
</section>
{bandeau(L)}

<section class="section wrap">
  <h2 class="titre-l">{esc(c["deux_h2"])}</h2>
  <div class="deux-col">{formules}</div>
  <div class="bloc-vert reste">
    <h2 class="titre-l">{esc(c["reste_h2"])}</h2>
    <ul class="liste">{reste}</ul>
    <p class="petit">{esc(c["note"])}</p>
  </div>
</section>

<section class="section wrap">
  <div class="faq">
    <h2 class="titre-l">{esc(c["faq_h2"])}</h2>
    {faq}
  </div>
</section>

<section class="section wrap">
  <div class="privat">
    <div>
      <h2 class="titre-l">{esc(c["cta_h2"])}</h2>
      <p>{esc(c["cta_p"])}</p>
    </div>
    <div class="actions">
      {btn_resa(L, "btn btn-rouge", t["reserver_table"])}
      <a class="btn btn-contour" href="tel:{INFOS["tel"]}">{esc(c["appeler"])}</a>
    </div>
  </div>
</section>'''


def page_legale(contenu):
    return f'<div class="wrap prose">{typo(contenu)}</div>'

# ---------------------------------------------------------------- données structurées

def adresse_ld():
    return {"@type": "PostalAddress", "streetAddress": INFOS["rue"], "postalCode": INFOS["cp"],
            "addressLocality": INFOS["ville"], "addressRegion": "Nouvelle-Aquitaine", "addressCountry": "FR"}


def ld_etablissement(L):
    return {
        "@context": "https://schema.org",
        "@type": ["Restaurant", "BarOrPub"],
        "@id": DOMAINE + "/#etablissement",
        "name": "GAZTAK",
        "alternateName": "GAZTAK – le bar à fromages d’Agen",
        "description": ACCUEIL[L]["desc"],
        "url": DOMAINE + ROUTES["accueil"][L],
        "logo": DOMAINE + "/assets/logo/gaztak-logo.png",
        "image": [DOMAINE + OG] + [DOMAINE + f"/assets/img/{IMAGES[k][0]}-{IMAGES[k][1][-1]}.webp" for k in IMAGES],
        "telephone": INFOS["tel"],
        "email": INFOS["email"],
        "address": adresse_ld(),
        "geo": {"@type": "GeoCoordinates", "latitude": INFOS["lat"], "longitude": INFOS["lon"]},
        "hasMap": INFOS["maps"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "18:00", "closes": "23:59"}],
        "servesCuisine": ["Fromages", "Charcuterie", "Raclette"],
        "acceptsReservations": INFOS["resmio"],
        "hasMenu": DOMAINE + ROUTES["carte"][L],
        "foundingDate": "2022",
        "amenityFeature": [
            {"@type": "LocationFeatureSpecification", "name": "Terrasse ouverte toute l’année", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Accès PMR", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Chiens acceptés", "value": True}],
        "sameAs": [INFOS["instagram"], INFOS["facebook"], INFOS["maps"]],
    }


def ld_menu(L):
    sections = []
    for s in CARTE:
        if "plats" in s:
            items = [{"@type": "MenuItem", "name": p["nom"], **({"description": p["desc"][L]} if p.get("desc") else {})} for p in s["plats"]]
        else:
            items = [{"@type": "MenuItem", "name": s["titre"][L], "description": s["texte"][L]}]
        sections.append({"@type": "MenuSection", "name": s["titre"][L], "hasMenuItem": items})
    sections.append({"@type": "MenuSection", "name": PAGE_CARTE[L]["raclette_h2"],
                     "hasMenuItem": [{"@type": "MenuItem", "name": f["nom"][L], "description": f["cond"][L]} for f in FORMULES]})
    return {"@context": "https://schema.org", "@type": "Menu", "name": PAGE_CARTE[L]["menu_nom"],
            "inLanguage": L, "url": DOMAINE + ROUTES["carte"][L], "hasMenuSection": sections,
            "isPartOf": {"@id": DOMAINE + "/#etablissement"}}


def ld_faq(L):
    c = PAGE_RACLETTE[L]
    return {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L,
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": r.replace("{lien_carte}", c["lien_carte"] + ".")}}
                           for q, r in c["faq"]]}

# ---------------------------------------------------------------- gabarit

def gabarit(L, page, titre, desc, corps, lds=(), canon=None, alternates=True, robots="index, follow"):
    t = T[L]
    canon = canon or (DOMAINE + ROUTES[page][L])
    alt = ""
    if alternates and page in ROUTES:
        for l2 in LANGUES:
            alt += f'<link rel="alternate" hreflang="{l2}" href="{DOMAINE + ROUTES[page][l2]}">\n'
        alt += f'<link rel="alternate" hreflang="x-default" href="{DOMAINE + ROUTES[page]["fr"]}">\n'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in lds)
    autres_locales = "".join(f'<meta property="og:locale:alternate" content="{T[l2]["locale"]}">\n' for l2 in LANGUES if l2 != L)
    return f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(titre)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
{alt}<meta property="og:type" content="website">
<meta property="og:site_name" content="GAZTAK">
<meta property="og:title" content="{html.escape(titre)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAINE + OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
{autres_locales}<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#a8322a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
{ld}<!-- Statistiques Cloudflare Web Analytics : le code sera ajouté ici lors de la mise en ligne -->
</head>
<body>
{entete(L, page)}
<main id="contenu">
{corps}
</main>
{pied(L)}
{fenetre_resa(L)}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

# ---------------------------------------------------------------- génération

def ecrire(chemin, contenu):
    f = os.path.join(SITE, chemin.lstrip("/"))
    if f.endswith("/"):
        f += "index.html"
    os.makedirs(os.path.dirname(f), exist_ok=True)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(contenu)


def pages(apercu=False):
    """Retourne la liste (langue, clé, route, html) de toutes les pages."""
    out = []
    for L in LANGUES:
        out.append((L, "accueil", ROUTES["accueil"][L], gabarit(L, "accueil", ACCUEIL[L]["title"], ACCUEIL[L]["desc"], page_accueil(L, apercu), [ld_etablissement(L)])))
        out.append((L, "carte", ROUTES["carte"][L], gabarit(L, "carte", PAGE_CARTE[L]["title"], PAGE_CARTE[L]["desc"], page_carte(L, apercu), [ld_menu(L)])))
        out.append((L, "raclette", ROUTES["raclette"][L], gabarit(L, "raclette", PAGE_RACLETTE[L]["title"], PAGE_RACLETTE[L]["desc"], page_raclette(L, apercu), [ld_faq(L)])))
    out.append(("fr", "mentions", "/mentions-legales/", gabarit("fr", "mentions", "Mentions légales | GAZTAK", "Mentions légales du site de GAZTAK, bar à fromages à Agen.", page_legale(MENTIONS), canon=DOMAINE + "/mentions-legales/", alternates=False)))
    out.append(("fr", "confid", "/confidentialite/", gabarit("fr", "confid", "Confidentialité et cookies | GAZTAK", "Politique de confidentialité du site de GAZTAK, bar à fromages à Agen.", page_legale(CONFIDENTIALITE), canon=DOMAINE + "/confidentialite/", alternates=False)))
    return out


def construire():
    for L, cle, route, contenu in pages():
        ecrire(route, contenu)
    # 404
    corps404 = f'''<div class="wrap prose">
<h1 class="titre-l">Cette page n’existe pas (ou plus).</h1>
<p>La carte, la raclette et nos horaires vous attendent sur la page d’accueil.</p>
<div class="actions" style="margin-top:24px"><a class="btn btn-rouge" href="/">Retour à l’accueil</a><a class="btn btn-contour" href="/la-carte/">Voir la carte</a></div>
<p lang="en" style="margin-top:32px">Page not found. <a href="/en/">Go to the English home page</a>.</p>
<p lang="es">Página no encontrada. <a href="/es/">Ir a la página de inicio en español</a>.</p>
</div>'''
    ecrire("/404.html", gabarit("fr", "404", "Page introuvable | GAZTAK", "Page introuvable.", corps404, canon=DOMAINE + "/", alternates=False, robots="noindex"))
    # sitemap
    urls = ""
    for cle in ROUTES:
        for L in LANGUES:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l2}" href="{DOMAINE + ROUTES[cle][l2]}"/>' for l2 in LANGUES)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{DOMAINE + ROUTES[cle]["fr"]}"/>'
            prio = "1.0" if cle == "accueil" and L == "fr" else "0.8"
            urls += f"<url><loc>{DOMAINE + ROUTES[cle][L]}</loc><lastmod>{MAJ}</lastmod><priority>{prio}</priority>{alts}</url>\n"
    for r in ("/mentions-legales/", "/confidentialite/"):
        urls += f"<url><loc>{DOMAINE + r}</loc><lastmod>{MAJ}</lastmod><priority>0.2</priority></url>\n"
    ecrire("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')
    ecrire("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAINE}/sitemap.xml\n")
    ecrire("/CNAME", "gaztak.fr\n")
    ecrire("/.nojekyll", "")

# ---------------------------------------------------------------- aperçu monofichier

def data_uri(chemin):
    f = os.path.join(SITE, chemin.lstrip("/"))
    ext = f.rsplit(".", 1)[-1]
    mime = {"webp": "image/webp", "svg": "image/svg+xml", "jpg": "image/jpeg", "png": "image/png", "woff2": "font/woff2"}[ext]
    return f"data:{mime};base64," + base64.b64encode(open(f, "rb").read()).decode()


def construire_apercu(sortie):
    css = open(os.path.join(SITE, "assets/site.css"), encoding="utf-8").read()
    css = re.sub(r"url\((/assets/fonts/[^)]+)\)", lambda m: f"url({data_uri(m.group(1))})", css)
    css += """
.apercu-cadre{flex-grow:1;min-height:320px;display:flex;align-items:center;justify-content:center;text-align:center;padding:24px;color:var(--gris);background:#fff;border-radius:16px;border:2px dashed var(--sable)}
.apercu-plan{width:100%;min-height:clamp(300px,40vw,420px);border:2px dashed var(--encre);border-radius:var(--r-bloc);background:var(--sable)}
.apercu-bandeau{background:#1d1d1b;color:#fff;font-size:.875rem;text-align:center;padding:10px 16px}
"""
    assets, corps = {}, ""
    for L, cle, route, page_html in pages(apercu=True):
        b = re.search(r"<body>(.*)</body>", page_html, re.S).group(1)
        b = re.sub(r'<script src="/assets/site.js" defer></script>', "", b)
        b = re.sub(r'<dialog class="resa-dialog".*?</dialog>', "", b, flags=re.S)
        b = b.replace('<a class="evitement" href="#contenu">', '<a class="evitement" href="#" hidden>')
        b = re.sub(r'\s(srcset|sizes)="[^"]*"', "", b)
        b = re.sub(r'\sid="contenu"', "", b)
        def rep_src(m):
            assets[m.group(1)] = data_uri(m.group(1))
            return f'data-asset="{m.group(1)}"'
        b = re.sub(r'src="(/assets/[^"]+)"', rep_src, b)
        def rep_lien(m):
            chemin, ancre = m.group(1), m.group(3)
            return f'href="#{chemin}@{ancre}"' if ancre else f'href="#{chemin}"'
        b = re.sub(r'href="(/(?!assets/)[^"#]*)(#([^"]*))?"', rep_lien, b)
        corps += f'<div class="apercu-page" data-route="{route}" data-lang="{L}" hidden>{b}</div>\n'
    js = """
(function(){
  var A=%s;
  document.querySelectorAll('img[data-asset]').forEach(function(i){i.src=A[i.getAttribute('data-asset')];});
  var pages=[].slice.call(document.querySelectorAll('.apercu-page'));
  function voir(){
    var h=decodeURIComponent(location.hash.slice(1))||'/'; var p=h.split('@'); var route=p[0], ancre=p[1];
    var page=pages.filter(function(x){return x.getAttribute('data-route')===route;})[0]||pages[0];
    pages.forEach(function(x){x.hidden=(x!==page);});
    document.documentElement.lang=page.getAttribute('data-lang');
    var cible=ancre?page.querySelector('#'+ancre):null;
    if(cible){cible.scrollIntoView();}else{window.scrollTo(0,0);}
  }
  window.addEventListener('hashchange',voir); voir();
  var d=document.getElementById('apercu-resa');
  document.addEventListener('click',function(e){var a=e.target.closest('[data-resa]'); if(a){e.preventDefault(); d.showModal();}});
  d.querySelector('button').addEventListener('click',function(){d.close();});
})();
""" % json.dumps(assets)
    doc = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>GAZTAK – aperçu du site</title>
<style>{css}</style>
</head>
<body>
<div class="apercu-bandeau">Aperçu du site GAZTAK. Les liens, les langues et les boutons fonctionnent ; le module resmio et le plan s’activeront sur le site en ligne.</div>
{corps}
<dialog class="resa-dialog" id="apercu-resa" aria-labelledby="apercu-resa-titre">
  <div class="resa-tete"><h2 id="apercu-resa-titre">Réserver une table</h2><button type="button" class="btn-fermer" aria-label="Fermer">{ICONES["fermer"]}</button></div>
  <p style="padding:28px 22px 32px">Sur le site en ligne, ce bouton ouvre ton module de réservation resmio dans cette fenêtre, sans quitter le site.</p>
</dialog>
<script>{js}</script>
</body>
</html>'''
    with open(sortie, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return len(doc)


if __name__ == "__main__":
    construire()
    if "--apercu" in sys.argv:
        n = construire_apercu("/mnt/user-data/outputs/gaztak-apercu.html")
        print("aperçu :", round(n / 1024), "Ko")
    print("ok")
