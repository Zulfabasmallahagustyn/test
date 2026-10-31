"""
prompt:
Act as a software test engineer. Create test cases for the following Student Academic Evaluation System functions: `calculate_gpa()`, `calculate_grade()`, `check_graduation()`, and `rank_students()`. Include normal cases, boundary cases, and invalid-input considerations. For each test case, specify the input, expected output, purpose, and pass/fail criteria. Do not modify the source code.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.0:
        return "C"
    return "D"

def check_graduation(gpa):
    return gpa >= 2.0

def rank_students(students):
    return sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

chatgpt:
Test case	Input	                Expected output	    Objective
TC1.1	    calculate_gpa([80, 90])	3.4	                Normal GPA
TC1.2	    calculate_gpa([0, 100])	2.0	                Minimum and maximum values
TC1.3	    calculate_grade(3.5)	"A"	                Threshold for an A grade
TC1.4	    calculate_grade(3.0)	"B"	                Threshold for an B grade
TC1.5	    calculate_grade(2.0)	"C"	                Threshold for an C grade
TC1.6	    check_graduation(1.99)	False	            Does not meet graduation requirements
TC1.7	    check_graduation(2.0)	True	            Right on the verge of graduation
TC1.8	    Ranking GPA 3.4, 3.8	Sequence 3.8, 3.4	Descending order
"""