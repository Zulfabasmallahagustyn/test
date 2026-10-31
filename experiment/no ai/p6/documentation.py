"""
Results of manual documentation:

# Grade Thresholds

'GRADE_THRESHOLDS' stores the GPA boundaries and their corresponding letter grades. The list is ordered from the highest GPA boundary to the lowest.

'calculate_grade(gpa)' checks the thresholds in order and returns the first grade whose boundary is met.

Examples:
- GPA 3.5 returns A.
- GPA 3.4 returns B.
- GPA 3.0 returns B.
- GPA 2.0 returns C.
- GPA 1.9 returns D.

The threshold order should be maintained when the grading rules are changed. The function does not validate GPA input or restrict it to the 0-4 range.
"""