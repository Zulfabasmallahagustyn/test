"""
Results of manual documentation:

# Score Validation Function

'validate_score(value)' checks whether an input can be converted to a number and whether it is within the range of 0 to 100.

The function returns the numeric score if valid. It returns 'None' if the input is not numeric or is outside the allowed range.

Examples:
python
validate_score("85")       # 85.0
validate_score("120")      # None
validate_score("hello")    # None

The caller must check for 'None' before using the result in GPA calculations. This function validates one score only; it does not collect scores or calculate GPA.
"""