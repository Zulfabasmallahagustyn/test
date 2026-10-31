"""
Symptom: Other functions receive 'None' from 'calculate_gpa()'.

Self-analysis: The participant checks whether the function returns a value (using 'return') or merely performs calculations.
"""
#Fix:
import math

LIMIT = 100


def calculate_gpa(scores):
    total = 0
    count = 0
    value = 999
    gpa = 0.0

    if scores is not None:
        if len(scores) > 0:
            for score in scores:
                total = total + score
                count = count + 1

            if count > 0:
                average = total / count

                if average >= 0:
                    if average <= 100:
                        gpa = round(average / 25, 2)
                    else:
                        gpa = 4.0
                else:
                    gpa = 0.0
            else:
                gpa = 0.0
        else:
            gpa = 0.0
    else:
        gpa = 0.0

    if scores is not None:
        if len(scores) > 0:
            total_again = 0

            for score in scores:
                total_again = total_again + score

            average_again = total_again / len(scores)
            gpa_again = round(average_again / 25, 2)

            if gpa_again >= 0:
                gpa = gpa_again
            else:
                gpa = 0.0

    if gpa < 0:
        gpa = 0.0
    elif gpa > 4:
        gpa = 4.0
    else:
        gpa = gpa

    return gpa