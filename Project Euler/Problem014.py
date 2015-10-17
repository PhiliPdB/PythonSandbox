def sequence(n):
	sequence = [n]
	while n != 1:
		if n % 2 == 0:
			n /= 2	
		else:
			n = 3 * n + 1
		sequence.append(n)
	return sequence

def find_longest_sequence():
	current_longest = 0
	number = 0
	for i in range(2, 1000000):
		if len(sequence(i)) > current_longest:
			current_longest = len(sequence(i))
			number = i
	return [number, current_longest]

print(find_longest_sequence())
