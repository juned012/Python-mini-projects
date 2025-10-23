# ----------------------------
#  Student Management System
# ----------------------------


students = [] 
courses = ("Python", "Java", "C++", "AI", "Data Science") 
unique_courses = set() 


def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").title()
    age = int(input("Enter age: "))
    course = input(f"Enter course ({', '.join(courses)}): ").title()

    student = {
        'name': name,
        'age': age,
        'course': course
    }

    students.append(student)
    unique_courses.add(course)
    print(f"Student {name} added successfully!")


def view_students():
    print("\n---- All Students ----")

    if not students:
        print("No student found.")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")


def delete_student():
# name = input("Enter name to delete: ").title()
# for s in students:
#     if s['name'] == name:
#         students.remove(s)
#         print(f"{name} deleted successfully!")
# print("Student not found.")

    print("\n-----Delete Student-----")

    if not students:
        print("No student to delete.")
        return

    for i , s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")

    delete_index = int(input(f"Enter the index number of the student to delete (1-{len(students)}): "))

    if 1 <= delete_index <= len(students):
        delete_student = students.pop(delete_index - 1)
        print(f"Student '{delete_student['name']}' deleted successfully!")
    else:
        print("Invalid student number. please try again.")   

def update_student():
    print("\n------Update Students-------")

    if not students:
        print("No student to update.")
        return
    
    for i , s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")

    update_index = int(input(f"Enter the index number of the student to update (1-{len(students)}): "))

    if  1 <= update_index <= len(students):
         student = students[update_index - 1]

         print(f"\nEditing Student: {student['name']}")
         new_name = input("Enter new name (leave blank to keep same): ").title()
         new_age = input("Enter new age (leave blank to keep same): ")     
         new_course = input("Enter new course (leave black to keep same): ").title()

    if new_name:
        student['name'] = new_name
    if new_age:
        try:
            student['age'] = int(new_age)
        except ValueError:
            print("Invalid age, Keeping old value.")

    if new_course:
        student['course'] = new_course
        unique_courses.add(new_course)

        print(f"Student {student['name']} details  updated successfully!")
    else:
        print("Invalid index number.")


def search_student():
    print("\n------Search Students--------")

    if not students:
        print("No student to search.")
        return
    
    search_name = input("Enter name to search: ").title()

    for s in students:
        if s['name'] == search_name:
            print(f"Found: {s['name']} | Age: {s['age']} | Course: {s['course']}")
            return
    print("Student not found.")


def show_summary():
    print("\n------Summary------")
    print(f"Total Students: {len(students)}")
    print(f"Unique Courses: {', '.join(unique_courses) if unique_courses else "None"}")


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Summary")
    print("7. Exit")

    choice = input("Enter your option (1-7): ")

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
        show_summary()
    elif choice == "7":
        print("Exiting Program. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")