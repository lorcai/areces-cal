# Research Events Calendar – Fundación Ramón Areces

This repository:
- Scrapes Fundación Ramón Areces event listings
- Generates a stable ICS calendar
- Publishes it via GitHub Pages
- Updates automatically via GitHub Actions

## Usage

- Local run: `python src/pipeline.py`
- Docker: `docker build -t areces-calendar`
- Subscribe: Use the published `.ics` URL in Google Calendar

--

# Local testing

```
cd areces-cal
docker build -t areces-calendar .
docker run --rm \
  -v "$(pwd)/calendars:/app/calendars" \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/src:/app/src" \
areces-calendar
```



