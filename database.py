
student_database = {}

def add_student():
    print("\nAdd Student:")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

   
    student_info = {
        'Name': name,
        'Age': age,
        'Grade': grade
    }

   
    student_database[name] = student_info
    print(f"{name} has been added to the database.")

def view_student():
    print("\nView Student:")
    name = input("Enter student name to view details: ")


    if name in student_database:
        student_info = student_database[name]
        print("\nStudent Details:")
        for key, value in student_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Student with name {name} not found in the database.")

def list_all_students():
    print("\nList of All Students:")
    for name, student_info in student_database.items():
        print(f"\nStudent Name: {name}")
        for key, value in student_info.items():
            print(f"{key}: {value}")

def update_student():
    print("\nUpdate Student Information:")
    name = input("Enter student name to update information: ")

  
    if name in student_database:
     
        student_info = student_database[name]

        
        age = int(input("Enter updated age (press Enter to keep current age): ") or student_info['Age'])
        grade = input("Enter updated grade (press Enter to keep current grade): ") or student_info['Grade']

        
        student_info['Age'] = age
        student_info['Grade'] = grade

        print(f"Information for {name} has been updated.")
    else:
        print(f"Student with name {name} not found in the database.")

def delete_student():
    print("\nDelete Student:")
    name = input("Enter student name to delete: ")

    
    if name in student_database:
       
        del student_database[name]
        print(f"{name} has been deleted from the database.")
    else:
        print(f"Student with name {name} not found in the database.")


while True:
    print("\nStudent Database Program")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_all_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
