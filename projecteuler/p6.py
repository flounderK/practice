k = 0
m = 0
for i in range(1,101):
	k += i ** 2
	m += i
m = m ** 2
diff = m-k
print(" {:d} - {:d} = {:d}".format(m,k,diff))
