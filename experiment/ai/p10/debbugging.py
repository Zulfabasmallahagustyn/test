"""
prompt:
Debug the student summary program. It incorrectly identifies the student with the lowest GPA as the top student.
Correct the selection logic, handle an empty student list, and demonstrate the result for students
with GPAs of 3.2, 3.8, and 3.5.

chatgpt:
Diagnosis: To select the highest GPA, the program should use 'max()'.
Empty lists must be handled so that the function call does not trigger a 'ValueError'.
"""
#Corrected code:
def find_top_student(students):
    if not students:
        return None

    return max(
        students,
        key=lambda student: student["gpa"]
    )

students = [
    {"name": "Alya", "gpa": 3.2},
    {"name": "Bima", "gpa": 3.8},
    {"name": "Citra", "gpa": 3.5}
]

top_student = find_top_student(students)

if top_student:
    print(
        f"Top student: {top_student['name']} "
        f"(GPA: {top_student['gpa']})"
    )
else:
    print("No student records available.")