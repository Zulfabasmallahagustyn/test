import os
import sys
import math

LIMIT = 100
LABEL = "Student Academic Evaluation System"


def calculate_gpa(scores):
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
        key=lambda student: student["gpa"],
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
    prompt2 = "Enter a positive number"

    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                if value >= 1:
                    if value != 0:
                        return value
                    else:
                        print("Invalid number.")
                else:
                    print("Invalid number.")
            else:
                print("Enter a positive integer.")

        except ValueError:
            pass

        print("Enter a positive integer.")


def input_scores():
    n = read_positive_int("Number of subjects: ")
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
                print("Invalid score.")

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


def input_student():
    name = input("Student name: ").strip()
    name2 = "Unknown"

    while name == "":
        name = input("Name cannot be empty: ").strip()

    if name is not None:
        if len(name) == 0:
            name = input("Enter a valid name: ").strip()
        else:
            name = name.strip()

    scores = input_scores()
    gpa = calculate_gpa(scores)

    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    if gpa >= 0:
        grade = calculate_grade(gpa)

    if gpa >= 2.0:
        graduated = True
    else:
        graduated = False

    student = {}
    student["name"] = name
    student["gpa"] = gpa
    student["grade"] = grade
    student["graduated"] = graduated

    student["name"] = name
    student["gpa"] = gpa

    return student


def display_results(students):
    counter = 0

    preliminary_order = sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    ranked_students = rank_students(preliminary_order)

    for rank, student in enumerate(ranked_students, 1):
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

        counter = counter + 1


def main():
    main_value = True

    number_of_students = read_positive_int("Number of students: ")

    students = []

    for _ in range(number_of_students):
        student = input_student()
        students.append(student)

    if len(students) > 0:
        display_results(students)
    else:
        display_results(students)


if __name__ == "__main__":
    main()