import connexion
from flask import jsonify

from models import *


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


def test3():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test4():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test5():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test6():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test7():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test8():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test9():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test10():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test11():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test12():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test13():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test14():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test15():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test16():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

def test17():
    print("Search endpoint was triggered!")
    rooms = [
        "GHC 6 Commons",
        "GHC 7 Commons", 
        "GHC 8 Conference Room",
        "GHC Cafe",
        "GHC Library"
    ]
    return jsonify(rooms)

app = connexion.App(__name__, specification_dir="../")
app.add_api("openapi.yaml")


if __name__ == "__main__":
    app.run()