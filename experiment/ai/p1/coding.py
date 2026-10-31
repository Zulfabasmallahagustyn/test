"""
prompt:
Create a Python Student Academic Evaluation System. Ask the user to enter the student's name and scores for three subjects.
Implement four functions: calculate_gpa(), calculate_grade(), check_graduation(), and rank_students(). +
Calculate GPA on a 4.0 scale by dividing the average score by 25. Assign grades A for GPA >= 3.5, B for GPA >= 3.0, C for GPA >= 2.0, and D otherwise.
A student graduates if their GPA is at least 2.0. Display all results and rank the students by GPA. Use user input instead of hardcoded student data.
"""

#chatgpt:

def calculate_gpa(scores):
    return round(sum(scores) / len(scores) / 25, 2)

def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    return "D"

def check_graduation(gpa):
    return gpa >= 2.0

def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)

students = []
n = int(input("Number of students: "))

for _ in range(n):
    name = input("Student name: ")
    scores = [
        float(input("Score for subject 1: ")),
        float(input("Score for subject 2: ")),
        float(input("Score for subject 3: "))
    ]
    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    })

for student in rank_students(students):
    print(student)
