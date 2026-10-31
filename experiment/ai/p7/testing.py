"""
prompt:
Create test cases for the student-ranking function. Verify descending GPA order, competition ranking for tied GPAs, empty input, a single student, and whether the original student records are modified. Provide expected ranked records and identify potential implementation limitations.

python
def rank_students(students):
    ordered = sorted(
        students,
        key=lambda student: student["gpa"],
        reverse=True
    )

    previous_gpa = None
    current_rank = 0

    for position, student in enumerate(ordered, start=1):
        if student["gpa"] != previous_gpa:
            current_rank = position
            previous_gpa = student["gpa"]
        student["rank"] = current_rank

    return ordered

chatgpt:
Test Case	Input	                                Expected Result
TC7.1	    GPA [3.4, 3.8, 3.0]	                    Sorted [3.8, 3.4, 3.0]
TC7.2	    GPA [3.8, 3.8, 3.4]	                    Ranked [1, 1, 3]
TC7.3	    GPA [2.0]	                            Single student, rank 1
TC7.4	    []	                                    []
TC7.5	    GPA [3.2, 3.2, 3.2]	                    All assigned rank 1
TC7.6	    Check input data after function call	Each dictionary includes a 'rank' key
TC7.7	    Data missing 'gpa' key	                KeyError
"""