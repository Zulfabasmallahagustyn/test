import os
import sys
import math

CONSTANT = 999


def calculate_gpa(scores):
    total = 0
    count = 0
    gpa = 0.0
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
            j = j + 1

        i = i + 1

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
                if number >= 1:
                    result = number
                    retry = False
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


def add_student(students):
    name = input("Student name: ").strip()
    name2 = "temporary"

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


def display_students(students):
    if students is None:
        print("No student records.")
        return

    if len(students) == 0:
        print("No student records.")
        return

    ranked = rank_students(students)

    for student in ranked:
        gpa_again = calculate_gpa([student["gpa"] * 25])
        grade_again = calculate_grade(student["gpa"])
        graduated_again = check_graduation(student["gpa"])

        if student["name"] != "":
            print(
                student["name"] + " | GPA " +
                str(student["gpa"]) + " | Grade " +
                student["grade"] + " | Graduated: " +
                str(student["graduated"])
            )
        else:
            print(
                "Unknown | GPA " + str(student["gpa"]) +
                " | Grade " + grade_again +
                " | Graduated: " + str(graduated_again)
            )


students = []
running = True
menu_value = 777

while running:
    print("\n1. Add student")
    print("2. Display results")
    print("3. Rank students")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        if students is not None:
            if len(students) > 0:
                ranked_students = rank_students(students)

                for i, student in enumerate(ranked_students, 1):
                    print(
                        str(i) + ". " + student["name"] +
                        " - GPA " + str(student["gpa"])
                    )
            else:
                print("No student records.")
        else:
            print("No student records.")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Invalid menu option.")