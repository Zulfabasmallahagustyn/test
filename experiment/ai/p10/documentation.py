"""
prompt:
Create technical documentation for the following Python student-summary program. Describe how individual student records are evaluated, how students are ranked, what information is included in the summary, and what happens when the student list is empty. Provide a small example and clearly state any assumptions.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def evaluate_students(students):
    results = []

    for student in students:
        gpa = calculate_gpa(student["scores"])
        results.append({
            "name": student["name"],
            "gpa": gpa
        })

    return sorted(
        results,
        key=lambda student: student["gpa"],
        reverse=True
    )

def create_summary(students):
    ranked = evaluate_students(students)

    return {
        "total_students": len(ranked),
        "top_student": ranked[0]["name"] if ranked else None,
        "ranked_students": ranked
    }

chatgpt:
# Student Academic Evaluation System — Summary and Ranking

## Overview
This program evaluates a collection of students, sorts them by GPA, and produces a summary of the results.

## Function: 'calculate_gpa(scores)'
Calculates GPA as the average score divided by 25. The score list must be non-empty.

## Function: 'evaluate_students(students)'
Processes each student record and returns a list containing each student's name and calculated GPA, sorted from highest to lowest GPA.

Each input student record must contain:
- 'name': the student's name.
- 'scores': a list of numeric subject scores.

## Function: 'create_summary(students)'
Returns a summary dictionary with three fields:

- 'total_students': number of students evaluated.
- 'top_student': name of the student with the highest GPA, or 'None' if the list is empty.
- 'ranked_students': list of student names and GPAs sorted in descending order.

## Example
python
students = [
    {"name": "Alya", "scores": [80, 90]},
    {"name": "Bima", "scores": [90, 100]},
    {"name": "Citra", "scores": [70, 80]}
]

summary = create_summary(students)

Bima has the highest GPA because the average of the scores is 95, producing a GPA of 3.8.

## Limitations
An empty student list produces a valid summary with a count of zero and 'top_student' set to 'None'. However, a student with an empty score list causes a division-by-zero error. This implementation sorts students but does not assign explicit rank numbers or resolve ties using competition ranking.
"""