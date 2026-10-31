"""
prompt:
Document the following Python grading component. Explain how 'GRADE_THRESHOLDS' is organized, how 'calculate_grade()' selects a grade, and what happens at the grade boundaries. Include examples for GPA values of 3.5, 3.4, 3.0, 2.0, and 1.9.

python
GRADE_THRESHOLDS = [
    (3.5, "A"),
    (3.0, "B"),
    (2.0, "C"),
    (0.0, "D")
]

def calculate_grade(gpa):
    for threshold, grade in GRADE_THRESHOLDS:
        if gpa >= threshold:
            return grade
    return "D"

chatgpt:
# Student Academic Evaluation System — Grade Thresholds

## Overview
This module assigns a letter grade based on a student's GPA using a configurable list of grade thresholds.

## Constant: 'GRADE_THRESHOLDS'
A list of '(threshold, grade)' tuples ordered from the highest threshold to the lowest:

- GPA ≥ 3.5: A
- GPA ≥ 3.0: B
- GPA ≥ 2.0: C
- GPA ≥ 0.0: D

The order is important because the function returns the first matching grade.

## Function: 'calculate_grade(gpa)'
**Parameter:** 'gpa', a numeric GPA value.

**Returns:** A letter grade as a string.

The function iterates through the thresholds and returns the grade associated with the first threshold that the GPA meets or exceeds.

## Examples
| GPA | Grade |
|---:|:---|
| 3.5 | A |
| 3.4 | B |
| 3.0 | B |
| 2.0 | C |
| 1.9 | D |

## Maintenance Note
When changing grading rules, update 'GRADE_THRESHOLDS' in descending order. The function does not validate whether GPA is within the expected 0–4 range.
"""