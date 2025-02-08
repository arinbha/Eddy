zones = {"Ansys" : 1, "Scaife" : 1, "Scott" : 2, "Hammerschlag" : 2, "Wean" : 2, "Doherty" : 2, "Gates" : 3, "Newell" : 3, 
"Tepper" : 4, "Porter" : 5, "Baker" : 5, "CUC" : 6, "Maggie Mo" : 6, "Posner" : 6}

seating_type = {0: "Couches", 1 : "Tables", 2: "Both"}
levels = {0: "Low", 1: "Medium", 2: "High"}

class StudySpace:
    def __init__(self, location, seat, capacity, noise, foot_traffic, crowdedness):
        self.location = location
        self.opcode = zones[location]
        self.seating_type = seating_type[seat]
        self.capacity = capacity
        self.noise = noise
        self.foot_traffic = foot_traffic
        self.crowdedness = crowdedness
    def get_noise(self):
        return self.location
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

class StudySpaceList:
    def __init__(self):
        self.study_spaces = []
    def add_studyspace(self, study_space):
        self.study_spaces.append(study_space)
    def update_list(self, reports):
        pass

class User:
    def _init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


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
    def __init__(self):
        # TODO
        pass

class ReportList:
    def __init__(self):
        # TODO
        pass



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


Gates_6 = StudySpace("Gates", 2, 20, "Loud", "High", "High")