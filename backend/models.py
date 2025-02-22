import json

zones = {"Ansys" : 1, "Scaife" : 1, "Scott" : 2, "Hammerschlag" : 2, "Wean" : 2, "Doherty" : 2, "Gates" : 3, "Newell" : 3, 
"Tepper" : 4, "Porter" : 5, "Baker" : 5, "CUC" : 6, "Maggie Mo" : 6, "Posner" : 6}

places = {"Gates 6" : "Gates", "Gates 5" : "Gates", "Gates 4" : "Gates", "Gates 3" : "Gates", "Gates 2" : "Gates", 
          "Gates 1" : "Gates", "Gates 7" : "Gates", "Baker 5" : "Baker", "Tepper 4" : "Tepper",
          "Scaife 1" : "Scaife", "Baker 1" : "Baker", "Maggie Mo 1": "Maggie Mo", "Scott 5" : "Scott", "Newell 3" : "Newell"}

seating_type = {0: "Couches", 1 : "Tables", 2: "Both"}
levels = {0: "Low", 1: "Medium", 2: "High"}

class StudySpace:
    def __init__(self, loc, seat, capacity, noise, foot_traffic, crowdedness):
        self.overall = loc
        self.location = places[str(loc)]
        self.opcode = zones[str(places[loc])]
        self.seating_type = seat
        self.capacity = capacity
        self.noise = noise
        self.foot_traffic = foot_traffic
        self.crowdedness = crowdedness
    def get_overall(self):
        return self.overall
    def get_seatingtype(self):
        return self.seating_type
    def get_capacity(self):
        return self.capacity
    def get_noise(self):
        return self.noise
    def get_foottraffic(self):
        return self.foot_traffic
    def get_crowdedness(self):
        return self.crowdedness
    def update_noise(self, noise):
        self.noise = noise
    def update_foottraffic(self, foot_traffic):
        self.foot_traffic = foot_traffic
    def update_crowdedness(self, crowdedness):
        self.crowdedness = crowdedness
    def print_study_space(self):
        print(self.overall)

class StudySpaceList:
    def __init__(self):
        self.study_spaces = []
    def add_studyspace(self, study_space):
        (self.study_spaces).append(study_space)
    def update_list(self, reports):
        pass
    def print_list(self):
        for space in self.study_spaces:
            space.print_study_space()

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    def to_json(self):
        return json.dumps(self.__dict__)


class Group:
    def __init__(self, id, user_list, prefs):
        self.id = id
        self.user_list = user_list
        self.prefs = prefs


class Prefs:
    def __init__(self, seating_type, size, start_time, end_time, noise, foot_traffic, crowdedness):
        self.seating_type = seating_type
        self.size = size
        self.start_time = start_time
        self.end_time = end_time
        self.noise = noise
        self.foot_traffic = foot_traffic
        self.crowdedness = crowdedness

class RoomStatus:
    def __init__(self, study_space, ppl_count, noise, foot_traffic, crowdedness):
        self.study_space = study_space
        self.ppl_count = ppl_count
        self.noise = noise
        self.foot_traffic = foot_traffic
        self.crowdedness = crowdedness

class ReportList:
    def __init__(self, reports: list[tuple[int, RoomStatus]]):
        self.reports = reports


class StudyEvent:
    def __init__(self, location, start_time, end_time):
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

class Availability_Map:
    def __init__(self, availability):
        self.availability = availability

class Availability_ListByDay:
    def __init__(self, dailyfree):
        self.dailyfree = dailyfree
