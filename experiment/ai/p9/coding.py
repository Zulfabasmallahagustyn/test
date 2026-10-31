"""
prompt:
Create a modular Python Student Academic Evaluation System by separating data input, calculations, and output.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students() as independent functions.
Create an additional input_student() function to collect the student's name and subject scores, and a display_results() function to print the report.
Allow users to enter multiple students and display the final ranking. Keep the code readable, reusable, and easy to test.
"""

#chatgpt:3

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

def input_student():
    name = input("Student name: ")
    scores = list(map(float, input(
        "Enter subject scores separated by spaces: ").split()))
    gpa = calculate_gpa(scores)

    return {
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduation": check_graduation(gpa)
    }

def display_results(students):
    for rank, s in enumerate(rank_students(students), 1):
        print(f"{rank}. {s['name']} | GPA: {s['gpa']} | "
              f"Grade: {s['grade']} | "
              f"Graduation: {s['graduation']}")

students = []
for _ in range(int(input("Number of students: "))):
    students.append(input_student())

display_results(students)
