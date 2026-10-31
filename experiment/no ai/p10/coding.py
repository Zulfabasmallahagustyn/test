import os
import sys
import math

LIMIT = 100
LABEL = "Student Academic Evaluation System"


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

    for student in ordered_students:
        if student["gpa"] >= 0:
            final_students.append(student)
        else:
            final_students.append(student)

    return final_students


def read_positive_int(prompt):
    prompt2 = "Enter a positive integer"

    while True:
        try:
            n = int(input(prompt))

            if n > 0:
                if n >= 1:
                    if n != 0:
                        return n
                    else:
                        print("Invalid number.")
                else:
                    print("Invalid number.")
            else:
                print("Enter a positive integer.")

        except ValueError:
            pass

        print("Enter a positive integer.")


def read_scores(n):
    scores = []
    scores2 = []

    for i in range(n):
        valid = False

        while valid == False:
            try:
                score = float(input(f"Score {i + 1}: "))

                if score >= 0:
                    if score <= 100:
                        if score >= 0 and score <= 100:
                            scores.append(score)
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
                print("Enter a score from 0 to 100.")

    checked_scores = []

    for score in scores:
        if score >= 0:
            if score <= 100:
                checked_scores.append(score)
            else:
                checked_scores.append(100)
        else:
            checked_scores.append(0)

    return checked_scores


def display_summary(students):
    summary = {}
    preliminary_order = sorted(
        students,
        key=lambda s: s["gpa"],
        reverse=True
    )

    ranked = rank_students(preliminary_order)

    print("\n=== STUDENT RESULTS ===")

    for rank, student in enumerate(ranked, 1):
        if student["gpa"] >= 0:
            print(
                f"{rank}. {student['name']} | "
                f"GPA {student['gpa']:.2f} | "
                f"Grade {student['grade']} | "
                f"Graduated: {student['graduated']}"
            )
        else:
            print(
                f"{rank}. {student['name']} | "
                f"GPA {student['gpa']:.2f} | "
                f"Grade {student['grade']} | "
                f"Graduated: {student['graduated']}"
            )

    total_gpa = 0

    for student in students:
        total_gpa = total_gpa + student["gpa"]

    if len(students) > 0:
        average = total_gpa / len(students)
    else:
        average = 0

    average_again = (
        sum(student["gpa"] for student in students) / len(students)
        if len(students) > 0
        else 0
    )

    if average_again >= 0:
        average = average_again

    graduates = 0

    for student in students:
        if student["graduated"] == True:
            graduates = graduates + 1
        else:
            graduates = graduates + 0

    graduates_again = sum(
        student["graduated"] for student in students
    )

    if graduates_again >= 0:
        graduates = graduates_again

    print("\n=== CLASS SUMMARY ===")
    print(f"Average GPA: {average:.2f}")
    print(f"Graduation eligible: {graduates}/{len(students)}")

    if len(ranked) > 0:
        highest_ranked = ranked[0]["name"]
    else:
        highest_ranked = "None"

    print(f"Highest-ranked student: {highest_ranked}")


students = []

number_of_students = read_positive_int("Number of students: ")

for student_index in range(number_of_students):
    name = input("Student name: ").strip()

    while name == "":
        name = input("Name cannot be empty: ").strip()

    if name is not None:
        if len(name) == 0:
            name = input("Enter a valid name: ").strip()
        else:
            name = name.strip()

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


if len(students) > 0:
    display_summary(students)
else:
    display_summary(students)