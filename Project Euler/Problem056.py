def digit_sum(n):
	return sum([int(x) for x in str(n)])

max_sum = 0
for a in range(100):
	for b in range(100):
		if digit_sum(a ** b) > max_sum:
			max_sum = digit_sum(a ** b)

print(max_sum)
