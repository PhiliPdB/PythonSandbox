from itertools import permutations

def is_prime(n):
	if n == 1: return False
	if n == 2: return True
	# look for factors of 2 first
	if n % 2 == 0: return False
	# now look for odd factors
	p = 3
	while p < n**0.5+1:
		if n % p == 0: return False
		p += 2
	return True

largest = 0

for n in range(9, 0, -1):
	for i in list(permutations(range(1, n + 1), n)):
		number = int(''.join([str(x) for x in i]))
		if is_prime(number) and number > largest:
			largest = number

	if largest > 0:
		break

print(largest)
