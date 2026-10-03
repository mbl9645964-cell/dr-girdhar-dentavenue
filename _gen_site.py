#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dr. Girdhar's DentAvenue — Faridabad — from-scratch static site generator."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/"

PHONE_DISPLAY = "+91 88261 25929"
PHONE_TEL = "tel:+918826125929"
WA_NUM = "918826125929"
def wa(msg):
    import urllib.parse
    return f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}"
WA_BOOK = wa("Hello Dr. Girdhar's DentAvenue, I would like to book an appointment.")
WA_CHAT = wa("Hello Dr. Girdhar's DentAvenue, how can I help you?")
EMAIL = "dentavenuefaridabad@gmail.com"
CITY = "Faridabad, Haryana"
HOURS_1 = "Mon–Sat · 5:00 pm – 9:00 pm"
HOURS_2 = "Sunday · 10:00 am – 2:00 pm"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("doctors.html", "Doctors"),
    ("treatments.html", "Treatments"),
    ("clinic.html", "Clinic"),
    ("contact.html", "Contact"),
]

def ic(path, size=18):
    return f'<svg class="ic" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

I_PHONE = ic('<path d="M6.5 3h3l1.5 5-2 1.5a12 12 0 0 0 5.5 5.5L16 18l5 1.5v3a1 1 0 0 1-1.1 1A18 18 0 0 1 3.5 6.1 1 1 0 0 1 4.5 5"/>')
I_WA = '<svg class="ic" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.29-.14-1.7-.84-1.96-.94-.26-.1-.45-.14-.64.15-.19.29-.74.94-.91 1.13-.17.19-.34.21-.62.07-.29-.14-1.21-.45-2.3-1.42-.85-.76-1.42-1.7-1.59-1.98-.17-.29-.02-.44.13-.58.13-.13.29-.34.43-.51.14-.17.19-.29.29-.48.1-.19.05-.36-.02-.51-.07-.14-.64-1.55-.88-2.12-.23-.55-.47-.48-.64-.48h-.55c-.19 0-.5.07-.76.36-.26.29-1 .98-1 2.38 0 1.4 1.02 2.76 1.17 2.95.14.19 2.01 3.08 4.88 4.32.68.29 1.21.47 1.63.6.68.22 1.31.19 1.8.12.55-.08 1.7-.69 1.94-1.36.24-.67.24-1.24.17-1.36-.07-.12-.26-.19-.55-.33z"/><path d="M12 .9C5.87.9.9 5.87.9 12c0 1.95.51 3.86 1.48 5.55L.8 23.1l5.68-1.49A11.06 11.06 0 0 0 12 23.1c6.13 0 11.1-4.97 11.1-11.1S18.13.9 12 .9zm0 20.2c-1.72 0-3.4-.46-4.87-1.34l-.35-.21-3.37.89.9-3.29-.23-.35A9.06 9.06 0 0 1 2.9 12 9.1 9.1 0 1 1 12 21.1z"/></svg>'
I_CLOCK = ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
I_PIN = ic('<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')
I_ARROW = ic('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_MAIL = ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/>')
I_IG = ic('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>', 15)
I_FB = '<svg class="ic" viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true"><path d="M14 8h2V5h-2c-1.7 0-3 1.3-3 3v2H9v3h2v6h3v-6h2l1-3h-3V8.5c0-.3.2-.5.5-.5z"/></svg>'
I_MENU = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'
I_CLOSE = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
I_TOOTH = ic('<path d="M12 5.2c-1.6-1.3-3.1-1.9-4.5-1.5-1.9.5-3.2 2.2-3.2 4.5 0 1.7.4 2.9.9 4.5.3 1.3.4 2.6.6 4 .2 1.5.5 3.3 1.7 3.3s1.3-1.4 1.6-2.8c.3-1.3.6-2.6 1.5-2.6s1.2 1.3 1.5 2.6c.3 1.4.5 2.8 1.6 2.8 1.2 0 1.5-1.8 1.7-3.3.2-1.4.3-2.7.6-4 .5-1.6.9-2.8.9-4.5 0-2.3-1.3-4-3.2-4.5-1.4-.4-2.9.2-4.5 1.5z"/>', 22)
I_MICROSCOPE = ic('<path d="M9 19h6M10 15l-1.5 4M14 15l1.5 4M8 11h8M12 3v8M12 3c-1.5 0-2.5 1-2.5 2.2S10.5 7 12 7s2.5-1 2.5-1.8S13.5 3 12 3z"/><circle cx="12" cy="11" r="3.5"/>', 34)
I_BRACES = ic('<path d="M4 9c2 6 4 8 8 8s6-2 8-8M6 9l1 2M10 9l.5 2.5M14 9l-.5 2.5M18 9l-1 2" /><path d="M5 7h14" />', 34)
I_PHOTO = ic('<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="M21 16l-5-5-4 4-2-2-5 5"/>', 34)

