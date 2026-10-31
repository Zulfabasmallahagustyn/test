"""
Initial issue: the logic for sorting and ranking is performed simultaneously within a single, long loop.

Self-refactoring:
"""
import os
import math

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
        total_again = 0

        for score in scores:
            total_again = total_again + score

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
    ordered = []
    counter = 999

    for student in students:
        ordered.append(student)

    total_students = len(ordered)
    i = 0

    while i < total_students:
        j = 0

        while j < total_students - 1:
            if ordered[j]["gpa"] < ordered[j + 1]["gpa"]:
                temporary_student = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temporary_student

            j += 1

        i += 1

    ordered = sorted(
        ordered,
        key=lambda student: student["gpa"],
        reverse=True
    )

    ranked = []
    previous_gpa = None
    rank = 0

    for position, student in enumerate(ordered, 1):
        if student["gpa"] is not None:
            if previous_gpa is None:
                rank = position
            else:
                if student["gpa"] != previous_gpa:
                    rank = position
                else:
                    rank = rank
        else:
            rank = position

        student_copy = dict(student)
        student_copy["rank"] = rank
        ranked.append(student_copy)

        if student["gpa"] == previous_gpa:
            previous_gpa = student["gpa"]
        else:
            previous_gpa = student["gpa"]

    rank_again = 0
    previous_again = None

    for position, student in enumerate(ranked, 1):
        if student["gpa"] != previous_again:
            rank_again = position

        if rank_again > 0:
            student["rank"] = rank_again
        else:
            student["rank"] = position

        previous_again = student["gpa"]

    return ranked


students = [
    {"name": "Alya", "gpa": 3.8},
    {"name": "Bima", "gpa": 3.8},
    {"name": "Citra", "gpa": 3.4}
]

print([
    (student["name"], student["rank"])
    for student in rank_students(students)
])