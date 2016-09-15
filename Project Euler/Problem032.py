products = []

multiplicand = 1
while True:
	multiplier = 1
	while True:
		product = multiplicand * multiplier

		numbers = str(multiplicand) + str(multiplier) + str(product)
		if len(numbers) is 9 and len(set(numbers)) is 9:
			if set(numbers) == set([str(x) for x in range(1, 10)]):
				products.append(product)
		elif len(numbers) > 9:
			break

		multiplier += 1

	multiplicand += 1
	if multiplicand > 100:
		break

print(sum(set(products)))
