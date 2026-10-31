"""
prompt:
Perform a code review of this Python academic evaluation program, focusing on dynamically entered subject counts,
score validation, edge cases, and ranking correctness. Verify that all four required functions comply with the specified GPA formula,
letter-grade thresholds, and graduation threshold. Identify concrete bugs and suggest targeted corrections.
Do not introduce weighted GPA or change the functional requirements.

chatgpt:
Finding 1 - Input for the number of students: A function that exclusively accepts positive numbers must be used consistently.
Any input of zero or a negative number must be rejected.

Finding 2 - Course grades: The validation of the grade range (0-100) is appropriate,
provided that all grades are processed through this validation function.
Calling the calculation function directly could result in the processing of invalid data.

Finding 3 - Number of courses: The program must reject an input of zero for the number of courses to prevent division by zero.

Finding 4 - Ranking: Sorting GPAs in descending order is appropriate;
however, the method for handling students with identical GPAs needs to be defined.
"""