"""
Results of manual documentation:

# Basic Student Evaluation Functions

The program has four functions for evaluating student performance.

- 'calculate_gpa(scores)' calculates the average of the scores and divides the result by 25 to convert it to a GPA on a 0–4 scale.
- 'calculate_grade(gpa)' returns A, B, C, or D based on the GPA thresholds.
- 'check_graduation(gpa)' returns 'True' when GPA is at least 2.0.
- 'rank_students(students)' sorts student records by GPA from highest to lowest.

Example: scores '[80, 90]' produce a GPA of '3.4', grade B, and a passing graduation status.

The functions assume that the score list is not empty and that all scores are valid numbers. The ranking function expects each student record to have a 'gpa' field.
"""