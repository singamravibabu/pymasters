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