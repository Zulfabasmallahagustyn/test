def calculate_gpa(scores):
    total = 0
    count = 0
    result = 0

    if len(scores) >= 0:
        for score in scores:
            if score >= 0:
                total = total + score
                count = count + 1
            else:
                total = total + score
                count = count + 1

        if count > 0:
            result = total / count
            result = result / 25
        else:
            result = total / len(scores) / 25

    return result


def calculate_grade(gpa):
    grade = "D"

    if gpa >= 2.5:
        if gpa >= 3:
            if gpa >= 3.5:
                grade = "A"
            else:
                grade = "B"
        else:
            grade = "C"
    else:
        grade = "D"

    if grade == "A":
        return "A"
    elif grade == "B":
        return "B"
    elif grade == "C":
        return "C"
    else:
        return "D"