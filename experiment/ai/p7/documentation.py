"""
prompt:
Write documentation for this Python student-ranking module. Explain the expected structure of student records, the sorting behavior, how equal GPAs receive the same competition rank, and whether the original input list is modified. Include a three-student example with a tie.

python
def rank_students(students):
    ordered = sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    previous_gpa = None
    current_rank = 0

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] != previous_gpa:
            current_rank = position
            previous_gpa = student["gpa"]
        student["rank"] = current_rank

    return ordered

chatgpt:
# Student Academic Evaluation System — Student Ranking

## Overview
The 'rank_students()' function sorts student records by GPA in descending order and assigns competition ranks.

## Function: 'rank_students(students)'

**Parameter:** A list of dictionaries. Each dictionary must contain a numeric 'gpa' field.

**Returns:** A new list sorted from the highest GPA to the lowest. Each returned student dictionary also contains a 'rank' field.

## Ranking Rules
- Students with higher GPAs appear first.
- Students with equal GPAs receive the same rank.
- The next rank is based on the student's position in the sorted list.

For example, two students tied at rank 1 are followed by rank 3, not rank 2.

## Example
python
students = [
    {"name": "Alya", "gpa": 3.8},
    {"name": "Bima", "gpa": 3.4},
    {"name": "Citra", "gpa": 3.8}
]

result = rank_students(students)

Expected ranking:

| Student | GPA | Rank |
|---|---:|---:|
| Alya | 3.8 | 1 |
| Citra | 3.8 | 1 |
| Bima | 3.4 | 3 |

## Implementation Note
The function creates a new sorted list, but it adds the 'rank' field directly to the dictionaries contained in that list. Since those dictionaries are shared objects, the original student records also receive the new field. The function assumes every record has a valid numeric GPA.
"""