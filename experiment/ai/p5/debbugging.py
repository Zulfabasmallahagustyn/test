"""
prompt:
Debug the input validation program. It currently accepts scores outside the valid range of 0 to 100,
which can produce an invalid GPA. Add boundary validation and handle non-numeric input.
Demonstrate the behavior for scores of 120 and 85.

chatgpt:
Diagnosis: The program needs to check the input type and value constraints before saving the score.
"""
#Corrected code:
def validate_score(value):
    try:
        score = float(value)
    except ValueError:
        return None

    if not 0 <= score <= 100:
        return None

    return score

print(validate_score("120"))
print(validate_score("85"))