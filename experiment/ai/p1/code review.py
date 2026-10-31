"""
prompt:
Review the following Python Student Academic Evaluation System for correctness,
input validation, code readability, and compliance with its functional requirements.
Check calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Identify specific defects, explain their impact, and recommend minimal fixes
without unnecessarily rewriting the entire program. The GPA formula is average score divided by 25,
the grade thresholds are A >= 3.5, B >= 3.0, C >= 2.0, and D otherwise, and graduation requires GPA >= 2.0.
The program must accept multiple students and validate user input.

chatgpt:
Finding 1 - GPA Calculation
The 'calculate_gpa()' function computes the GPA by dividing the average score by 25.
While this formula aligns with the specifications, the function will trigger a 'ZeroDivisionError' if called with an empty list.
Priority: High

Finding 2 - Student Names
The program checks for empty names using 'strip()'; however, duplicate names are not handled.
This could lead to ambiguous reports if two students share the same name.
Priority: Low

Finding 3 - Ranking
Sorting by GPA in descending order has been implemented correctly.
If two students have the same GPA, their relative order remains the same as in the original dataset;
a policy for handling ties has not yet been established.
Priority: Low
"""