PH_FRAME = lambda icon, label: f'<div class="ph-frame">{icon}<span>{label}</span></div>'

def page(title, description, body, active="", extra_head=""):
    def _nav_item(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    nav_links = "".join(_nav_item(href, label) for href, label in NAV)
    mobile_links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Dr. Girdhar's DentAvenue</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar"><div class="wrap topbar__row">
<div class="topbar__info">
<a href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp</span></a>
<span>{I_CLOCK}<span>{HOURS_1}</span></span>
</div>
<div class="topbar__soc">
<a href="mailto:{EMAIL}" aria-label="Email">{I_MAIL}</a>
</div>
</div></div>

<header class="site-header" data-header>
<div class="wrap nav">
<a class="brand" href="index.html">
<span class="brand__mark">{I_TOOTH}</span>
<span class="brand__word"><span class="brand__name">Dr. Girdhar's</span><span class="brand__tag">DentAvenue</span></span>
</a>
<ul class="nav__menu">{nav_links}</ul>
<a class="btn nav__cta" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<button class="nav__toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false">{I_MENU}</button>
</div>
</header>

<div class="nav-scrim" data-nav-scrim></div>
<nav class="mobile-nav" data-mobile-nav aria-label="Mobile">
<button class="mobile-nav__close" data-nav-close aria-label="Close menu">{I_CLOSE}</button>
<ul>{mobile_links}</ul>
<a class="btn" style="width:100%;justify-content:center" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
</nav>

<main id="main">
{body}
</main>

<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<p class="footer-brand__name">Dr. Girdhar's DentAvenue</p>
<p class="footer-brand__stmt">A specialist-led dental practice in {CITY} — endodontics and orthodontics, under one roof.</p>
</div>
<div class="footer-col"><h5>Explore</h5><ul>
<li><a href="about.html">About</a></li><li><a href="doctors.html">Doctors</a></li>
<li><a href="treatments.html">Treatments</a></li><li><a href="clinic.html">Clinic</a></li></ul></div>
<div class="footer-col"><h5>Specialities</h5><ul>
<li><a href="treatments.html#root-canal">Root Canal Therapy</a></li><li><a href="treatments.html#aligners">Aligners &amp; Orthodontics</a></li>
<li><a href="treatments.html#implants">Dental Implants</a></li><li><a href="treatments.html#cosmetic">Cosmetic Dentistry</a></li></ul></div>
<div class="footer-col"><h5>Visit</h5><ul>
<li>{CITY}</li><li><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS_1}</li><li>{HOURS_2}</li></ul></div>
</div>
<div class="wrap footer-bottom">
<span>&copy; 2026 Dr. Girdhar's DentAvenue. All rights reserved.</span>
<span><a href="privacy.html">Privacy Policy</a><a href="disclaimer.html">Medical Disclaimer</a></span>
</div>
</footer>

<a class="wa-fab" href="{WA_CHAT}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I_WA}</a>
<nav class="mobar" aria-label="Quick contact"><div class="mobar__row">
<a href="{PHONE_TEL}">{I_PHONE}<span>Call</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>Chat</span></a>
<a class="is-primary" href="{WA_BOOK}" target="_blank" rel="noopener">{I_ARROW}<span>Book</span></a>
</div></nav>

