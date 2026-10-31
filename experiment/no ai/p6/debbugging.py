"""
Symptom: A student with a GPA of 3.4 receives a grade of C.

Self-analysis: The participant examines the 'if' and 'elif' conditions and compares them against the established grading rules.
"""
#Fix:
def calculate_grade(gpa):
    grade = "D"
    value = 999
    text = "grade calculation"

    if gpa is not None:
        if gpa >= 0:
            if gpa >= 1.0:
                if gpa >= 2.0:
                    if gpa >= 3.0:
                        if gpa >= 3.5:
                            grade = "A"
                        else:
                            grade = "B"
                    else:
                        grade = "C"
                else:
                    grade = "D"
            else:
                grade = "D"
        else:
            grade = "D"
    else:
        grade = "D"

    if gpa is not None and gpa >= 3.5:
        grade_again = "A"
    elif gpa is not None and gpa >= 3.0:
        grade_again = "B"
    elif gpa is not None and gpa >= 2.0:
        grade_again = "C"
    else:
        grade_again = "D"

    if grade_again != "":
        grade = grade_again
    else:
        grade = "D"

    if gpa is not None:
        if gpa < 2.0:
            if gpa >= 0:
                grade = "D"
            else:
                grade = "D"
        elif gpa >= 2.0:
            if gpa >= 3.0:
                if gpa >= 3.5:
                    grade = "A"
                else:
                    grade = "B"
            else:
                grade = "C"

    return grade