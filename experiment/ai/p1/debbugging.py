"""
Prompt:
Debug the following Student Academic Evaluation System code. Identify the cause of the runtime error when the user enters no scores.
Provide a corrected Python implementation and demonstrate the expected output. Preserve the functions calculate_gpa(), calculate_grade(),
check_graduation(), and rank_students().

chatgpt:
Diagnosis: 'calculate_gpa()' triggers a 'ZeroDivisionError' when the list of grades is empty.
The function should validate the input before performing any division.
"""
#Corrected code:
def calculate_gpa(scores):
    if not scores:
        return 0.0
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
    return sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )