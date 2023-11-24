'''
ENCAPSULATION
In this example the attribute '_made' and '_model' are encapsulated within the Car class,
and access to them is controlled through getter and setter methods.
This helps in hiding the internal details of the Car class. 
'''
class Car:
    def __init__(self, make, model):
        self._make = make  # Encapsulation: _make is a protected attribute
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, new_make):
        if isinstance(new_make, str):
            self._make = new_make

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        if isinstance(new_model, str):
            self._model = new_model

# Usage
my_car = Car("Toyota", "Camry")
print(my_car.get_make())  # Accessing make using a getter method
my_car.set_model("Corolla")  # Setting model using a setter method




'''
INHERITANCE
Here, the Animal class is the base class, and Dog and Cat are derived classes. 
The derived classes inherit the attributes and methods of the base class. 
This promotes code reuse and establishes a hierarchy.
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the method to be overridden in subclasses

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.make_sound())  # Output: Woof!
print(my_cat.make_sound())  # Output: Meow!




'''
POLYMORPHISM
Polymorphism allows objects of different types (here, Circle and Square) to be treated 
as objects of a common type (Shape). 
Both objects can be used interchangeably, providing flexibility and a consistent interface.
'''
class Shape:
    def area(self):
        pass  # Placeholder for the method to be overridden in subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Usage
circle = Circle(5)
square = Square(4)

print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16




'''
ABSTRACTION
In this example, the Shape class is an abstract base class with an abstract method area. 
Subclasses (Circle and Square) must provide their own implementation of the area method. 
This enforces abstraction, allowing us to work with the concept of a shape without specifying its details.
'''
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # Abstract method that must be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Usage
# Shape cannot be instantiated directly; it enforces abstraction
