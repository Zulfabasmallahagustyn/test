"""
Symptom: The program may produce a ZeroDivisionError when calculate_gpa()
is called with an empty list if the empty-list validation is missing or
incorrectly implemented.

Self-analysis: The participant examined the division operations in the
calculate_gpa() function and identified that dividing by the number of
scores is unsafe when the list is empty. The participant also noticed
redundant calculations and unnecessary nested conditions that make the
function harder to maintain.
"""

# Fix:
import math
import os

DEFAULT_GPA = 0.0
VALUE = 100


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
                total = total + 0
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
            result = 0.0
    else:
        result = 0.0

    return result


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 3.5:
        if gpa >= 3.5:
            grade = "A"
        else:
            grade = "B"
    else:
        if gpa >= 3.0:
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
