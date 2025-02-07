from ics import Calendar
import sys

class Event:
  def __init__(self, name):
    self.name = name
    self.days = []
    self.location = ""

def process_ics_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        calendar = Calendar(f.read())
    
    for event in calendar.events:
        print(f"Event: {event.name}")
        print(f"Start: {event.begin}")
        print(f"End: {event.end}")
        print(f"Description: {event.description}")
        print(f"Location: {event.location}")
        print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_ics.py <path_to_ics_file>")
    else:
        process_ics_file(sys.argv[1])
