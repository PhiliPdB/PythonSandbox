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

def is_permutation(m, n):
	p = list(permutations([x for x in str(m)]))
	final_p = []
	for x in p:
		final_p.append(int(''.join([y for y in x])))

	return n in final_p

primes = [i for i in range(1489, int(1e4), 2) if is_prime(i)]
result = 0

for i in range(0, len(primes)):
	for j in range(i + 1, len(primes)):
		k = primes[j] + (primes[j] - primes[i])
		if k < int(1e4) and k in primes:
			if is_permutation(primes[i], primes[j]) and is_permutation(primes[i], k):
				result = int(str(primes[i]) + str(primes[j]) + str(k))
				break

	if result > 0:
		break

print(result)
