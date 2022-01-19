# account book application

# read past saved csv file
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if 'product, price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# input new products & price you buy
while True:
	name = input('Please enter the name of the product: ')
	if name == 'q':
		break
	price = input('How much is this product?: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
	# Quicker way: p = [name, price]
	# Even quicker: products.append([name, price])
print(products)

# List out all purchase history
for product in products:
	print('the', product[0], 'has cost you', str(product[1]))

# Write into file
with open('products.csv', 'w') as f:
	f.write('product, price\n')
	for x in products:
		f.write(x[0] + ',' + str(x[1]) + '\n')

