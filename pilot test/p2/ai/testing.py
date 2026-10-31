"""
Prompt:
Generate Python unittest test cases with boundary conditions.

Output:
@dataclass
class Student:
    name: str
    scores: list

    def gpa(self):
        return round(
            sum(self.scores) / len(self.scores) / 25,
            2
        )


def test_gpa():
    student = Student("Alice", [80, 90, 85])
    assert student.gpa() == 3.4


def test_grade():
    student = Student("Alice", [90, 90, 90])
    gpa = student.gpa()

    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.5:
        grade = "C"
    else:
        grade = "D"

    assert grade == "A"


def test_graduation():
    student = Student("Bob", [80, 80, 80])
    graduation_status = student.gpa() >= 2.75

    assert graduation_status is True


def test_rank():
    students = [
        Student("Alice", [80, 80, 80]),
        Student("Bob", [90, 90, 90]),
        Student("Charlie", [70, 70, 70])
    ]

    ranked_students = sorted(
        students,
        key=lambda student: student.gpa(),
        reverse=True
    )

    assert [student.name for student in ranked_students] == [
        "Bob", "Alice", "Charlie"
    ]
"""