#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dr. Girdhar's DentAvenue — Faridabad — from-scratch static site generator."""
import os
import hashlib

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/"

def _ver(rel_path):
    with open(os.path.join(BASE, rel_path), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

CSS_VER = _ver("assets/css/site.css")
JS_VER = _ver("assets/js/site.js")

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
HOURS_2 = "Sunday · 10:00 am – 2:00 pm / by appointment"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("doctors.html", "Doctors"),
    ("treatments.html", "Treatments"),
    ("clinic.html", "Clinic"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

# ================================================================ BLOG =====
BLOG_POSTS = [
    {
        "slug": "signs-you-need-a-root-canal",
        "img": "room-real-1.jpg",
        "kicker": "Endodontics",
        "title": "How to tell if you need a root canal",
        "excerpt": "Tooth pain doesn't always mean a root canal — but a few specific signs are worth getting checked promptly.",
        "body": [
            ("p", "A toothache can come from many places — a cavity, a cracked filling, gum irritation. But certain signs point more specifically to the kind of deep infection that a root canal treats, and it helps to know what to watch for before the pain becomes an emergency."),
            ("h3", "Signs worth getting checked"),
            ("p", "Persistent, throbbing pain that doesn't settle with an over-the-counter painkiller is the most common signal. So is sharp sensitivity to hot or cold that lingers well after the stimulus is gone, rather than fading in a few seconds. Swelling or a small pimple-like bump on the gum near a tooth, or a tooth that has darkened in colour, are also reasons to get an assessment rather than wait it out."),
            ("h3", "Why early assessment matters"),
            ("p", "The earlier an infected tooth is examined, the more conservative the treatment usually is. Left untreated, an infection can spread beyond the tooth and lead to more complex management later — including retreatment of a tooth that's already had a root canal, which is its own specialised area within endodontics."),
            ("h3", "What an assessment involves"),
            ("p", "A proper diagnosis starts with a clinical examination and, where needed, digital imaging to see what's happening beneath the surface. From there, the treatment plan — whether it's a straightforward root canal, a retreatment, or something else entirely — is explained before anything begins."),
            ("p", "If any of this sounds familiar, it's worth having it looked at rather than waiting for the pain to pass."),
        ],
    },
    {
        "slug": "aligners-vs-braces",
        "img": "room-1.jpg",
        "kicker": "Orthodontics",
        "title": "Clear aligners vs. traditional braces: what's right for you?",
        "excerpt": "Both can straighten teeth effectively — the right choice depends on the case, not just preference.",
        "body": [
            ("p", "Clear aligners have become a popular alternative to metal braces, and for good reason — they're far less visible and can be removed for eating and brushing. But they aren't automatically the better option for every case, and a proper assessment matters more than the marketing."),
            ("h3", "What aligners do well"),
            ("p", "Aligners are well suited to mild-to-moderate crowding, spacing and certain bite corrections, and tend to be more comfortable day-to-day since there's no wire or bracket. Treatment also requires real discipline — they only work if worn for the recommended hours each day."),
            ("h3", "Where traditional braces still win"),
            ("p", "More complex bite corrections, significant crowding, or cases that need precise control over tooth movement — particularly in growing patients — are often better managed with traditional braces, sometimes alongside tools like temporary anchorage devices for more demanding corrections."),
            ("h3", "The honest answer"),
            ("p", "There isn't a universally \"better\" option — there's a better option for your specific bite, your goals and your lifestyle. That's decided after a detailed assessment of your teeth, jaws and facial proportions, not before one."),
        ],
    },
    {
        "slug": "life-after-a-root-canal",
        "img": "room-2.jpg",
        "kicker": "Endodontics",
        "title": "Life after a root canal: recovery, do's and don'ts",
        "excerpt": "A root canal is usually the end of the pain, not the start of a long recovery — here's what to expect.",
        "body": [
            ("p", "One of the most persistent myths about root canal treatment is that it's painful or that recovery is difficult. In reality, for most patients, the procedure relieves pain that was already there — and the days after are usually uneventful."),
            ("h3", "The first few days"),
            ("p", "Mild sensitivity or tenderness around the treated tooth for a day or two is normal, especially when biting down, and generally settles with a simple over-the-counter painkiller if needed. Avoiding chewing on that side until any temporary filling or crown is finalised is a sensible precaution."),
            ("h3", "What to avoid"),
            ("p", "Very hard or sticky foods on the treated tooth in the days immediately after, and skipping the follow-up visit for a permanent restoration — a treated tooth left without its final crown or filling for too long is more vulnerable to fracture."),
            ("h3", "When to call the clinic"),
            ("p", "Pain that worsens rather than improves after a few days, noticeable swelling, or a bite that feels distinctly \"off\" are reasons to get in touch rather than wait. These are uncommon, but worth acting on quickly when they happen."),
        ],
    },
    {
        "slug": "signs-you-need-an-orthodontist",
        "img": "room-3.jpg",
        "kicker": "Orthodontics",
        "title": "5 signs you might need to see an orthodontist",
        "excerpt": "Orthodontic treatment isn't just about appearance — these signs are worth a specialist opinion at any age.",
        "body": [
            ("p", "Orthodontic concerns aren't limited to crooked front teeth, and treatment certainly isn't limited to teenagers. Here are a few signs that are worth a specialist opinion, whichever stage of life you're at."),
            ("h3", "1. Crowded or overlapping teeth"),
            ("p", "Beyond appearance, crowding can make teeth genuinely harder to clean properly, which over time raises the risk of decay and gum issues in the spots that are hardest to reach."),
            ("h3", "2. Noticeable gaps between teeth"),
            ("p", "Spacing that's widened over time, rather than been there since childhood, is worth having assessed — it can sometimes point to an underlying bite or gum issue rather than being purely cosmetic."),
            ("h3", "3. Difficulty biting or chewing comfortably"),
            ("p", "A bite that doesn't meet evenly, or jaw discomfort with regular use, often has an orthodontic component worth investigating."),
            ("h3", "4. A jaw that shifts or clicks"),
            ("p", "This can be linked to bite alignment and is worth a joint look between orthodontic and general assessment."),
            ("h3", "5. You were told to \"wait and see\" years ago"),
            ("p", "Orthodontic treatment works at any age — the plan is simply adjusted to your bite, bone and goals. If it was raised once and never followed up on, it's worth a fresh look."),
        ],
    },
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
<link rel="stylesheet" href="assets/css/site.css?v={CSS_VER}">
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
<p class="footer-brand__stmt">A specialist dental clinic in {CITY} — every treatment led by the right specialist, under one roof.</p>
</div>
<div class="footer-col"><h5>Explore</h5><ul>
<li><a href="about.html">About</a></li><li><a href="doctors.html">Doctors</a></li>
<li><a href="treatments.html">Treatments</a></li><li><a href="clinic.html">Clinic</a></li><li><a href="blog.html">Blog</a></li></ul></div>
<div class="footer-col"><h5>Specialities</h5><ul>
<li><a href="treatments.html#root-canal">Root Canal Therapy</a></li><li><a href="treatments.html#aligners">Aligners &amp; Orthodontics</a></li>
<li><a href="treatments.html#implants">Dental Implants</a></li><li><a href="treatments.html#cosmetic">Cosmetic Dentistry</a></li></ul></div>
<div class="footer-col"><h5>Visit</h5><ul>
<li>{CITY}</li><li><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS_1}</li><li>{HOURS_2}</li></ul></div>
</div>
<div class="wrap footer-bottom">
<span>&copy; 2026 Dr. Girdhar's DentAvenue. All rights reserved.</span>
<span><a href="privacy.html">Privacy Policy</a><a href="disclaimer.html">Medical Disclaimer</a><span class="footer__credit">Designed by <a href="https://jafenmedia.com" target="_blank" rel="noopener">Jafen Media</a></span></span>
</div>
</footer>

<a class="wa-fab" href="{WA_CHAT}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I_WA}</a>
<nav class="mobar" aria-label="Quick contact"><div class="mobar__row">
<a href="{PHONE_TEL}">{I_PHONE}<span>Call</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>Chat</span></a>
<a class="is-primary" href="{WA_BOOK}" target="_blank" rel="noopener">{I_ARROW}<span>Book</span></a>
</div></nav>

<script src="assets/js/site.js?v={JS_VER}"></script>
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
<p class="hero__lead">A specialised dental clinic in {CITY} — every treatment, from a root canal to a complete smile correction, planned and delivered by the specialist it actually needs.</p>
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
<div class="hero__side has-img is-slideshow" data-reveal data-slideshow>
<img src="{IMG}room-real-1.jpg" alt="Treatment room at Dr. Girdhar's DentAvenue" class="is-active">
<img src="{IMG}room-1.jpg" alt="Treatment room at Dr. Girdhar's DentAvenue">
<img src="{IMG}room-2.jpg" alt="Treatment room at Dr. Girdhar's DentAvenue">
<img src="{IMG}room-3.jpg" alt="Treatment room at Dr. Girdhar's DentAvenue">
<span class="hero__side__tag">The clinic &middot; {CITY}</span>
</div>
</div>
</div>
</section>'''

    factstrip = f'''<section class="factstrip"><div class="wrap factstrip__row" data-reveal>
<div class="fact"><span class="fact__no">01</span><h3>Specialist-led</h3><p>Every treatment handled by a trained specialist in that discipline — not one generalist covering everything.</p></div>
<div class="fact"><span class="fact__no">02</span><h3>Academic rigour</h3><p>Both doctors teach and research alongside clinical practice.</p></div>
<div class="fact"><span class="fact__no">03</span><h3>Microscope-assisted care</h3><p>Precision techniques for complex root canal and retreatment cases.</p></div>
<div class="fact"><span class="fact__no">04</span><h3>Personalised planning</h3><p>Every treatment plan is built around your teeth, bite and goals.</p></div>
</div></section>'''

    intro = f'''<section class="section bg-card"><div class="wrap split">
<div data-reveal>
<span class="eyebrow">Our approach</span>
<h2 class="display-2">All specialities, one considered plan.</h2>
<p class="lead" style="margin-top:1.3rem">Dr. Girdhar's DentAvenue brings together specialists across root canal treatment, orthodontics, implants and restorative dentistry — so every treatment is planned by the specialist it actually needs, rather than handed between unconnected clinics.</p>
<p class="muted" style="margin-top:1rem">Every case starts with a careful diagnosis and an honest conversation about what it actually needs — explained in plain language, before any treatment begins.</p>
<p class="muted" style="margin-top:1rem">A family of dentists — Dr. Divyam Girdhar's parents are doctors too, and this practice carries that tradition into its second generation.</p>
<a class="text-link" style="margin-top:1.6rem" href="about.html">Our story{I_ARROW}</a>
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
{section_head("The doctors", "Specialist care, academic rigour.", "The clinic's founding specialists and owners, each trained in a single discipline.", center=True, light=True)}
<div class="doc-circles stagger" data-reveal>
<div class="doc-circle"><div class="doc-circle__ph">{I_MICROSCOPE}</div><h3>Dr. Divyam Girdhar</h3><p class="doc-circle__role">Endodontics &amp; Conservative Dentistry</p><span class="doc-circle__rule"></span><p>BDS, MDS — Root Canal Specialist. Ex. Senior Resident, PGIDS Rohtak.</p></div>
<div class="doc-circle"><div class="doc-circle__ph">{I_BRACES}</div><h3>Dr. Nikita Mohelay Girdhar</h3><p class="doc-circle__role">Orthodontics &amp; Dentofacial Orthopaedics</p><span class="doc-circle__rule"></span><p>BDS, MDS, PhD (in progress) — Aligners &amp; myofunctional therapy specialist.</p></div>
</div>
<p class="center" style="margin-top:clamp(2rem,4vw,2.8rem)" data-reveal><a class="text-link text-link--light" href="doctors.html">Meet the doctors{I_ARROW}</a></p>
</div></section>'''

    philosophy = f'''<section class="section bg-card"><div class="wrap split">
<div data-reveal>
<div class="quote"><blockquote>Successful endodontic treatment is not simply about treating a tooth — it is about preserving natural tooth structure, restoring function, and providing long-term oral health through careful diagnosis and precise treatment.</blockquote><cite>Dr. Divyam Girdhar, Endodontics</cite></div>
</div>
<div data-reveal>
<div class="quote"><blockquote>No two smiles are the same, and no two treatment plans should be either. Every treatment begins with a detailed assessment of the patient's teeth, jaws and individual concerns.</blockquote><cite>Dr. Nikita Mohelay Girdhar, Orthodontics</cite></div>
</div>
</div></section>'''

    technology = f'''<section class="section bg-ink"><div class="wrap">
{section_head("Technique &amp; technology", "Precision tools, used with judgement.", "Technology is used where it genuinely improves the outcome — never for its own sake.", light=True)}
<div class="feat-grid stagger" data-reveal>
<div class="feat"><h3>Dental operating microscope</h3><p>Used for microscopic endodontics, retreatment and endodontic microsurgery — precision beyond what the naked eye allows.</p></div>
<div class="feat"><h3>Digital imaging</h3><p>Used for diagnosis and treatment planning, read directly by the specialist treating you.</p></div>
<div class="feat"><h3>Temporary anchorage devices</h3><p>Used in orthodontics for complex bite correction and accelerated treatment, where appropriate.</p></div>
<div class="feat"><h3>Growth &amp; dentofacial planning</h3><p>Used for younger patients and cleft cases, where treatment must account for ongoing facial growth.</p></div>
</div>
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

    audience = f'''<section class="section bg-band"><div class="wrap">
{section_head("Who we see", "Specialist care for specific concerns.", "If any of these sound familiar, a consultation is the right next step.")}
<div class="feat-grid feat-grid--3 stagger" data-reveal>
<div class="feat"><h3>Tooth pain or infection</h3><p>Needing a root canal assessment, including teeth that have been treated before.</p></div>
<div class="feat"><h3>Crowding or bite issues</h3><p>Considering aligners or braces, for a teenager or as an adult.</p></div>
<div class="feat"><h3>Missing teeth</h3><p>Exploring dental implants or bridges to restore function and appearance.</p></div>
<div class="feat"><h3>Gum concerns or sensitivity</h3><p>Bleeding, receding or sensitive gums that need a proper assessment.</p></div>
<div class="feat"><h3>A complex or unusual case</h3><p>Referred by another dentist for a second opinion or specialist management.</p></div>
<div class="feat"><h3>A cleft lip &amp; palate case</h3><p>Requiring coordinated orthodontic planning across stages of growth.</p></div>
</div>
</div></section>'''

    faq_items = [
        ("Do I need a referral to see a specialist here?", "No. You can book directly with either doctor — a referral from another dentist is welcome but not required."),
        ("How many visits does root canal treatment usually need?", "Many straightforward cases are completed in a single sitting; more complex or retreatment cases may need two visits. This is confirmed after examination, not assumed in advance."),
        ("I'm an adult — can I still get aligners or braces?", "Yes. Orthodontic treatment works at any age; the plan and timeline are simply adjusted to your bite, bone and goals."),
        ("What should I bring to my first visit?", "Any previous X-rays, treatment records or referral notes you have. If you don't have any, that's fine — we'll assess from scratch."),
    ]
    faq_html = "".join(f'<div style="border-top:1px solid var(--line);padding:clamp(1.4rem,3vw,1.9rem) 0"><h3 class="display-3" style="font-size:1.1rem">{q}</h3><p class="muted" style="margin-top:.6rem">{a}</p></div>' for q, a in faq_items)
    faq = f'''<section class="section bg-card"><div class="wrap">
{section_head("Questions", "A few things patients often ask.", "", center=True)}
<div style="max-width:74ch;margin-inline:auto" data-reveal>{faq_html}<div class="rule"></div></div>
</div></section>'''

    blog_cards = "".join(f'''<a class="blog-card" href="blog-{p['slug']}.html">
<figure class="frame frame--duo"><img src="{IMG}{p['img']}" alt="{p['title']}"></figure>
<span class="blog-card__kicker">{p['kicker']}</span>
<h3>{p['title']}</h3>
<p>{p['excerpt']}</p>
<span class="text-link">Read more{I_ARROW}</span>
</a>''' for p in BLOG_POSTS[:3])
    blog_teaser = f'''<section class="section bg-band"><div class="wrap">
{section_head("From the blog", "Notes on dental health.", "Plain-language explainers on the questions we hear most often in clinic.")}
<div class="blog-grid stagger" data-reveal>{blog_cards}</div>
<p style="margin-top:2.2rem" data-reveal><a class="text-link" href="blog.html">View all articles{I_ARROW}</a></p>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book your visit</span><h2>Ready when you are.</h2><p>Message us on WhatsApp or call the clinic — new patients are always welcome.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a><a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">Chat with us{I_ARROW}</a></div>
</div></section>'''

    body = hero + factstrip + intro + treatments_teaser + audience + doctors_teaser + philosophy + technology + process + blog_teaser + faq + cta
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
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Dr. Girdhar's DentAvenue opened in 2025 in {CITY} — founded and personally run by Dr. Divyam Girdhar and Dr. Nikita Mohelay Girdhar, its two owner-specialists, around a simple idea: every treatment deserves the specialist it actually needs.</p>
</div></section>'''

    legacy = f'''<section class="section bg-band"><div class="wrap">
<div data-reveal style="max-width:70ch">
<span class="eyebrow">A family tradition</span>
<h2 class="display-2">Dentistry runs in the family.</h2>
<p class="lead" style="margin-top:1.3rem">Dr. Divyam Girdhar comes from a family of doctors — his parents have run a hospital in Niwana, Haryana for more than 35 years. Dr. Girdhar's DentAvenue carries that tradition into its second generation, now established as its own independent specialist dental practice in {CITY}.</p>
</div>
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

    body = hero + legacy + story + values + cta
    return page("About", "The philosophy behind Dr. Girdhar's DentAvenue, Faridabad.", body, active="about.html")

open(os.path.join(BASE, "about.html"), "w", encoding="utf-8").write(build_about())
print("about.html written")

# ============================================================= DOCTORS ====
def build_doctors():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Doctors</nav>
<span class="eyebrow">The doctors</span>
<h1 class="display-1" style="max-width:16ch">Specialist care, academic rigour.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Two specialists, each trained and experienced in a single discipline — endodontics and orthodontics — and the founding owners of the clinic.</p>
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
<p class="lead" style="margin-top:1.4rem;max-width:60ch">From root canal therapy and orthodontics to implants, gum care and cosmetic dentistry — every treatment here is led by the specialist trained for it.</p>
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
{section_head("Specialist focus", "Led by the right specialist, every time.", "", light=True)}
<div class="timeline">{"".join(tl_items)}</div>
</div></section>'''

    items = [
        ("cosmetic", I_TOOTH, "Cosmetic Dentistry", "Veneers, professional whitening and smile design, planned around your natural proportions for results that look like you."),
        ("restorative", I_TOOTH, "Crowns, Bridges &amp; Restorative Care", "Tooth-coloured restorations for damaged or worn teeth, including full-mouth restorative planning."),
        ("gums", I_TOOTH, "Gum &amp; Periodontal Care", "Assessment and treatment for bleeding, receding or sensitive gums, alongside deep cleaning where needed."),
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


def build_blog_index():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Blog</nav>
<span class="eyebrow">From the clinic</span>
<h1 class="display-1" style="max-width:18ch">Notes on dental health, from our specialists.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Plain-language explainers on the questions we hear most often in clinic.</p>
</div></section>'''

    cards = []
    for post in BLOG_POSTS:
        cards.append(f'''<a class="blog-card" href="blog-{post['slug']}.html">
<figure class="frame frame--duo"><img src="{IMG}{post['img']}" alt="{post['title']}"></figure>
<span class="blog-card__kicker">{post['kicker']}</span>
<h3>{post['title']}</h3>
<p>{post['excerpt']}</p>
<span class="text-link">Read more{I_ARROW}</span>
</a>''')
    grid = f'''<section class="section bg-card"><div class="wrap">
<div class="blog-grid stagger" data-reveal>{"".join(cards)}</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Have a question?</span><h2>Ask us directly.</h2><p>Not every question needs a Google search — message us and we'll answer it properly.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_CHAT}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div></section>'''

    body = hero + grid + cta
    return page("Blog", "Dental health articles from Dr. Girdhar's DentAvenue, Faridabad.", body, active="blog.html")

open(os.path.join(BASE, "blog.html"), "w", encoding="utf-8").write(build_blog_index())
print("blog.html written")

def build_blog_post(post, idx):
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / <a href="blog.html">Blog</a> / {post['title']}</nav>
<span class="eyebrow">{post['kicker']}</span>
<h1 class="display-1" style="max-width:20ch">{post['title']}</h1>
</div></section>'''

    media = f'''<section class="section bg-card" style="padding-top:0"><div class="wrap">
<figure class="frame frame--duo frame--tall" style="max-width:900px;margin-inline:auto"><img src="{IMG}{post['img']}" alt="{post['title']}"></figure>
</div></section>'''

    parts = []
    for tag, text in post["body"]:
        parts.append(f"<{tag}>{text}</{tag}>")
    article = f'''<section class="section bg-card" style="padding-top:0"><div class="wrap">
<div class="article" style="margin-inline:auto" data-reveal>{"".join(parts)}</div>
</div></section>'''

    others = [p for p in BLOG_POSTS if p["slug"] != post["slug"]][:3]
    more_cards = "".join(f'''<a class="blog-card" href="blog-{o['slug']}.html">
<figure class="frame frame--duo"><img src="{IMG}{o['img']}" alt="{o['title']}"></figure>
<span class="blog-card__kicker">{o['kicker']}</span>
<h3>{o['title']}</h3>
<p>{o['excerpt']}</p>
<span class="text-link">Read more{I_ARROW}</span>
</a>''' for o in others)
    more = f'''<section class="section bg-band"><div class="wrap">
{section_head("More from the blog", "Related articles.")}
<div class="blog-grid stagger" data-reveal>{more_cards}</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Not sure what you need?</span><h2>Tell us your concern — we&rsquo;ll recommend a plan.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div></section>'''

    body = hero + media + article + more + cta
    return page(post["title"], post["excerpt"], body, active="blog.html")

for idx, post in enumerate(BLOG_POSTS):
    fname = f"blog-{post['slug']}.html"
    open(os.path.join(BASE, fname), "w", encoding="utf-8").write(build_blog_post(post, idx))
    print(fname + " written")

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
