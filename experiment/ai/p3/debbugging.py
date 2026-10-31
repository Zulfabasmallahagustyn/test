"""
prompt:
Debug this object-oriented Student Academic Evaluation System. The calculate_gpa() method returns a GPA,
but other methods use self.gpa and receive None or an outdated value. Fix the state-management issue and
show how the corrected Student object calculates the GPA, grade, and graduation status.

chatgpt:
Diagnosis: The GPA value should be stored in an object, rather than simply being returned from a method.
"""
#Corrected code:
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.gpa = None

    def calculate_gpa(self):
        if not self.scores:
            self.gpa = 0.0
        else:
            self.gpa = round(
                sum(self.scores) / len(self.scores) / 25, 2
            )
        return self.gpa

    def calculate_grade(self):
        if self.gpa is None:
            self.calculate_gpa()

        if self.gpa >= 3.5:
            return "A"
        elif self.gpa >= 3.0:
            return "B"
        elif self.gpa >= 2.0:
            return "C"
        return "D"

    def check_graduation(self):
        if self.gpa is None:
            self.calculate_gpa()
        return self.gpa >= 2.0