largest = 0

for i in range(2, int(1e5)):
	number = ''
	n = 1
	while len(number) < 9:
		number += str(i * n)
		n += 1

	if n > 1 and len(number) is 9 and len(set(number)) is 9 and set(number) == set([str(x) for x in range(1, 10)]) and int(number) > largest:
		largest = int(number)

print(largest)
