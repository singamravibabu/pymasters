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
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def display_info(self):
        status = "Available" if self.is_available else "Checked out"
        print(f"'{self.title}' by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You checked out '{book.title}'")
                return
        print("Book not available")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"'{book.title}' has been returned")
                return
        print("Book not found")
    
    def list_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_info()
            
# Using the Library Mangement System
library = Library()

book1 = Book("One Minute Management", "Ken Blanchard")
book2 = Book("21 Indespensible Laws of Leadership", "John C Maxwell")

library.add_book(book1)
library.add_book(book2)

library.list_books()
library.checkout_book("21 Indespensible Laws of Leadership")
library.list_books()
library.return_book("21 Indespensible Laws of Leadership")
library.list_books()
```

## Class Methods, Static Methods, and Instance Methods
In Python, methods can be classified into three types:
1. Instance Methods: Operate on instances of a class.
2. Class Methods: Operate on the class itself, not on instance.
3. Static Methods: Do not operate on instances or the class; they are utility functions related to the class.

### Instance Methods
These are the most common types of methods that operate on an instance of the class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")


# Using instance methods
dog1 = Dog("Buddy", 3)
dog1.bark()     # Output: Buddy says Woof!
```

### Class Methods
Class methods have access to the class itself (not instances). They are defined using the @classmethod decorator.

```python
class Animal:
    species = "Mannal"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def set_species(cls, species_name):
        cls.species = species_name

# Using class method
Animal.set_species("Reptile")
print(Animal.species)       # Output: Reptile
```

**Explanation:**
- `set_species` is a class method that changes the class attribute `species`.

### Static Methods
Static methods do not access class attributes or instance attributes. They are utility functions.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using static method
result = MathUtils.add(5, 10)
print(result)       # Output: 15
```

**Explanation:**
- `add()` is a static method because it doesn't operate on any instance or class attributes.

## Inheritance and Method Overriding
Inheritance allows to define a class that inherits all the methods and properties from another class. Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

### Multilevel Inheritance Example

```python
# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Child class
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

# Grandchild class
class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently...")

# Create an object of ElectricCar
tesla = ElectricCar()
tesla.start()   # Output: Electric car is starting silently...
```

## Super() Function
The `super()` function is used to call methods of a parent class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age) # calling the parent class constructor
        self.employee_id = employee_id
        
# Creating an Employee object
emp = Employee("Alice", 30, "E12345")
print(f"Name: {emp.name}, Age: {emp.age}, ID: {emp.employee_id}")
```

**Output:**
```yaml
Name: Alice, Age: 30, ID: E12345
```

**Explanation:**
- `super()` allows you to access methods of the parent class, which is helpful when you want to extend or modify the parent class behavior.

## Magic (Dunder) Methods
Magic methods, also known as dunder methods (double underscore), allow us to define how our objects behave with built-in Python operations like printing, adding, etc.

### Common Magic Methods
1. `__init__(self)`: Constructor method.
2. `__str__(self)`: Defines behavior for `print()`.
3. `__add__(self, other)`: Defines behavior for `+` operator.
4. `__len__(self)`: Defines behavior for `len()` function.

**Example:** Using `__str__()` and `__add__()`
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __add__(self, other):
        return self.pages + other.pages
    
# Creating two book objects
book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

# Using __str__() method
print(book1)    # Output: 'Python Basics' has 200 pages

# Using __add__() method
total_pages = book1 + book2
print(f"Total pages: {total_pages}")    # Output: Total pages: 500
```

## Decorators in OOP
Decorators are a way to add extra functionality to methods without modifying their code.

**Example: Using Property Decorator**
