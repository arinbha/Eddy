from ics import Calendar
import sys
from datetime import datetime

class Schedule:
  def __init__(self):
    self.list_of_classes = []

  def join(self, event):
    self.list_of_classes.append(event)

def print_schedule(self):
    for event in self.list_of_classes:
       Event.print_event(event)

class Event:
  def __init__(self, name):
    self.name = name
    self.days = []
    self.location = ""
    self.start = ""
    self.end = ""
  def add_days(self, days):
    self.days = days
  def add_location(self, location):
    self.location = location
  def add_start(self, start):
    self.start = start
  def add_end(self, end):
    self.end = end
  def print_event(self):
    print(self.name)
    for day in self.days:
       print(day)
    print(self.location)
    print(self.start)
    print(self.end)

def read_location(location):
   d = {'PH': "Porter Hall", 'BH' : "Baker Hall", 'POS': "Posner Hall", 
        'GHC' : "Gates Hillman Center", 'DH' : "Doherty Hall", 'HH' : "Hammerschlag Hall"}
   s = location.split('-')
   return d[s[0]]

def read_days(days):
    d = {'MO': "Monday", 'TU' : "Tuesday", 'WE': "Wednesday", 
        'TH' : "Thursday", 'FR' : "Friday"}
    res = []
    for day in days:
       res.append(d[day])
    return res


def process_ics_file(file_path):
    schedule = Schedule()
    with open(file_path, "r", encoding="utf-8") as f:
        calendar = Calendar(f.read())
    for event in calendar.events:
        rrule = None
        for line in event.extra:
            if line.name == "RRULE":
                rrule = line
                break
        name = event.name
        location = read_location(event.location)
        classevent = Event(name)
        if rrule:
           rrule = str(rrule)
           byday = None
           parts = rrule.split(';')
           for part in parts:
              if part.startswith("BYDAY="):
                byday = (part.split("=", 1)[1].split)(',')
                break
        days = read_days(byday)
        classevent.add_days(days)
        classevent.add_location(location)

        begin = (((str(event.begin)).split('T'))[1]).split("+")[0]
        begin = datetime.strptime(begin, "%H:%M:%S")
        begin = begin.strftime("%-I:%M %p")

        end = (((str(event.end)).split('T'))[1]).split("+")[0]
        end = datetime.strptime(end, "%H:%M:%S")
        end = end.strftime("%-I:%M %p")

        classevent.add_start(begin)
        classevent.add_end(end)
        schedule.join(classevent)
    print_schedule(schedule)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_ics.py <path_to_ics_file>")
    else:
        process_ics_file(sys.argv[1])
