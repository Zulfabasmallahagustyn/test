"""
prompt:
Debug the helper-functions version of the Student Academic Evaluation System.
A student with a GPA of 3.40 incorrectly receives grade C. Inspect the grade thresholds and
correct the logic according to these rules: A for GPA >= 3.5, B for GPA >= 3.0, C for GPA >= 2.0, and D otherwise.
Include boundary tests.

chatgpt:
Diagnosis: For the threshold condition of value B, a GPA >= 3.0 must be used.
The order of examination must also begin from the highest threshold.
"""
#Correction code:
def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    return "D"

for gpa in [3.50, 3.40, 3.00, 2.00, 1.99]:
    print(gpa, calculate_grade(gpa))