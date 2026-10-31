"""
# Manual Test Report: Dynamic Score Input

**Objective:** Verify score collection and evaluation.

| Test | Input | Expected result |
|---|---|---|
| T1 | Scores `80, 90, 70` | GPA 3.2, grade B, graduated |
| T2 | Scores `100, 100` | GPA 4.0, grade A, graduated |
| T3 | Scores `0, 25` | GPA 0.5, grade D, not graduated |
| T4 | Scores `50, 50` | GPA 2.0, grade C, graduated |
| T5 | Enter `"abc"` | `ValueError` |
| T6 | Number of subjects = 0 | Division by zero during evaluation |
| T7 | Enter score 120 | Accepted without validation |
| T8 | Enter score -5 | Accepted without validation |

**Expected conclusion:** Normal numeric cases should pass. The program does not reject out-of-range values, and invalid text or an empty score list causes an error.
"""