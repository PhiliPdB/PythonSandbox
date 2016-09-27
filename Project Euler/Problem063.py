from math import ceil

result = 0
n = 1
lower = 0

while lower < 10:
	lower = int(ceil(10 ** ((n - 1) / n)))
	result += 10 - lower
	n += 1

print(result)
