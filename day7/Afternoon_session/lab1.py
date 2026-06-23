#Encapsulation
#student, name, reg_No, gender, Student No, age,
class Student:
    def __init__(self, name, age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number
        
student_1 = Student("John", 20, 250078645)

print(student_1.name)