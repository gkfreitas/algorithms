def study_schedule(permanence_period, target_time):
    if (target_time is None):
        return None
    students = 0
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        time = list(range(student[0], student[1] + 1))
        if target_time in time:
            students += 1
    return students
