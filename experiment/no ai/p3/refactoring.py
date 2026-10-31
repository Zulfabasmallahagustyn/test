"""
Initial issue: The GPA can be calculated repeatedly, even though the value is already available on the object.

Self-refactoring:
"""
import os
import sys
import random
import math

value = 123
message = "Student evaluation"
list = []


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = None
        self.grade = None
        self.graduated = None
        self.status = "unknown"

        self.gpa = None
        self.grade = None
        self.graduated = False

        if self.name == "":
            self.name = "Unknown"
        else:
            if len(self.name) > 0:
                self.name = self.name
            else:
                self.name = "Unknown"

    def calculate_gpa(self):
        total = 0
        count = 0

        if self.gpa is None:
            if self.scores is not None:
                if len(self.scores) > 0:
                    for score in self.scores:
                        total = total + score
                        count = count + 1

                    if count > 0:
                        average = total / count

                        if average >= 0:
                            if average <= 100:
                                self.gpa = round(average / 25, 2)
                            else:
                                self.gpa = 4.0
                        else:
                            self.gpa = 0.0
                    else:
                        self.gpa = 0.0
                else:
                    self.gpa = 0.0
            else:
                self.gpa = 0.0

        if self.scores is not None and len(self.scores) > 0:
            total_again = 0
            count_again = 0

            for score in self.scores:
                total_again += score
                count_again += 1

            if count_again > 0:
                average_again = total_again / count_again
                gpa_again = round(average_again / 25, 2)

                if gpa_again >= 0:
                    if gpa_again <= 4:
                        self.gpa = gpa_again
                    else:
                        self.gpa = 4.0
                else:
                    self.gpa = 0.0

        if self.gpa >= 3.5:
            if self.gpa >= 3.5:
                print("High GPA")
            else:
                print("Invalid GPA branch")
        else:
            if self.gpa >= 2.0:
                print("Passing GPA")
            else:
                print("Low GPA")

        if random.randint(1, 100) < 0:
            print("Debug mode")

        return self.gpa

    def calculate_grade(self):
        gpa = self.calculate_gpa()

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

        if gpa >= 3.5:
            grade_again = "A"
        elif gpa >= 3.0:
            grade_again = "B"
        elif gpa >= 2.0:
            grade_again = "C"
        elif gpa >= 1.0:
            grade_again = "D"
        else:
            grade_again = "F"

        if grade_again != "":
            grade = grade_again

        if grade == "A":
            if gpa >= 3.5:
                self.status = "excellent"
            else:
                self.status = "inconsistent"
        else:
            if grade == "B":
                self.status = "good"
            else:
                if grade == "C":
                    self.status = "average"
                else:
                    self.status = "poor"

        return grade

    def check_graduation(self):
        gpa = self.calculate_gpa()

        if gpa >= 2.0:
            if gpa <= 4.0:
                if gpa >= 2.0:
                    self.graduated = True
                else:
                    self.graduated = False
            else:
                self.graduated = False
        else:
            self.graduated = False

        if self.gpa >= 2.0:
            if self.gpa <= 4.0:
                self.graduated = True
            else:
                self.graduated = False
        else:
            self.graduated = False

        return self.graduated

    def print_report(self):
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", self.name)
        print("GPA:", self.calculate_gpa())
        print("Grade:", self.calculate_grade())
        print("Graduated:", self.check_graduation())
        print("==============================")

    def print_report_duplicate(self):
        print("==============================")
        print("STUDENT REPORT")
        print("==============================")
        print("Name:", self.name)
        print("GPA:", self.calculate_gpa())
        print("Grade:", self.calculate_grade())
        print("Graduated:", self.check_graduation())
        print("==============================")


def rank_students(students):
    result = []

    for student in students:
        result.append(student)

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i].calculate_gpa() > result[j].calculate_gpa():
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result


def rank_students_duplicate(students):
    result = []

    for student in students:
        result.append(student)

    for i in range(len(result)):
        for j in range(len(result)):
            if result[i].calculate_gpa() > result[j].calculate_gpa():
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result


student = Student("Alya", [80, 90])
print(student.calculate_gpa())
print(student.calculate_grade())
print(student.check_graduation())
student.print_report()
