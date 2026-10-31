"""
prompt:
Write modular developer documentation for this Python program. Explain the purpose of each function, how 'evaluate_student()' combines the individual operations, the structure of its returned dictionary, and an example of how another module could use the result. Do not alter the code.

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
# Student Academic Evaluation System — Modular Version

## Overview
This program separates GPA calculation, grade assignment, and student evaluation into reusable functions.

## Function Reference

### 'calculate_gpa(scores)'
Calculates GPA by dividing the average score by 25. It expects a non-empty list of numeric scores.

### 'calculate_grade(gpa)'
Returns a letter grade using the following thresholds: A ≥ 3.5, B ≥ 3.0, C ≥ 2.0, and D otherwise.

### 'evaluate_student(name, scores)'
Coordinates the evaluation process and returns a dictionary containing:
- 'name': student's name.
- 'gpa': calculated GPA.
- 'grade': assigned letter grade.
- 'graduated': 'True' if GPA is at least 2.0, otherwise 'False'.

## Example
python
result = evaluate_student("Alya", [80, 90])
print(result)

Expected result:

python
{
    "name": "Alya",
    "gpa": 3.4,
    "grade": "B",
    "graduated": True
}

## Integration
Other application components can call 'evaluate_student()' and use its returned fields to display reports, store evaluation results, or prepare rankings.

## Limitations
The code does not validate input types, score ranges, or empty lists. These responsibilities should be addressed by an input-validation layer if required by the application.
"""