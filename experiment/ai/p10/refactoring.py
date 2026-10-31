"""
prompt:
Refactor the student summary program to improve readability and reduce repeated calculations.
Create reusable functions for student evaluation and summary generation, handle an empty student list,
and preserve GPA, grade, graduation, and ranking rules. Demonstrate the summary for three students.
"""

#chatgpt:
def calculate_gpa(scores):
    if not scores:
        return 0.0
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


def evaluate_student(student):
    gpa = calculate_gpa(student["scores"])
    return {
        "name": student["name"],
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    }


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)


def generate_summary(students):
    evaluated = [evaluate_student(s) for s in students]
    ranked = rank_students(evaluated)

    if not ranked:
        return {"total": 0, "top_student": None, "students": []}

    return {
        "total": len(ranked),
        "top_student": ranked[0]["name"],
        "students": ranked
    }


students = [
    {"name": "Alya", "scores": [80, 90]},
    {"name": "Bima", "scores": [90, 95]},
    {"name": "Citra", "scores": [70, 80]}
]

summary = generate_summary(students)
print("Total:", summary["total"])
print("Top student:", summary["top_student"])