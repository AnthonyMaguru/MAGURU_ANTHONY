class Employee:
    def __init__(self):
        self.name = "Tony"
#       self.__salary = 70000000  # Private attribute

emp = Employee()

print(emp.name)  # Accessible
#print(emp.__salary)

#exercise 1        
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def display_info(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: ${self.__price}")

car1 = Car("Toyota", "Corolla", 25000)
car1.display_info()