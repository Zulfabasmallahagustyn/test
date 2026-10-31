"""
prompt:
Debug the student ranking program. Students with identical GPAs should receive the same competition rank.
For example, if two students tie for first place, the next student should be ranked third.
Correct the ranking algorithm and demonstrate it with three students whose GPAs are 3.8, 3.8, and 3.4.

chatgpt:
Diagnosis: A position in an ordered list is not always the same as a rank in a competition.
Ranks should only be updated when the GPA changes.
"""
#Correction code:
def rank_students(students):
    ordered = sorted(
        students,
        key=lambda s: s["gpa"],
        reverse=True
    )

    previous_gpa = None
    rank = 0

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] != previous_gpa:
            rank = position

        student["rank"] = rank
        previous_gpa = student["gpa"]

    return ordered

students = [
    {"name": "Alya", "gpa": 3.8},
    {"name": "Bima", "gpa": 3.8},
    {"name": "Citra", "gpa": 3.4}
]

for student in rank_students(students):
    print(student["name"], student["rank"])