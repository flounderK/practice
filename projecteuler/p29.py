product_set = set()
for a in range(2,101):
	for b in range(2, 101):
		product_set.add(a**b)

print(len(product_set))