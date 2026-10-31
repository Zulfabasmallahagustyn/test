"""
# Manual Test Report: Modular Student Evaluation

**Objective:** Verify evaluation outputs and returned dictionary structure.

| Test | Input | Expected result |
|---|---|---|
| T1 | Alya `[80, 90]` | GPA 3.4, B, graduated |
| T2 | Bima `[100, 100]` | GPA 4.0, A, graduated |
| T3 | Citra `[25, 25]` | GPA 1.0, D, not graduated |
| T4 | Dina `[50, 50]` | GPA 2.0, C, graduated |
| T5 | Inspect result keys | `name`, `gpa`, `grade`, `graduated` |
| T6 | Empty scores | `ZeroDivisionError` |
| T7 | Scores `[80, "abc"]` | `TypeError` |

**Expected conclusion:** Valid cases should pass. The code needs input validation to handle empty lists and incompatible data types safely.
"""