#exe2
# Function to display student information
def display_student(name, age, course, student_number):
    print("\n===== STUDENT INFORMATION =====")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("Student Number:", student_number)


# Getting input from the user
name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")
student_number = input("Enter student number: ")

# Calling the function
display_student(name, age, course, student_number)

#exercise 3

print("\n===== AREA OF CIRCLE CALCULATOR =====")

import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of circle:", area_of_circle(radius))





#exercise 4
# Global
message = "I am a global variable"

def show_variables():
    message = "I am a local variable"
    
    print("Inside function:")
    print(message)

show_variables()

print("\nOutside function:")
print(message)