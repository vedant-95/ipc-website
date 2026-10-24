import json, os
ROOT = os.path.expanduser('~/repos/ipc-website')
NAME = 'Integral Psychedelic Community'
VENMO = 'https://venmo.com/u/hummingbirdmagic'
FORM = 'events.html#submit'
INSTA = 'https://www.instagram.com/integral.psych3delic/'
STAR = '<svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.6 7-6.2-3.8-6.2 3.8 1.6-7L2 9.2l7.1-.6z"/></svg>'
IG = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="currentColor"/></svg>'
NAV = [('index.html', 'Home'), ('events.html', 'Events'), ('leads.html', 'Community Leads'), ('partners.html', 'Community Partners')]

def page(fname, title, desc, body, extra_head=''):
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{h}"{cur if h == fname else ""}>{l}</a>' for h, l in NAV)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/og-image.jpg">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="assets/icon-32.png">
<link rel="apple-touch-icon" href="assets/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
{extra_head}<script src="assets/site.js" defer></script>
</head>
<body>
<header class="site-header"><div class="wrap hdr">
  <a class="brand" href="index.html"><img src="assets/mark.png" alt="" width="61" height="40"><span>{NAME}</span></a>
  <button class="burger" aria-label="Open menu">☰</button>
  <nav class="nav" aria-label="Main">{nav}<a class="insta" href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram">{IG}</a><a class="btn btn-sm btn-primary" href="{VENMO}" target="_blank" rel="noopener">Donate</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap foot">
  <div><a class="brand" href="index.html"><img src="assets/logo-circle.png" alt="{NAME} logo" width="56" height="56"><span>{NAME}</span></a><p>San Francisco Bay Area · SF · Berkeley · Marin</p><p class="credit">Website built by <a href="https://www.linkedin.com/in/vedant-kshirsagar/" target="_blank" rel="noopener">Vedant Kshirsagar</a></p></div>
  <div class="foot-links"><a href="events.html">Events</a><a href="leads.html">Community Leads</a><a href="partners.html">Community Partners</a><a href="{VENMO}" target="_blank" rel="noopener">Donate (Venmo)</a><a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></div>
  <p class="disclaimer">The {NAME} is an educational and community organization. Nothing on this site is medical or legal advice. We do not sell or provide any substances. Community partners are independent organizations.</p>
</div></footer>
</body>
</html>
'''
    open(os.path.join(ROOT, fname), 'w').write(html)

org = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "logo": "assets/logo-circle.png",
       "description": "A San Francisco Bay Area psychedelic community centering collective liberation, spirituality, and brave spaces for mutual growth.",
       "sameAs": [INSTA], "areaServed": ["San Francisco", "Berkeley", "Marin County", "San Francisco Bay Area"]}

page('index.html', f'{NAME} | Bay Area Psychedelic Community',
     'A San Francisco Bay Area psychedelic community for collective liberation, spirituality and brave spaces for mutual growth. Community hikes in SF and Marin and Medicine Music Study groups in Berkeley.',
f'''<section class="hero"><div class="wrap hero-inner">
  <div><p class="eyebrow">San Francisco Bay Area</p>
    <h1>{NAME}</h1>
    <p class="lede">Collective liberation, spirituality, and brave spaces for mutual growth, rooted in the Bay Area.</p>
    <div class="cta-row"><a class="btn btn-primary btn-lg" href="events.html">See upcoming events</a><a class="btn btn-ghost btn-lg" href="leads.html">Meet our leads</a></div>
  </div>
  <div class="hero-logo"><img src="assets/logo-circle.png" alt="{NAME} logo: two hummingbirds beneath a sun, above a flower" width="640" height="640"></div>
</div></section>
<div class="wrap">
  <section class="mission"><p class="eyebrow">Our mission</p>
    <blockquote>The Integral Psychedelic Community aims to center ideals of collective liberation, spirituality, and the creation of brave spaces for mutual growth. We utilize the medicine of community, values of social justice, and land connection to help bring us closer to ourselves, one another, and the divine.</blockquote>
  </section>
  <section class="gather"><p class="eyebrow">How we gather</p><h2>Psychedelic community around the Bay</h2>
    <div class="gather-grid">
      <div class="gather-card"><span class="ico"><svg viewBox="0 0 24 24"><path d="M3 20l6-10 4 6 3-4 5 8z"/><circle cx="17" cy="6" r="2"/></svg></span><h3>Community hikes</h3><p>Connecting with the land and each other on trails around the Bay.</p><span class="where">San Francisco · Marin</span></div>
      <div class="gather-card"><span class="ico"><svg viewBox="0 0 24 24"><path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></svg></span><h3>Medicine Music Study groups</h3><p>Gathering to learn, share and sing medicine music together.</p><span class="where">Berkeley</span></div>
    </div>
  </section>
  <section class="explore" aria-label="Explore"><p class="eyebrow">Explore</p><h2>Find your way in</h2>
  <div class="cards3">
    <a class="tile" href="events.html"><span class="tile-ico">{STAR}</span><h3>Events</h3><p>See what's happening this month.</p><span class="tile-cta">See the calendar <span aria-hidden="true">→</span></span></a>
    <a class="tile" href="leads.html"><span class="tile-ico">◎</span><h3>Community Leads</h3><p>Meet the people who hold the space.</p><span class="tile-cta">Meet the leads <span aria-hidden="true">→</span></span></a>
    <a class="tile" href="partners.html"><span class="tile-ico">∞</span><h3>Community Partners</h3><p>Healers, sanctuaries and retreats we trust.</p><span class="tile-cta">Meet our partners <span aria-hidden="true">→</span></span></a>
  </div></section>
  <section class="upnext"><div class="row-head"><h2>Coming up</h2><a href="events.html">Full calendar →</a></div><div class="ev-list" id="ev-next"></div></section>
  <section class="cta-band">
    <div><h3>Support the community</h3><p>Donations help keep our gatherings accessible to everyone.</p><a class="btn btn-light" href="{VENMO}" target="_blank" rel="noopener">Donate via Venmo</a></div>
    <div><h3>Follow along</h3><p>Photos, announcements and event reminders.</p><a class="btn btn-light" href="{INSTA}" target="_blank" rel="noopener">@integral.psych3delic</a></div>
  </section>
