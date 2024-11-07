class Product:
	name = ""		# attr1: name
	price = 0		# attr2: price
	discountPercent = 0.0	# attr3: discountPercent

p1 = Product()
print("## DEFAULT VALUES")
print(p1.name)
print(p1.price)
print(p1.discountPercent)

p1.name = "Samsung A22"
p1.price = 22000.0
p1.discountPercent = 8

print()
print("## UPDATED VALUES")
print(p1.name)
print(p1.price)
print(p1.discountPercent)