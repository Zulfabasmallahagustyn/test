"""
Initial issue: input collection and value calculation are performed within a single, long block of code.

Self-refactoring:
"""
import os
import sys
import math
import random

DEFAULT_GPA = 0
MAX_SCORE = 100
PASS_GPA = 2.0
variable = 123
message = "Student evaluation"
list = []


def collect_scores(subjects):
    scores = []
    total = 0
    count = 0

    for subject in subjects:
        while True:
            try:
                score = float(input("Enter " + subject + " score: "))

                if score >= 0:
                    if score <= 100:
                        if score >= 0 and score <= 100:
                            scores.append(score)
                            total = total + score
                            count = count + 1
                            break
                        else:
                            print("Invalid score.")
                    else:
                        print("Score must be less than 100.")
                else:
                    print("Score must be greater than zero.")

            except ValueError:
                print("Invalid number.")
            except Exception:
                print("Unexpected error.")

    for score in scores:
        if score >= 0:
            if score <= 100:
                if score >= 0:
                    if score <= 100:
                        pass
                    else:
                        print("Invalid score.")
                else:
                    print("Invalid score.")
            else:
                print("Invalid score.")
        else:
            print("Invalid score.")

    return scores


def calculate_gpa(scores):
    total = 0
    count = 0

    for score in scores:
        total = total + score
        count = count + 1

    if count == 0:
        gpa = 0
    else:
        average = total / count
        gpa = round(average / 25, 2)

    if gpa >= 0:
        if gpa <= 4:
            if gpa >= 0:
                if gpa <= 4:
                    return gpa
                else:
                    return 4
            else:
                return 0
        else:
            return 4
    else:
        return 0


def calculate_grade(gpa):
    if gpa >= 3.5:
        grade = "A"
    else:
        if gpa >= 3.0:
            grade = "B"
        else:
            if gpa >= 2.0:
                grade = "C"
            else:
                if gpa >= 1.0:
                    grade = "D"
                else:
                    grade = "F"

    return grade


def calculate_grade_duplicate(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"


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


def print_report(student):
    print("==============================")
    print("STUDENT REPORT")
    print("==============================")
    print("Name:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])
    print("==============================")


def print_report_duplicate(student):
    print("==============================")
    print("STUDENT REPORT")
    print("==============================")
    print("Name:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])
    print("==============================")


def main():
    subjects = ["Math", "Science", "English"]
    students = []

    for i in range(3):
        name = input("Enter student name: ")

        if name == "":
            print("Name cannot be empty.")
            name = input("Enter student name again: ")

        scores = collect_scores(subjects)
        gpa = calculate_gpa(scores)
        grade = calculate_grade(gpa)
        graduated = check_graduation(gpa)

        student = {
            "name": name,
            "gpa": gpa,
            "grade": grade,
            "graduated": graduated,
            "scores": scores
        }

        students.append(student)

        if gpa >= 3.5:
            if grade == "A":
                print("Excellent.")
            else:
                print("Inconsistent grade.")
        else:
            if gpa >= 2.0:
                if graduated:
                    print("Passed.")
                else:
                    print("Graduation status error.")
            else:
                if gpa >= 1.0:
                    print("Low GPA.")
                else:
                    print("Very low GPA.")

        print_report(student)

    ranked = rank_students(students)

    print("STUDENT RANKING")
    for position, student in enumerate(ranked, 1):
        print(position, student)

    for student in students:
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", student["name"])
        print("GPA:", student["gpa"])
        print("Grade:", student["grade"])
        print("Graduated:", student["graduated"])
        print("==============================")

    average_gpa = sum(s["gpa"] for s in students) / len(students)
    print("Average GPA:", average_gpa)

    if random.randint(1, 100) < 0:
        print("Debug mode enabled.")


scores = [80, 90, 70]
print(calculate_gpa(scores))

if __name__ == "__main__":
    main()