</div>''', f'<script type="application/ld+json">{json.dumps(org)}</script>\n')

page('events.html', f'Events | {NAME}',
     'Upcoming psychedelic community events in the San Francisco Bay Area: community hikes in SF and Marin, Medicine Music Study groups in Berkeley, and more.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">Gatherings</p><h1>Events</h1><p class="lede">Community hikes in SF and Marin and Medicine Music Study groups in Berkeley.</p></div></div>
  <p class="notice" id="sample-note">Events marked <span class="tag">Sample</span> are examples. Real events will appear here once the calendar is connected.</p>
  <div class="events-split"><div id="ev-cal"></div><div id="ev-detail" class="detail-panel"></div></div>
  <section class="all-events"><h2>All upcoming events</h2><div class="ev-list" id="ev-all"></div></section>
  <p class="fine">Event details are provided by hosts. Please check each event's own page for the latest information.</p>
</div>''')

KATH_EMAIL = 'hummingbirdmagic@protonmail.com'
KATH_IG = 'https://www.instagram.com/integralwithkatherine/'
SANDRO_EMAIL = 'sandro.turriate@gmail.com'
HN = 'https://humannaturemushrooms.com'
def ext(u, t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
L = [
  ('katherine.jpg', 'Katherine Tomlinson', 'she/they', 'Founder &amp; Coordinator · Marin hikes · Medicine Music Study Group', [
    "Katherine Tomlinson is the founder and coordinator of the Integral Psychedelic Community, where she co-leads the community’s Marin hikes and Medicine Music Study Group, creating spaces for people to connect with nature, music, and one another. Currently she lives in unceded Coastal Miwok territory, also known as Sausalito, CA.",
    "Katherine has been involved in psychedelic education, advocacy, and community organizing since 2007. She holds a liberal arts degree from The Evergreen State College, where she was able to focus her study on psychedelics and plant teachers, space holding for expanded states of consciousness, and community building. Currently, she is working towards a masters degree from the California Institute of Integral Studies, works as ceremonialist in one-on-one containers, organizes educational events, contributes to conferences, and has supported the development of spaces for learning, dialogue, and community building with psychedelics and plant teachers for over half of her life.",
    "Her current studies focus on the traditional Andean teacher plant Wachuma (San Pedro), with a particular interest in its archaeological history, cultural significance, and relationship to Andean cosmology. Through ongoing study, travel, and relationships with traditional knowledge keepers in Peru, she seeks to deepen her understanding of the cactus and the cultures that have maintained relationships with it for thousands of years.",
    f"Katherine’s approach emphasizes cultural respect, reciprocity, lifelong learning, harm reduction, and the importance of building meaningful relationships between people, communities, and the natural world. She can be reached via <a href=\"mailto:{KATH_EMAIL}\">email</a>, or on Instagram at {ext(KATH_IG, '@integralwithkatherine')}."],
   [(f'mailto:{KATH_EMAIL}', 'Email Katherine'), (KATH_IG, 'Instagram ↗')]),
  ('sandro.jpg', 'Sandro', 'he/him', 'Community Lead · San Francisco &amp; Marin hikes', [
    "Sandro is a medicine guide and musician offering a heart-centered and grounded approach to healing. A Peruvian American cis man residing on unceded Ohlone land in San Francisco, he has been immersed in the study of plant medicine and master plant diets across Central and South America. His primary training draws from his ancestral heritage in Peru, specifically within the Shipibo tradition. Sandro’s healing journey includes exploring various realms of consciousness through breathwork with Wim Hof, Vipassana meditation, Reiki energy healing, Leela School Psychedelic Facilitation, and Hakomi Somatic Coaching.",
    f"For the Integral Psychedelic Community, he leads the hikes in San Francisco and occasionally helps lead the hikes in Marin. He finds joy tuning in with people and nature during group hikes, connecting deeply with the land and those around him. You can reach out to him at {ext('https://turriate.com', 'turriate.com')} or by <a href=\"mailto:{SANDRO_EMAIL}\">email</a>."],
   [('https://turriate.com', 'Visit website ↗'), (f'mailto:{SANDRO_EMAIL}', 'Email Sandro')]),
  ('romeo.jpg', 'Romeo', 'he/him', 'Community Lead · Medicine Music Study Group', [
    "Romeo is a lifelong musician and student of sacred traditions who co-facilitates the Integral Psychedelic Community’s Medicine Music Study Group. His musical journey now focuses on sacred and devotional music and traditional instruments. Drawing inspiration from his initiation in three spiritual lineages, he explores music as a pathway for healing, meditation, and connection.",
    "He also co-leads a Bay Area music collective and hosts community gatherings centered on meditation, sacred sound, shared musical experiences, and community building. He also provides spiritual guidance, energy healing, meditation, and integrative approaches to personal transformation. His approach emphasizes cultural respect, lifelong learning, and the power of music to bring people together."], []),
  ('sky.jpg', 'Sky', None, 'Community Lead · Marin hikes', [
    f"Sky co-leads the community hikes in Marin and is the founder of the company {ext(HN, 'Human Nature')}. Bio and photo coming soon!"],
   [(HN, 'Human Nature ↗')]),
]
def lead_card(img, n, pr, role, paras, links):
    TGT = ' target="_blank" rel="noopener"'
    pron = f' <span class="pronouns">({pr})</span>' if pr else ''
    photo = (f'<img class="lead-photo" src="assets/leads/{img}" alt="{n}, {NAME} community lead" width="640" height="640">' if img
             else f'<div class="lead-photo lead-photo-empty"><span>{n}</span><small>Photo coming soon</small></div>')
    btns = ''.join(f'<a class="btn btn-sm {"btn-primary" if i == 0 else "btn-ghost"}" href="{u}"{"" if u.startswith("mailto:") else TGT}>{t}</a>' for i, (u, t) in enumerate(links))
    return (f'<article class="lead">{photo}<div class="lead-body"><h3>{n}{pron}</h3><p class="role">{role}</p>'
            + ''.join(f'<p>{x}</p>' for x in paras) + (f'<div class="lead-links">{btns}</div>' if btns else '') + '</div></article>')
leads = ''.join(lead_card(*l) for l in L)
page('leads.html', f'Community Leads | {NAME}',
     'Meet the community leads of the Integral Psychedelic Community: Katherine Tomlinson, Sandro, Romeo and Sky, who lead community hikes in SF and Marin and the Medicine Music Study Group in Berkeley.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">The people</p><h1>Community Leads</h1><p class="lede">The facilitators and organizers who hold space for our community.</p></div></div>
  <div class="leads">{leads}</div>
</div>''')

P = [
  ('ronin-rao.jpg', 'Ronin Rao', 'Sound healing &amp; ceremony', 'https://roninrao.com', 'Sound baths · Meditation · Cacao circles',
   'A medicine guide and musician offering a heart-centered, grounded approach to healing through sound baths, individual and group meditation, and cacao circles. His training is rooted in the Shipibo tradition of Peru, and includes psilocybin facilitator training and the Zendo Project\'s integration program.'),
  ('human-nature.jpg', 'Human Nature', 'Human Nature Sanctuary', 'https://humannaturemushrooms.com', 'Nonprofit sanctuary · 21+',
   'A nonprofit religious community rooted in reverence for nature, consciousness and intentional practice. They describe themselves as a sanctuary at the intersection of science and spirit, supporting self-inquiry, connection and personal growth.'),
  ('honeymoon-farm.jpg', 'Honey Moon Farm', 'Sierra Nevada retreats', 'https://www.honeymoonfarm.org', 'Retreats · Gatherings',
   '"Where it\'s summer camp all the time." Honey Moon Farm hosts intimate retreats and prayerful gatherings on their land in the Sierra Nevada.'),
]
cards = ''.join(f'''<article class="partner"><a class="partner-shot" href="{u}" target="_blank" rel="noopener" tabindex="-1"><img src="assets/partners/{img}" alt="Preview of the {n} website" loading="lazy" width="800" height="500"></a>
  <div class="partner-body"><h3>{n}</h3><p class="partner-org">{org_}</p><p class="partner-tags">{tags}</p><p>{blurb}</p><a class="btn btn-sm btn-primary" href="{u}" target="_blank" rel="noopener">Visit website ↗</a></div></article>''' for img, n, org_, u, tags, blurb in P)
page('partners.html', f'Community Partners | {NAME}',
     'Community partners of the Integral Psychedelic Community: Ronin Rao, Human Nature and Honey Moon Farm.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">Friends of the community</p><h1>Community Partners</h1><p class="lede">Healers, sanctuaries and retreats we work alongside and trust.</p></div></div>
  <div class="partners">{cards}</div>
</div>''')
print('built')
