circular_primes = [2]

# function to factor a given positive integer n
def is_prime(n):
	if n == 2: return True
	# look for factors of 2 first
	if n % 2 == 0: return False
	# now look for odd factors
	p = 3
	while p < n**0.5+1:
		if n % p == 0: return False
		p += 2
	return True

def get_rotations(n):
	number = list(str(n))
	rotations = []
	for i in range(len(number)):
		number.insert(0, number.pop())
		rotations.append(int(''.join([x for x in number])))

	return rotations

for i in range(3, int(1e6)):
	if is_prime(i):
		is_circular = True
		rotations = get_rotations(i)
		for j in rotations:
			if not is_prime(j):
				is_circular = False
				break
			else:
				is_circular = True

		if is_circular:
			circular_primes.append(i)

print(len(circular_primes))