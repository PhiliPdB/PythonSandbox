numbers = []

# Checks if the number is a palindrome
def is_palindrome(n):
	return str(n) == str(n)[::-1]

def dec_to_bin(n):
    return bin(n)[2:]

for i in range(0, int(1e6)):
	if is_palindrome(i) and is_palindrome(dec_to_bin(i)):
		numbers.append(i)

print(sum(numbers))