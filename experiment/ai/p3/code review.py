"""
prompt:
Review this object-oriented Python implementation of the Student Academic Evaluation System.
Assess class design, method responsibilities, consistency between stored GPA and calculated GPA, input handling,
and the correctness of the four required functions. Identify potential defects and recommend minimal changes
while retaining the Student class and the existing functional specification.

chatgpt:
Finding 1 - GPA Consistency: The 'self.gpa' attribute is calculated when an object is created.
If 'self.scores' is subsequently modified, the stored GPA value may no longer be accurate.

Finding 2 - Class Responsibilities: The 'calculate_grade()' and 'check_graduation()' methods consistently rely on the object's GPA,
under the assumption that the scores remain unchanged.

Finding 3 - Input Validation: Inputs for names and scores must be validated before a 'Student' object is created.

Finding 4 - Ranking: 'rank_students()' correctly uses the object's GPA as the sorting key.
"""