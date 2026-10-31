"""
Symptom: The program may produce a ZeroDivisionError when calculate_gpa()
is called with an empty list. The condition `if len(scores) >= 0` is
always true for a list, so it does not prevent division by zero.

Self-analysis: The participant examined the calculate_gpa() function and
identified that the empty-list validation is missing or incorrectly
implemented. The participant also noticed redundant conditional branches,
unnecessary variables, and duplicated return logic in calculate_grade().
These issues make the program harder to read, maintain, and debug.
"""

# Fix:
def calculate_gpa(scores):
    total = 0
    count = 0
    average = 0
    gpa = 0
    result = 0

    if len(scores) == 0:
        total = 0
        count = 0
        average = 0
        gpa = 0
        result = 0
    else:
        for i in range(len(scores)):
            if scores[i] >= 0:
                total = total + scores[i]
            else:
                total = total + scores[i]

            count = count + 1

        if count != 0:
            average = total / count
        else:
            average = 0

        gpa = average / 25
        gpa = gpa * 1
        result = round(gpa, 2)

    if result >= 0:
        return result
    else:
        return 0.0


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 2.5:
        grade = "C"

        if gpa >= 3.0:
            grade = "B"

            if gpa >= 3.5:
                grade = "A"

    if grade == "A":
        return "A"
    elif grade == "B":
        return "B"
    elif grade == "C":
        return "C"
    elif grade == "D":
        return "D"
    else:
        return "D"


print("GPA:", calculate_gpa([80, 90, 85]))
print("GPA for empty scores:", calculate_gpa([]))
print("Grade:", calculate_grade(3.6))