"""
prompt:
Build a Python Student Academic Evaluation System using object-oriented programming.
Create a Student class with name and scores attributes.
Implement calculate_gpa(), calculate_grade(), and check_graduation() as instance methods.
Implement rank_students() as a separate function that sorts Student objects by GPA.
Get all student names and subject scores from user input. Display each student's academic results and final ranking.
"""

#chatgpt:

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_gpa(self):
        return round(sum(self.scores) / len(self.scores) / 25, 2)

    def calculate_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.5:
            return "A"
        elif gpa >= 3.0:
            return "B"
        elif gpa >= 2.0:
            return "C"
        return "D"

    def check_graduation(self):
        return self.calculate_gpa() >= 2.0

def rank_students(students):
    return sorted(students, key=lambda s: s.calculate_gpa(),
                  reverse=True)

students = []
n = int(input("Number of students: "))

for _ in range(n):
    name = input("Student name: ")
    scores = [float(x) for x in input(
        "Enter scores separated by spaces: ").split()]
    students.append(Student(name, scores))

for i, s in enumerate(rank_students(students), 1):
    print(f"{i}. {s.name} | GPA: {s.calculate_gpa()} | "
          f"Grade: {s.calculate_grade()} | "
          f"Graduation: {s.check_graduation()}")
