"""
Prompt:
Generate project README.

chatgpt:
python
# Student Academic Evaluation System

A simple Python program for storing student information and calculating Grade Point Average (GPA).

## Features
- Student Information Management
- GPA Calculation
- Score Averaging
- GPA Rounding to Two Decimal Places

## Requirements
- Python 3.7 or later

## Usage
Run the Python program:

    python main.py

## Example
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    scores: list

    def gpa(self):
        return round(
            sum(self.scores) / len(self.scores) / 25,
            2
        )

student = Student("Alice", [80, 90, 85])
print(student.gpa())
"""