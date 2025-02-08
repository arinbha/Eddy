zones = {"Ansys" : 1, "Scaife" : 1, "Scott" : 2, "Hammerschlag" : 2, "Wean" : 2, "Doherty" : 2, "Gates" : 3, "Newell" : 3, 
"Porter" : 4, "Baker" : 4, "CUC" : 5, "Maggie Mo" : 5, "Posner" : 5, "Tepper" : 6}

seating_type = {0: "Couches", 1 : "Tables", 2: "Both"}

class StudySpace:
    def __init__(self, location, seat, capacity, noise, foot_traffic, crowdedness):
        self.location = location
        self.opcode = zones[location]
        self.seating_type = seating_type[seat]
        self.capacity = capacity
        self.noise = noise
        self.foot_traffic = foot_traffic
        self.crowdedness = crowdedness

Gates_6 = StudySpace("Gates", 2, 20, "Loud", "High", "High")
