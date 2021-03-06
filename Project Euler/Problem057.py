from fractions import Fraction
import time

start = time.time()

limit = 1000
result = 0

# Keep track of all the expensions
expansions = [0 for x in range(limit + 1)]
expansions[0] = 1


for i in range(1, limit + 1):
	# Calculate next expension
	expansions[i] = 1 + Fraction(1, 1 + expansions[i-1])

	# When numerator has more numbers than denominator add 1 to the result
	if len(str(expansions[i].numerator)) > len(str(expansions[i].denominator)):
		result += 1


stop = time.time()

# Print result
print("Result: " + str(result))
# Print timing
print("Time taken: " + str((stop - start) * 1000) + "ms")

