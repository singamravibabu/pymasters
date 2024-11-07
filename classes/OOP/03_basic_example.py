class Product:
	# constructor
	def __init__(self, name, price, discountPercent):
		self.name = name
		self.price = price
		self.discountPercent = discountPercent

	def discountAmount(self):
		return self.price * self.discountPercent / 100

	def discountPrice(self):
		return self.price - self.discountAmount()

p1 = Product("Vivo", 25000.0, 2)
print("Name", p1.name)
print("Price:", p1.price)
print("Discount percent:", p1.discountPercent)
print("Discount Amount:", p1.discountAmount())
print("Discount Price:", p1.discountPrice())

print()
p2 = Product("Oppo", 30000.0, 3)
print("Name", p2.name)
print("Price:", p2.price)
print("Discount percent:", p2.discountPercent)
print("Discount Amount:", p2.discountAmount())
print("Discount Price:", p2.discountPrice())