"""
prompt:
Conduct a code review of this menu-driven Python Student Academic Evaluation System.
Inspect menu control flow, invalid menu choices, student record creation, repeated operations,
empty-record handling, and input validation. Verify the four required functions and
ensure that all displayed results follow the same GPA, grade, graduation, and ranking rules.
Recommend specific corrections without removing the interactive menu.

chatgpt:
Finding 1 - Menu flow: The looping mechanism and exit options function as intended; unrecognized input triggers an error message.

Finding 2 - Empty data: The display function must handle scenarios where no students have been added yet.

Finding 3 - Input consistency: Grade data must be validated before being saved.

Finding 4 - Code maintenance: The logic for displaying rankings should be encapsulated within a 'rank_students()' function
to avoid code duplication across different parts of the program.
"""