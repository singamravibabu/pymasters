# OBJECT-ORIENTED PROGRAMMING

Python:
- General-purpose
- Interpreted
- Interactive
- Object-oriented

## Overview of Python OOPS
- We solve problems by creating objects
- Objects:
people
businesses
employees
students
physical objects - book, pen, chair, phone, laptop
intangible objects - bank account, insurance

### Objects that we create
- The objects that we create are called "software objects"
- These objects contain "data" and "functions" that can be performed on them

### Encapsulation
- Encapsulation is the concept of restricting access to certain attributes and methods to protect the data
- Attributes prefixed with __ are considered private

### Inheritance
- Inheritance allows to create a new class (child class) from an existing class (parent class).

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class
class Dog(Animal):
    def speak(self):    # method overriding
        print(f"{self.name} barks")

# Create objects
animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy")
dog.speak()
```

### Polymorphism
> Polymorphism allows methods to have the same name but behave differently based on the object calling them.

**Example**:

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly but can swim")

def make_it_fly(bird):
    bird.fly()

# Create objects
sparrow = Bird()
penguin = Penguin()

make_it_fly(sparrow)    # Output: Bird is flying
make_it_fly(penguin)    # Output: Penguin can't fly but can swim
```

### Abstraction
> Abstraction focuses on hiding implementation details and exposing only the functionality.

**Example: Using Abstract Base Class**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")
        
# Create objects
car = Car()
car.start()

bike = Bike()
bike.start()
```

### Simple Library Management System using OOP concepts
