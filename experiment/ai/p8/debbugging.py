"""
prompt:
Debug the menu-driven Student Academic Evaluation System. The program crashes or behaves incorrectly
when the user enters an invalid menu choice. Add robust input handling, display an error message for unsupported choices,
and allow the menu to continue until the user selects Exit.

chatgpt:
Diagnosis: Converting menu input into an integer can trigger a ValueError.
The program also needs to handle selections that fall outside the provided options.
"""
#Corrected code:
def run_menu():
    while True:
        print("\n1. Calculate GPA")
        print("2. Calculate Grade")
        print("3. Check Graduation")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("GPA calculation selected.")
        elif choice == "2":
            print("Grade calculation selected.")
        elif choice == "3":
            print("Graduation check selected.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

run_menu()