"""
prompt:
Develop a Python Student Academic Evaluation System that calculates weighted GPA using subject credits.
Ask the user for each student's name, the number of subjects, each subject's score, and its credit value.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Calculate weighted average score by multiplying each score by its credits and dividing by total credits,
then convert it to a 4.0 GPA scale. Rank students by weighted GPA and display all academic results.
"""

#chatgpt:

def calculate_gpa(scores, credits):
    weighted = sum(s * c for s, c in zip(scores, credits))
    total_credits = sum(credits)
    return round(weighted / total_credits / 25, 2)

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
    count = int(input("Number of subjects: "))
    scores, credits = [], []

    for i in range(count):
        scores.append(float(input(f"Subject {i+1} score: ")))
        credits.append(float(input(f"Subject {i+1} credits: ")))

    gpa = calculate_gpa(scores, credits)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    })

for rank, s in enumerate(rank_students(students), 1):
    print(f"{rank}. {s['name']} - GPA {s['gpa']}, "
          f"Grade {s['grade']}, Graduation: {s['graduated']}")
