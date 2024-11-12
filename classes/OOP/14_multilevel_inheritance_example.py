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