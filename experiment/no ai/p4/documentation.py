"""
Results of manual documentation:

# Student Evaluation Report

This program creates and displays a report for one student.

'generate_report(name, scores)' calculates the GPA and returns a dictionary with the student's name, GPA, letter grade, and graduation status. 'display_report(report)' prints those values, with GPA displayed to two decimal places.

Example input:
python
report = generate_report("Alya", [80, 90])
display_report(report)

Expected report:
text
Student: Alya
GPA: 3.40
Grade: B
Graduated: True

The report function separates result calculation from output formatting. The code assumes that the name and score list are provided correctly and that the score list contains at least one numeric value.
"""