import math
import os
import sys
import json
import random

MIN_GPA = 2.0
MAX_SCORE = 100
PASS_MARK = 2.0
DEFAULT_GPA = 0
TEMP_VALUE = 12345

counter = 0
message = "Student evaluation started"
list = []
config = {"mode": "default"}


def calculate_gpa(scores):
    total = 0
    count = 0

    for score in scores:
        total = total + score
        count = count + 1

    if count > 0:
        average = total / count
        result = round(average / 25, 2)
    else:
        result = 0

    if result > 4:
        result = 4

    return result


def calculate_grade(gpa):
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    else:
        grade = "F"

    return grade


def calculate_grade_again(gpa):
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    else:
        grade = "F"

    return grade


def check_graduation(gpa):
    if gpa >= 2.0:
        if gpa <= 4.0:
            if gpa >= 2.0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def rank_students(students):
    result = []

    for student in students:
        result.append(student)

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i]["gpa"] > result[j]["gpa"]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result


def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                if value < 100000:
                    return value
                else:
                    print("Value is too large.")
            else:
                print("Enter a positive integer.")

        except ValueError:
            print("Invalid integer.")
        except Exception:
            print("Something went wrong.")


def read_score(i):
    while True:
        try:
            value = float(input(f"Subject {i} score: "))

            if value >= 0:
                if value <= 100:
                    if value >= 0:
                        return value
                    else:
                        print("Invalid score.")
                else:
                    print("Score is too high.")
            else:
                print("Score is too low.")

        except ValueError:
            print("Invalid number.")
        except Exception:
            print("Something went wrong.")


def read_student_name():
    name = input("Student name: ")

    if name == "":
        print("Name cannot be empty.")
        name = input("Student name: ")

        if name == "":
            print("Name cannot be empty.")
            name = input("Student name: ")

            if name == "":
                print("Name cannot be empty.")
                name = "Unknown"

    return name


def process_student_scores():
    number_of_subjects = read_int("Number of subjects: ")
    scores = []

    for i in range(1, number_of_subjects + 1):
        scores.append(read_score(i))

    total = 0
    count = 0

    for score in scores:
        total = total + score
        count = count + 1

    if count > 0:
        average = total / count
        gpa = round(average / 25, 2)
    else:
        gpa = 0

    return scores, gpa


def print_student_report(student):
    print("================================")
    print("STUDENT REPORT")
    print("================================")
    print("Name:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])
    print("================================")


def print_student_report_again(student):
    print("================================")
    print("STUDENT REPORT")
    print("================================")
    print("Name:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])
    print("================================")


def calculate_statistics(students):
    total_gpa = 0
    highest_gpa = 0
    lowest_gpa = 4
    passed = 0
    failed = 0
    student_count = 0

    for student in students:
        student_count = student_count + 1
        total_gpa = total_gpa + student["gpa"]

        if student["gpa"] > highest_gpa:
            highest_gpa = student["gpa"]

        if student["gpa"] < lowest_gpa:
            lowest_gpa = student["gpa"]

        if student["gpa"] >= 2.0:
            if student["graduated"] == True:
                passed = passed + 1
            else:
                failed = failed + 1
        else:
            if student["graduated"] == False:
                failed = failed + 1
            else:
                passed = passed + 1

    average_gpa = total_gpa / student_count

    print("Average GPA:", average_gpa)
    print("Highest GPA:", highest_gpa)
    print("Lowest GPA:", lowest_gpa)
    print("Passed:", passed)
    print("Failed:", failed)


def evaluate_student(student):
    score = 0

    if student["gpa"] >= 3.5:
        score = score + 10
    else:
        if student["gpa"] >= 3.0:
            score = score + 8
        else:
            if student["gpa"] >= 2.0:
                score = score + 6
            else:
                if student["gpa"] >= 1.0:
                    score = score + 3
                else:
                    score = score + 0

    if student["grade"] == "A":
        score = score + 10
    else:
        if student["grade"] == "B":
            score = score + 8
        else:
            if student["grade"] == "C":
                score = score + 6
            else:
                score = score + 1

    if student["graduated"]:
        if student["gpa"] >= 2.0:
            if student["grade"] != "F":
                return score
            else:
                return score - 5
        else:
            return score - 10
    else:
        if student["gpa"] < 2.0:
            return score - 10
        else:
            return score - 5


def main():
    students = []
    number_of_students = read_int("Number of students: ")

    for i in range(number_of_students):
        name = read_student_name()
        scores, gpa = process_student_scores()

        student = {
            "name": name,
            "gpa": gpa,
            "grade": calculate_grade(gpa),
            "graduated": check_graduation(gpa),
            "scores": scores,
            "evaluation": 0
        }

        student["evaluation"] = evaluate_student(student)
        students.append(student)

        if i >= 0:
            if student["gpa"] >= 2.0:
                if student["grade"] == "A":
                    print("Excellent performance.")
                elif student["grade"] == "B":
                    print("Good performance.")
                else:
                    print("Student passed.")
            else:
                if student["gpa"] < 1.0:
                    print("Very poor performance.")
                else:
                    print("Student did not graduate.")

        if len(students) > 0:
            print_student_report(student)

    print("\nSTUDENT RANKING")

    ranked_students = rank_students(students)

    for position, student in enumerate(ranked_students, 1):
        print(position, student)

    if len(students) > 0:
        calculate_statistics(students)
    else:
        print("No students available.")

    for student in students:
        print("================================")
        print("STUDENT REPORT")
        print("================================")
        print("Name:", student["name"])
        print("GPA:", student["gpa"])
        print("Grade:", student["grade"])
        print("Graduated:", student["graduated"])
        print("================================")


if __name__ == "__main__":
    main()
