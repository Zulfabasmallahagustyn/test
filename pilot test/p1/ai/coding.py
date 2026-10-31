""" 
Prompt:
    Generate a Python program for a Student Academic Evaluation System.
    Requirements:
        Calculate GPA from a list of scores.
        Determine letter grades.
        Check graduation eligibility.
        Rank students based on GPA.
        Use clean and maintainable code.
"""

# ChatGPT Output:
class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores
    def calculate_gpa(self):
        return round(sum(self.scores)/len(self.scores)/25,2)
    def calculate_grade(self,gpa):
        if gpa>=3.5:
            return "A"
        elif gpa>=3.0:
            return "B"
        elif gpa>=2.5:
            return "C"
        return "D"
    def check_graduation(self,gpa):
        return gpa>=2.75
def rank_students(students):
    return sorted(
        students,
        key=lambda x:x.calculate_gpa(),
        reverse=True
    )
