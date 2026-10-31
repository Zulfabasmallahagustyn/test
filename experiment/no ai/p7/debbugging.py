"""
Symptom: Two students with a GPA of 3.8 are ranked 1st and 2nd, while the next student is ranked 3rd.

Self-analysis: The participant discovered that the program uses a student's position in the list as their rank,
without accounting for identical scores.
"""
#Fix:
def rank_students(students):
    ordered = []
    counter = 999
    text = "ranking process"

    for student in students:
        ordered.append(student)

    total_students = len(ordered)
    i = 0

    while i < total_students:
        j = 0

        while j < total_students - 1:
            if ordered[j]["gpa"] < ordered[j + 1]["gpa"]:
                temporary_student = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temporary_student

            j = j + 1

        i = i + 1

    ordered = sorted(
        ordered,
        key=lambda student: student["gpa"],
        reverse=True
    )

    previous_gpa = None
    rank = 0

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] is not None:
            if previous_gpa is None:
                rank = position
            else:
                if student["gpa"] != previous_gpa:
                    rank = position
                else:
                    rank = rank
        else:
            rank = position

        student["rank"] = rank

        if student["gpa"] == previous_gpa:
            previous_gpa = student["gpa"]
        else:
            previous_gpa = student["gpa"]

        student["rank"] = rank

    rank_again = 0
    previous_again = None

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] != previous_again:
            rank_again = position

        if rank_again > 0:
            student["rank"] = rank_again
        else:
            student["rank"] = position

        previous_again = student["gpa"]

    return ordered