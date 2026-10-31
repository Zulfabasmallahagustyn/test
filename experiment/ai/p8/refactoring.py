"""
prompt:
Refactor the menu-driven Student Academic Evaluation System. Reduce deeply nested conditional statements,
separate menu display from menu processing, and keep the program running until the user selects Exit.
Preserve all available menu options and provide an example of handling an invalid choice.
"""

#chatgpt:
def display_menu():
    print("\n1. Calculate GPA")
    print("2. Calculate Grade")
    print("3. Check Graduation")
    print("4. Exit")


def process_choice(choice):
    actions = {
        "1": "GPA calculation selected.",
        "2": "Grade calculation selected.",
        "3": "Graduation check selected."
    }

    if choice == "4":
        return False

    print(actions.get(choice, "Invalid choice."))
    return True


def run_menu():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if not process_choice(choice):
            print("Exiting program.")
            break


def calculate_gpa(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores) / 25, 2)


def calculate_grade(gpa):
    if gpa >= 3.5:
        return "A"
    if gpa >= 3.0:
        return "B"
    if gpa >= 2.0:
        return "C"
    return "D"


def check_graduation(gpa):
    return gpa >= 2.0


def rank_students(students):
    return sorted(students, key=lambda s: s["gpa"], reverse=True)