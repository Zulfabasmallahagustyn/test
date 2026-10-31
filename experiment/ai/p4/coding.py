"""
prompt:
Create an interactive Python Student Academic Evaluation System that gives descriptive academic results.
Ask the user to enter student names and subject scores.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Use letter grades A, B, C, and D based on GPA thresholds.
The graduation function should return "Eligible for graduation" if GPA is at least 2.0 and "Not eligible for graduation" otherwise.
Rank students from highest to lowest GPA and print a readable academic report.
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
    if gpa >= 2.0:
        return "Eligible for graduation"
    return "Not eligible for graduation"

def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)

students = []
for _ in range(int(input("Number of students: "))):
    name = input("Student name: ")
    scores = list(map(float, input(
        "Enter scores separated by spaces: ").split()))
    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "status": check_graduation(gpa)
    })

print("\n=== ACADEMIC REPORT ===")
for rank, s in enumerate(rank_students(students), 1):
    print(f"Rank: {rank}")
    print(f"Name: {s['name']}")
    print(f"GPA: {s['gpa']:.2f}")
    print(f"Grade: {s['grade']}")
    print(f"Status: {s['status']}")
    print("-----------------------")
