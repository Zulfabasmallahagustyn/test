"""
prompt:
Refactor the helper-functions Student Academic Evaluation System to make the grading logic more maintainable.
Replace repetitive conditional code with a clear, reusable structure while preserving these rules:
A for GPA >= 3.5, B for GPA >= 3.0, C for GPA >= 2.0, and D otherwise. Keep the four required functions and include boundary tests.
"""

#chatgpt:
GRADE_THRESHOLDS = [
    (3.5, "A"),
    (3.0, "B"),
    (2.0, "C")
]


def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)


def calculate_grade(gpa):
    for threshold, grade in GRADE_THRESHOLDS:
        if gpa >= threshold:
            return grade
    return "D"


def check_graduation(gpa):
    return gpa >= 2.0


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)


for value in [3.5, 3.4, 3.0, 2.0, 1.9]:
    print(value, calculate_grade(value))