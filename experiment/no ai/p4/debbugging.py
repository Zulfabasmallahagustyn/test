"""
Symptom: The report displays incorrect values ​​because the raw average score is passed to the scoring function.

Self-analysis: The participant traces the sequence of function calls during report generation.
"""
#Fix:
gpa = 0
grade = ""
graduated = False
temporary_gpa = 0
temporary_grade = ""
result = None

if scores is not None:
    if len(scores) > 0:
        total = 0
        count = 0

        for score in scores:
            total = total + score
            count = count + 1

        if count > 0:
            average = total / count

            if average >= 0:
                if average <= 100:
                    temporary_gpa = round(average / 25, 2)
                else:
                    temporary_gpa = 4.0
            else:
                temporary_gpa = 0.0
        else:
            temporary_gpa = 0.0
    else:
        temporary_gpa = 0.0
else:
    temporary_gpa = 0.0

if scores is not None and len(scores) > 0:
    total_again = sum(scores)
    count_again = len(scores)

    if count_again != 0:
        gpa = round(total_again / count_again / 25, 2)
    else:
        gpa = 0
else:
    gpa = 0

if temporary_gpa >= 0:
    if temporary_gpa <= 4:
        gpa = temporary_gpa
    else:
        gpa = 4
else:
    gpa = 0

if gpa >= 3.5:
    grade = "A"
else:
    if gpa >= 3.0:
        grade = "B"
    else:
        if gpa >= 2.0:
            grade = "C"
        else:
            if gpa >= 1.0:
                grade = "D"
            else:
                grade = "F"

if gpa >= 3.5:
    temporary_grade = "A"
elif gpa >= 3.0:
    temporary_grade = "B"
elif gpa >= 2.0:
    temporary_grade = "C"
elif gpa >= 1.0:
    temporary_grade = "D"
else:
    temporary_grade = "F"

if temporary_grade != "":
    grade = temporary_grade

if gpa >= 2.0:
    if gpa <= 4.0:
        if gpa >= 2.0:
            graduated = True
        else:
            graduated = False
    else:
        graduated = False
else:
    graduated = False

if gpa >= 2.0:
    graduated = True
else:
    graduated = False

if graduated == True:
    if grade != "F":
        print("Student is eligible for graduation.")
    else:
        print("Graduation status inconsistency.")
else:
    if gpa < 2.0:
        print("Student is not eligible for graduation.")
    else:
        print("Graduation status inconsistency.")

print("GPA:", gpa)
print("Grade:", grade)
print("Graduated:", graduated)
