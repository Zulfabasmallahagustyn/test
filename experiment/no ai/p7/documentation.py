"""
Results of manual documentation:

# Student Ranking

'rank_students(students)' sorts student dictionaries in descending order based on their GPA and adds a rank to each student.

Students with the same GPA receive the same rank. For example, GPAs of 3.8, 3.8, and 3.4 produce ranks 1, 1, and 3.

The function returns the sorted list. It expects each student dictionary to contain a numeric 'gpa' value.

Although the list itself is newly sorted, the dictionaries are not copied. Therefore, adding the 'rank' field also affects the original student dictionaries. Missing or invalid GPA values can cause errors or unexpected results.
"""