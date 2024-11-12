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