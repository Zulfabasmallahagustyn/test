"""
Prompt:
Reduce duplication and cognitive complexity.
"""

#chatgpt
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    scores: list

    def gpa(self):
        average_score = sum(self.scores) / len(self.scores)
        return round(average_score / 25, 2)