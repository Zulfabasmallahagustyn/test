"""
prompt:
Refactor the detailed student report program by separating academic calculations from report formatting.
Avoid mixing print statements with business logic, use a reusable report-generation function,
and preserve the existing GPA, grade, and graduation rules. Show the report for a student named Alya with scores of 80 and 90.
"""

#chatgpt:
def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)


def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    if gpa >= 3.0:
        return "B"
    if gpa >= 2.0:
        return "C"
    return "D"


def check_graduation(gpa):
    return gpa >= 2.0


def generate_report(name, scores):
    gpa = calculate_gpa(scores)

    return {
        "name": name,
        "gpa": gpa,
        "grade": calculate_grade(gpa),
        "graduation": check_graduation(gpa)
    }


def display_report(report):
    print(f"Student: {report['name']}")
    print(f"GPA: {report['gpa']:.2f}")
    print(f"Grade: {report['grade']}")
    status = "Passed" if report["graduation"] else "Not passed"
    print(f"Graduation: {status}")


report = generate_report("Alya", [80, 90])
display_report(report)