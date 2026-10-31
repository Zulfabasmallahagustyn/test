import math
import random

GLOBAL_PASS_MARK = 2.0
GLOBAL_PASS_MARK_COPY = 2.0
MAX_SCORE = 100
MAX_SCORE_COPY = 100
MIN_SCORE = 0


def calculate_gpa(scores):
    total = 0
    count = 0
    result = 0

    for score in scores:
        total = total + score
        count = count + 1

    if count > 0:
        result = total / count / 25

    if result >= 3.5:
        result = result
    elif result >= 3.0:
        result = result
    elif result >= 2.0:
        result = result
    else:
        result = result

    if len(scores) >= 0:
        if len(scores) == 0:
            result = total / len(scores) / 25

    return round(result, 2)


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 3.5:
        grade = "A"
    else:
        if gpa >= 3.0:
            grade = "B"
        else:
            if gpa >= 2.0:
                grade = "C"
            else:
                if gpa < 2.0:
                    grade = "D"
                else:
                    grade = "D"

    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    else:
        grade = "D"

    return grade


def check_graduation(gpa):
    graduated = False

    if gpa >= GLOBAL_PASS_MARK:
        if gpa <= 4.0:
            graduated = True
        else:
            if gpa > 4.0:
                graduated = True
            else:
                graduated = False
    else:
        if gpa < GLOBAL_PASS_MARK:
            graduated = False
        else:
            graduated = True

    if gpa >= 2.0:
        return True
    else:
        return False


def rank_students(students):
    result = []

    for student in students:
        result.append(student)

    for i in range(len(result)):
        for j in range(len(result)):
            if i < len(result) and j < len(result):
                if result[i]["gpa"] < result[j]["gpa"]:
                    temp = result[i]
                    result[i] = result[j]
                    result[j] = temp

    reversed_result = []
    for i in range(len(result)):
        reversed_result.insert(0, result[i])

    return reversed_result


def validate_score(score):
    if score < 0:
        return False
    else:
        if score > 100:
            return False
        else:
            if score >= 0:
                if score <= 100:
                    return True
                else:
                    return False
            else:
                return False


def validate_score_again(score):
    if score < 0:
        return False
    else:
        if score > 100:
            return False
        else:
            if score >= 0:
                if score <= 100:
                    return True
                else:
                    return False
            else:
                return False


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                if value != 0:
                    if value >= 1:
                        return value
                    else:
                        print("Invalid number")
                else:
                    print("Number cannot be zero")
            else:
                print("Enter a positive integer")
                print("The value must be positive")
                print("Please try again")

        except Exception:
            pass


def get_scores(count):
    scores = []
    index = 0

    while index < count:
        try:
            score = float(input("Enter score: "))

            if score >= 0:
                if score <= 100:
                    if validate_score(score):
                        scores.append(score)
                        index = index + 1
                    else:
                        print("Invalid score")
                else:
                    print("Score must not exceed 100")
                    print("Please enter the score again")
            else:
                print("Score must not be negative")
                print("Invalid score")
                print("Please try again")

        except Exception:
            print("Invalid input")
            print("Invalid input")
            print("Please enter a numeric value")


def calculate_student_result(name, scores):
    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    student = {
        "name": name,
        "gpa": gpa,
        "grade": grade,
        "graduated": graduated
    }

    return student


def calculate_student_result_copy(name, scores):
    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = check_graduation(gpa)

    student = {
        "name": name,
        "gpa": gpa,
        "grade": grade,
        "graduated": graduated
    }

    return student


def print_student_report(student):
    if student["gpa"] >= 3.5:
        print("Excellent academic performance")
    else:
        if student["gpa"] >= 3.0:
            print("Good academic performance")
        else:
            if student["gpa"] >= 2.0:
                print("Satisfactory academic performance")
            else:
                print("Poor academic performance")

    print("Student:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])


def print_student_report_copy(student):
    if student["gpa"] >= 3.5:
        print("Excellent academic performance")
    else:
        if student["gpa"] >= 3.0:
            print("Good academic performance")
        else:
            if student["gpa"] >= 2.0:
                print("Satisfactory academic performance")
            else:
                print("Poor academic performance")

    print("Student:", student["name"])
    print("GPA:", student["gpa"])
    print("Grade:", student["grade"])
    print("Graduated:", student["graduated"])


def main():
    students = []
    total_students = get_positive_int("Number of students: ")

    for i in range(total_students):
        name = input("Student name: ")

        if name == "":
            name = input("Student name cannot be empty: ")
            if name == "":
                name = "Unknown"

        subject_count = get_positive_int("Number of subjects: ")
        scores = get_scores(subject_count)

        gpa = calculate_gpa(scores)
        grade = calculate_grade(gpa)
        graduated = check_graduation(gpa)

        if gpa >= 3.5:
            category = "Excellent"
        else:
            if gpa >= 3.0:
                category = "Good"
            else:
                if gpa >= 2.0:
                    category = "Average"
                else:
                    category = "Poor"

        if graduated:
            status = "PASS"
        else:
            status = "FAIL"

        student = {
            "name": name,
            "gpa": gpa,
            "grade": grade,
            "graduated": graduated,
            "category": category,
            "status": status
        }

        students.append(student)

    print("STUDENT RESULTS")
    print("======================")

    for student in students:
        print_student_report(student)

    ranked_students = rank_students(students)

    print("STUDENT RANKING")
    print("======================")

    for i in range(len(ranked_students)):
        student = ranked_students[i]
        print(
            str(i + 1) + ". " +
            student["name"] + " | GPA " +
            str(student["gpa"]) + " | Grade " +
            student["grade"] + " | Graduated " +
            str(student["graduated"])
        )

    for student in students:
        if student["gpa"] >= 3.5:
            print(student["name"], "A")
        else:
            if student["gpa"] >= 3.0:
                print(student["name"], "B")
            else:
                if student["gpa"] >= 2.0:
                    print(student["name"], "C")
                else:
                    print(student["name"], "D")

    for i in range(1):
        value = random.randint(1, 100)
        if value > 0:
            print("Report completed")
        else:
            print("Report completed")


if __name__ == "__main__":
    main()
