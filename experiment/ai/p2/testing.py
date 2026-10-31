"""
prompt:Design a functional test suite for a Python program that collects subject scores dynamically, calculates GPA, assigns a letter grade, and checks graduation eligibility. Test a normal input sequence, decimal scores, non-numeric input, zero subjects, and scores outside the 0–100 range. Provide expected outputs and explain which cases the current implementation is expected to pass or fail.

python
def collect_scores(number_of_subjects):
    scores = []
    for i in range(number_of_subjects):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)
    return scores

def calculate_gpa(scores):
    return sum(scores) / len(scores) / 25

def evaluate_student(scores):
    gpa = calculate_gpa(scores)
    if gpa >= 3.5:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    else:
        grade = "D"
    return gpa, grade, gpa >= 2.0

chatgpt:
Test case	Input	                Expected output	                    Evaluation
TC2.1	    Score [80, 90, 70]	    (3.2, "B", True)	                Pass
TC2.2	    Score [100, 100]	    (4.0, "A", True)	                Pass
TC2.3	    Score [0, 25]	        (0.5, "D", False)	                Pass
TC2.4	    Score [50, 50]	        (2.0, "C", True)	                Pass
TC2.5	    Text "abc" as a score	ValueError	                        Failure to handle invalid input securely
TC2.6	    Number of courses 0     An error occurred while calculating Failure in the event of empty input must be handled
                                    the GPA from an empty list.	        
TC2.7	    Score 120	            The program accepts a number and    Fails if range validation is required
                                    produces an evaluation.
TC2.8	    Score -5	            The program accepts a number and    Fails if range validation is required
                                    produces an evaluation.
"""