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

primes = [i for i in range(1, int(1e6)) if is_prime(i)]
prime_sum = [0]
for i in range(len(primes)):
	prime_sum.append(prime_sum[i] + primes[i])

result = 0
number_of_primes = 0
for i in range(number_of_primes, len(prime_sum)):
	for j in range(i - (number_of_primes + 1), 0 , -1):
		if (prime_sum[i] - prime_sum[j] > int(1e6)): break

		if prime_sum[i] - prime_sum[j] in primes:
			number_of_primes = i - j
			result = prime_sum[i] - prime_sum[j]

print(result)
