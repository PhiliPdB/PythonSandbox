from math import factorial

limit  = int(1e6)
length = 60

count = 0

def sumFact(n):
	return sum([factorial(int(i)) for i in str(n)])


for i in range(1, limit + 1):
	if i % 100000 == 0: print(i)

	numbers = set([i])

	currentNumber = i
	nextNumber = sumFact(currentNumber)
	while nextNumber not in numbers:
		currentNumber = nextNumber
		numbers.add(nextNumber)

		nextNumber = sumFact(currentNumber)

		if len(numbers) > length:
			break

	if len(numbers) == length:
		count += 1

print(count)

