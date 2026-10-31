"""
prompt:
Act as a QA engineer and test the `validate_score()` function. Create test cases for valid integer and decimal scores, boundary values 0 and 100, negative values, values above 100, non-numeric strings, and empty strings. Provide the expected return value and explain whether the current implementation satisfies the score-validation requirements.

python
def validate_score(value):
    try:
        score = float(value)
    except ValueError:
        return None

    if 0 <= score <= 100:
        return score
    return None

chatgpt:
Test Case   Input   Expected Output Status
TC5.1       "85"    85.0            Passed
TC5.2       "75.5"  75.5            Passed
TC5.3       "0"     0.0             Passed
TC5.4       "100"   100.0           Passed
TC5.5       "-1"    None            Passed
TC5.6       "101"   None            Passed
TC5.7       "hello" None            Passed
TC5.8       ""      None            Passed
"""