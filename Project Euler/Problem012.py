
def factors(n):
	# Returns all the factors of a positive integer
	factors = []
	for i in range(1, int(n**0.5) + 1):
		if n % i == 0:
			factors.append(i)
			factors.append(n//i)

	# set() is used to remove double values
	# list() you have to make it a list again to sort
	# sorted() sorts the list
	return sorted(list(set(factors)))

def get_nth_triangle_number(n):
	return sum([int(i) for i in range(1, n + 1)])

number = 1
while True:
	if len(factors(get_nth_triangle_number(number))) > 500:
		break

	number += 1

print(get_nth_triangle_number(number))
