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