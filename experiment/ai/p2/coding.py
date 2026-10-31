"""
prompt:
Develop a Python Student Academic Evaluation System that allows users to enter any number of subjects for each student.
Ask for the student's name, the number of subjects, and each subject score. Implement calculate_gpa(), calculate_grade(),
check_graduation(), and rank_students(). Validate that scores are between 0 and 100 and that the number of subjects is positive.
Calculate GPA from the average score using a 4.0 scale. Display each student's GPA, letter grade, graduation eligibility, and ranking.
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

students = []
count = int(input("Number of students: "))

for _ in range(count):
    name = input("Student name: ")
    total = int(input("Number of subjects: "))

    while total <= 0:
        total = int(input("Enter a positive number of subjects: "))

    scores = []
    for i in range(total):
        score = float(input(f"Score for subject {i + 1}: "))
        while not 0 <= score <= 100:
            score = float(input("Score must be 0-100: "))
        scores.append(score)

    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    })

for rank, s in enumerate(rank_students(students), 1):
    print(f"{rank}. {s['name']} | GPA: {s['gpa']} | "
          f"Grade: {s['grade']} | Graduation: {s['graduated']}")
