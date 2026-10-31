"""
prompt:
Review this Python Student Academic Evaluation System with a class summary.
Check GPA calculations, grade assignments, graduation counts, class-average GPA, top-student identification, ranking,
and empty-data handling. Evaluate numeric accuracy, rounding consistency, input validation, and maintainability.
Report concrete issues and suggest minimal corrections while preserving the summary-report requirements.

chatgpt:
Finding 1 - Class average: The program calculates the average score based on students GPAs,
rather than on the grades of individual courses. This aligns with the definition of a class GPA average being used.

Finding 2 - Handling empty data: Checking for the existence of students prevents division by zero in situations
where no students are enrolled.

Finding 3 - Top student: Selecting the first student from a sorted list accurately identifies one of the students with the highest GPA.

Finding 4 - Validation: The number of courses and the grades entered still require consistent validation.
"""