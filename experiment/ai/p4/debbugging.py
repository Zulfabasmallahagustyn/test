"""
prompt:
Debug the detailed student report program. The report displays an incorrect grade
because the grading function receives the average raw score instead of the calculated GPA.
Correct the data flow and demonstrate a report for a student with scores of 80 and 90.

chatgpt:
Diagnosis: The 'calculate_grade()' function accepts a GPA as a parameter; therefore, the value provided must be a GPA on a 0-4 scale.
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

def generate_report(name, scores):
    gpa = calculate_gpa(scores)
    grade = calculate_grade(gpa)
    graduated = gpa >= 2.0

    print(f"Student: {name}")
    print(f"GPA: {gpa:.2f}")
    print(f"Grade: {grade}")
    print(f"Graduation: {'Passed' if graduated else 'Not passed'}")