<script src="assets/js/site.js"></script>
</body>
</html>'''

def section_head(kicker, title, intro="", center=False, light=False):
    c = " is-center" if center else ""
    ec = "eyebrow--center" if center else ""
    el = "eyebrow--light" if light else ""
    out = f'<div class="section-head{c}" data-reveal><span class="eyebrow {ec} {el}">{kicker}</span><h2 class="display-2">{title}</h2><span class="section-head__rule"></span>'
    if intro:
        out += f'<p class="lead" style="margin-top:1.2rem">{intro}</p>'
    return out + "</div>"

HERO_PATTERN = '''<svg class="hero__pattern" viewBox="0 0 1200 700" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<g stroke="#F6F2EA" stroke-opacity="0.10" fill="none" stroke-width="1.1">
<path d="M-80 640 Q 0 560 80 640 T 240 640 T 400 640 T 560 640 T 720 640 T 880 640 T 1040 640 T 1200 640 T 1360 640"/>
<path d="M-80 686 Q 0 610 80 686 T 240 686 T 400 686 T 560 686 T 720 686 T 880 686 T 1040 686 T 1200 686 T 1360 686" stroke-opacity="0.06"/>
</g>
</svg>'''

# ============================================================== INDEX =====
def build_index():
    hero = f'''<section class="hero">
{HERO_PATTERN}
<div class="wrap hero__inner">
<div class="hero__grid">
<div data-reveal>
<span class="hero__eyebrow">{CITY}</span>
<h1 class="hero__title">Specialist dental care, <em>precisely</em> delivered.</h1>
<p class="hero__lead">Root canal therapy and orthodontics, led by two specialists under one roof — Dr. Divyam Girdhar (Endodontics) and Dr. Nikita Mohelay Girdhar (Orthodontics).</p>
<div class="hero__actions">
<a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp us</span></a>
<a class="text-link text-link--light" href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
</div>
<dl class="hero__ticket">
<div><dt>Hours</dt><dd>{HOURS_1}<br>{HOURS_2}</dd></div>
<div><dt>Location</dt><dd>{CITY}</dd></div>
</dl>
</div>
<div class="hero__side has-img" data-reveal>
<img src="{IMG}room-1.jpg" alt="Treatment room at Dr. Girdhar's DentAvenue">
<span class="hero__side__tag">The clinic &middot; {CITY}</span>
</div>
</div>
</div>
</section>'''

    factstrip = f'''<section class="factstrip"><div class="wrap factstrip__row" data-reveal>
<div class="fact"><span class="fact__no">01</span><h3>Specialist-led</h3><p>A root canal specialist and an orthodontist, not generalists covering everything.</p></div>
<div class="fact"><span class="fact__no">02</span><h3>Academic rigour</h3><p>Both doctors teach and research alongside clinical practice.</p></div>
<div class="fact"><span class="fact__no">03</span><h3>Microscope-assisted care</h3><p>Precision techniques for complex root canal and retreatment cases.</p></div>
<div class="fact"><span class="fact__no">04</span><h3>Personalised planning</h3><p>Every treatment plan is built around your teeth, bite and goals.</p></div>
</div></section>'''

    intro = f'''<section class="section bg-card"><div class="wrap split">
<div data-reveal>
<span class="eyebrow">Our approach</span>
<h2 class="display-2">Two specialities, one considered plan.</h2>
<p class="lead" style="margin-top:1.3rem">Dr. Girdhar's DentAvenue brings together an endodontist and an orthodontist — so root canal care, restorative work and orthodontic treatment are planned together, not handed between unconnected clinics.</p>
<p class="muted" style="margin-top:1rem">Every case starts with a careful diagnosis and an honest conversation about what it actually needs — explained in plain language, before any treatment begins.</p>
<a class="text-link" style="margin-top:1.6rem" href="doctors.html">Meet the doctors{I_ARROW}</a>
</div>
<div class="split__media" data-reveal><figure class="frame frame--tall frame--duo"><img src="{IMG}room-2.jpg" alt="Treatment room"></figure></div>
</div></section>'''

    treatments_teaser = f'''<section class="section bg-band"><div class="wrap">
{section_head("What we treat", "Specialist care, under one roof.", "From a painful tooth to a complete smile correction — planned by the specialist it actually needs.")}
<ul class="tlist" data-reveal>
<li><a href="treatments.html#root-canal"><span class="tlist__ic">{I_TOOTH}</span><span class="tlist__body"><h3>Root Canal Therapy</h3><p>Microscope-assisted endodontics, including retreatment of previously treated teeth.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="treatments.html#aligners"><span class="tlist__ic">{I_BRACES}</span><span class="tlist__body"><h3>Aligners &amp; Orthodontics</h3><p>Comprehensive orthodontic treatment, including complex bite correction and TADs.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="treatments.html#implants"><span class="tlist__ic">{I_TOOTH}</span><span class="tlist__body"><h3>Dental Implants</h3><p>Long-lasting replacements for missing teeth.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="treatments.html#cosmetic"><span class="tlist__ic">{I_TOOTH}</span><span class="tlist__body"><h3>Cosmetic Dentistry</h3><p>Veneers, whitening and smile design, planned around your natural proportions.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
</ul>
<p style="margin-top:2.2rem" data-reveal><a class="text-link" href="treatments.html">View every treatment{I_ARROW}</a></p>
</div></section>'''

    doctors_teaser = f'''<section class="section bg-ink"><div class="wrap">
{section_head("The doctors", "Specialist care, academic rigour.", "", center=True, light=True)}
<div class="doc-circles stagger" data-reveal>
<div class="doc-circle"><div class="doc-circle__ph">{I_MICROSCOPE}</div><h3>Dr. Divyam Girdhar</h3><p class="doc-circle__role">Endodontics &amp; Conservative Dentistry</p><span class="doc-circle__rule"></span><p>BDS, MDS — Root Canal Specialist. Ex. Senior Resident, PGIDS Rohtak.</p></div>
<div class="doc-circle"><div class="doc-circle__ph">{I_BRACES}</div><h3>Dr. Nikita Mohelay Girdhar</h3><p class="doc-circle__role">Orthodontics &amp; Dentofacial Orthopaedics</p><span class="doc-circle__rule"></span><p>BDS, MDS, PhD (in progress) — Aligners &amp; myofunctional therapy specialist.</p></div>
</div>
<p class="center" style="margin-top:clamp(2rem,4vw,2.8rem)" data-reveal><a class="text-link text-link--light" href="doctors.html">Meet the doctors{I_ARROW}</a></p>
</div></section>'''

    process = f'''<section class="section bg-card"><div class="wrap">
{section_head("How it works", "A calm path from consultation to result.")}
<div class="steps stagger" data-reveal>
<div class="step"><span class="step__no">01</span><h3>Consultation</h3><p>A thorough assessment of your concern — and an honest conversation about it.</p></div>
<div class="step"><span class="step__no">02</span><h3>Diagnosis</h3><p>Digital imaging where it helps, read by the specialist treating you.</p></div>
<div class="step"><span class="step__no">03</span><h3>Treatment plan</h3><p>Options and recommendations explained clearly, before anything begins.</p></div>
<div class="step"><span class="step__no">04</span><h3>Treatment &amp; review</h3><p>Precise, unhurried care, with follow-up built in.</p></div>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book your visit</span><h2>Ready when you are.</h2><p>Message us on WhatsApp or call the clinic — new patients are always welcome.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a><a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">Chat with us{I_ARROW}</a></div>
</div></section>'''

    body = hero + factstrip + intro + treatments_teaser + doctors_teaser + process + cta
    return page(
        "Specialist Dental Clinic in Faridabad",
        "Dr. Girdhar's DentAvenue — a specialist-led dental practice in Faridabad, combining endodontics and orthodontics.",
        body, active="index.html"
    )

open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(build_index())
print("index.html written")

# ============================================================== ABOUT =====
def build_about():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / About</nav>
<span class="eyebrow">About the practice</span>
<h1 class="display-1" style="max-width:17ch">A new practice, built on specialist experience.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Dr. Girdhar's DentAvenue opened in 2025 in {CITY} — founded around a simple idea: root canal care and orthodontic treatment deserve a specialist each, working together.</p>
</div></section>'''

    story = f'''<section class="section bg-card"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall frame--duo"><img src="{IMG}room-3.jpg" alt="Treatment room"></figure></div>
<div data-reveal>
<span class="eyebrow">Why two specialists</span>
<h2 class="display-2">Depth, not just convenience.</h2>
<p class="lead" style="margin-top:1.3rem">Dr. Divyam Girdhar brings over a decade of specialist experience in endodontics, including three years as a Senior Resident at PGIDS Rohtak. Dr. Nikita Mohelay Girdhar brings specialist orthodontic training and an active academic and research profile in orthodontics.</p>
<p class="muted" style="margin-top:1rem">Together, they plan root canal, restorative and orthodontic care as one — rather than passing patients between unconnected specialists.</p>
</div>
</div></section>'''

    values = f'''<section class="section bg-ink"><div class="wrap">
{section_head("How we work", "A short list of things we take seriously.", "", light=True)}
<div class="feat-grid stagger" data-reveal>
<div class="feat"><span class="feat__no">i.</span><h3>Precision first</h3><p>Microscope-assisted technique for root canal and retreatment cases.</p></div>
<div class="feat"><span class="feat__no">ii.</span><h3>Plans in writing</h3><p>You leave knowing what was found, what is recommended, and why.</p></div>
<div class="feat"><span class="feat__no">iii.</span><h3>Specialist by discipline</h3><p>Endodontics and orthodontics, each led by a trained specialist.</p></div>
<div class="feat"><span class="feat__no">iv.</span><h3>Evidence-based</h3><p>Both doctors maintain active academic and research involvement.</p></div>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Meet the team</span><h2>Get to know the doctors.</h2><p>Qualifications, training and focus — in full.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="doctors.html">Meet the Doctors</a></div>
</div></section>'''

    body = hero + story + values + cta
    return page("About", "The philosophy behind Dr. Girdhar's DentAvenue, Faridabad.", body, active="about.html")

