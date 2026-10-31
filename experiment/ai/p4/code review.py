"""
prompt:
Conduct a code review of this Python Student Academic Evaluation System with a formatted academic report.
Examine separation of concerns, report accuracy, graduation-status messages, input validation, and ranking behavior.
Verify that GPA, letter grades, and graduation eligibility match the given requirements. Report actionable issues
and avoid changing the intended output format unnecessarily.

chatgpt:
Finding 1 - Separation of responsibilities: Separating 'display_report()' from the calculation logic
will improve code readability and maintainability.

Finding 2 - Graduation status: Converting a boolean value into a text message is an appropriate approach,
provided that the 'graduated' value is derived from 'check_graduation()'.

Finding 3 - Output consistency: Formatting the GPA value to two decimal places enhances readability
without altering the actual numerical value.

Finding 4 - Validation: The program still requires handling for non-numerical values,
values ​​outside the expected range, and empty lists of grades.
"""