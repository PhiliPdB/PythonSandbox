from math import gcd

result = 0
limit = int(1e6)

phi = list(range(0, limit + 1))

for i in range(2, limit + 1):
	if phi[i] == i:
		for j in range(i, limit + 1, i):
			phi[j] = phi[j] / i * (i - 1)

	result = result + phi[i]


print(int(result))
