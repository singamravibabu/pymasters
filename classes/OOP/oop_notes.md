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