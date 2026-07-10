import json 
import os 

FILE_NAME = "student.json"


# Load students from JSON file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file) 
    return [] 

# Save students to JSON file
def save_students(students): 
    with open(FILE_NAME, "w") as file: 
        json.dump(students, file, indent=4) 

# Add student
def add_student():
    students = load_students()

    def get_int(prompt):
            while True:
                try:
                    return int(input(prompt))
                except ValueError:
                    print("Please enter a valid integer.")

    def get_float(prompt):
            while True:
                try:
                    return float(input(prompt))
                except ValueError:
                    print("Please enter a valid number.")

    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Name: "),
        "age": get_int("Enter Age: "),
        "course": input("Enter Course: "),
        "marks": get_float("Enter Marks: ")
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View students
def view_students():
    students = load_students()
    students.sort(key=lambda student: float(student["marks"]), reverse=True)

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
        print("-" * 50)


# Search student
def search_student():
    students = load_students()
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found.")


# Update student
def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    def get_int(prompt):
            while True:
                try:
                    return int(input(prompt))
                except ValueError:
                    print("Please enter a valid integer.")

    def get_float(prompt):
            while True:
                try:
                    return float(input(prompt))
                except ValueError:
                    print("Please enter a valid number.")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("New Name: ")
            student["age"] = get_int(input("New Age: "))
            student["course"] = input("New Course: ")
            student["marks"] = get_float(input("New Marks: "))

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete student
def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    updated_students = [s for s in students if s["id"] != student_id]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    save_students(updated_students)

    print("Student deleted successfully!")


# Main menu
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__=="__main__":
    main()