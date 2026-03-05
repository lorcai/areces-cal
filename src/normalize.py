import re
from dateutil import parser
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Madrid")
SPANISH_MONTH_TO_ENGLISH = {
    "ene": "jan",
    "feb": "feb",
    "mar": "mar",
    "abr": "apr",
    "may": "may",
    "jun": "jun",
    "jul": "jul",
    "ago": "aug",
    "sep": "sep",
    "set": "sep",
    "oct": "oct",
    "nov": "nov",
    "dic": "dec",
}

# Dateutil parser doesn't support Spanish months. Translate to English.
def _to_english_month(raw_date):
    pattern = r"\b(?:ene|feb|mar|abr|may|jun|jul|ago|sep|set|oct|nov|dic)\b"
    return re.sub(
        pattern,
        lambda m: SPANISH_MONTH_TO_ENGLISH[m.group(0).lower()],
        raw_date,
        flags=re.IGNORECASE,
    )


def normalize_event(raw):
    english_date = _to_english_month(raw["raw_date"])
    dt = parser.parse(english_date, fuzzy=True)

    start = dt.replace(tzinfo=TZ)
    end = start  # policy: same-day event unless specified

    return {
        "title": raw["title"],
        "url": raw["url"],
        "start": start,
        "end": end,
        "location": raw["raw_location"] or "",
    }

