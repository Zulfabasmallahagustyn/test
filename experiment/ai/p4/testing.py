"""
prompt:
Test the report-generation program below. Verify the dictionary fields, GPA precision, grade boundaries, graduation status, and displayed output. Include at least one test with a student who passes and one who does not. Distinguish between the raw GPA value and its formatted display.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def generate_report(name, scores):
    gpa = calculate_gpa(scores)
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    else:
        grade = "D"

    return {
        "name": name,
        "gpa": gpa,
        "grade": grade,
        "graduated": gpa >= 2.0
    }

def display_report(report):
    print(f"Student: {report['name']}")
    print(f"GPA: {report['gpa']:.2f}")
    print(f"Grade: {report['grade']}")
    print(f"Graduated: {report['graduated']}")

chatgpt:
Test Case   Input                                   Expected Result
TC4.1       generate_report("Alya", [80, 90])       GPA 3.4, grade B, passed: True
TC4.2       generate_report("Bima", [25, 25])       GPA 1.0, grade D, passed: False
TC4.3       generate_report("Image", [100, 100])    GPA 4.0, grade A, passed: True
TC4.4       Displaying the report GPA 3.4           Text: GPA 3.40
TC4.5       Checking the report dictionary          Contains name, GPA, grade, and pass status
TC4.6       Empty list of grades                    ZeroDivisionError
"""