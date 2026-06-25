#When a class inherits from more than one base class
#Diamond problem - occurs when two classes inherit from a common superclass and another class inherits from both
#If a method is over ridden in the immediate classes, ambiguity arises about which method the derived class should use
#Method Resolution Order - determines the order in which base classes are searched when executing a method. 
#Python uses C3 linearization to resolve this ambiguity.

class class1:
    def w(self):
        print("Method from class1")
        
class class2(class1):
    def w(self):
        print("Method from class2")

class class3(class1):
    def w(self):
        print("Method from class3")

class class4(class2, class3):
    pass

obj = class4()
obj.w()
print(class4.__mro__)  # Display the Method Resolution Order