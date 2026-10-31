"""
prompt:
Perform a code review of this modular GPA calculation program. Examine the correctness of the grade-threshold loop,
GPA conversion, graduation decision, and descending ranking. Evaluate whether helper functions improve maintainability
and whether edge cases such as empty scores, invalid numbers, and threshold boundary values are handled. Recommend minimal,
testable improvements.

chatgpt:
Finding 1 - Threshold values: Sorting the thresholds from largest to smallest ensures accurate grade assignment.

Finding 2 - Empty list: The 'calculate_gpa()' function remains susceptible to division-by-zero errors.

Finding 3 - GPA boundaries: GPA values ​​of 3.50, 3.00, and 2.00 should be tested to ensure that the assigned grades are correct.

Finding 4 - Readability: Using a list of thresholds helps reduce repetitive conditional statements and makes it easier to modify the rules.
"""