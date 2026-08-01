from .core import list_events, run_event
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(run_event(sys.argv[1]))
    else:
        print("Available events:", ", ".join(list_events()))
