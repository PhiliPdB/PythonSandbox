product_numerator = 1
product_denominator = 1

for i in range(1, 10):
	for denominator in range(1, i):
		for numerator in range(1, denominator):
			if denominator * (10 * numerator + i) is numerator * (10 * i + denominator):
				product_numerator *= numerator
				product_denominator *= denominator

print(product_denominator)
