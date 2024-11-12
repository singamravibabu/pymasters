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