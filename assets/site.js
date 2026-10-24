// Leads' Google Sheet. Paste the Sheet's ID (the long code in its web address) between the quotes.
// The Sheet must be shared as "Anyone with the link: Viewer". Leave empty to use only the events below.
const SHEET_ID = '';
const SHEET_TAB = 'Events';

// Hand-added events and samples. Samples are hidden once the Sheet is connected.
// Eventbrite events are loaded from assets/eventbrite.json, which a daily GitHub Action updates.
let EVENTS = [
  { date: '2026-10-15', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Berkeley', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
  { date: '2026-10-17', title: 'Gathering for Prayer with Ronin Rao', start: '3:00 PM', end: '10:00 PM', city: 'San Francisco', desc: 'A ceremony gathering hosted by community partner Ronin Rao.', link: 'https://roninrao.com', rsvp: null, sample: false },
  { date: '2026-10-29', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Berkeley', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
  { date: '2026-11-12', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Berkeley', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
].map(e => ({ ...e, date: new Date(e.date + 'T12:00:00') }));

const STAR = '<svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.6 7-6.2-3.8-6.2 3.8 1.6-7L2 9.2l7.1-.6z"/></svg>';
const now = new Date();
const sameDay = (a, b) => a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
const eventsOn = dt => EVENTS.filter(e => sameDay(e.date, dt));
const upcoming = () => EVENTS.filter(e => e.date >= new Date(now.getFullYear(), now.getMonth(), now.getDate())).sort((a, b) => a.date - b.date);
const fmtDay = dt => dt.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });

function eventCard(e, showDate = true) {
  return `<article class="ev-card">
    ${showDate ? `<div class="ev-date"><span class="ev-mon">${e.date.toLocaleDateString('en-US', { month: 'short' })}</span><span class="ev-num">${e.date.getDate()}</span></div>` : ''}
    <div class="ev-body">
      <h4 class="ev-title">${e.title}${e.sample ? '<span class="tag">Sample</span>' : ''}</h4>
      <p class="ev-meta">${showDate ? e.date.toLocaleDateString('en-US', { weekday: 'short' }) + ' · ' : ''}${e.start} – ${e.end} · ${e.city}</p>
      <p class="ev-desc">${e.desc}</p>
      <div class="ev-actions">
        ${e.rsvp ? `<a class="btn btn-sm btn-primary" href="${e.rsvp}" target="_blank" rel="noopener">RSVP</a>` : ''}
        ${e.link ? `<a class="btn btn-sm btn-ghost" href="${e.link}" target="_blank" rel="noopener">Event details ↗</a>` : ''}
      </div>
    </div>
  </article>`;
}

function calendar(container, detailEl) {
  const first = upcoming()[0];
  let viewY = now.getFullYear(), viewM = now.getMonth(), selected = null;
  function draw() {
    const start = new Date(viewY, viewM, 1), days = new Date(viewY, viewM + 1, 0).getDate();
    let cells = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].map(w => `<div class="cal-dow">${w}</div>`).join('');
    for (let i = 0; i < start.getDay(); i++) cells += '<div class="cal-day empty"></div>';
    for (let n = 1; n <= days; n++) {
      const dt = new Date(viewY, viewM, n), evs = eventsOn(dt);
      const cls = ['cal-day', evs.length && 'has-event', sameDay(dt, now) && 'today', selected && sameDay(dt, selected) && 'selected'].filter(Boolean).join(' ');
      cells += `<button class="${cls}" data-day="${n}" ${evs.length ? `aria-label="${fmtDay(dt)}: ${evs.length} event${evs.length > 1 ? 's' : ''}"` : 'tabindex="-1" aria-hidden="true"'}><span class="cal-num">${n}</span>${evs.length ? STAR + (evs.length > 1 ? `<span class="cal-count">${evs.length}</span>` : '') + `<span class="cal-peek">${evs[0].title}</span>` : ''}</button>`;
    }
    container.innerHTML = `<div class="cal">
      <div class="cal-head"><button class="cal-nav" data-nav="-1" aria-label="Previous month">‹</button>
      <h3>${start.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</h3>
      <button class="cal-nav" data-nav="1" aria-label="Next month">›</button></div>
      <div class="cal-grid">${cells}</div>
      <p class="cal-legend">${STAR} = event that day · tap a star to see details</p></div>`;
    container.querySelectorAll('[data-nav]').forEach(b => b.onclick = () => { viewM += +b.dataset.nav; if (viewM < 0) { viewM = 11; viewY--; } if (viewM > 11) { viewM = 0; viewY++; } draw(); });
    container.querySelectorAll('.cal-day.has-event').forEach(b => b.onclick = () => { selected = new Date(viewY, viewM, +b.dataset.day); draw(); showDetail(); });
  }
  function showDetail() {
    if (!selected) {
      detailEl.innerHTML = `<p class="eyebrow">Next up</p>${first ? eventCard(first) : '<p>No upcoming events yet. Check back soon.</p>'}<p class="hint">Tap any ${STAR} day on the calendar to see what's happening.</p>`;
      return;
    }
    detailEl.innerHTML = `<p class="eyebrow">${fmtDay(selected)}</p>` + eventsOn(selected).map(e => eventCard(e, false)).join('');
    if (window.innerWidth < 860) detailEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  draw(); showDetail();
}

function parseCSV(text) {
  const rows = []; let row = [], cell = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) { if (ch === '"' && text[i + 1] === '"') { cell += '"'; i++; } else if (ch === '"') q = false; else cell += ch; }
    else if (ch === '"') q = true;
    else if (ch === ',') { row.push(cell); cell = ''; }
    else if (ch === '\n' || ch === '\r') { if (ch === '\r' && text[i + 1] === '\n') i++; row.push(cell); rows.push(row); row = []; cell = ''; }
    else cell += ch;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  return rows;
}

