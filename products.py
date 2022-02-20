# account book application

import os

# read past saved csv file
def read_file(filename):
	products = []
	if os.path.isfile(filename): # Check if the file is the folder
		print('The file has been found !!!')
		# read past saved csv file
		with open(filename, 'r') as f:
			for line in f:
				if 'product, price' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
		print(products)
	else:
		print('The file cannot be found...')
	return products

# input new products & price you buy
def user_input(products):
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
	return products

# List out all purchase history
def print_products(products):
	for product in products:
		print('the', product[0], 'has cost you', str(product[1]))

# Write into file
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('product, price\n')
		for x in products:
			f.write(x[0] + ',' + str(x[1]) + '\n')

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)
