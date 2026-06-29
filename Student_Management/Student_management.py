#Student_managemt system source code block

import csv
import json
import logging
import os

# Logging Configuration

logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


CSV_FILE = "students.csv"
JSON_FILE = "students.json"

class StudentNotFoundError(Exception):
    #for when a student is not found in the records
    pass

# Create files if missing

def initialize_files():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RegistrationNo", "Name", "Gender", "Age", "Score"])

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as file:
            json.dump({}, file, indent=4)


# CSV Functions

def load_students():
    students = []

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def save_students(students):

    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = ["RegistrationNo", "Name", "Gender", "Age", "Score"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


# JSON Functions

def load_details():

    with open(JSON_FILE, "r") as file:
        return json.load(file)


def save_details(details):

    with open(JSON_FILE, "w") as file:
        json.dump(details, file, indent=4)


# For Adding Student

def add_student():

    try:

        reg = input("Registration Number: ").strip()

        students = load_students()

        for student in students:
            if student["RegistrationNo"] == reg:
                print("Student already exists.")
                return

        name = input("Name: ")

        gender = input("Gender: ")

        age = input("Age: ")

        score = input("Score: ")

        address = input("Address: ")

        contact = input("Contact: ")

        program = input("Program: ")

        students.append({
            "RegistrationNo": reg,
            "Name": name,
            "Gender": gender,
            "Age": age,
            "Score": score
        })

        save_students(students)

        details = load_details()

        details[reg] = {
            "Address": address,
            "Contact": contact,
            "Program": program
        }

        save_details(details)

        print("Student added successfully.")

        logging.info(f"Added student {reg}")

    except Exception as e:

        logging.error(e)

        print("Error:", e)

    finally:
        print()


# Viewing Students

def view_students():

    try:

        students = load_students()

        details = load_details()

        if not students:
            print("No student records.")

        for student in students:

            reg = student["RegistrationNo"]

            print("--------------------------------")

            print("Registration:", reg)

            print("Name:", student["Name"])

            print("Gender:", student["Gender"])

            print("Age:", student["Age"])

            print("Score:", student["Score"])

            if reg in details:

                print("Address:", details[reg]["Address"])

                print("Contact:", details[reg]["Contact"])

                print("Program:", details[reg]["Program"])

        logging.info("Viewed all students")

    except Exception as e:

        logging.error(e)

        print(e)


# Searching Student

def search_student():

    try:

        reg = input("Enter Registration Number: ")

        students = load_students()

        details = load_details()

        for student in students:

            if student["RegistrationNo"] == reg:

                print(student)

                if reg in details:
                    print(details[reg])

                logging.info(f"Searched {reg}")

                return

        raise StudentNotFoundError("Student not found.")

    except StudentNotFoundError as e:

        print(e)

        logging.error(e)


# Update Student

def update_student():

    try:

        reg = input("Registration Number: ")

        students = load_students()

        details = load_details()

        found = False

        for student in students:

            if student["RegistrationNo"] == reg:

                student["Name"] = input("New Name: ")

                student["Gender"] = input("New Gender: ")

                student["Age"] = input("New Age: ")

                student["Score"] = input("New Score: ")

                found = True

        if not found:
            raise StudentNotFoundError("Student not found.")

        details[reg] = {
            "Address": input("Address: "),
            "Contact": input("Contact: "),
            "Program": input("Program: ")
        }

        save_students(students)

        save_details(details)

        print("Student updated.")

        logging.info(f"Updated {reg}")

    except StudentNotFoundError as e:

        logging.error(e)

        print(e)


# Deletion of Students

def delete_student():

    try:

        reg = input("Registration Number: ")

        students = load_students()

        details = load_details()

        new_students = []

        found = False

        for student in students:

            if student["RegistrationNo"] == reg:
                found = True
            else:
                new_students.append(student)

        if not found:
            raise StudentNotFoundError("Student not found.")

        save_students(new_students)

        if reg in details:
            del details[reg]

        save_details(details)

        print("Student deleted.")

        logging.info(f"Deleted {reg}")

    except StudentNotFoundError as e:

        logging.error(e)

        print(e)


# Main Menu

def menu():

    initialize_files()

    while True:

        print("\n====== STUDENT RECORD SYSTEM ======")

        print("1. Add Student")

        print("2. View Students")

        print("3. Search Student")

        print("4. Update Student")

        print("5. Delete Student")

        print("6. Exit")

        choice = input("Choose option: ")

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

            logging.info("Program closed.")

            print("Goodbye.")

            break

        else:

            print("Invalid option.")

            logging.warning("Invalid menu choice")


if __name__ == "__main__":
    menu()