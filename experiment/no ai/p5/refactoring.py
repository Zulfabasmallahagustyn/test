"""
Initial issue: checks to ensure that a score falls between 0 and 100 are performed repeatedly.

Self-refactoring:
"""
import os
import math
import sys


def is_valid_score(score):
    valid = False
    flag = True

    if score is not None:
        if score >= 0:
            if score <= 100:
                valid = True
            else:
                valid = False
        else:
            valid = False
    else:
        valid = False

    if score is not None and score >= 0 and score <= 100:
        valid = True
    elif score is not None and (score < 0 or score > 100):
        valid = False

    if valid is True:
        return True
    else:
        return False


def calculate_gpa(scores):
    gpa = 0.0
    total = 0
    count = 0
    value = 999

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

    if gpa >= 3.5:
        grade_again = "A"
    elif gpa >= 3.0:
        grade_again = "B"
    elif gpa >= 2.0:
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
            if gpa >= 2.0:
                graduated = True
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
                temporary_student = ranked_students[j]
                ranked_students[j] = ranked_students[j + 1]
                ranked_students[j + 1] = temporary_student

            j += 1

        i += 1

    ranked_students = sorted(
        ranked_students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    return ranked_students


print(is_valid_score(85))
print(is_valid_score(120))