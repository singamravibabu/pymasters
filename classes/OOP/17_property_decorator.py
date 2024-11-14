class Circle:
    def __init__(self, radius):
        self.__radius = radius
        
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

circle = Circle(10)     
print(circle.radius)    # Output: 10
c.radius = 15           # Modifies radius
print(circle.radius)    # Output: 15