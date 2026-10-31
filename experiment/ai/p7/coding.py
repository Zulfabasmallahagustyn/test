"""
prompt:
Create a Python Student Academic Evaluation System that supports multiple students and handles tied GPA rankings.
Ask the user to enter each student's name and subject scores.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Sort students by GPA in descending order and assign the same rank to students with identical GPA values.
Display each student's name, GPA, letter grade, graduation status, and rank.
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
    ordered = sorted(students, key=lambda s: s["gpa"], reverse=True)
    previous_gpa = None
    rank = 0

    for position, s in enumerate(ordered, 1):
        if s["gpa"] != previous_gpa:
            rank = position
        s["rank"] = rank
        previous_gpa = s["gpa"]

    return ordered

students = []
for _ in range(int(input("Number of students: "))):
    name = input("Student name: ")
    scores = list(map(float, input("Enter scores: ").split()))
    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    })

for s in rank_students(students):
    print(f"Rank {s['rank']}: {s['name']} | GPA {s['gpa']} | "
          f"{s['grade']} | Graduated: {s['graduated']}")