open(os.path.join(BASE, "about.html"), "w", encoding="utf-8").write(build_about())
print("about.html written")

# ============================================================= DOCTORS ====
def build_doctors():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Doctors</nav>
<span class="eyebrow">The doctors</span>
<h1 class="display-1" style="max-width:16ch">Specialist care, academic rigour.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Two specialists, each trained and experienced in a single discipline — endodontics and orthodontics.</p>
</div></section>'''

    divyam = f'''<section class="section bg-card"><div class="wrap doc" data-reveal>
<div class="doc__media">{PH_FRAME(I_MICROSCOPE, "Add doctor photo")}</div>
<div>
<h2 class="display-2">Dr. Divyam Girdhar</h2>
<p class="doc__role">Endodontics &amp; Conservative Dentistry — Root Canal Specialist</p>
<p class="doc__qual">BDS (Kurukshetra University) &middot; MDS, Conservative Dentistry &amp; Endodontics (B.R. Ambedkar University, Agra) &middot; Ex. Senior Resident, PGIDS Rohtak</p>
<div class="doc__bio">
<p>Dr. Divyam Girdhar is a distinguished endodontist with over 10 years of clinical and academic experience, bringing together advanced endodontic expertise, meticulous clinical precision, and an academic approach to comprehensive dental care.</p>
<p>He completed his BDS from Kurukshetra University and his MDS in Conservative Dentistry and Endodontics from B.R. Ambedkar University, Agra, where he received specialised training in contemporary endodontic diagnosis and treatment.</p>
<p>He subsequently served for three years as a Senior Resident at the Post Graduate Institute of Dental Sciences (PGIDS), Rohtak — one of India's premier centres for advanced dental education and clinical training — where he developed a particular interest in microscopic endodontics, endodontic microsurgery and complex root canal retreatment. He has since served as a Professor at leading institutions across the Delhi-NCR region, combining clinical practice with teaching, postgraduate mentoring and academic research.</p>
<h4>Areas of special interest</h4>
<ul class="doc__list">
<li>Microscopic endodontics</li>
<li>Endodontic retreatment</li>
<li>Endodontic microsurgery</li>
<li>Management of complex root canal cases</li>
<li>Aesthetic &amp; restorative dentistry, smile design</li>
</ul>
<p>Alongside his clinical career, Dr. Divyam has maintained a strong academic and research profile, publishing in national and international peer-reviewed journals and contributing chapters to academic dentistry books. For him, successful endodontic treatment is not simply about treating a tooth — it is about preserving natural tooth structure, restoring function, and providing long-term oral health through careful diagnosis and precise, minimally invasive treatment.</p>
</div>
</div>
</div></section>'''

    nikita = f'''<section class="section bg-band"><div class="wrap doc doc--rev" data-reveal>
