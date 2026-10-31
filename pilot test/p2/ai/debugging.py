"""
Prompt:
Analyze this code and identify all defects.

ChatGPT:
Diagnosis: The gpa() method triggers a ZeroDivisionError when the scores list is empty because it divides by len(self.scores), which is zero. The method should validate that the scores list is not empty before performing the calculation. It should also validate the score values to prevent invalid input.
"""

# Corrected code:
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    scores: list

    def gpa(self):
        if not self.scores:
            return 0.0

        if not all(isinstance(score, (int, float)) for score in self.scores):
            raise ValueError("All scores must be numeric.")

        if not all(0 <= score <= 100 for score in self.scores):
            raise ValueError("Scores must be between 0 and 100.")

        return round(
            sum(self.scores) / len(self.scores) / 25,
            2
        )


# Demonstration:
student1 = Student("Alice", [80, 90, 85])
student2 = Student("Bob", [])

print(f"{student1.name}'s GPA: {student1.gpa()}")
print(f"{student2.name}'s GPA: {student2.gpa()}")