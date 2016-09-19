import itertools

most_solutions = 0
p_most_solutions = 0

for p in range(3, 1000 + 1):
	solutions = []
	# Calculate the triangle
	a = 1
	while a < p / 2:
		b = 1
		while b < p / 2:
			c = (a**2 + b**2)**.5
			if c % 1 == 0 and a + b + c == p:
				solutions.append([a, b, int(c)])
			b += 1
		a += 1

	# Sort and remove double solutions
	for solution in solutions:
		solution.sort()
	solutions.sort()
	solutions = list(solution for solution,_ in itertools.groupby(solutions))

	if len(solutions) > most_solutions:
		most_solutions = len(solutions)
		p_most_solutions = p

print(p_most_solutions)
