"""
# Manual Test Report: Grade Thresholds

**Objective:** Check grade boundaries.

| Test | GPA | Expected grade |
|---|---:|---|
| T1 | 3.49 | B |
| T2 | 3.50 | A |
| T3 | 3.51 | A |
| T4 | 2.99 | C |
| T5 | 3.00 | B |
| T6 | 3.01 | B |
| T7 | 1.99 | D |
| T8 | 2.00 | C |
| T9 | 0.00 | D |
| T10 | 4.00 | A |

**Expected conclusion:** All listed cases should pass according to the implemented threshold rules. GPA values outside the 0–4 range are not explicitly rejected by the function.
"""