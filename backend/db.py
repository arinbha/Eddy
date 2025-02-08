import sqlite3
from typing import Optional

from calprocessor import Schedule
from models import *
from calprocessor import *


conn: Optional[sqlite3.Connection] = None

DEAD = 1000000
USER_ID = 0
GROUP_ID = 0

default_prefs = Prefs(0, 0, 0, 0, 0, 0, 0)
default_schedule = Schedule()

def init_db():
    global conn
    conn = sqlite3.connect('db.sqlite')

username_password_map = {}
id_user_map = {}
id_userpref_map = {}
id_schedule_map = {}
id_studyevent_map = {}
id_group_map = {}

def login(user, password) -> Optional[User]:
    res = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, password))
    res = res.fetchone()

    if res is None:
        return None

    return User(res[0], res[1], "")


def new_user(username, password) -> User:
    username_password_map[username] = password
    user = User(USER_ID, username, password)
    id_user_map[USER_ID] = user
    id_userpref_map[USER_ID] = default_prefs
    id_schedule_map[USER_ID] = default_schedule
    USER_ID = USER_ID + 1
    return user


def get_user(id: int) -> User:
    return id_user_map[id]


def get_user_groups(user_id: int) -> list[Group]:
    groups = []
    for id in id_group_map:
        group = id_group_map[id]
        users_list = group.user_list
        for user in users_list:
            if user.id == user_id:
                groups.append(group)
    return groups


def new_user_group(user_id: int, group: Group) -> Group:
    id = GROUP_ID
    GROUP_ID = GROUP_ID + 1
    user = id_user_map[user_id]
    user_list = [user]
    group = Group(id, user_list, default_prefs)
    id_group_map[id] = group
    return group


def update_group_prefs(group_id: int, prefs: Prefs) -> Prefs:
    group = id_group_map[group_id]
    group.prefs = prefs
    id_group_map[group_id] = group
    return prefs


def user_prefs(user_id: int) -> Prefs:
    return id_userpref_map[user_id]


def user_schedule(user_id: int) -> Schedule:
    return id_schedule_map[user_id]


def update_user_schedule(user_id: int, schedule: Schedule) -> Schedule:
    id_schedule_map[user_id] = schedule
    return schedule

def book(study_event: StudyEvent, id, is_group) -> StudyEvent:
    if not is_group:
        schedule = id_schedule_map[id]
        new_event = Event("Dummy")
        today = datetime.datetime.now()
        day_name = today.strftime("%A")
        new_event.days = [day_name]
        new_event.location = study_event.location
        new_event.start = study_event.start_time
        new_event.end = study_event.end_time
        schedule.join(new_event)
        id_schedule_map[id] = schedule
    else:
        group = id_group_map[id]
        for user in group.user_list:
            user_id = user.id
            schedule = id_schedule_map[user_id]
            new_event = Event("Dummy")
            today = datetime.datetime.now()
            day_name = today.strftime("%A")
            new_event.days = [day_name]
            new_event.location = study_event.location
            new_event.start = study_event.start_time
            new_event.end = study_event.end_time
            schedule.join(new_event)
            id_schedule_map[user_id] = schedule



def user_next_event(user_id: int) -> StudyEvent:
    schedule = id_schedule_map[user_id]


def get_reports_list() -> ReportList:
    pass


def get_study_spaces() -> StudySpaceList:
    pass



def search(availability, pref, spaces) -> StudySpaceList:    
    def find_zone_list(availability, query_start, query_end):
        overlapping_zones = []
        for start, end, zones in availability:
            if not (query_end <= start or query_start >= end):
                overlapping_zones += list(zones)
        return list(set(overlapping_zones))
    
    zones = find_zone_list(availability, pref.start_time, pref.end_time)

    def calculate_score(space, pref, zones):
        overall_score = 0
        pref_seating = pref.seating_type
        actual_seating = space.seating_type
        if pref_seating == 2 or actual_seating == 2:
            overall_score += 0
        else:
            overall_score += abs(int(pref_seating) - int(actual_seating))
        if pref.size > space.capacity:
            overall_score += DEAD
        overall_score += int(space.noise) * pref.noise
        overall_score += int(space.foot_traffic) * pref.foot_traffic
        overall_score += int(space.crowdedness) * pref.crowdedness
        location = space.opcode
        res = []
        for zone in zones:
            res.append(abs(location - zone))
        best_zone = min(res) * DEAD // 2
        return overall_score, best_zone
    
    score_map = {}
    zone_map = {}
    for space in spaces.study_spaces:
        overall, zonescore = calculate_score(space, pref, zones)
        score_map[space] = overall
        zone_map[space] = zonescore
    zone_map = dict(sorted(zone_map.items(), key=lambda x: x[1]))
    best_spaces_by_zone = []
    for space in zone_map:
        if (zone_map[space]) == 0 or len(best_spaces_by_zone) < 5:
            best_spaces_by_zone.append(space)
    best_spaces_by_score = []
    for space in best_spaces_by_zone:
        best_spaces_by_score.append((space, score_map[space]))
    
    best_spaces_by_score.sort(key=lambda x: x[1])

    final_list = StudySpaceList()
    score_list = []
    for elem in best_spaces_by_score:
        final_list.add_studyspace(elem[0])
        score_list.append(elem[1])
    return final_list, score_list


def update_status(space: StudySpace):
    pass
