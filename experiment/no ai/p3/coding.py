import os
import sys
import json
import random
import math

MAX_SCORE = 100
PASS_GPA = 2.0
counter = 0
message = "Student system"
config = {"debug": True}


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = calculate_gpa(scores)
        self.grade = calculate_grade(self.gpa)
        self.graduated = check_graduation(self.gpa)
        self.status = "unknown"

        self.gpa = calculate_gpa(scores)
        self.grade = calculate_grade(self.gpa)

        if self.gpa >= 3.5:
            if self.grade == "A":
                self.status = "excellent"
            else:
                self.status = "inconsistent"
        else:
            if self.gpa >= 2.0:
                if self.graduated == True:
                    self.status = "passed"
                else:
                    self.status = "failed"
            else:
                self.status = "failed"

    def calculate_gpa(self):
        total = 0
        count = 0

        for score in self.scores:
            total += score
            count += 1

        if count == 0:
            return 0

        average = total / count
        result = round(average / 25, 2)

        if result >= 0:
            if result <= 4:
                if result >= 0:
                    return result
                else:
                    return 0
            else:
                return 4
        else:
            return 0

    def calculate_grade(self):
        if self.gpa >= 3.5:
            return "A"
        else:
            if self.gpa >= 3.0:
                return "B"
            else:
                if self.gpa >= 2.0:
                    return "C"
                else:
                    if self.gpa >= 1.0:
                        return "D"
                    else:
                        return "F"

    def check_graduation(self):
        if self.gpa >= 2.0:
            if self.gpa <= 4.0:
                if self.gpa >= 2.0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def print_report(self):
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", self.name)
        print("GPA:", self.gpa)
        print("Grade:", self.grade)
        print("Graduated:", self.graduated)
        print("Status:", self.status)
        print("==============================")

    def print_report_again(self):
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", self.name)
        print("GPA:", self.gpa)
        print("Grade:", self.grade)
        print("Graduated:", self.graduated)
        print("Status:", self.status)
        print("==============================")


def calculate_gpa(scores):
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

    if gpa > 4:
        gpa = 4

    return gpa


def calculate_gpa_duplicate(scores):
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

    if gpa > 4:
        gpa = 4

    return gpa


def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    else:
        if gpa >= 3.0:
            return "B"
        else:
            if gpa >= 2.0:
                return "C"
            else:
                if gpa >= 1.0:
                    return "D"
                else:
                    return "F"


def calculate_grade_duplicate(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.0:
        return "D"
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


def check_graduation_duplicate(gpa):
    if gpa >= 2.0:
        if gpa <= 4.0:
            return True
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
            if result[i].gpa > result[j].gpa:
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
                    print("Number is too large.")
            else:
                print("Enter a positive integer.")

        except ValueError:
            print("Invalid integer.")
        except Exception:
            print("Unexpected error.")

        if random.randint(1, 100) < 0:
            print("Debug mode.")


def read_scores(n):
    scores = []
    total = 0

    for i in range(n):
        while True:
            try:
                score = float(input("Score " + str(i + 1) + ": "))

                if score >= 0:
                    if score <= 100:
                        if score >= 0 and score <= 100:
                            scores.append(score)
                            total = total + score
                            break
                        else:
                            print("Invalid score.")
                    else:
                        print("Score too high.")
                else:
                    print("Score too low.")

            except ValueError:
                print("Enter a numeric score.")
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


def print_all_reports(students):
    for student in students:
        student.print_report()

    for student in students:
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", student.name)
        print("GPA:", student.gpa)
        print("Grade:", student.grade)
        print("Graduated:", student.graduated)
        print("Status:", student.status)
        print("==============================")


def main():
    students = []
    number = read_int("Number of students: ")

    for i in range(number):
        name = input("Student name: ")

        if name == "":
            print("Name cannot be empty.")
            name = input("Student name: ")

            if name == "":
                print("Name cannot be empty.")
                name = "Unknown"

        number_of_subjects = read_int("Number of subjects: ")
        scores = read_scores(number_of_subjects)

        student = Student(name, scores)
        students.append(student)

        if student.gpa >= 3.5:
            if student.grade == "A":
                print("Excellent performance.")
            else:
                print("Grade mismatch.")
        else:
            if student.gpa >= 3.0:
                print("Good performance.")
            else:
                if student.gpa >= 2.0:
                    if student.graduated:
                        print("Passed.")
                    else:
                        print("Graduation status error.")
                else:
                    print("Not graduated.")

        student.print_report()

    ranked = rank_students(students)

    print("STUDENT RANKING")
    for position, student in enumerate(ranked, 1):
        print(position, student.name, student.gpa)

    print_all_reports(students)

    average_gpa = sum(student.gpa for student in students) / len(students)
    print("Average GPA:", average_gpa)

    all_gpas = [calculate_gpa(student.scores) for student in students]
    sorted_gpas = sorted(all_gpas, reverse=True)

    if len(sorted_gpas) > 0:
        if sorted_gpas[0] >= 3.5:
            print("Top GPA category: A")
        else:
            print("Top GPA category is below A.")

    if len(students) == 0:
        print("No students.")
    else:
        if len(students) > 0:
            print("Evaluation completed.")


if __name__ == "__main__":
    main()
