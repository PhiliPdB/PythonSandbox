
begin = 3
step = 2 # Do not check even number
end = 2000000
prime_list = []

# function to factor a given positive integer n
def is_prime(n):
	# look for factors of 2 first
	if n % 2 == 0: return False
	# now look for odd factors
	p = 3
	while p < n**0.5+1:
		if n % p == 0: return False
		p += 2
	return True

while begin < end:
	if is_prime(begin): prime_list.append(begin)
	begin += step

print(sum(prime_list) + 2) # We skipped the first prime so add it to the results