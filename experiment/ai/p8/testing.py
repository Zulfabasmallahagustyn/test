"""
prompt:
Prepare functional tests for the menu-driven academic evaluation program. Test every valid option, invalid choices, empty input, and the behavior of the exit option. Verify the actual return messages and identify any menu actions that are not implemented.

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
Test Case   Input               Expected Output
TC8.1       "1"                 "GPA calculation selected"
TC8.2       "2"                 "Grade calculation selected"
TC8.3       "3"                 "Graduation check selected"
TC8.4       "4"                 "Exit"
TC8.5       "5"                 "Invalid option"
TC8.6       ""                  "Invalid option"
TC8.7       "abc"               "Invalid option"
TC8.8       Call display_menu() Four options are displayed
"""