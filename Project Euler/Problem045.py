def t(n):
	return int(n * (n + 1) / 2)

def is_pentagonal(n):
	return ((24 * n + 1) ** .5 + 1) / 6 % 1 == 0

def is_hexagonal(n):
	return ((8 * n + 1) ** .5 + 1) / 4 % 1 == 0

numbers = [t(n) for n in range(286, int(1e5))]
for i in numbers:
	if is_pentagonal(i) and is_hexagonal(i):
		print(i)
		break
