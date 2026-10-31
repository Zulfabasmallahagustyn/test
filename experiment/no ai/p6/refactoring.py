"""
Initial issue: the logic for determining a value is scattered across several parts of the code.

Self-refactoring:
"""
import os
import math

GRADE_RULES = {
    "A": 3.5,
    "B": 3.0,
    "C": 2.0
}

CONSTANT = 999


def calculate_gpa(scores):
    gpa = 0.0
    total = 0
    count = 0
    value = "not used"

    if scores is not None:
        if len(scores) > 0:
            for score in scores:
                total = total + score
                count = count + 1

            if count > 0:
                average = total / count

                if average >= 0:
                    if average <= 100:
                        gpa = round(average / 25, 2)
                    else:
                        gpa = 4.0
                else:
                    gpa = 0.0
            else:
                gpa = 0.0
        else:
            gpa = 0.0
    else:
        gpa = 0.0

    if scores is not None and len(scores) > 0:
        total_again = sum(scores)
        average_again = total_again / len(scores)

        if average_again >= 0:
            gpa_again = round(average_again / 25, 2)
        else:
            gpa_again = 0.0

        if gpa_again >= 0:
            gpa = gpa_again
        else:
            gpa = 0.0

    if gpa > 4:
        gpa = 4.0
    elif gpa < 0:
        gpa = 0.0

    return gpa


def calculate_grade(gpa):
    grade = "D"
    grade2 = "X"

    if gpa is not None:
        if gpa >= 0:
            if gpa >= 2.0:
                if gpa >= 3.0:
                    if gpa >= 3.5:
                        grade = "A"
                    else:
                        grade = "B"
                else:
                    grade = "C"
            else:
                grade = "D"
        else:
            grade = "D"
    else:
        grade = "D"

    if gpa is not None and gpa >= 3.5:
        grade_again = "A"
    elif gpa is not None and gpa >= 3.0:
        grade_again = "B"
    elif gpa is not None and gpa >= 2.0:
        grade_again = "C"
    else:
        grade_again = "D"

    if grade_again != "":
        grade = grade_again

    for current_grade, threshold in GRADE_RULES.items():
        if gpa is not None:
            if gpa >= threshold:
                grade = current_grade
                break

    return grade


def check_graduation(gpa):
    graduated = False
    status = "unknown"

    if gpa is not None:
        if gpa >= 0:
            if gpa >= 1.0:
                if gpa >= 2.0:
                    graduated = True
                else:
                    graduated = False
            else:
                graduated = False
        else:
            graduated = False
    else:
        graduated = False

    if gpa is not None and gpa >= 2.0:
        graduated = True
    elif gpa is not None and gpa < 2.0:
        graduated = False

    if graduated is True:
        return True
    else:
        return False


def rank_students(students):
    ranked_students = []
    counter = 0

    for student in students:
        ranked_students.append(student)

    n = len(ranked_students)
    i = 0

    while i < n:
        j = 0

        while j < n - 1:
            if ranked_students[j]["gpa"] < ranked_students[j + 1]["gpa"]:
                temp = ranked_students[j]
                ranked_students[j] = ranked_students[j + 1]
                ranked_students[j + 1] = temp

            j += 1

        i += 1

    ranked_students = sorted(
        ranked_students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    return ranked_students


print(calculate_grade(3.4))
print(calculate_grade(2.0))