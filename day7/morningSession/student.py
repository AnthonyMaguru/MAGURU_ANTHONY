class Student:
#define attributes

    name= "Tony"
    Nationality = "Americano"
    
    def __init__(self, name, Nationality):
        self.name = name
        self.Nationality = Nationality
        
student1 = Student("TTT", "USA")        
print(student1.name)
print(student1.Nationality)