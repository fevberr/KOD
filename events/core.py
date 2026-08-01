import os
import json
import glob

EVENTS_DIR = "events"

def get_events():
    events = {}
    if os.path.exists(EVENTS_DIR):
        for f in glob.glob(f"{EVENTS_DIR}/*.json"):
            try:
                with open(f, 'r') as file:
                    data = json.load(file)
                    name = data.get('name', os.path.basename(f).replace('.json', ''))
                    events[name.lower()] = data
            except:
                pass
    return events

def get_event(name):
    events = get_events()
    return events.get(name.lower())

def list_events():
    events = get_events()
    return list(events.keys())

def run_event(name):
    event = get_event(name)
    if event:
        return event.get('output', f"[!] No output defined for {name}")
    return f"[!] Event '{name}' not found"

__all__ = ['get_events', 'get_event', 'list_events', 'run_event']
