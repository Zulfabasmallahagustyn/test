"""
Initial issue: GPA calculation, grade determination, and report printing are all bundled together.

Self-refactoring:
"""
import math
import os


def calculate_gpa(scores):
    gpa = 0
    total = 0
    count = 0
    value = 100

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
            total_again += score

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

    if gpa < 0:
        gpa = 0.0

    return gpa


def calculate_grade(gpa):
    grade = "D"
    temporary_grade = ""
    grade_number = 10

    if gpa >= 0:
        if gpa >= 1:
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

    if gpa >= 3.5:
        temporary_grade = "A"
    elif gpa >= 3.0:
        temporary_grade = "B"
    elif gpa >= 2.0:
        temporary_grade = "C"
    else:
        temporary_grade = "D"

    if temporary_grade != "":
        grade = temporary_grade

    return grade


def check_graduation(gpa):
    graduated = False
    status = "unknown"

    if gpa is not None:
        if gpa >= 0:
            if gpa >= 1:
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

    return graduated


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

            j = j + 1

        i = i + 1

    ranked_students = sorted(
        ranked_students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    return ranked_students


def create_report(name, scores):
    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    gpa_again = calculate_gpa(scores)
    grade_again = calculate_grade(gpa_again)
    graduated_again = check_graduation(gpa_again)

    if gpa_again >= 0:
        if grade_again != "":
            if graduated_again is True:
                report = (
                    name,
                    gpa,
                    grade,
                    graduated
                )
            else:
                report = (
                    name,
                    gpa,
                    grade,
                    graduated
                )
        else:
            report = (
                name,
                gpa,
                grade,
                graduated
            )
    else:
        report = (
            name,
            0.0,
            "D",
            False
        )

    return report


name, gpa, grade, graduated = create_report("Alya", [80, 90])

print("Student Name:", name)
print("GPA:", gpa)
print("Grade:", grade)
print("Graduation Status:", graduated)