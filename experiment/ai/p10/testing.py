"""
prompt:
Design an integration test suite for the student-summary program. Test a normal list of students, GPA ordering, identification of the top student, an empty student list, tied GPAs, and a student with an empty score list. Specify expected summary fields and explain any limitations of the current implementation.

python
def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def evaluate_students(students):
    results = []

    for student in students:
        gpa = calculate_gpa(student["scores"])
        results.append({
            "name": student["name"],
            "gpa": gpa
        })

    return sorted(
        results,
        key=lambda student: student["gpa"],
        reverse=True
    )

def create_summary(students):
    ranked = evaluate_students(students)

    return {
        "total_students": len(ranked),
        "top_student": ranked[0]["name"] if ranked else None,
        "ranked_students": ranked
    }

chatgpt:
Test Case	Input	                            Expected Output
TC10.1	    Alya [80,90], Bima [90,100]	        Total 2, top student: Bima
TC10.2	    Single student with [100,100]	    Total 1, GPA 4.0
TC10.3	    Empty list of students	            Total 0, top student: None, result list []
TC10.4	    Alya and Bima have the same GPA	    Both ranked with the same GPA; relative order follows the input
TC10.5	    Student has an empty list of grades	ZeroDivisionError
TC10.6	    One of the entries lacks a name	    KeyError
TC10.7	    All grades are valid and distinct	List sorted by GPA from highest to lowest
"""