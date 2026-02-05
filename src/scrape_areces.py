import requests

URL = "https://www.fundacionareces.es/fundacionareces/es/actividades/"

def fetch_html(timeout=15):
    headers = {
        "User-Agent": "areces-calendar-bot/1.0 (research calendar aggregation)"
    }
    r = requests.get(URL, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text

