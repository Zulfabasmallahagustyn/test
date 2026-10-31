"""
prompt:
Refactor the input validation version of the Student Academic Evaluation System.
Consolidate repeated score validation into one reusable function, use clear error-handling logic,
and keep all valid scores within the range of 0 to 100. Do not change the academic calculation rules.
Demonstrate the validation function with valid and invalid inputs.
"""

#chatgpt:
def validate_score(value):
    try:
        score = float(value)
    except (ValueError, TypeError):
        return None

    if not 0 <= score <= 100:
        return None

    return score


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


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)


print(validate_score("85"))
print(validate_score("120"))
print(validate_score("hello"))