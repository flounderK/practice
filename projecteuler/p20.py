total=1
for i in range(100,0, -1):
    total = total * i
digits = list(str(total))
sum_total = 0
for i in digits:
    sum_total = sum_total + int(i)
print(sum_total)
