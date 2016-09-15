from math import factorial

curious_numbers = []

for i in range(10, int(1e6)):
	numbers = [int(x) for x in str(i)]

	total = 0
	for number in numbers:
		total += factorial(number)

	if total == i:
		curious_numbers.append(i)

print(sum(curious_numbers))
