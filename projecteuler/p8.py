b=0
e=13
savede_set=""
largest_product=0
while e <= 1000:
	product = 1
	for c in list(number[b:e]):
		product = product * int(c)
	if product > largest_product:
		largest_product = product
		savede_set = number[b:e]
	e+=1
	b+=1
print("Largest product: {:d}".format(largest_product))
print("set of numbers: {:d}".format(savede_set))
