from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://www.fundacionareces.es"

def extract_events(html):
    soup = BeautifulSoup(html, "lxml")

    events = []

    # Each event is a <li class="itemlistado ...">
    for block in soup.select("li.itemlistado"):
        link = block.select_one("span.nombre a[href]")
        date_el = block.select_one("span.fecha-comienzo")

        if not link or not date_el:
            continue

        # Extract raw date text exactly as shown
        raw_date = date_el.get_text(" ", strip=True)

        events.append({
            "title": link.get_text(strip=True),
            "url": urljoin(BASE, link["href"]),
            "raw_date": raw_date,
            "raw_location": None
        })

    print(f"Extracted {len(events)} events from default page")

    return events

