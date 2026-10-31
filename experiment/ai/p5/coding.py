"""
prompt:
Write a Python Student Academic Evaluation System with robust input validation.
Ask the user for each student's name, number of subjects, and scores one by one.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Reject non-numeric scores and scores outside the 0-100 range.
Calculate GPA on a 4.0 scale, determine letter grades, check graduation eligibility,
and display students in descending GPA order. Use functions to keep the program modular.
"""

#chatgpt:

def calculate_gpa(scores):
    return round(sum(scores) / len(scores) / 25, 2)

def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    if gpa >= 3.0:
        return "B"
    if gpa >= 2.0:
        return "C"
    return "D"

def check_graduation(gpa):
    return gpa >= 2.0

def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)

def get_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score: "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

students = []
n = int(input("Number of students: "))

for _ in range(n):
    name = input("Student name: ")
    total = int(input("Number of subjects: "))

    while total <= 0:
        total = int(input("Enter a positive subject count: "))

    scores = [get_score(f"subject {i+1}") for i in range(total)]
    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduation": check_graduation(gpa)
    })

for i, s in enumerate(rank_students(students), 1):
    print(i, s)
