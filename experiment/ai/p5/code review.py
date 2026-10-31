"""
prompt:
Review this Python program with a focus on robust input validation, exception handling, numeric boundaries,
and maintainability. Check whether the input helper functions correctly distinguish positive integer counts
from numeric scores between 0 and 100, including decimal scores. Verify all four academic evaluation functions
and suggest specific fixes for any validation or correctness problems.

chatgpt:
Finding 1 - Data type validation: Functions that only accept integers should not be used to process valid values ​​such as 87.5.

Finding 2 - Value constraints: Values ​​of 0 and 100 must be accepted; values ​​below 0 or above 100 must be rejected.

Finding 3 - Exception handling: 'ValueError' must be handled so that text-based input does not cause the program to crash.

Finding 4 - Academic function: Input validation does not eliminate the need for safeguards against empty values ​​within 'count_gpa()'.
"""