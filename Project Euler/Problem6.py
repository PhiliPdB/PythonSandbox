
def sum_of_squares(number):
	result = 0

	for i in range(1, number + 1):
		result += i ** 2

	return result

def square_of_sum(number):
	return sum(range(1, number + 1)) ** 2

print(square_of_sum(100) - sum_of_squares(100))