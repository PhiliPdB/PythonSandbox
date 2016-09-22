def prime_factors(n):
	# Returns all the prime factors of a positive integer
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(round(d))
			n /= d
		d = d + 1

		if d*d > n:
			if n > 1: factors.append(round(n))
			break

	return factors

sequence = []
for i in range(int(1e3), int(1e6)):
	print(i)

	if len(set(prime_factors(i))) is 4 and (not sequence or sequence[-1] == i - 1):
		sequence.append(i)
	else:
		sequence = []

	if len(sequence) is 4:
		print(sequence[0])
		break
