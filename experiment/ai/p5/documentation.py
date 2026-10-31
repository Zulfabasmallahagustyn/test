"""
prompt:
Prepare developer documentation for this Python input-validation component. Explain how 'validate_score()' handles numeric input, the valid score range, the return values, and how calling code should respond to invalid input. Include examples for valid, out-of-range, and non-numeric values.

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
# Student Academic Evaluation System — Score Validation

## Overview
The 'validate_score()' function converts a user-provided value into a floating-point score and checks whether it falls within the accepted range.

## Function: 'validate_score(value)'

**Parameter**
- 'value': a value that can potentially be converted to a number, commonly a string from user input.

**Behavior**
1. Attempts to convert 'value' to a floating-point number.
2. Returns 'None' if conversion raises 'ValueError'.
3. Returns the numeric score if it is between 0 and 100, inclusive.
4. Returns 'None' for values outside the valid range.

**Return value**
- 'float': valid score.
- 'None': invalid or out-of-range input.

## Examples
python
validate_score("85")       # 85.0
validate_score("120")      # None
validate_score("hello")    # None
validate_score("0")        # 0.0
validate_score("100")      # 100.0

## Integration Guidance
Calling code should check whether the return value is 'None'. If it is, the program should request another input or display an error message.

## Limitations
The function catches 'ValueError', but not every possible exception type. It validates the score range but does not determine whether a score is academically appropriate for a particular subject.
"""