<div>
<h2 class="display-2">Dr. Nikita Mohelay Girdhar</h2>
<p class="doc__role">Orthodontics &amp; Dentofacial Orthopaedics</p>
<p class="doc__qual">BDS (Datta Meghe Institute of Medical Sciences, Wardha) &middot; MDS, Orthodontics (Rajiv Gandhi University of Health Sciences, Karnataka) &middot; Stage II Certified Orthodontist, Indian Board of Orthodontics</p>
<div class="doc__bio">
<p>Dr. Nikita Girdhar is a specialist orthodontist with extensive experience creating healthy, balanced and confident smiles through personalised orthodontic care. As an Associate Professor in Orthodontics &amp; Dentofacial Orthopaedics, she combines specialist clinical expertise with a meticulous, patient-centred approach to treatment.</p>
<p>Her philosophy is simple: no two smiles are the same, and no two treatment plans should be either. Every treatment begins with a detailed assessment of the patient's teeth, jaws, facial proportions and individual concerns — developing a personalised plan around the patient's needs, lifestyle and desired outcome.</p>
<h4>Areas of clinical expertise</h4>
<ul class="doc__list">
<li>Comprehensive orthodontic treatment</li>
<li>Growth modification &amp; dentofacial orthopaedics</li>
<li>Accelerated orthodontic treatment</li>
<li>Temporary anchorage devices (TADs)</li>
<li>Complex bite &amp; alignment correction</li>
<li>Orthodontic care for cleft lip &amp; palate</li>
<li>Aesthetic smile enhancement</li>
</ul>
<p>Dr. N has a particular interest in cleft lip and palate orthodontics, where treatment requires careful planning across different stages of facial growth and dental development, alongside an interest in accelerated orthodontics and temporary anchorage devices. Her recognition as a recipient of the Charley Schultz and William Proffit Research Scholar Awards from the American Association of Orthodontists reflects her continued engagement with advances in orthodontic care. She is currently pursuing a PhD in Cleft Orthodontics.</p>
</div>
</div>
<div class="doc__media">{PH_FRAME(I_BRACES, "Add doctor photo")}</div>
</div></section>'''

    recognition = f'''<section class="section bg-ink"><div class="wrap">
{section_head("Academic &amp; research", "Recognition beyond the clinic.", "Both doctors stay close to the evidence behind their specialities — teaching, publishing and training alongside clinical practice.", light=True)}
<div class="feat-grid stagger" data-reveal>
<div class="feat"><h3>Senior Residency, PGIDS Rohtak</h3><p>Dr. Divyam completed three years as Senior Resident at one of India&rsquo;s premier centres for advanced dental education.</p></div>
<div class="feat"><h3>Published research &amp; book chapters</h3><p>Dr. Divyam has published in national and international peer-reviewed journals and contributed chapters to academic dentistry books.</p></div>
<div class="feat"><h3>AAO Research Scholar Awards</h3><p>Dr. Nikita is a recipient of the Charley Schultz and William Proffit Research Scholar Awards from the American Association of Orthodontists.</p></div>
<div class="feat"><h3>Stage II IBO Certification</h3><p>Dr. Nikita is a Stage II certified orthodontist under the Indian Board of Orthodontics, with a PhD in Cleft Orthodontics in progress.</p></div>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book a consultation</span><h2>Meet the doctors in person.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a></div>
</div></section>'''

    body = hero + divyam + nikita + recognition + cta
    return page("Doctors", "Dr. Divyam Girdhar (Endodontics) and Dr. Nikita Mohelay Girdhar (Orthodontics) — Dr. Girdhar's DentAvenue, Faridabad.", body, active="doctors.html")

open(os.path.join(BASE, "doctors.html"), "w", encoding="utf-8").write(build_doctors())
print("doctors.html written")

# ========================================================== TREATMENTS ====
def build_treatments():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Treatments</nav>
<span class="eyebrow">Treatments</span>
<h1 class="display-1" style="max-width:18ch">Every treatment, led by the right specialist.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Root canal and orthodontic care are our specialist focus — alongside the restorative and cosmetic treatments every smile occasionally needs.</p>
</div></section>'''

    featured = [
        ("root-canal", I_MICROSCOPE, "Root Canal Therapy", "Microscope-assisted root canal treatment, led by an endodontic specialist — including retreatment of previously treated teeth and management of complex cases."),
        ("aligners", I_BRACES, "Aligners &amp; Orthodontics", "Comprehensive orthodontic treatment including clear aligners, growth modification, complex bite correction and temporary anchorage devices (TADs)."),
        ("implants", I_TOOTH, "Dental Implants", "Long-lasting replacements for missing teeth, carefully planned to preserve surrounding bone and teeth."),
    ]
    tl_items = []
    for i, (anchor, icon, title, desc) in enumerate(featured):
        rev = " tl-item--rev" if i % 2 else ""
        tl_items.append(f'''<div class="tl-item{rev}" id="{anchor}" data-reveal>
<div class="tl-media">{PH_FRAME(icon, "Add treatment photo")}</div>
<span class="tl-num">{i+1}</span>
<div class="tl-body"><h3>{title}</h3><span class="section-head__rule"></span><p>{desc}</p><a class="text-link text-link--light" href="{WA_BOOK}" target="_blank" rel="noopener">Enquire about this{I_ARROW}</a></div>
</div>''')
    timeline = f'''<section class="section bg-ink"><div class="wrap">
{section_head("Specialist focus", "Our two core disciplines, in depth.", "", light=True)}
<div class="timeline">{"".join(tl_items)}</div>
</div></section>'''

    items = [
        ("cosmetic", I_TOOTH, "Cosmetic Dentistry", "Veneers, professional whitening and smile design, planned around your natural proportions for results that look like you."),
        ("restorative", I_TOOTH, "Crowns, Bridges &amp; Restorative Care", "Tooth-coloured restorations for damaged or worn teeth, including full-mouth restorative planning."),
        ("preventive", I_TOOTH, "Preventive &amp; Family Dentistry", "Check-ups, cleaning and fluoride care for every member of the family, from first visit onward."),
        ("cleft", I_BRACES, "Cleft Lip &amp; Palate Orthodontics", "Specialised orthodontic planning across the stages of facial growth and dental development."),
    ]
    lis = []
    for anchor, icon, title, desc in items:
        lis.append(f'<li id="{anchor}"><a href="{WA_BOOK}" target="_blank" rel="noopener"><span class="tlist__ic">{icon}</span><span class="tlist__body"><h3>{title}</h3><p>{desc}</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>')
    listing = f'''<section class="section bg-card"><div class="wrap">
{section_head("General care", "Everyday dentistry, done well.")}
<ul class="tlist" data-reveal>{"".join(lis)}</ul>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Not sure what you need?</span><h2>Tell us your concern — we&rsquo;ll recommend a plan.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div></section>'''

    body = hero + timeline + listing + cta
    return page("Treatments", "Root canal therapy, orthodontics and general dentistry at Dr. Girdhar's DentAvenue, Faridabad.", body, active="treatments.html")

