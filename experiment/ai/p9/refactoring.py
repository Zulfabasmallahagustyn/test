"""
prompt:
Refactor the modular Student Academic Evaluation System to improve separation of concerns and reduce coupling.
Keep academic calculations in reusable functions, avoid duplicated GPA logic, and make each function easy to test independently.
Preserve the four required functions and demonstrate the output for scores of 80 and 90.
"""

#chatgpt:
def calculate_gpa(scores):
    if not scores:
        return 0.0
    average = sum(scores) / len(scores)
    return round(average / 25, 2)


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


def evaluate_student(name, scores):
    gpa = calculate_gpa(scores)
    return {
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": check_graduation(gpa)
    }


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)


result = evaluate_student("Alya", [80, 90])
print(result)