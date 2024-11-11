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