"""
prompt:
Refactor the object-oriented Student Academic Evaluation System. Improve class cohesion, avoid repeated GPA calculations,
and make the methods easier to maintain. Preserve the Student class and its GPA, grade, graduation, and ranking functionality.
Keep the current grading thresholds and demonstrate the result with one Student instance.
"""

#chatgpt:
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = None

    def calculate_gpa(self):
        if not self.scores:
            self.gpa = 0.0
        else:
            average_score = sum(self.scores) / len(self.scores)
            self.gpa = round(average_score / 25, 2)
        return self.gpa

    def calculate_grade(self):
        gpa = self.gpa if self.gpa is not None else self.calculate_gpa()

        if gpa >= 3.5:
            return "A"
        if gpa >= 3.0:
            return "B"
        if gpa >= 2.0:
            return "C"
        return "D"

    def check_graduation(self):
        gpa = self.gpa if self.gpa is not None else self.calculate_gpa()
        return gpa >= 2.


def rank_students(students):
    return sorted(students, key=lambda s: s.gpa or 0, reverse=True)


student = Student("Alya", [80, 90])
print(student.calculate_gpa())
print(student.calculate_grade())
print(student.check_graduation())