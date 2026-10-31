"""
prompt:
Develop a complete Python Student Academic Evaluation System with a class summary report.
Ask users to enter multiple student names and subject scores.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Display each student's GPA, letter grade, and graduation eligibility.
Also calculate and display the class average GPA, the number of students eligible for graduation, and the highest-ranked student.
Use user input, separate functions, and clear formatted output.
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
n = int(input("Number of students: "))

for _ in range(n):
    name = input("Student name: ")
    scores = list(map(float, input("Enter subject scores: ").split()))
    gpa = calculate_gpa(scores)
    students.append({
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    })

if students:
    ranked = rank_students(students)
    print("\n=== STUDENT RESULTS ===")

    for i, s in enumerate(ranked, 1):
        print(f"{i}. {s['name']} | GPA {s['gpa']:.2f} | "
              f"Grade {s['grade']} | Graduation: {s['graduated']}")

    average_gpa = sum(s["gpa"] for s in students) / len(students)
    graduates = sum(s["graduated"] for s in students)

    print("\n=== CLASS SUMMARY ===")
    print(f"Class average GPA: {average_gpa:.2f}")
    print(f"Eligible for graduation: {graduates}/{len(students)}")
    print(f"Top student: {ranked[0]['name']}")
else:
    print("No student records available.")
