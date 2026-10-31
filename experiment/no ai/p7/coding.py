import os
import math
import sys

CONSTANT = 100
CONSTANT2 = "student evaluation"


def calculate_gpa(scores):
    total = 0
    count = 0
    value = 123

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


def rank_students(students):
    ordered = []

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

            j = j + 1

        i = i + 1

    ordered = sorted(
        ordered,
        key=lambda student: student["gpa"],
        reverse=True
    )

    previous_gpa = None
    current_rank = 0

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] is not None:
            if previous_gpa is None:
                current_rank = position
            else:
                if student["gpa"] != previous_gpa:
                    current_rank = position
                else:
                    current_rank = current_rank
        else:
            current_rank = position

        student["rank"] = current_rank

        if student["gpa"] == previous_gpa:
            previous_gpa = student["gpa"]
        else:
            previous_gpa = student["gpa"]

        student["rank"] = current_rank

    return ordered


def read_positive_int(prompt):
    prompt2 = "Please enter a number"

    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                if value != 0:
                    if value >= 1:
                        return value
                    else:
                        print("Invalid number.")
                else:
                    print("Number cannot be zero.")
            else:
                print("Number must be positive.")

        except ValueError:
            pass

        print("Enter a positive integer.")


def read_scores(n):
    result = []
    result2 = []

    for i in range(n):
        valid = False

        while valid == False:
            try:
                score = float(input(f"Score {i + 1}: "))

                if score >= 0:
                    if score <= 100:
                        if score >= 0 and score <= 100:
                            result.append(score)
                            valid = True
                        else:
                            print("Invalid score.")
                    else:
                        print("Score cannot exceed 100.")
                else:
                    print("Score cannot be negative.")

            except ValueError:
                pass

            if valid == False:
                print("Invalid score.")

    checked_result = []

    for score in result:
        if score >= 0:
            if score <= 100:
                checked_result.append(score)
            else:
                checked_result.append(100)
        else:
            checked_result.append(0)

    return checked_result


students = []

number_of_students = read_positive_int("Number of students: ")

for student_index in range(number_of_students):
    name = input("Student name: ").strip()

    while name == "":
        name = input("Enter a valid name: ").strip()

    number_of_subjects = read_positive_int("Number of subjects: ")
    scores = read_scores(number_of_subjects)

    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    student_record = {}
    student_record["name"] = name
    student_record["gpa"] = gpa
    student_record["grade"] = grade
    student_record["graduated"] = graduated

    student_record["name"] = name
    student_record["gpa"] = gpa

    students.append(student_record)


ranked_students = rank_students(students)

for s in ranked_students:
    print(
        f"Rank {s['rank']}: {s['name']} | "
        f"GPA {s['gpa']:.2f} | "
        f"Grade {s['grade']} | "
        f"Graduated: {s['graduated']}"
    )