function sheetDate(v) {
  v = (v || '').trim();
  const iso = v.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/);
  if (iso) return new Date(+iso[1], iso[2] - 1, +iso[3], 12);
  const us = v.match(/^(\d{1,2})\/(\d{1,2})\/(\d{2,4})/);
  if (us) return new Date(us[3].length === 2 ? 2000 + +us[3] : +us[3], us[1] - 1, +us[2], 12);
  const d = new Date(v);
  return isNaN(d) ? null : new Date(d.getFullYear(), d.getMonth(), d.getDate(), 12);
}

function sheetTime(v) {
  v = (v || '').trim();
  const m = v.match(/^(\d{1,2}):(\d{2})(?::\d{2})?$/);
  if (!m) return v;
  const h = +m[1];
  return `${h % 12 || 12}:${m[2]} ${h < 12 ? 'AM' : 'PM'}`;
}

const esc = v => (v || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const url = v => /^https?:\/\//i.test((v || '').trim()) ? v.trim() : null;

async function loadSheet() {
  const res = await fetch(`https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:csv&sheet=${encodeURIComponent(SHEET_TAB)}`);
  if (!res.ok) throw new Error(res.status);
  const [head, ...rows] = parseCSV(await res.text());
  const col = name => head.findIndex(h => h.trim().toLowerCase().startsWith(name));
  const c = { date: col('date'), title: col('event name'), start: col('start'), end: col('end'), city: col('location'), desc: col('description'), rsvp: col('rsvp'), link: col('more info') };
  return rows.map(r => ({
    date: sheetDate(r[c.date]), title: esc(r[c.title]), start: esc(sheetTime(r[c.start])), end: esc(sheetTime(r[c.end])),
    city: esc(r[c.city]), desc: esc(r[c.desc]), rsvp: url(r[c.rsvp]), link: url(r[c.link]), sample: false,
  })).filter(e => e.date && e.title);
}

function render() {
  const note = document.getElementById('sample-note');
  if (note) note.hidden = !EVENTS.some(e => e.sample);
  const cal = document.getElementById('ev-cal');
  if (cal) calendar(cal, document.getElementById('ev-detail'));
  const all = document.getElementById('ev-all');
  if (all) all.innerHTML = upcoming().map(e => eventCard(e)).join('') || '<p>No upcoming events yet.</p>';
  const next = document.getElementById('ev-next');
  if (next) next.innerHTML = upcoming().slice(0, 3).map(e => eventCard(e)).join('') || '<p>No upcoming events yet. Check back soon.</p>';
}

document.addEventListener('DOMContentLoaded', async () => {
  document.querySelector('.burger').onclick = () => document.querySelector('.nav').classList.toggle('open');
  if (!document.querySelector('#ev-cal, #ev-all, #ev-next')) return;
  try {
    const res = await fetch('assets/eventbrite.json', { cache: 'no-cache' });
    if (res.ok) EVENTS = [...EVENTS, ...(await res.json()).map(e => ({ ...e, date: new Date(e.date + 'T12:00:00'), sample: false }))];
  } catch (err) { console.warn('Could not load Eventbrite events', err); }
  if (SHEET_ID) {
    try {
      const fromSheet = await loadSheet();
      const key = e => `${e.date.toDateString()}|${e.rsvp || e.title.toLowerCase()}`;
      const seen = new Set(fromSheet.map(key));
      EVENTS = [...fromSheet, ...EVENTS.filter(e => !e.sample && !seen.has(key(e)))];
    } catch (err) { console.warn('Could not load events sheet', err); }
  }
  render();
});
