"""Fetch the community's live Eventbrite events and write them to assets/eventbrite.json for the calendar."""
import json, os, re, urllib.request
from datetime import datetime

ORGANIZER_ID = '69260502343'
API = f'https://www.eventbrite.com/api/v3/organizers/{ORGANIZER_ID}/events/?status=live&page='
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'eventbrite.json')


def fetch_all():
    events, page = [], 1
    while True:
        with urllib.request.urlopen(urllib.request.Request(API + str(page), headers={'User-Agent': 'ipc-website-sync'}), timeout=30) as r:
            data = json.load(r)
        events += data.get('events', [])
        if not data.get('pagination', {}).get('has_more_items'):
            return events
        page += 1


def clock(iso):
    return datetime.fromisoformat(iso).strftime('%I:%M %p').lstrip('0')


def to_calendar(e):
    name = e['name']['text'].strip()
    m = re.match(r'^Integral Psychedelic Community (.+?)\s*-\s*(.+)$', name)
    title, city = (f'Community {m.group(1)}: {m.group(2)}', m.group(2)) if m else (name, 'Bay Area')
    return {
        'date': e['start']['local'][:10], 'title': title, 'start': clock(e['start']['local']), 'end': clock(e['end']['local']),
        'city': 'Online' if e.get('online_event') else city, 'desc': (e.get('summary') or '').strip(), 'rsvp': e['url'], 'link': None,
    }


if __name__ == '__main__':
    events = sorted((to_calendar(e) for e in fetch_all()), key=lambda e: (e['date'], e['start']))
    with open(OUT, 'w') as f:
        json.dump(events, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(f'Wrote {len(events)} events')
