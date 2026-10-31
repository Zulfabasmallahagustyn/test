"""
prompt:
Write technical documentation for the following Python program that generates a student evaluation report. Describe the responsibilities of 'generate_report()' and 'display_report()', explain the report fields, and provide a sample output. Keep the documentation aligned with the existing implementation.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def generate_report(name, scores):
    gpa = calculate_gpa(scores)
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    else:
        grade = "D"

    return {
        "name": name,
        "gpa": gpa,
        "grade": grade,
        "graduated": gpa >= 2.0
    }

def display_report(report):
    print(f"Student: {report['name']}")
    print(f"GPA: {report['gpa']:.2f}")
    print(f"Grade: {report['grade']}")
    print(f"Graduated: {report['graduated']}")

chatgpt:
# Student Academic Evaluation System — Report Generation Version

## Overview
This program evaluates a student and produces a structured report containing the student's name, GPA, letter grade, and graduation status.

## Functions

### 'calculate_gpa(scores)'
Calculates GPA by dividing the average score by 25. It expects a non-empty list of numeric scores.

### 'generate_report(name, scores)'
Creates a dictionary containing the evaluation results.

**Parameters**
- 'name': student's name.
- 'scores': list of subject scores.

**Return fields**
- 'name': student's name.
- 'gpa': calculated GPA.
- 'grade': letter grade.
- 'graduated': Boolean graduation status.

### 'display_report(report)'
Prints the report in a readable format. GPA is displayed to two decimal places.

## Example
python
report = generate_report("Alya", [80, 90])
display_report(report)

Expected output:

text
Student: Alya
GPA: 3.40
Grade: B
Graduated: True


## Design
The report-generation function separates evaluation from presentation. The returned dictionary can be used by other parts of the application, while the display function handles console output.

## Limitations
No validation is performed for the student's name or score list. The program assumes scores are valid and the list is non-empty.
"""