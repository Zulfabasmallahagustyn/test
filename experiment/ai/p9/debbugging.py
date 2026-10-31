"""
prompt:
Debug the modular Student Academic Evaluation System. The calculate_gpa() function calculates a value but does not return it,
causing other functions to receive None. Fix the function and verify that calculate_grade() and check_graduation() work correctly
for scores of 80 and 90.

chatgpt:
Diagnosis: The calculation result must be returned using 'return', rather than just being calculated or printed.
"""
#Corrected code:
def calculate_gpa(scores):
    if not scores:
        return 0.0

    gpa = sum(scores) / len(scores) / 25
    return round(gpa, 2)

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

gpa = calculate_gpa([80, 90])
print(gpa)
print(calculate_grade(gpa))
print(check_graduation(gpa))