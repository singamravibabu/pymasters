# # Define a class named 'Car'
class Car:
    # Constructor method to initialize the attributes
    def __init__(self, brand, model, year):
        self.brand = brand      # Attribute: car brand
        self.model = model      # Attribute: car model
        self.year = year        # Attribute: manufacturing year
        
    def display_details(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")
    
    def start_engine(self):
        print(f"{self.brand} {self.model} is starting...")
    
    def stop_engine(self):
        print(f"{self.brand} {self.model} is stoping...")


# Creat an object and call  methods
my_car = Car("Ford", "Mustang", 2021)
my_car.start_engine()
my_car.stop_engine()    