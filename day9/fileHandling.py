# Module: FILE HANDLING, DATA PROCESSING, EXCEPTION HANDLING, LOGGING AND DEBUGGING

"""
Outcomes
- Read data from a file
-Append data to file
- Process CSV file
-Read and Write JSON file
"""
# FILE HANDLING
#COMMON FILE TYPES

"""
- Text file (.txt)
- CSV file (.csv)
- JSON file (.json)
- Excel file (.xlsx)
"""
# Opening a file

# Syntax
# file = open(filename, mode)

"""
MODE           MEANING
r                 Read
w                 Write
a                 Append
x                 Create new file
rb                Read binary
wb                Write binary
"""

#EXAMPLE1 read a student.txt file
# file = open("student.txt", "r")

# content = file.read()

#print(content)

#file.close()

# Recommended method
# 'with' automatically closes the file after the block of code is executed
# with open('student.txt','r') as file:
#    data = file.read()

# print(data)

#READING LINE BY LINE
# with open('student.txt', 'r') as file:
    
#     # Read one line at a time
#     for line in file:
#         print(line.strip())

# Lab Exercise 1: Write a file with the conten 'I love Python Programming' first line,
# ' I am becoming a data Scientist' , second line. , save your file as report.txt

# Lab Exercise 1

# Open the file in write mode
with open("report.txt", "a") as file:
    file.write("I love Python Programming\n")
    file.write("I am becoming a Data Scientist")
    file.write("\nEvery Data Scientist Must learn Python\n")

print("File 'report.txt' has been created successfully.")


# Appending a file , use the sample report.txt append
# append ' Every Data Scientist Must learn python'

# Real World Example
# Attendance System
# Live Demo

name = input('Enter Student: ')
with open('attendance.txt', 'a') as file:
     # Save
    file.write(name + '\n')
print('Attendance Saved Successfully')

# Work with a CSV File
# What is CSV? Comma Seprated Values

# Reading a CSV File

import csv

# Open CSV File
with open('student.csv', 'r') as file:
    reader = csv.reader(file)

    # loops through each row 
    for row in reader:
        print(row)
        
# Lab activity add your ['RegistrationNo', 'Name', 'Gender', 'Age', 'Course', 'Score'] 
# to the students.csv, using a dictionary csv writer

import csv

# Student data stored in a dictionary
student = {
    "RegistrationNo": "2025/BSCS/001",
    "Name": "Anthony Maguru",
    "Gender": "Male",
    "Age": 22,
    "Course": "Bachelor of Computer Science",
    "Score": 85
}

# Column names
fields = ["RegistrationNo", "Name", "Gender", "Age", "Course", "Score"]

# Open the CSV file in append mode
with open("student.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)

    # writer.writeheader()

    # Write the student's record
    writer.writerow(student)

print("Student record added successfully.")

# JSON PROCSSING 

# What is JSON (), JavaScript Object Notation

"""
JSON Format
{
    "name": "TONY"
    "Age":  "26"
    "Course": "Python"
}

"""

# Writing a JSON file
import json

student = {
    "name": "TONY",
    "Age":  "26",
    "Course": "Python"
}

with open('student.json', 'w') as file:
    json.dump(student,file,indent=4)



