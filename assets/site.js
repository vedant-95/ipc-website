// Events data.
const EVENTS = [
  { date: '2026-10-11', title: 'Community Hike: Lands End', start: '10:00 AM', end: '1:00 PM', city: 'San Francisco', desc: 'An easy coastal walk with time for sharing and quiet reflection.', link: null, rsvp: null, sample: true },
  { date: '2026-10-15', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Oakland', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
  { date: '2026-10-17', title: 'Gathering for Prayer with Ronin Rao', start: '3:00 PM', end: '10:00 PM', city: 'San Francisco', desc: 'A ceremony gathering hosted by community partner Ronin Rao.', link: 'https://roninrao.com', rsvp: null, sample: false },
  { date: '2026-10-25', title: 'Community Hike: Tennessee Valley', start: '9:30 AM', end: '12:30 PM', city: 'Marin', desc: 'A morning hike to the beach and back, followed by an optional picnic.', link: null, rsvp: null, sample: true },
  { date: '2026-10-29', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Marin', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
  { date: '2026-11-08', title: 'Community Hike: Mount Tamalpais', start: '10:00 AM', end: '1:30 PM', city: 'Marin', desc: 'A moderate hike with views of the whole Bay.', link: null, rsvp: null, sample: true },
  { date: '2026-11-12', title: 'Medicine Music Study Group', start: '7:00 PM', end: '9:00 PM', city: 'Oakland', desc: 'Learning and singing medicine songs together. All voices welcome.', link: null, rsvp: null, sample: true },
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

document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('.burger').onclick = () => document.querySelector('.nav').classList.toggle('open');
  const cal = document.getElementById('ev-cal');
  if (cal) calendar(cal, document.getElementById('ev-detail'));
  const all = document.getElementById('ev-all');
  if (all) all.innerHTML = upcoming().map(e => eventCard(e)).join('') || '<p>No upcoming events yet.</p>';
  const next = document.getElementById('ev-next');
  if (next) next.innerHTML = upcoming().slice(0, 3).map(e => eventCard(e)).join('') || '<p>No upcoming events yet. Check back soon.</p>';
});
