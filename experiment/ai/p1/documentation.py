"""
prompt:
Write clear and concise technical documentation for the following Python Student Academic Evaluation System.
Explain the purpose of each function, its parameters, return values, grading rules, and graduation criteria.
Include a short usage example. Do not change the program logic.

chatgpt:
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

def check_graduation(gpa):
    return gpa >= 2.0

def rank_students(students):
    return sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

chatgpt:
# Student Academic Evaluation System — Basic Procedural Version

## Overview
This program evaluates students' academic performance by calculating GPA, assigning letter grades, determining graduation eligibility, and ranking students by GPA.

## Functions

### 'calculate_gpa(scores)'
Calculates GPA from a list of numeric subject scores.

- **Parameter:** 'scores' — a non-empty list of scores.
- **Returns:** A GPA on a 0–4 scale, calculated as the average score divided by 25.
- **Example:** '[80, 90]' returns '3.4'.

### 'calculate_grade(gpa)'
Converts a GPA into a letter grade.

- **Parameter:** 'gpa' — the student's GPA.
- **Returns:** '"A"', '"B"', '"C"', or '"D"'.
- **Rules:** A ≥ 3.5; B ≥ 3.0; C ≥ 2.0; otherwise D.

### 'check_graduation(gpa)'
Checks whether the student meets the graduation threshold.

- **Parameter:** 'gpa' — the student's GPA.
- **Returns:** 'True' if GPA is at least 2.0; otherwise 'False'.

### 'rank_students(students)'
Sorts student records from highest to lowest GPA.

- **Parameter:** 'students' — a list of dictionaries containing a 'gpa' field.
- **Returns:** A new sorted list.

## Usage Example
python
scores = [80, 90]
gpa = calculate_gpa(scores)

print(gpa)                         # 3.4
print(calculate_grade(gpa))        # B
print(check_graduation(gpa))       # True


## Limitations
The GPA function assumes that the score list is non-empty and contains valid numeric values. Input validation should be implemented separately if required.
"""