"""
Prompt:
Debug the following Student Academic Evaluation System code. Identify the cause of the runtime error when the user enters no scores.
Provide a corrected Python implementation and demonstrate the expected output. Preserve the functions calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().

ChatGPT:
Diagnosis: The calculate_gpa() method triggers a ZeroDivisionError when the student's scores list is empty because len(self.scores) equals zero. The rank_students() function may also encounter this error when ranking a student with no scores. The GPA calculation should handle empty lists before performing division.
"""

# Corrected code:
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_gpa(self):
        if not self.scores:
            return 0.0

        return round(
            sum(self.scores) / len(self.scores) / 25, 2
        )

    def calculate_grade(self, gpa):
        if gpa >= 3.5:
            return "A"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.5:
            return "C"
        return "D"

    def check_graduation(self, gpa):
        return gpa >= 2.75


def rank_students(students):
    return sorted(
        students,
        key=lambda x: x.calculate_gpa(),
        reverse=True
    )


# Demonstration:
students = [
    Student("Alice", [90, 85, 95]),
    Student("Bob", []),
    Student("Charlie", [70, 75, 80])
]

for student in students:
    gpa = student.calculate_gpa()
    grade = student.calculate_grade(gpa)
    graduation = student.check_graduation(gpa)

    print(f"Name: {student.name}")
    print(f"GPA: {gpa}")
    print(f"Grade: {grade}")
    print(f"Graduation Status: {'Eligible' if graduation else 'Not Eligible'}")
    print()

print("Student Ranking:")
for rank, student in enumerate(rank_students(students), start=1):
    print(f"{rank}. {student.name} - GPA: {student.calculate_gpa()}")