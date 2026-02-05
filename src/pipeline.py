from pathlib import Path
from scrape_areces import fetch_html
from parse_events import extract_events
from normalize import normalize_event
from uid_store import load_uid_map, save_uid_map, uid_for_event
from ics_generator import generate_ics

ICS_PATH = Path("calendars/fundacion_areces.ics")

def main():
    html = fetch_html()
    raw_events = extract_events(html)

    if not raw_events:
        raise RuntimeError("No events extracted; aborting")

    uid_map = load_uid_map()
    events = []

    for raw in raw_events:
        norm = normalize_event(raw)
        norm["uid"] = uid_for_event(norm, uid_map)
        events.append(norm)

    ics = generate_ics(events)

    if ICS_PATH.exists() and ICS_PATH.read_bytes() == ics:
        return  # no change

    ICS_PATH.parent.mkdir(exist_ok=True)
    ICS_PATH.write_bytes(ics)
    save_uid_map(uid_map)

if __name__ == "__main__":
    main()

