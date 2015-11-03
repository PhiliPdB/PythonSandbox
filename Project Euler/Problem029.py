sequence = []

for a in range(2, 100 + 1):
	for b in range(2, 100 + 1):
		sequence.append(a ** b)

sequence = sorted(set(sequence))

print(len(sequence))