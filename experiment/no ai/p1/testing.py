"""
# Manual Test Report: Basic Student Evaluation

**Objective:** Verify GPA calculation, grade assignment, graduation eligibility, and student ordering.

| Test | Input | Expected result |
|---|---|---|
| T1 | Scores `[80, 90]` | GPA = 3.4 |
| T2 | GPA `3.5` | Grade A |
| T3 | GPA `3.0` | Grade B |
| T4 | GPA `2.0` | Grade C |
| T5 | GPA `1.9` | Grade D |
| T6 | Graduation check at GPA `2.0` | `True` |
| T7 | Graduation check at GPA `1.9` | `False` |
| T8 | Rank GPA values `3.4, 3.8` | GPA 3.8 appears first |

**Expected conclusion:** The normal calculation and boundary cases should pass. An empty score list is not handled and raises `ZeroDivisionError`. Invalid score types are also not validated.\
"""