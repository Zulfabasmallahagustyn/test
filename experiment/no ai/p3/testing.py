"""
# Manual Test Report: Student Class

**Objective:** Check object initialization, GPA caching, grading, and graduation status.

| Test | Action | Expected result |
|---|---|---|
| T1 | Create `Student("Alya", [80, 90])` | Name Alya; GPA initially `None` |
| T2 | Calculate GPA | 3.4 |
| T3 | Calculate grade | B |
| T4 | Check graduation | `True` |
| T5 | Calculate GPA twice | Both calls return 3.4 |
| T6 | Change scores to `[100, 100]` after GPA calculation | Cached GPA remains 3.4 |
| T7 | Create a student with `[]` and calculate GPA | `ZeroDivisionError` |

**Expected conclusion:** Basic operations should pass. T6 reveals a stale-cache problem after scores change. T7 reveals missing empty-list handling.
"""