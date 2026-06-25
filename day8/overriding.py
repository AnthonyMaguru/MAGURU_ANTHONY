class Animal:
    def sound(self):
        print("animal speaks")
        
#child speaks
class Dog(Animal):
    def sound(self):
        print("dog barks")
        
s = Dog()
s.sound()  # Output: dog barks