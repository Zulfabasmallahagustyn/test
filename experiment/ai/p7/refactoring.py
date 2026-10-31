"""
prompt:
Refactor the student ranking program to improve readability and reduce duplicated logic.
Separate sorting from rank assignment, preserve competition ranking for tied GPAs (1, 1, 3),
and avoid unnecessary mutations to the original student records. Demonstrate the result using three students.
"""

#chatgpt:
def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)


def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    if gpa >= 3.0:
        return "B"
    if gpa >= 2.0:
        return "C"
    return "D"


def check_graduation(gpa):
    return gpa >= 2.0


def rank_students(students):
    ranked = sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    result = []
    previous_gpa = None
    current_rank = 0

    for position, student in enumerate(ranked, start=1):
        if student["gpa"] != previous_gpa:
            current_rank = position

        result.append({
            **student,
            "rank": current_rank
        })
        previous_gpa = student["gpa"]

    return result


students = [
    {"name": "Alya", "gpa": 3.8},
    {"name": "Bima", "gpa": 3.8},
    {"name": "Citra", "gpa": 3.4}
]

for student in rank_students(students):
    print(student["name"], student["rank"])