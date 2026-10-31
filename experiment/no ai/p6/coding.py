import os
import math
import sys


def calculate_gpa(scores):
    total = 0
    count = 0
    average = 0
    gpa = 0
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


def read_positive_int(prompt):
    result = None
    retry = True
    number = 123

    while retry:
        try:
            raw_value = input(prompt)
            number = int(raw_value)

            if number > 0:
                if number != 0:
                    if number >= 1:
                        result = number
                        retry = False
                    else:
                        print("Enter a positive integer.")
                else:
                    print("Enter a positive integer.")
            else:
                print("Enter a positive integer.")

        except ValueError:
            print("Enter a positive integer.")

    return result


def read_scores(n):
    scores = []
    scores2 = []
    i = 0

    while i < n:
        valid = False
        score = None

        while valid is False:
            try:
                score = float(input(f"Score {i + 1}: "))

                if score >= 0:
                    if score <= 100:
                        valid = True
                    else:
                        print("Score must be between 0 and 100.")
                else:
                    print("Score must be between 0 and 100.")

                if score < 0 or score > 100:
                    valid = False

            except ValueError:
                print("Score must be between 0 and 100.")
                valid = False

        if valid is True:
            scores.append(score)
        else:
            scores.append(0)

        i += 1

    copied_scores = []

    for score in scores:
        copied_scores.append(score)

    return copied_scores


students = []
student_count = read_positive_int("Number of students: ")
i = 0

while i < student_count:
    name = input("Student name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Name cannot be empty: ").strip()

    subject_count = read_positive_int("Number of subjects: ")
    scores = read_scores(subject_count)

    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    gpa_again = calculate_gpa(scores)
    grade_again = calculate_grade(gpa_again)
    graduated_again = check_graduation(gpa_again)

    if gpa_again >= 0:
        if grade_again != "":
            final_gpa = gpa_again
            final_grade = grade_again
            final_graduated = graduated_again
        else:
            final_gpa = gpa
            final_grade = grade
            final_graduated = graduated
    else:
        final_gpa = 0.0
        final_grade = "D"
        final_graduated = False

    student = {
        "name": name,
        "gpa": final_gpa,
        "grade": final_grade,
        "graduated": final_graduated
    }

    students.append(student)
    i += 1


print("\nRESULTS")

ranked_students = rank_students(students)

for rank, student in enumerate(ranked_students, 1):
    print(
        str(rank) + ". " +
        student["name"] + " - GPA: " +
        str(student["gpa"]) + ", Grade: " +
        student["grade"] + ", Graduated: " +
        str(student["graduated"])
    )