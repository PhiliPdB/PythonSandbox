def d(n):
	# Returns the sum of all the divisors of a positive integer
	divisors = []
	for i in range(1, int(n**0.5) + 1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n//i)

	# Remove itself
	divisors = [int(i) for i in divisors if i != n]

	# set() is used to remove double values
	# list() you have to make it a list again to sort
	# sorted() sorts the list
	return sum(sorted(list(set(divisors))))

def find_amicable_numbers():
	amicable_numbers = []
	for a in range(1, 10000):
		b = d(a)
		if a != b and d(b) == a:
			amicable_numbers.append(a)
	return amicable_numbers

print(sum(find_amicable_numbers()))
