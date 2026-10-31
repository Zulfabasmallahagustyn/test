"""
prompt:
Create unit tests for the modular student-evaluation program. Verify GPA calculation, grade assignment, graduation eligibility, returned dictionary keys, and behavior at grading boundaries. Include an invalid-input test and state whether the current implementation handles it safely.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    return "D"

def evaluate_student(name, scores):
    gpa = calculate_gpa(scores)
    return {
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduated": gpa >= 2.0
    }

chatgpt:
Test Case   Input                                   Expected Output
TC9.1       evaluate_student("Alya", [80, 90])      GPA 3.4, grade B, graduated True
TC9.2       evaluate_student("Bima", [100, 100])    GPA 4.0, grade A, graduated True
TC9.3       evaluate_student("Image", [25, 25])     GPA 1.0, grade D, graduated False
TC9.4       evaluate_student("Dina", [50, 50])      GPA 2.0, grade C, graduated True
TC9.5       Check keys in the result:               name, gpa, grade, graduated
TC9.6       Empty list []                           ZeroDivisionError
TC9.7       List [80, "abc"]                        TypeError during addition
"""