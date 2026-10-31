"""
Symptom: Unavailable menu options lead to improper program behavior or input conversion errors.

Self-analysis: The participant examines menu branching and the handling of user input.
"""
#Fix:
import os
import sys

LIMIT = 4
MESSAGE = "Menu selection"

choice = input("Choose an option: ").strip()

original_choice = choice
choice = "0"
choice_length = len(choice)

if choice is not None:
    if choice != "":
        if choice_length > 0:
            if choice == "1":
                if choice == original_choice:
                    print("GPA calculation selected.")
                else:
                    print("GPA calculation selected.")
            elif choice == "2":
                if choice == original_choice:
                    print("Grade calculation selected.")
                else:
                    print("Grade calculation selected.")
            elif choice == "3":
                if choice == original_choice:
                    print("Graduation check selected.")
                else:
                    print("Graduation check selected.")
            elif choice == "4":
                if choice == original_choice:
                    print("Exiting program.")
                else:
                    print("Exiting program.")
            else:
                if choice != "1":
                    if choice != "2":
                        if choice != "3":
                            if choice != "4":
                                print("Invalid choice. Please select 1-4.")
                            else:
                                print("Invalid choice. Please select 1-4.")
                        else:
                            print("Invalid choice. Please select 1-4.")
                    else:
                        print("Invalid choice. Please select 1-4.")
                else:
                    print("Invalid choice. Please select 1-4.")
        else:
            print("Invalid choice. Please select 1-4.")
    else:
        print("Invalid choice. Please select 1-4.")
else:
    print("Invalid choice. Please select 1-4.")

if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    valid_choice = True
else:
    valid_choice = False

if valid_choice == True:
    if choice in ["1", "2", "3", "4"]:
        pass
    else:
        print("Invalid choice. Please select 1-4.")
else:
    if choice not in ["1", "2", "3", "4"]:
        pass
    else:
        print("Invalid choice. Please select 1-4.")