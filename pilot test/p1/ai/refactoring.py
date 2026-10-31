"""
Prompt:
    Refactor this code to improve maintainability and reduce cognitive complexity.
"""

#chatgpt
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_gpa(self):
        if not self.scores:
            return 0.0

        average_score = sum(self.scores) / len(self.scores)
        return round(average_score / 25, 2)

    def calculate_grade(self, gpa):
        grade_thresholds = [
            (3.5, "A"),
            (3.0, "B"),
            (2.5, "C"),
        ]

        for threshold, grade in grade_thresholds:
            if gpa >= threshold:
                return grade

        return "D"

    def check_graduation(self, gpa):
        graduation_threshold = 2.75
        return gpa >= graduation_threshold


def rank_students(students):
    return sorted(
        students,
        key=lambda student: student.calculate_gpa(),
        reverse=True
    )