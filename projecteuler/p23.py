import math

def proper_divisors(n):
	divs = list()
	for i in range(math.floor(n/2),0,-1):
		if not (n % i):
			divs.append(i)
	return divs
	
def d(a):
	total = 0
	for i in proper_divisors(a):
		total = total + i
	return total

def is_abundant(n):
	if d(n) > n:
		return True
	return False

#might not be needed
def is_in_set(n, s):
	for i in s:
		if i == n:
			return True
	return False
	
def get_sum_of_abundants(nums, sums):
	for r in nums:
		for c in nums:
			this_sum = r + c
			sums.add(this_sum)
	return sums
			
abundant_nums = set()
abundant_sums = set()
for i in range(1, 28124):
	if is_abundant(i):
		abundant_nums.add(i)

abundant_sums = get_sum_of_abundants(nums=abundant_nums, sums=abundant_sums)

total = 0	
for i in range(1,28124):
	if not is_in_set(i, abundant_sums):
		total = total + i


print("Sum of all numbers that cannot be written as the sum of two abundant numbers: {:d}".format(total))
