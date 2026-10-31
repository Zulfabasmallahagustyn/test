"""
# Manual Test Report: Academic Evaluation Menu

**Objective:** Verify menu output and input selection.

| Test | Input or action | Expected result |
|---|---|---|
| T1 | Choice `"1"` | GPA selection message |
| T2 | Choice `"2"` | Grade selection message |
| T3 | Choice `"3"` | Graduation selection message |
| T4 | Choice `"4"` | `Exit` |
| T5 | Choice `"5"` | `Invalid choice` |
| T6 | Empty string | `Invalid choice` |
| T7 | Choice `"abc"` | `Invalid choice` |
| T8 | Call `display_menu()` | Four menu options printed |

**Expected conclusion:** The menu selection functions should pass these checks. Options 1–3 do not perform the actual academic calculations; they only return selection messages.
"""