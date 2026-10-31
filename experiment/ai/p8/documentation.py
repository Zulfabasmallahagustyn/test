"""
prompt:
Create user documentation for this menu-driven Python academic evaluation program. Explain the menu options, the responsibilities of each function, how the program handles invalid menu selections, and which actions are currently placeholders. Do not claim that unimplemented actions perform full evaluations.

python
def display_menu():
    print("1. Calculate GPA")
    print("2. Calculate Grade")
    print("3. Check Graduation")
    print("4. Exit")

def process_choice(choice):
    actions = {
        "1": "GPA calculation selected",
        "2": "Grade calculation selected",
        "3": "Graduation check selected"
    }

    if choice == "4":
        return "Exit"

    return actions.get(choice, "Invalid choice")

chatgpt:
# Student Academic Evaluation System — Menu-Driven Version

## Overview
This program provides a simple text menu for selecting academic evaluation operations.

## Function: 'display_menu()'
Prints four options:
1. Calculate GPA
2. Calculate Grade
3. Check Graduation
4. Exit

This function displays the menu only; it does not process user input.

## Function: 'process_choice(choice)'
Receives a menu selection as a string and returns a status message.

| Input | Return value |
|---|---|
| '"1"' | 'GPA calculation selected' |
| '"2"' | 'Grade calculation selected' |
| '"3"' | 'Graduation check selected' |
| '"4"' | 'Exit' |
| Other values | 'Invalid choice' |

## Usage Example
python
display_menu()
print(process_choice("2"))

Example output:

text
1. Calculate GPA
2. Calculate Grade
3. Check Graduation
4. Exit
Grade calculation selected

## Current Limitations
Options 1–3 return selection messages only. They do not yet calculate GPA, assign grades, or check graduation eligibility. A complete application would need to connect these options to the relevant evaluation functions. A loop for repeatedly displaying the menu is also not included in this code.
"""