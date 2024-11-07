class Product:
	# constructor
	def __init__(self, name, price, discountPercent):
		self.name = name
		self.price = price
		self.discountPercent = discountPercent


p1 = Product("Vivo", 25000.0, 2)
print(p1.name)
print(p1.price)
print(p1.discountPercent)
