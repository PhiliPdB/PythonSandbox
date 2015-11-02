import math

primes = [2, 3]

def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	else: 
		for x in range(3, int(math.sqrt(n)+1), 2):
			if n % x == 0:
				return False

	return True 

def longestPrimeQuadraticProduct(a_range, b_range):
	longest_length = 0
	longest_a = None
	longest_b = None

	for a in range(-a_range + 1, a_range):
		for b in range(2, b_range):
			count = 0
			n = 0
			while is_prime((n ** 2) + a * n + b):
				count += 1
				n += 1

			if count > longest_length:
				longest_length = count
				longest_a = a
				longest_b = b

	return longest_a * longest_b

print(longestPrimeQuadraticProduct(1000, 1000))