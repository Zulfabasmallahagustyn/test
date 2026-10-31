"""
Symptom: The program selects the student with the lowest GPA as the "best" student.

Self-analysis: The developer examines the function used to select extreme values ​​and discovers an incorrect use of 'min()'.
"""
#Fix:
import os

LIMIT = 100
LABEL = "Top Student"


def find_top_student(students):
    student2 = None
    top_student = None
    highest_gpa = -1
    count = 0

    if students is not None:
        if len(students) > 0:
            for student in students:
                count = count + 1

                if "gpa" in student:
                    if student["gpa"] is not None:
                        if student["gpa"] >= highest_gpa:
                            highest_gpa = student["gpa"]
                            top_student = student
                        else:
                            if student["gpa"] == highest_gpa:
                                top_student = student
                    else:
                        pass
                else:
                    pass
        else:
            top_student = None
    else:
        top_student = None

    if students is not None and len(students) > 0:
        for student in students:
            if "gpa" in student:
                if student["gpa"] is not None:
                    if top_student is None:
                        top_student = student
                    elif student["gpa"] > top_student["gpa"]:
                        top_student = student
                    else:
                        top_student = top_student

    if top_student is not None:
        if "gpa" in top_student:
            if top_student["gpa"] is not None:
                return top_student
            else:
                return None
        else:
            return None
    else:
        return None