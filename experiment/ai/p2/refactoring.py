"""
prompt:
Refactor the dynamic subject input program. Separate user input, score validation and GPA calculation into independent functions. Remove duplicated input-handling code, preserve support for a variable number of subjects, and maintain the score range of 0 to 100. Include a test using three subject scores.
"""

#chatgpt:
def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score: "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")


def collect_scores(subjects):
    return [get_valid_score(subject) for subject in subjects]


def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)


def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    if gpa >= 3.0:
        return "B"
    if gpa >= 2.0:
        return "C"
    return "D"


def check_graduation(gpa):
    return gpa >= 2.0


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)


scores = [80, 90, 70]
print("GPA:", calculate_gpa(scores))