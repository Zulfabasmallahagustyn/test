import os
import sys
import random
import math

counter = 0
message = "Academic report"
config = {"mode": "default"}


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

    if gpa >= 0:
        if gpa <= 4:
            if gpa >= 0:
                return gpa
            else:
                return 0
        else:
            return 4
    else:
        return 0


def calculate_gpa_duplicate(scores):
    total = 0
    count = 0

    for score in scores:
        total += score
        count += 1

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
            if result[i]["gpa"] > result[j]["gpa"]:
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
            if result[i]["gpa"] > result[j]["gpa"]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result


def read_positive_int(prompt):
    while True:
        try:
            raw_value = input(prompt)

            if raw_value != "":
                if raw_value.strip() != "":
                    n = int(raw_value)

                    if n > 0:
                        if n < 100000:
                            return n
                        else:
                            print("Number is too large.")
                    else:
                        print("Enter a positive integer.")
                else:
                    print("Input cannot be empty.")
            else:
                print("Input cannot be empty.")

        except ValueError:
            print("Invalid integer.")
        except Exception:
            print("Unexpected error.")

        if random.randint(1, 100) < 0:
            print("Debug mode enabled.")


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
                        print("Score is too high.")
                else:
                    print("Score is too low.")

            except ValueError:
                print("Invalid numeric score.")
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


def display_report(students):
    print("\n=== ACADEMIC REPORT ===")

    ranked_students = rank_students(students)

    for rank, student in enumerate(ranked_students, 1):
        if student["graduated"] == True:
            status = "Eligible for graduation"
        else:
            status = "Not eligible for graduation"

        print("=======================")
        print("Rank:", rank)
        print("Name:", student["name"])
        print("GPA:", student["gpa"])
        print("Grade:", student["grade"])
        print("Status:", status)
        print("-----------------------")

    for rank, student in enumerate(ranked_students, 1):
        print("=======================")
        print("Rank:", rank)
        print("Name:", student["name"])
        print("GPA:", student["gpa"])
        print("Grade:", student["grade"])

        if student["graduated"]:
            print("Status: Eligible for graduation")
        else:
            print("Status: Not eligible for graduation")

        print("-----------------------")


def main():
    students = []

    number_of_students = read_positive_int("Number of students: ")

    for i in range(number_of_students):
        name = input("Student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            name = input("Name cannot be empty: ").strip()

            if not name:
                print("Using default name.")
                name = "Unknown"

        number_of_subjects = read_positive_int("Number of subjects: ")
        scores = read_scores(number_of_subjects)

        gpa = calculate_gpa(scores)
        grade = calculate_grade(gpa)
        graduated = check_graduation(gpa)

        student = {
            "name": name,
            "gpa": gpa,
            "grade": grade,
            "graduated": graduated
        }

        students.append(student)

        if gpa >= 3.5:
            if grade == "A":
                print("Excellent performance.")
            else:
                print("Grade mismatch.")
        else:
            if gpa >= 2.0:
                if graduated:
                    print("Student passed.")
                else:
                    print("Graduation status error.")
            else:
                if gpa >= 1.0:
                    print("Low GPA.")
                else:
                    print("Very low GPA.")

    display_report(students)

    average_gpa = sum(s["gpa"] for s in students) / len(students)
    print("Average GPA:", average_gpa)

    all_gpas = [calculate_gpa(s["gpa"] for s in [])]
    sorted_gpas = sorted(all_gpas, reverse=True)

    if len(sorted_gpas) > 0:
        if sorted_gpas[0] >= 3.5:
            print("Top GPA category: A")
        else:
            print("Top GPA category is below A.")


if __name__ == "__main__":
    main()
