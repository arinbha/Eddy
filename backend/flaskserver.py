import connexion
from flask import jsonify

from models import *
from calprocessor import *


def search():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def login():
    print("Login endpoint was triggered!")
    user = User(101, "arinb", "dummy")
    return user.__dict__

def newuser():
    print("New User endpoint was triggered!")
    user = User(101, "arinb", "dummy")
    return user.__dict__

def userId(userId):
    print("User ID endpoint was triggered!")
    user = User(userId, "arinb", "dummy")
    return user.__dict__

def userIdgroups(userId):
    print("User ID group endpoint was triggered!")
    group = Group(userId, [], [])
    return group.__dict__

def userIdgroupsnew(userId):
    print("User ID group new endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdgroupsgroupId(userId, groupId):
    print("User ID group groupId endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdgroupsgroupIddelete(userId, groupId):
    print("User ID group groupId delete endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdgroupsjoin(userId):
    print("User ID group join endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdpostprefs(userId):
    print("User ID post prefs endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdgetprefs(userId):
    print("User ID get prefs endpoint was triggered!")
    prefs = Prefs(1, 10, 930, 1230, 3, 3, 3)
    return prefs.__dict__

def userIdgetschedule(userId):
    print("User ID get prefs endpoint was triggered!")
    schedule = Schedule()
    schedule.join(Event("AI").__dict__)
    return schedule.__dict__

def userIdpostschedule(userId):
    print("User ID post prefs endpoint was triggered!")
    schedule = Schedule()
    schedule.join(Event("AI").__dict__)
    return schedule.__dict__

def userIdscheduleics(userId):
    print("User ID schedule ics was triggered!")
    return jsonify("ICS")

def userIdnextevent(userId):
    print("User ID next event was triggered!")
    class Test():
        def __init__(self, start_time, end_time, location):
            self.start_time = start_time
            self.end_time = end_time
            self.location = location
    test = Test("09:30", "12:30", "Posner")
    return test.__dict__

def book():
    print("Book event was triggered!")
    return jsonify("Book")

def update_status():
    print("Update Status event was triggered!")
    return jsonify("Update Status")

app = connexion.App(__name__, specification_dir="../")
app.add_api("openapi.yaml")


if __name__ == "__main__":
    app.run()