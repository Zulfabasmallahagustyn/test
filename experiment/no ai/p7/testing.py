"""
# Manual Test Report: Student Ranking

**Objective:** Verify descending sorting and competition ranking.

| Test | Input | Expected result |
|---|---|---|
| T1 | GPA `[3.4, 3.8, 3.0]` | Sorted `[3.8, 3.4, 3.0]` |
| T2 | GPA `[3.8, 3.8, 3.4]` | Ranks 1, 1, 3 |
| T3 | One student with GPA 2.0 | Rank 1 |
| T4 | Empty list | Empty list |
| T5 | Three students with GPA 3.2 | All rank 1 |
| T6 | Inspect original dictionaries after ranking | Original dictionaries contain `rank` |
| T7 | Record without `gpa` | `KeyError` |

**Expected conclusion:** Sorting and ranking should work for valid records. The function modifies the original dictionaries by adding rank fields and does not handle missing GPA values.
"""