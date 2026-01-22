students = []

def register_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    course = input("Enter course code: ")
    students.append({
        "name": name,
        "matric": matric,
        "course": course
    })
    print("Student registered successfully!")

def view_registered_students():
    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            print(
                "Name:", student["name"],
                "| Matric:", student["matric"],
                "| Course:", student["course"]
            )

while True:
    print("\nStudent Course Registration System")
    print("1. Register Student")
    print("2. View Registered Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        view_registered_students()
    elif choice == "3":
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")
