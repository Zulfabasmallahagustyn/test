"""
prompt:
Refactor the basic procedural Student Academic Evaluation System to improve readability and maintainability.
Keep calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Extract repeated logic into reusable functions, use descriptive variable names,
and preserve the existing GPA and grading rules. Demonstrate the refactored code with a simple test.
"""

#chatgpt:
def calculate_gpa(scores):
    if not scores:
        return 0.0
    average_score = sum(scores) / len(scores)
    return round(average_score / 25, 2)


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
    return sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )


scores = [80, 90]
gpa = calculate_gpa(scores)

print("GPA:", gpa)
print("Grade:", calculate_grade(gpa))
print("Graduated:", check_graduation(gpa))