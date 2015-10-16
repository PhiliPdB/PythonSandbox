
# Checks if the number is a palindrome
def is_palindrome(number):
	return str(number) == str(number)[::-1]

def find_palindromes(number_of_digits):
	first = 10 ** (number_of_digits - 1)
	second = 10 ** number_of_digits
	palindromes = []
	
	for i in range(first, second):
		for j in range(first, second):
			if is_palindrome(i * j):
				palindromes.append(i * j)

	return palindromes

print(max(find_palindromes(3)))