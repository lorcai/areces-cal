from dateutil import parser
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Madrid")

def normalize_event(raw):
    dt = parser.parse(raw["raw_date"], fuzzy=True)

    start = dt.replace(tzinfo=TZ)
    end = start  # policy: same-day event unless specified

    return {
        "title": raw["title"],
        "url": raw["url"],
        "start": start,
        "end": end,
        "location": raw["raw_location"] or "",
    }

