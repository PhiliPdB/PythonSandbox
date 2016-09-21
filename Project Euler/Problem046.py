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

for i in range(33, int(1e5), 2):
	if is_prime(i): continue

	j = 1
	found = False
	while 2 * (j ** 2) < i:
		if is_prime(i - 2 * (j ** 2)):
			found = True
			break
		
		j += 1

	if not found:
		print(i)
		break
