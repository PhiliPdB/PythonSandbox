def p(n):
	return int(n * (3 * n - 1) / 2)

def is_pentagonal(n):
	return ((24 * n + 1) ** .5 + 1) / 6 % 1 == 0

k = 0
found = False
while not found:
	k += 1
	n = p(k)
	for j in range(k - 1, 0, -1):
		m = p(j)
		if is_pentagonal(n - m) and is_pentagonal(n + m):
			print(n - m)
			found = True
			break
