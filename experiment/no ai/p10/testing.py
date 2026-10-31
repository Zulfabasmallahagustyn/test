"""
# Manual Test Report: Student Summary and Ranking

**Objective:** Verify student evaluation, ranking order, and summary generation.

| Test | Input | Expected result |
|---|---|---|
| T1 | Alya `[80, 90]`, Bima `[90, 100]` | Bima is the top student |
| T2 | One student with `[100, 100]` | Total 1, GPA 4.0 |
| T3 | Empty student list | Total 0, top student `None` |
| T4 | Two students with equal GPA | Both have equal GPA; original relative order retained |
| T5 | Student with empty scores | `ZeroDivisionError` |
| T6 | Record missing `name` | `KeyError` |
| T7 | Several valid records with different GPAs | Sorted from highest to lowest |

**Expected conclusion:** Summary generation should work for valid input and an empty student list. Empty score lists and incomplete student records are not handled safely. The implementation does not assign explicit rank numbers or calculate grades.
"""