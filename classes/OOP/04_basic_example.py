# # Define a class named 'Car'
class Car:
    # Constructor method to initialize the attributes
    def __init__(self, brand, model, year):
        self.brand = brand      # Attribute: car brand
        self.model = model      # Attribute: car model
        self.year = year        # Attribute: manufacturing year
        
    def display_details(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
        
        
# Create an object of the Car class
my_car = Car("Tesla", "Model S", 2022)

# Call the display_details method
print(my_car.display_details())

# Accessing attributes
print(my_car.brand)
print(my_car.year)

# Modifying attributes
my_car.year = 2023
print(my_car.year)