open(os.path.join(BASE, "treatments.html"), "w", encoding="utf-8").write(build_treatments())
print("treatments.html written")

# ============================================================== CLINIC ====
def build_clinic():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Clinic</nav>
<span class="eyebrow">The clinic</span>
<h1 class="display-1" style="max-width:16ch">A calm, considered space.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">In {CITY} — designed for precise, unhurried care.</p>
</div></section>'''

    gallery = f'''<section class="section bg-card"><div class="wrap">
<div class="gallery" data-reveal>
<figure class="frame frame--duo g1"><img src="{IMG}room-1.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame frame--duo g2"><img src="{IMG}room-2.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame frame--duo g3"><img src="{IMG}room-3.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
</div>
</div></section>'''

    access = f'''<section class="section bg-ink"><div class="wrap split">
<div data-reveal><span class="eyebrow eyebrow--light">Getting here</span><h2 class="display-2" style="color:var(--cream)">Easy to find, easy to reach.</h2><p class="mut" style="margin-top:1.2rem">Dr. Girdhar's DentAvenue, {CITY}.</p><a class="text-link text-link--light" style="margin-top:1.4rem" href="contact.html">Full address &amp; directions{I_ARROW}</a></div>
<div class="split__media" data-reveal>{PH_FRAME(I_PHOTO, "Add exterior photo")}</div>
</div></section>'''

    body = hero + gallery + access
    return page("Clinic", f"Inside Dr. Girdhar's DentAvenue, {CITY}.", body, active="clinic.html")

open(os.path.join(BASE, "clinic.html"), "w", encoding="utf-8").write(build_clinic())
print("clinic.html written")

# ============================================================= CONTACT ====
def build_contact():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Contact</nav>
<span class="eyebrow">Get in touch</span>
<h1 class="display-1" style="max-width:16ch">Let&rsquo;s find you a time.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Message us on WhatsApp, call the clinic, or send a note below — we usually reply the same day.</p>
</div></section>'''

    grid = f'''<section class="section bg-card"><div class="wrap contact-grid">
<div data-reveal>
<div class="contact-card"><h3>{I_PIN}Visit</h3><p>Dr. Girdhar's DentAvenue<br>{CITY}</p></div>
<div class="contact-card"><h3>{I_CLOCK}Hours</h3><p>{HOURS_1}<br>{HOURS_2}</p></div>
<div class="contact-card"><h3>{I_PHONE}Contact</h3><p><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><a class="text-link" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp us{I_ARROW}</a></div>
</div>
<div data-reveal>
<form data-wa-form>
<div class="formfield"><label for="cf-name">Your name</label><input id="cf-name" name="name" type="text" required></div>
<div class="formfield"><label for="cf-phone">Phone number</label><input id="cf-phone" name="phone" type="tel"></div>
<div class="formfield"><label for="cf-msg">How can we help?</label><textarea id="cf-msg" name="message" required></textarea></div>
<button class="btn" type="submit" style="width:100%;justify-content:center">Send via WhatsApp</button>
<p class="form__msg"></p>
</form>
</div>
</div></section>'''

    body = hero + grid
    return page("Contact", f"Contact Dr. Girdhar's DentAvenue, {CITY}.", body, active="contact.html")

