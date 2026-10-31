"""
# Manual Test Report: Score Validation

**Objective:** Verify valid and invalid score inputs.

| Test | Input | Expected result |
|---|---|---|
| T1 | `"85"` | 85.0 |
| T2 | `"75.5"` | 75.5 |
| T3 | `"0"` | 0.0 |
| T4 | `"100"` | 100.0 |
| T5 | `"-1"` | `None` |
| T6 | `"101"` | `None` |
| T7 | `"hello"` | `None` |
| T8 | `""` | `None` |

**Expected conclusion:** The listed test cases should pass. The function correctly handles ordinary numeric values, out-of-range values, and non-numeric strings. Non-finite numbers should be tested separately if they are prohibited by the requirements.
"""