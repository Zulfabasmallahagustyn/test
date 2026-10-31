"""
prompt:
Debug the dynamic subject input program. The program crashes when a user enters a non-numeric score such as "eighty".
Explain the exception and implement input validation so that the user can enter the score again without restarting the program.
Keep the GPA formula consistent with a 0–100 score scale.

chatgpt:
Diagnosis: 'float(input())' fails when the input is not a numerical representation. Use a loop and handle 'ValueError'.
"""
#Corrected code:
def get_score(subject):
    while True:
        try:
            score = float(
                input(f"Enter score for {subject}: ")
            )
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric score.")

def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)