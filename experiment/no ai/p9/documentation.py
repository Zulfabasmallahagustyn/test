"""
Results of manual documentation:

# Modular Student Evaluation

The program uses separate functions for GPA calculation, grade assignment, and student evaluation.

'calculate_gpa(scores)' calculates GPA. 'calculate_grade(gpa)' returns the corresponding letter grade. 'evaluate_student(name, scores)' calls the other functions and returns a dictionary containing 'name', 'gpa', 'grade', and 'graduated'.

Example:
python
evaluate_student("Alya", [80, 90])

The result contains a GPA of 3.4, grade B, and graduation status 'True'.

This structure allows other parts of the application to reuse the evaluation function without repeating the calculation logic. Input validation and empty-list handling are not included in the current implementation.
"""