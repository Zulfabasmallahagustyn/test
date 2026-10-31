"""
prompt:
Document the following object-oriented Python program for another developer. Explain the purpose of the 'Student' class, its attributes, constructor, GPA calculation, grade assignment, and graduation check. Include an example of creating and evaluating a student object. Mention any important implementation assumptions.

python
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = None

    def calculate_gpa(self):
        if self.gpa is None:
            self.gpa = sum(self.scores) / len(self.scores) / 25
        return self.gpa

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

chatgpt:
# Student Academic Evaluation System — Object-Oriented Version

## Overview
The program represents each student as an instance of the 'Student' class. Academic data and evaluation operations are grouped within the same object.

## Class: 'Student'

### Constructor: '__init__(name, scores)'
Initializes a student object.

- 'name': the student's name.
- 'scores': a list of subject scores.
- 'gpa': initialized to 'None' to indicate that GPA has not yet been calculated.

### Method: 'calculate_gpa()'
Calculates GPA as the average of the student's scores divided by 25. The result is cached in 'self.gpa' so subsequent calls reuse the stored value.

### Method: 'calculate_grade()'
Returns the letter grade based on the calculated GPA: A ≥ 3.5, B ≥ 3.0, C ≥ 2.0, and D otherwise.

### Method: 'check_graduation()'
Returns 'True' when GPA is at least 2.0 and 'False' otherwise.

## Usage Example
'''python
student = Student("Alya", [80, 90])

print(student.calculate_gpa())       # 3.4
print(student.calculate_grade())     # B
print(student.check_graduation())    # True
'''

## Implementation Note
The cached GPA assumes that 'scores' does not change after GPA calculation. If scores are modified, the cached value must be recalculated or invalidated. The class also assumes a non-empty list of valid numeric scores.
"""