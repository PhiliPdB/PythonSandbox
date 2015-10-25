def cycle_length(n):
	"""
	Computes the length of the recurring cycle in the decimal representation
	of the rational number 1/d if any, 0 otherwise
	"""

	remainder_list = []
	quotient_list_length = 0
	remainder = 1

	while remainder:
		remainder %= n
		if remainder in remainder_list:
			return quotient_list_length - remainder_list.index(remainder)
		remainder_list.append(remainder)
		remainder *= 10
		quotient_list_length += 1

	return 0

cycle_lengths = []
for i in range(2, 1000):
	cycle_lengths.append(cycle_length(i))

print(cycle_lengths.index(max(cycle_lengths)) + 2)
