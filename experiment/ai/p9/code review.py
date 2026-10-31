"""
prompt:
Review this modular Python implementation for separation of concerns, function reuse, testability, and correctness.
Examine input_student(), input_scores(), display_results(), main(), and the four required academic functions.
Identify missing edge-case handling, unnecessary coupling, duplicated logic, and
any problems that could affect the consistency of GPA calculations or rankings.

chatgpt:
Finding 1 - Modularity: Separating input, processing, and output makes functions easier to test.

Finding 2 - Name validation: Empty names must be rejected before creating a student record.

Finding 3 - List of scores: 'input_scores()' must ensure that the number of subjects is a positive value and
that each score falls within the range of 0-100.

Finding 4 - Unit testing: Calculation functions should be tested independently of 'input()' and 'print()' operations.
"""