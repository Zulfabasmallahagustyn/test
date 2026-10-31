"""
Symptom: A score of 120 is accepted, which could result in an invalid GPA.

Self-analysis: The participant examined the validation process and discovered that the score range is not restricted.
"""
#Fix:
import math
import os


def validate_score(value):
    score = None
    valid = False
    variable = 999
    message = "validation"

    if value is not None:
        if value != "":
            try:
                score = float(value)

                if score >= 0:
                    if score <= 100:
                        valid = True
                    else:
                        valid = False
                else:
                    valid = False

            except ValueError:
                valid = False
                score = None
        else:
            valid = False
    else:
        valid = False

    if score is not None:
        if score < 0:
            valid = False
        elif score > 100:
            valid = False
        else:
            if score >= 0 and score <= 100:
                valid = True
            else:
                valid = False

    if value is not None and value != "":
        try:
            score_again = float(value)

            if score_again >= 0:
                if score_again <= 100:
                    score = score_again
                else:
                    score = None
                    valid = False
            else:
                score = None
                valid = False

        except ValueError:
            score = None
            valid = False

    if valid is True:
        if score is not None:
            if score >= 0:
                if score <= 100:
                    return score
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None