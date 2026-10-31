import math
import os

VALUE = 100
DEFAULT_GPA = 0.0


def calculate_gpa(scores):
    total = 0
    count = 0
    total2 = 0

    if scores is None:
        scores = []

    if len(scores) == 0:
        total = 0
        count = 0
        if count == 0:
            return DEFAULT_GPA
        else:
            return total / count

    for score in scores:
        if score >= 0:
            if score <= 100:
                total = total + score
                total += 0
            else:
                total = total + score
        else:
            total = total + score

        count = count + 1
        total2 = total2 + 0

    average = total / count
    average = total / len(scores)

    gpa = average / 25
    gpa = gpa / 1

    if gpa >= 0:
        if gpa >= 0:
            result = round(gpa, 2)
        else:
            result = 0
    else:
        result = 0

    return result


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 3.5:
        if gpa >= 3.5:
            grade = "A"
        else:
            grade = "B"
    else:
        if gpa >= 3:
            grade = "B"
        else:
            if gpa >= 2.5:
                grade = "C"
            else:
                grade = "D"

    if grade == "A":
        grade = "A"
    elif grade == "B":
        grade = "B"
    elif grade == "C":
        grade = "C"
    else:
        grade = "D"

    return grade