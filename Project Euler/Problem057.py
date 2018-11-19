from fractions import Fraction

limit = 1000
result = 0

# Keep track of all the expensions
expansions = [0 for x in range(limit + 1)]
expansions[0] = 1


for i in range(1, limit + 1):
	# Calculate next expension
	expansions[i] = 1 + Fraction(1, 2 + (expansions[i-1] - 1))

	# When numerator has more numbers than denominator add 1 to the result
	if len(str(expansions[i].numerator)) > len(str(expansions[i].denominator)):
		result = result + 1


print(result)
