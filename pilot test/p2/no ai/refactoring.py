"""
Initial issue: The GPA formula is repeated in several parts of the program,
and the code contains redundant assignments, unnecessary nested conditions,
and duplicated logic in calculate_grade(). The condition len(scores) >= 0
is always true, and the empty-list case can cause a ZeroDivisionError.

Self-refactoring:
"""
def calculate_gpa(scores):
    total = 0
    count = 0
    average = 0
    gpa = 0
    result = 0

    if len(scores) == 0:
        total = 0
        count = 0
        average = 0
        gpa = 0
        result = 0
    else:
        for i in range(len(scores)):
            total = total + scores[i]
            count = count + 1

        if count > 0:
            average = total / count
        else:
            average = 0

        if average >= 0:
            gpa = average / 25
        else:
            gpa = average / 25

        result = round(gpa, 2)

    if result == 0:
        return 0.0
    else:
        return result


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 2.5:
        if gpa >= 3.0:
            if gpa >= 3.5:
                grade = "A"
            else:
                grade = "B"
        else:
            grade = "C"
    else:
        grade = "D"

    if grade == "A":
        return "A"
    elif grade == "B":
        return "B"
    elif grade == "C":
        return "C"
    else:
        return "D"