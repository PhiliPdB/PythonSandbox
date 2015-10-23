def divisors(n):
	"""
	Returns all nontrivial divisors of an integer, but makes no guarantees on the order.
	"""
	# "1" is always a divisor (at least for our purposes)
	yield 1

	largest = int(n ** 0.5)

	# special-case square numbers to avoid yielding the same divisor twice
	if largest * largest == n:
		yield largest
	else:
		largest += 1

	# all other divisors
	for i in range(2, largest):
		if n % i == 0:
			yield i
			yield n / i

def is_abundant(n):
	if n < 12:
		return False
	return sum(divisors(n)) > n

abundants = [int(i) for i in range(1, 28123 + 1) if is_abundant(i)]

abundants_set = set(abundants) # set() data structure is faster when searching for an element in a list
def is_abundant_sum(n):
	for i in abundants:
		if i > n: # assume "abundants" is ordered
			return False
		if (n - i) in abundants_set:
			return True
	return False

sum_of_non_abundants = sum([i for i in range(1, 28123 + 1) if not is_abundant_sum(i)])

print(sum_of_non_abundants)