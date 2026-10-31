"""
prompt:
Develop boundary-value tests for this grading module. Test values immediately below, exactly at, and immediately above the GPA thresholds of 2.0, 3.0, and 3.5. Also test the minimum and maximum expected GPA values. Report expected grades and identify any behavior outside the 0–4 GPA range.

python
GRADE_THRESHOLDS = [
    (3.5, "A"),
    (3.0, "B"),
    (2.0, "C"),
    (0.0, "D")
]

def calculate_grade(gpa):
    for threshold, grade in GRADE_THRESHOLDS:
        if gpa >= threshold:
            return grade
    return "D"

chatgpt:
Test Case   GPA     Expected Grade
TC6.1       3.49    B
TC6.2       3.50    A
TC6.3       3.51    A
TC6.4       2.99    C
TC6.5       3.00    B
TC6.6       3.01    B
TC6.7       1.99    D
TC6.8       2.00    C
TC6.9       2.01    C
TC6.10      0.00    D
TC6.11      4.00    A
TC6.12      4.50    A
"""