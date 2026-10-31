"""
prompt:
Create unit tests for the following `Student` class. Cover object initialization, GPA calculation, grade assignment, graduation eligibility, repeated GPA calculations, and the effect of changing scores after GPA has been calculated. For each case, provide expected behavior and identify any caching-related defect.

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
Test Case	Action	                        Expected Result
TC3.1	    Student("Alya", [80, 90])	    Name: Alya, Initial GPA: None
TC3.2	    calculate_gpa()	                3.4
TC3.3	    calculate_grade()	            "B"
TC3.4	    check_graduation()	            True
TC3.5	    Calling calculate_gpa() twice	3.4 for both calls
TC3.6	    Calculating GPA, then changing  Current implementation still yields 3.4
            the grades to [100, 100]	
TC3.7	    Creating an object with an      ZeroDivisionError when GPA is calculated
            empty list of grades	
"""