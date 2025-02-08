from ics import Calendar
import sys
from datetime import datetime
from models import *
from db import *

start = 900
end = 2100

zones = {"Ansys" : 1, "Scaife" : 1, "Scott" : 2, "Hammerschlag" : 2, "Wean" : 2, "Doherty" : 2, "Gates" : 3, "Newell" : 3, 
"Tepper" : 4, "Porter" : 5, "Baker" : 5, "CUC" : 6, "Maggie Mo" : 6, "Posner" : 6}

places = {"Gates 6" : "Gates", "Gates 5" : "Gates", "Gates 4" : "Gates", "Gates 3" : "Gates", "Gates 2" : "Gates", 
          "Gates 1" : "Gates", "Gates 7" : "Gates", "Baker 5" : "Baker", "Tepper 4" : "Tepper"}

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
    self.start = 0
    self.end = 0
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
   d = {'PH': "Porter", 'BH' : "Baker", 'POS': "Posner", 
        'GHC' : "Gates", 'DH' : "Doherty", 'HH' : "Hammerschlag",
        'WEH' : "Wean", 'MM' : "Maggie Mo", 'TEP': "Tepper"}
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
        begin = int(convert_timestamp(begin.strftime("%-I:%M %p")))

        end = (((str(event.end)).split('T'))[1]).split("+")[0]
        end = datetime.strptime(end, "%H:%M:%S")
        end = int(convert_timestamp(end.strftime("%-I:%M %p")))

        classevent.add_start(begin)
        classevent.add_end(end)
        schedule.join(classevent)
    return schedule


def convert_timestamp(timestamp):
    return datetime.strptime(timestamp, "%I:%M %p").strftime("%H%M")

def find_busy_by_day(schedule):
   d = {"Monday" : [], "Tuesday" : [], "Wednesday" : [], "Thursday" : [], "Friday" : []}
   for event in schedule.list_of_classes:
      for day in event.days:
         (d[day]).append((event.start, event.end))
   return d

def find_start_zones_codes(schedule, d):
   for event in schedule.list_of_classes:
      for day in event.days:
         if event.start not in d[day]:
             (d[day])[event.start] = []
             (d[day])[(event.start)].append(zones[event.location])
         if (zones[event.location]) not in (d[day])[event.start]:
            (d[day])[(event.start)].append(zones[event.location])
   return d

def find_end_zones_codes(schedule, d):
   for event in schedule.list_of_classes:
      for day in event.days:
         if event.end not in d[day]:
             (d[day])[event.end] = []
             (d[day])[event.end].append(zones[event.location])
         if (zones[event.location]) not in (d[day])[event.end]:
            (d[day])[event.end].append(zones[event.location])
   return d

     
def find_free_intervals(map, start_time, end_time):
    for key in map:
        intervals = map[key]
        intervals.sort()
        free_intervals = []
        current_time = start_time
        for interval in intervals:
            if interval[0] > current_time:
                free_intervals.append((current_time, interval[0]))
            current_time = max(current_time, interval[1])
        if current_time < end_time:
            free_intervals.append((current_time, end_time))
        map[key] = free_intervals
    return map

def find_available_times(map1, map2, start, end):
    result_map = {}
    for key in map1:
        free_times_1 = map1[key]
        free_times_2 = map2[key]
        result = []
        for start1, end1 in free_times_1:
            for start2, end2 in free_times_2:
                overlap_start = max(start1, start2)
                overlap_end = min(end1, end2)
                if overlap_start < overlap_end:
                    result.append((overlap_start, overlap_end))
        final_intervals = []
        for times in result:
           if not ((times[1] - times[0] == 10) or (times[1] - times[0] == 50 and (times[1] % 100 == 0) and (times[0] % 100 == 50))):
              final_intervals.append(times)
        result_map[key] = sorted(final_intervals)
    return result_map



if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python process_ics.py <path_to_ics_file>")
    else:
        free_times = []
        start_map = {"Monday" : {}, "Tuesday" : {}, "Wednesday" : {}, "Thursday" : {}, "Friday" : {}}
        end_map = {"Monday" : {}, "Tuesday" : {}, "Wednesday" : {}, "Thursday" : {}, "Friday" : {}}
        for i in range (1, len(sys.argv)):
            schedule = process_ics_file(sys.argv[i])
            busy_times = find_busy_by_day(schedule)
            start_map = find_start_zones_codes(schedule, start_map)
            end_map = find_end_zones_codes(schedule, end_map)
            free_times.append(find_free_intervals(busy_times, start, end))
        r = free_times[0]
        for elem in free_times:
            r = find_available_times(r, elem, start, end)
        return_map = {}
        for day in r:
           return_map[day] = []
           intervals = r[day]
           for start,end in intervals:
              end_locs = end_map.get(day, []).get(start, [])
              start_locs = start_map.get(day, []).get(end, [])
              merged = end_locs + start_locs
              merged = set(merged)
              return_map[day].append((start, end, merged))
        Gates_6 = StudySpace("Gates 6", 1, 20, 2, 2, 2)
        Baker_5 = StudySpace("Baker 5", 0, 20, 0, 0, 0)
        Tepper_4 = StudySpace("Tepper 4", 2, 20, 1, 1, 1)
        Scaife_1 = StudySpace("Scaife 1", 1, 20, 2, 2, 2)
        Baker_1 = StudySpace("Baker 1", 0, 20, 0, 0, 0)
        Maggie_1 = StudySpace("Maggie Mo 1", 2, 20, 1, 1, 1)
        Scott_5 = StudySpace("Scott 5", 1, 20, 2, 2, 2)
        Newell_3 = StudySpace("Newell 3", 0, 20, 0, 0, 0)

        studyspaces = StudySpaceList()
        studyspaces.add_studyspace(Gates_6)
        studyspaces.add_studyspace(Baker_5)
        studyspaces.add_studyspace(Tepper_4)
        studyspaces.add_studyspace(Scaife_1)
        studyspaces.add_studyspace(Baker_1)
        studyspaces.add_studyspace(Maggie_1)
        studyspaces.add_studyspace(Scott_5)
        studyspaces.add_studyspace(Newell_3)
        avail = Availability_ListByDay(return_map)
        prefs = Prefs(1, 3, 900, 2100, 5, 2, 3)
        for day in avail.dailyfree:
            print(day)
            spaces, overall = search(avail.dailyfree[day], prefs, studyspaces)
            for i in range(0, len(overall)):
                print(f"Location: {spaces.study_spaces[i].get_overall()}, Score: {(overall[i])}")