# Research Events Calendar – Fundación Ramón Areces

This repository automatically tracks public events from **Fundación Ramón Areces** and publishes them as a subscribable calendar.

The repository:
- Scrapes Fundación Ramón Areces event listings
- Extracts upcoming events from the default public page
- Generates a stable ICS calendar
- Publishes it via GitHub Pages
- Updates automatically via GitHub Actions

## Subscribe

Use the deployed GitHub Pages URL to avoid potential caching, rate-limiting, and stability issues associated with GitHub’s `raw.githubusercontent.com` domain:

`https://lorcai.github.io/areces-cal/fundacion_areces.ics`

### Google Calendar

1. Open Google Calendar
2. In the left sidebar, next to **Other calendars**, click **+**
3. Select **From URL**
4. Paste the URL above and click **Add calendar**
5. Change the calendar name

The calendar will be added as read-only and updated automatically.

## Event timing

Events are published as single **all-day events** on their scheduled date because reliable end times are not available from the listing page (would require a lot more effort).

## Scrape scope

The calendar is generated from the **default event listing page** only.

- Pagination and custom date ranges are ~cowardly avoided~ intentionally not used
- No past events

The default page usually covers all events for the current month and often the next, enough for tracking upcoming activities.

## Calendar update behavior

The calendar `ics` is regenerated on each workflow run. If new events are found or old events are deleted from the site, they will also be included/deleted from the `ics` file (and consequently updated by the calendar client when polling the file).

- The hashed URL of the event is used as UID to provide a persistent unique identifier that remains stable across calendar regenerations.
- Calendar clients use the event UID to determine whether an event is new or an update.

According to [spec](https://tools.ietf.org/html/rfc2445#section-4.8.7.2), the `DTSTAMP` property represents "the date/time that the instance of the iCalendar object was created". Here it is set to the date when the event is first included in this calendar.

## Automation

Updates run automatically via **GitHub Actions** on a daily schedule and can also be triggered manually.

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



