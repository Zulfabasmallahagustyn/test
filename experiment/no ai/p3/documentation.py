"""
Results of manual documentation:

# Student Class

The 'Student' class stores a student's name and subject scores. It also provides methods to calculate GPA, determine a letter grade, and check graduation eligibility.

The constructor receives 'name' and 'scores'. GPA starts as 'None' and is calculated when 'calculate_gpa()' is called. Once calculated, the value is stored in the object. 'calculate_grade()' uses that GPA to assign a grade, while 'check_graduation()' checks whether GPA is at least 2.0.

Example:
python
student = Student("Alya", [80, 90])
student.calculate_gpa()       # 3.4
student.calculate_grade()     # B
student.check_graduation()    # True

The score list must not be empty. If scores change after the GPA has been calculated, the stored GPA may become outdated because the current code does not refresh the cached value automatically.
"""