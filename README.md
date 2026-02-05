# Research Events Calendar – Fundación Ramón Areces

This repository automatically tracks public events from **Fundación Ramón Areces** and publishes them as a subscribable calendar.

The repository:
- Scrapes Fundación Ramón Areces event listings
- Extracts upcoming events from the default public page
- Generates a stable ICS calendar
- Publishes it via GitHub Pages
- Updates automatically via GitHub Actions

Subscribe: Use the published `.ics` URL in Google Calendar

---

## Event timing

Events are published as single **all-day events** on their scheduled date because reliable end times are not available from the listing page (would require a lot more effort).

---

## Scrape scope

The calendar is generated from the **default event listing page** only.

- Pagination and custom date ranges are ~cowardly avoided~ intentionally not used
- No past events

The default page usually covers all events for the current month and often the next, enough for tracking upcoming activities.

---

## Calendar update behavior

The calendar is regenerated on each workflow run.

- The `DTSTAMP` field reflects the generation time and therefore changes on every update.
- Calendar clients use the event UID to determine whether an event is new or an update.

There will be DTSTAMP changes for every event in every update (which will annoyingly show on the commit history) but the events will not duplicate on google calendar.

---

## Automation

Updates run automatically via **GitHub Actions** on a daily schedule and can also be triggered manually.

---

## Local testing

```
cd areces-cal
docker build -t areces-calendar .
docker run --rm \
  -v "$(pwd)/docs:/app/docs" \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/src:/app/src" \
areces-calendar
```



