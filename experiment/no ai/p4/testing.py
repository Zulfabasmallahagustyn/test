"""
# Manual Test Report: Evaluation Report

**Objective:** Verify the report fields and printed formatting.

| Test | Input | Expected result |
|---|---|---|
| T1 | Alya, scores `[80, 90]` | GPA 3.4, grade B, graduated |
| T2 | Bima, scores `[25, 25]` | GPA 1.0, grade D, not graduated |
| T3 | Citra, scores `[100, 100]` | GPA 4.0, grade A, graduated |
| T4 | Display GPA 3.4 | Output shows `3.40` |
| T5 | Inspect returned dictionary | Contains all four expected fields |
| T6 | Empty score list | `ZeroDivisionError` |

**Expected conclusion:** Report generation and formatting should work for valid scores. Empty input is not handled.
"""