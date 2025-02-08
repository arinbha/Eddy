from ics import Calendar
import sys
from datetime import datetime

start = 900
end = 2100

zones = {"Ansys" : 1, "Scaife" : 1, "Scott" : 2, "Hammerschlag" : 2, "Wean" : 2, "Doherty" : 2, "Gates" : 3, "Newell" : 3, 
"Porter" : 4, "Baker" : 4, "CUC" : 5, "Maggie Mo" : 5, "Posner" : 5, "Tepper" : 6}

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
        begin = begin.strftime("%-I:%M %p")

        end = (((str(event.end)).split('T'))[1]).split("+")[0]
        end = datetime.strptime(end, "%H:%M:%S")
        end = end.strftime("%-I:%M %p")

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
         (d[day]).append([int(convert_timestamp(event.start)), int(convert_timestamp(event.end))])
   return d

def find_start_zones_codes(schedule, d):
   for event in schedule.list_of_classes:
      for day in event.days:
         if int(convert_timestamp(event.start)) not in d[day]:
             (d[day])[int(convert_timestamp(event.start))] = []
             (d[day])[int(convert_timestamp(event.start))].append(zones[event.location])
         if (zones[event.location]) not in (d[day])[int(convert_timestamp(event.start))]:
            (d[day])[int(convert_timestamp(event.start))].append(zones[event.location])
   return d

def find_end_zones_codes(schedule, d):
   for event in schedule.list_of_classes:
      for day in event.days:
         if int(convert_timestamp(event.end)) not in d[day]:
             (d[day])[int(convert_timestamp(event.end))] = []
             (d[day])[int(convert_timestamp(event.end))].append(zones[event.location])
         if (zones[event.location]) not in (d[day])[int(convert_timestamp(event.end))]:
            (d[day])[int(convert_timestamp(event.end))].append(zones[event.location])
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
        range = free_times[0]
        for elem in free_times:
            range = find_available_times(range, elem, start, end)
        return_map = {}
        for day in range:
           return_map[day] = []
           intervals = range[day]
           for start,end in intervals:
              end_locs = end_map.get(day, []).get(start, [])
              start_locs = start_map.get(day, []).get(end, [])
              merged = end_locs + start_locs
              merged = set(merged)
              return_map[day].append((start, end, merged))
        print(return_map)