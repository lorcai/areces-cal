from icalendar import Calendar, Event
from datetime import datetime, timezone, timedelta

def generate_ics(events):
    cal = Calendar()
    cal.add("prodid", "-//Research Events//Areces//EN")
    cal.add("version", "2.0")

    # DTSTAMP represents when the calendar data was generated.
    # It is expected (and correct) that this changes between runs.
    now = datetime.now(timezone.utc)

    for e in sorted(events, key=lambda x: x["start"]):
        ve = Event()
        ve.add("uid", e["uid"])
        ve.add("summary", e["title"])

        # --- Previous behavior (kept for reference) ---
        # This created zero-duration midnight events, which are misleading
        # when the real start/end times are unknown.
        #
        # ve.add("dtstart", e["start"])
        # ve.add("dtend", e["end"])

        # --- New behavior: true all-day events ---
        # We only know the calendar day of the event, not its duration.
        # Representing it as an all-day event is semantically correct and
        # avoids fabricating times.
        #
        # Per RFC 5545:
        # - All-day events use VALUE=DATE
        # - DTEND is exclusive, so we add +1 day
        start_date = e["start"].date()
        ve.add("dtstart", start_date)
        ve.add("dtend", start_date + timedelta(days=1))

        ve.add("dtstamp", now)
        ve.add("url", e["url"])

        if e["location"]:
            ve.add("location", e["location"])

        cal.add_component(ve)

    return cal.to_ical()

