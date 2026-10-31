"""
Prompt:
Create a clean Python Student Academic Evaluation System with GPA calculation,
grade determination, graduation checking and ranking.
"""

# ChatGPT Output:
from dataclasses import dataclass
@dataclass
class Student:
    name:str
    scores:list
    def gpa(self):
        return round(
            sum(self.scores)/len(self.scores)/25,
            2
        )
