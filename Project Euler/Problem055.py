lychrel_numbers = 0

def is_palindrome(n):
	return n == reverse(n)

def reverse(n):
	return int(str(n)[::-1])

for i in range(11, int(1e4)):
	palindrome = False
	n = i
	for j in range(50):
		n += reverse(n)
		if is_palindrome(n):
			palindrome = True
			break

	if not palindrome:
		lychrel_numbers += 1

print(lychrel_numbers)