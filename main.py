import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course"])


# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course])

    print("\n✅ Student Added Successfully!\n")


# View Students
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n========== STUDENT LIST ==========")

        next(reader)

        found = False
        for row in reader:
            found = True
            print(
                f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}"
            )

        if not found:
            print("No student records found.")

        print("==================================\n")


# Search Student
def search_student():
    search_id = input("Enter Student ID to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[0] == search_id:
                print("\nStudent Found")
                print(f"ID     : {row[0]}")
                print(f"Name   : {row[1]}")
                print(f"Age    : {row[2]}")
                print(f"Course : {row[3]}")
                return

    print("❌ Student Not Found\n")


# Delete Student
def delete_student():
    delete_id = input("Enter Student ID to Delete: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows.append(header)

        deleted = False

        for row in reader:
            if row[0] != delete_id:
                rows.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("\n✅ Student Deleted Successfully!\n")
    else:
        print("\n❌ Student Not Found!\n")


# Update Student
def update_student():
    update_id = input("Enter Student ID to Update: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows.append(header)

        updated = False

        for row in reader:
            if row[0] == update_id:
                print("\nEnter New Details")

                name = input("Name: ")
                age = input("Age: ")
                course = input("Course: ")

                rows.append([update_id, name, age, course])
                updated = True
            else:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("\n✅ Student Updated Successfully!\n")
    else:
        print("\n❌ Student Not Found!\n")


# Menu
def main():
    create_file()

    while True:

        print("========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

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
            print("\nThank You!\n")
            break

        else:
            print("\nInvalid Choice!\n")


if __name__ == "__main__":
    main()