def sum_of_number(n):
	sum = 0
	for i in str(n):
		sum += int(i)
	return sum

print(sum_of_number(2 ** 1000))