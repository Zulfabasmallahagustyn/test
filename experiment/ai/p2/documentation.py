"""
prompt:
Create user-oriented documentation for a Python program that collects subject scores dynamically, calculates GPA, assigns a letter grade, and checks graduation eligibility. Describe the input format, processing steps, expected output, and possible input errors. Use this code as the reference and do not add features that are not implemented.

python
def collect_scores(number_of_subjects):
    scores = []
    for i in range(number_of_subjects):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)
    return scores

def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def evaluate_student(scores):
    gpa = calculate_gpa(scores)
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    else:
        grade = "D"
    return gpa, grade, gpa >= 2.0

chatgpt:
# Student Academic Evaluation System — Dynamic Input Version

## Overview
This program accepts subject scores from the user and evaluates a student's academic performance.

## Functions

### 'collect_scores(number_of_subjects)'
Requests a score for each subject.

- **Parameter:** 'number_of_subjects' — the number of scores to collect.
- **Returns:** A list of numeric scores entered by the user.
- **Input requirement:** Each entry must be convertible to a floating-point number.

### 'calculate_gpa(scores)'
Calculates GPA using the average score divided by 25.

- **Parameter:** 'scores' — a list of subject scores.
- **Returns:** A GPA on a 0–4 scale.

### 'evaluate_student(scores)'
Calculates the GPA, assigns a letter grade, and determines graduation eligibility.

- **Parameter:** 'scores' — the collected subject scores.
- **Returns:** A tuple containing '(gpa, grade, graduation_status)'.

## Processing Workflow
1. Specify the number of subjects.
2. Enter a score for each subject.
3. Calculate the GPA.
4. Determine the letter grade.
5. Check whether GPA is at least 2.0.

## Example
For scores '[80, 90, 70]', the average is 80 and the GPA is 3.2. The expected evaluation is grade B and graduation eligibility 'True'.

## Limitations
The program does not validate whether the number of subjects is positive or whether scores are within the 0–100 range. Non-numeric input causes a conversion error, and an empty score list causes a division-by-zero error during GPA calculation.
"""