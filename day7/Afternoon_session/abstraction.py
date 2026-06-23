#what is abstraction
#Abstraction is the process of hiding implementation
#details and showing only the essential
#features of an object.

#lab activity 3
"""from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


car = Car()
car.start_engine()
car.stop_engine()"""

#exercise 2
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

rect = Rectangle(5, 10)
circ = Circle(7)

print(f"Rectangle - Area: {rect.area():.2f}, Perimeter: {rect.perimeter()}")
print(f"Circle    - Area: {circ.area():.2f}, Perimeter: {circ.perimeter():.2f}")