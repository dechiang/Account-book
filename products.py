# products

products = []
while True:
	name = input('Please enter the name of the product: ')
	if name == 'q':
		break
	price = input('How much is this product?: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
	# Quicker way: p = [name, price]
	# Even quicker: products.append([name, price])
print(products)