from math import gcd

total = 0

for m in range(2, int((1e8 / 2) ** .5)):
	for n in range(1, m):
		if (m - n) % 2 == 1 and gcd(n, m) == 1:
			a = 2 * m * n
			b = m ** 2 - n ** 2
			c = m ** 2 + n ** 2
			if c % (b - a) == 0:
				total += int(1e8 / (a + b + c))

print(total)
