"""
prompt:
Review this student ranking implementation, especially the handling of equal GPA values.
Verify that students with the same GPA receive the same competition rank, such as 1, 1, 3.
Check sorting stability, grade calculation, graduation eligibility, and input validation.
Identify any side effects caused by modifying student dictionaries and
recommend appropriate fixes without changing the required ranking policy.

chatgpt:
Finding 1 - Ranking policy: A competition-based approach results in a ranking of 1, 1, 3 when two students tie for the first position.

Finding 2 - GPA comparison: GPA values ​​are rounded to two decimal places before ranking takes place.
Two distinct original values ​​may become identical after rounding.

Finding 3 - Side effects: This function adds a 'rank' attribute directly to the student dictionary, meaning the input data is modified.

Finding 4 - Empty input: Missing scores and empty names must be handled before any records are created.
"""