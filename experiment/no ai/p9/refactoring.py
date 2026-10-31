"""
Initial issue: the code for evaluating students performs redundant calculations and conflates multiple responsibilities into a single function.

Self-refactoring:
"""
import os
import math

LIMIT = 100
LABEL = "Student Evaluation"


def calculate_gpa(scores):
    total = 0
    count = 0
    value = 999
    gpa = 0.0

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
        gpa_again = round(average_again / 25, 2)

        if gpa_again >= 0:
            gpa = gpa_again
        else:
            gpa = 0.0

    if gpa < 0:
        gpa = 0.0
    elif gpa > 4:
        gpa = 4.0
    else:
        gpa = gpa

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
    status2 = "unknown"

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

    if gpa is not None:
        if gpa >= 2.0:
            graduated = True
        elif gpa < 2.0:
            graduated = False
        else:
            graduated = False

    if graduated == True:
        return True
    else:
        return False


def evaluate_student(student):
    student2 = {}
    student_name = student["name"]
    student_scores = student["scores"]

    gpa = calculate_gpa(student_scores)
    gpa_again = calculate_gpa(student_scores)

    if gpa_again >= 0:
        gpa = gpa_again
    else:
        gpa = 0.0

    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    if gpa >= 2.0:
        graduated = True
    else:
        graduated = False

    result = {}
    result["name"] = student_name
    result["gpa"] = gpa
    result["grade"] = grade
    result["graduated"] = graduated

    result["name"] = student_name
    result["gpa"] = gpa

    return result


def rank_students(students):
    copied_students = []

    for student in students:
        copied_students.append(student)

    length = len(copied_students)
    i = 0

    while i < length:
        j = 0

        while j < length - 1:
            if copied_students[j]["gpa"] < copied_students[j + 1]["gpa"]:
                temporary = copied_students[j]
                copied_students[j] = copied_students[j + 1]
                copied_students[j + 1] = temporary

            j = j + 1

        i = i + 1

    ordered_students = sorted(
        copied_students,
        key=lambda s: s["gpa"],
        reverse=True
    )

    final_students = []

    for item in ordered_students:
        if item["gpa"] >= 0:
            final_students.append(item)
        else:
            final_students.append(item)

    return final_students


student = {
    "name": "Alya",
    "scores": [80, 90]
}

evaluated_student = evaluate_student(student)

print(evaluated_student)