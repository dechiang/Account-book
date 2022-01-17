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

for product in products:
	print('the', product[0], 'has cost you', product[1])

# Write into file
with open('products.csv', 'w') as f:
	for x in products:
		f.write(x[0] + ',' + x[1] + '\n')

