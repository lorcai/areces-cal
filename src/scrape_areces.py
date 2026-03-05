import requests
from pathlib import Path

URL = "https://www.fundacionareces.es/fundacionareces/es/actividades/"

def fetch_html(timeout=15, save_to_file=False):
    headers = {
        "User-Agent": "areces-calendar-bot/1.0 (research calendar aggregation)"
    }
    r = requests.get(URL, headers=headers, timeout=timeout)
    r.raise_for_status()
    text = r.text

    if save_to_file:
        path = Path("scrape_areces_result_latest.html")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    return text

