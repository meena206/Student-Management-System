import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "student.json"


# ---------------- JSON FUNCTIONS ---------------- #

def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- CRUD FUNCTIONS ---------------- #

def add_student():
    students = load_students()

    student = {
        "id": entry_id.get(),
        "name": entry_name.get(),
        "age": entry_age.get(),
        "course": entry_course.get(),
        "marks": entry_marks.get()
    }

    if not student["id"] or not student["name"]:
        messagebox.showerror("Error", "ID and Name are required")
        return

    students.append(student)
    save_students(students)

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()
    display_students()


def search_student():
    student_id = entry_id.get()
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            entry_course.delete(0, tk.END)
            entry_marks.delete(0, tk.END)

            entry_name.insert(0, student["name"])
            entry_age.insert(0, student["age"])
            entry_course.insert(0, student["course"])
            entry_marks.insert(0, student["marks"])

            return

    messagebox.showwarning("Not Found", "Student not found")


def update_student():
    student_id = entry_id.get()
    students = load_students()

    for student in students:
        if student["id"] == student_id:
            student["name"] = entry_name.get()
            student["age"] = entry_age.get()
            student["course"] = entry_course.get()
            student["marks"] = entry_marks.get()

            save_students(students)
            display_students()

            messagebox.showinfo("Success", "Student Updated")
            clear_fields()
            return

    messagebox.showwarning("Not Found", "Student not found")


def delete_student():
    student_id = entry_id.get()

    students = load_students()

    students = [s for s in students if s["id"] != student_id]

    save_students(students)

    display_students()
    clear_fields()

    messagebox.showinfo("Success", "Student Deleted")


# ---------------- UI FUNCTIONS ---------------- #

def display_students():
    for row in tree.get_children():
        tree.delete(row)

    students = load_students()

    students.sort(key=lambda student:float(student["marks"]),reverse=True)

    for student in students:
        tree.insert(
            "",
            tk.END,
            values=(
                student["id"],
                student["name"],
                student["age"],
                student["course"],
                student["marks"]
            )
        )


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_marks.delete(0, tk.END)


def select_record(event):
    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected, "values")

    clear_fields()

    entry_id.insert(0, values[0])
    entry_name.insert(0, values[1])
    entry_age.insert(0, values[2])
    entry_course.insert(0, values[3])
    entry_marks.insert(0, values[4])


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x600")
root.configure(bg="#f0f0f0")

title = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0"
)
title.pack(pady=10)

left_frame=tk.LabelFrame(root, text="Student Details",
                      font=("Arial", 12, "bold"),
                      padx=15,pady=15)
left_frame.pack(side=tk.LEFT,fill=tk.Y,padx=10,pady=10)

# Form Frame

tk.Label(left_frame, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(left_frame)
entry_id.grid(row=0, column=1)

tk.Label(left_frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(left_frame)
entry_name.grid(row=1, column=1)

tk.Label(left_frame, text="Age").grid(row=2, column=0, padx=5, pady=5)
entry_age = tk.Entry(left_frame)
entry_age.grid(row=2, column=1)

tk.Label(left_frame, text="Course").grid(row=3, column=0, padx=5, pady=5)
entry_course = tk.Entry(left_frame)
entry_course.grid(row=3, column=1)

tk.Label(left_frame, text="Marks").grid(row=4, column=0, padx=5, pady=5)
entry_marks = tk.Entry(left_frame)
entry_marks.grid(row=4, column=1)

# Buttons

tk.Button(left_frame, text="Add", width=12, command=add_student).grid(row=5, column=0, padx=5,pady=5)
tk.Button(left_frame, text="Search", width=12, command=search_student).grid(row=5, column=1, padx=5,pady=5)
tk.Button(left_frame, text="Update", width=12, command=update_student).grid(row=6, column=0, padx=5,pady=5)
tk.Button(left_frame, text="Delete", width=12, command=delete_student).grid(row=6, column=1, padx=5,pady=5)
tk.Button(left_frame, text="Clear", width=12, command=clear_fields).grid(row=7, column=0, padx=5,pady=5)

# Table
right_frame=tk.LabelFrame(root,text="Student Records",
                          font=("Arial",12,"bold"))
right_frame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,padx=10,pady=10)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview.Heading",
    font=("Arial", 12, "bold")
)

tree = ttk.Treeview(
    right_frame,
    columns=("ID", "Name", "Age", "Course", "Marks"),
    show="headings"
)

V_scroll=ttk.Scrollbar(right_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=V_scroll.set)

V_scroll.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack()

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")
tree.heading("Marks", text="Marks")

tree.column("ID", width=85)
tree.column("Name", width=200)
tree.column("Age", width=120)
tree.column("Course", width=120)
tree.column("Marks", width=120)

tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

tree.bind("<ButtonRelease-1>", select_record)

display_students()

root.mainloop()