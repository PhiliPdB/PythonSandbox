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

result = 1
primes = [i for i in range(2, 200 + 1) if is_prime(i)]

i = 0
while result * primes[i] < int(1e6):
	result *= primes[i]
	i += 1

print(result)
