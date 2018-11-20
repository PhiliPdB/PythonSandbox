from fractions import Fraction
from math import ceil

def get_expansion(n):
	if n == 1:
		return 2

	if (n - 1) % 3 == 2:
		result = 2 * ceil((n - 1) / 3)
	else:
		result = 1

	for i in list(range(2, n))[::-1]:
		if (i - 1) % 3 == 2:
			result = (2 * ceil((i - 1) / 3)) + Fraction(1, result)
		else:
			result = 1 + Fraction(1, result)

	return 2 + Fraction(1, result)


expansion = get_expansion(100)
num = expansion.numerator

print(sum([int(x) for x in str(num)]))

