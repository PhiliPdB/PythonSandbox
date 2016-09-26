from math import factorial

def nCr(n, r):
	return int(factorial(n) / (factorial(r) * factorial(n - r)))

total = 0
for n in range(1, 100 + 1):
	for r in range(n):
		if nCr(n, r) > int(1e6):
			total += 1

print(total)