open(os.path.join(BASE, "contact.html"), "w", encoding="utf-8").write(build_contact())
print("contact.html written")

# ====================================================== PRIVACY/DISCLAIMER
def build_legal(title, active, paras):
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / {title}</nav>
<span class="eyebrow">Legal</span>
<h1 class="display-1" style="max-width:18ch">{title}</h1>
</div></section>'''
    body_paras = "".join(f'<p class="muted" style="margin-bottom:1.2rem">{p}</p>' for p in paras)
    content = f'<section class="section bg-card"><div class="wrap" style="max-width:70ch">{body_paras}</div></section>'
    body = hero + content
    return page(title, f"{title} — Dr. Girdhar's DentAvenue.", body, active=active)

open(os.path.join(BASE, "privacy.html"), "w", encoding="utf-8").write(build_legal(
    "Privacy Policy", "privacy.html",
    [
        "Dr. Girdhar's DentAvenue respects your privacy. Information you share with us — by phone, WhatsApp, email or the contact form on this site — is used only to respond to your enquiry and to manage your care.",
        "We do not sell or share your personal information with third parties for marketing purposes. Clinical records are kept confidential and handled in line with standard medical record-keeping practice.",
        "If you have questions about how your information is handled, please contact us directly at " + EMAIL + ".",
    ]
))
print("privacy.html written")

open(os.path.join(BASE, "disclaimer.html"), "w", encoding="utf-8").write(build_legal(
    "Medical Disclaimer", "disclaimer.html",
    [
        "The content on this website is provided for general informational purposes only and is not a substitute for professional dental advice, diagnosis or treatment.",
        "Always consult a qualified dentist regarding any dental concern before making treatment decisions. Individual results vary from patient to patient depending on clinical circumstances.",
        "In a dental emergency, please call the clinic directly at " + PHONE_DISPLAY + ".",
    ]
))
print("disclaimer.html written")
