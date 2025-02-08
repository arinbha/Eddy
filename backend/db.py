from typing import Optional

from backend.calprocessor import Schedule
from models import *


def login(user, password) -> Optional[User]:
    pass


def new_user(user, password) -> User:
    pass


def get_user(id: int) -> User:
    pass


def get_user_groups(user_id: int) -> list[Group]:
    pass


def new_user_group(user_id: int, group: Group) -> Group:
    pass


def update_group_prefs(group_id: int, prefs: Prefs) -> Prefs:
    pass


def user_prefs(user_id: int) -> Prefs:
    pass


def user_schedule(user_id: int) -> Schedule:
    pass


def update_user_schedule(user_id: int, schedule: Schedule) -> Schedule:
    pass


def user_next_event(user_id: int) -> StudyEvent:
    pass



def search(availability: Availability_ListByDay, pref: Prefs, id: int, is_group: bool) -> StudySpaceList:
    reports = ReportList
    spaces = StudySpaceList
    spaces.update_status(reports)

    def find_zone_list(availability, query_start, query_end):
        overlapping_zones = []
        for start, end, zones in availability:
            if not (query_end <= start or query_start >= end):
                overlapping_zones += list(zones)
        return list(set(overlapping_zones))
    
    zones = find_zone_list(availability, pref.start_time, pref.end_time)

    def calculate_score(space, pref, zones):
        score = 0
        pref_seating = pref.seating_type
        actual_seating = space.seating_type
        if pref_seating == 2 or actual_seating == 2:
            score += 0
        else:
            score += abs(pref_seating - actual_seating)




    score_map = {}
    for space in spaces:
        socre 

    


def book(study_event: StudyEvent, id, is_group) -> StudyEvent:
    pass


def update_status(space: StudySpace):
    pass
