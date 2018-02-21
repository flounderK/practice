from re import compile, sub
name_list = list()
quote_re = compile('"')
with open("p022_names.txt", "r") as f: 
    for i in sub(quote_re, "", f.read()).split(","):
		name_list.append(i)

name_list.sort()
		
		
def sum_value(name):
	total = 0
	for i in name:
		total = total + (ord(i) - 64)
	return total

total = 0
for name in name_list:
	val = sum_value(name)
	position = name_list.index(name) + 1
	total = total + (val * position)
print(total)
