truncatable_primes = []

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

def left_to_right(n):
	numbers = [n]
	for x in range(1, len(str(n))):
		number = str(numbers[x - 1])[1:].lstrip("0")
		if number is not '':
			numbers.append(int(number))
		else:
			numbers.append(1)
	return numbers
 
def right_to_left(n):
	numbers = [n]
	for x in range(1, len(str(n))):
		numbers.append(int(str(numbers[x - 1])[:-1]))
	return numbers

for i in range(10, int(1e6)):
	if is_prime(i):
		variations = left_to_right(i)[1:]
		variations.extend(right_to_left(i)[1:])
		
		truncatable_prime = True
		for j in variations:
			if not is_prime(j):
				truncatable_prime = False
				break

		if truncatable_prime:
			truncatable_primes.append(i)

print(sum(truncatable_primes))
