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
  <div><a class="brand" href="index.html"><img src="assets/logo-circle.png" alt="{NAME} logo" width="56" height="56"><span>{NAME}</span></a><p>San Francisco Bay Area · SF · Oakland · Marin</p></div>
  <div class="foot-links"><a href="events.html">Events</a><a href="leads.html">Community Leads</a><a href="partners.html">Community Partners</a><a href="{VENMO}" target="_blank" rel="noopener">Donate (Venmo)</a><a href="{INSTA}" target="_blank" rel="noopener">Instagram</a></div>
  <p class="disclaimer">The {NAME} is an educational and community organization. Nothing on this site is medical or legal advice. We do not sell or provide any substances. Community partners are independent organizations.</p>
  <p class="credit">Website built by <a href="https://www.linkedin.com/in/vedant-kshirsagar/" target="_blank" rel="noopener">Vedant Kshirsagar</a></p>
</div></footer>
</body>
</html>
'''
    open(os.path.join(ROOT, fname), 'w').write(html)

org = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "logo": "assets/logo-circle.png",
       "description": "A San Francisco Bay Area psychedelic community centering collective liberation, spirituality, and brave spaces for mutual growth.",
       "sameAs": [INSTA], "areaServed": ["San Francisco", "Oakland", "Marin County", "San Francisco Bay Area"]}

page('index.html', f'{NAME} | Bay Area Psychedelic Community',
     'A San Francisco Bay Area psychedelic community for collective liberation, spirituality and brave spaces for mutual growth. Community hikes in SF and Marin and Medicine Music Study groups in Oakland and Marin.',
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
      <div class="gather-card"><span class="ico"><svg viewBox="0 0 24 24"><path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></svg></span><h3>Medicine Music Study groups</h3><p>Gathering to learn, share and sing medicine music together.</p><span class="where">Oakland · Marin</span></div>
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
     'Upcoming psychedelic community events in the San Francisco Bay Area: community hikes in SF and Marin, Medicine Music Study groups in Oakland and Marin, and more.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">Gatherings</p><h1>Events</h1><p class="lede">Community hikes in SF and Marin and Medicine Music Study groups in Oakland and Marin.</p></div></div>
  <p class="notice">Events marked <span class="tag">Sample</span> are examples. Real events will appear here once the calendar is connected.</p>
  <div class="events-split"><div id="ev-cal"></div><div id="ev-detail" class="detail-panel"></div></div>
  <section class="all-events"><h2>All upcoming events</h2><div class="ev-list" id="ev-all"></div></section>
  <p class="fine">Event details are provided by hosts. Please check each event's own page for the latest information.</p>
</div>''')

leads = ''.join(f'''<article class="lead"><div class="lead-photo">Photo</div><div><h3>Lead name {i}</h3><p class="role">Role coming soon</p><p>A short bio for this community lead is coming soon.</p></div></article>''' for i in range(1, 5))
page('leads.html', f'Community Leads | {NAME}',
     'Meet the community leads of the Integral Psychedelic Community in the San Francisco Bay Area.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">The people</p><h1>Community Leads</h1><p class="lede">The facilitators and organizers who hold space for our community.</p></div></div>
  <div class="leads">{leads}</div>
</div>''')

P = [
  ('ronin-rao.jpg', 'Sandro Turriate', 'Ronin Rao', 'https://roninrao.com', 'Sound baths · Meditation · Cacao circles',
   'A medicine guide and musician offering a heart-centered, grounded approach to healing through sound baths, individual and group meditation, and cacao circles. His training is rooted in the Shipibo tradition of Peru, and includes psilocybin facilitator training and the Zendo Project\'s integration program.'),
  ('human-nature.jpg', 'Human Nature', 'Human Nature Sanctuary', 'https://humannaturemushrooms.com', 'Nonprofit sanctuary · 21+',
   'A nonprofit religious community rooted in reverence for nature, consciousness and intentional practice. They describe themselves as a sanctuary at the intersection of science and spirit, supporting self-inquiry, connection and personal growth.'),
  ('honeymoon-farm.jpg', 'Honey Moon Farm', 'Sierra Nevada retreats', 'https://www.honeymoonfarm.org', 'Retreats · Gatherings',
   '"Where it\'s summer camp all the time." Honey Moon Farm hosts intimate retreats and prayerful gatherings on their land in the Sierra Nevada.'),
]
cards = ''.join(f'''<article class="partner"><a class="partner-shot" href="{u}" target="_blank" rel="noopener" tabindex="-1"><img src="assets/partners/{img}" alt="Preview of the {n} website" loading="lazy" width="800" height="500"></a>
  <div class="partner-body"><h3>{n}</h3><p class="partner-org">{org_}</p><p class="partner-tags">{tags}</p><p>{blurb}</p><a class="btn btn-sm btn-primary" href="{u}" target="_blank" rel="noopener">Visit website ↗</a></div></article>''' for img, n, org_, u, tags, blurb in P)
page('partners.html', f'Community Partners | {NAME}',
     'Community partners of the Integral Psychedelic Community: Sandro Turriate (Ronin Rao), Human Nature and Honey Moon Farm.',
f'''<div class="wrap">
  <div class="page-head"><div><p class="eyebrow">Friends of the community</p><h1>Community Partners</h1><p class="lede">Healers, sanctuaries and retreats we work alongside and trust.</p></div></div>
  <div class="partners">{cards}</div>
</div>''')
print('built')
