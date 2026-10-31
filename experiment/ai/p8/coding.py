"""
prompt:
Build a menu-driven Python Student Academic Evaluation System.
Provide options to add a student, display all student results, rank students, and exit.
Ask users to enter student names and scores when adding students.
Implement calculate_gpa(), calculate_grade(), check_graduation(), and rank_students().
Keep student records in a list while the program runs. Ensure the menu repeats until the user chooses to exit.
"""

#chatgpt:

def calculate_gpa(scores):
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

students = []

while True:
    print("\n1. Add student")
    print("2. Display results")
    print("3. Rank students")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        scores = list(map(float, input("Enter scores: ").split()))
        gpa = calculate_gpa(scores)
        students.append({
            "name": name,
            "gpa": gpa,
            "grade": calculate_grade(gpa),
            "graduated": check_graduation(gpa)
        })
        print("Student added.")

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        for i, s in enumerate(rank_students(students), 1):
            print(f"{i}. {s['name']} - GPA {s['gpa']}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
