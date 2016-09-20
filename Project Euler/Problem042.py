words = open('Problem042Data.txt').read().replace('"', '').split(',')
triangle_words = 0

def t(n):
	return int(.5 * n * (n + 1))

numbers = [t(i) for i in range(1, 1000)]

for word in words:
	word = word.lower()
	
	total = 0
	for letter in word:
		total += ord(letter) - 96

	if total in numbers:
		triangle_words += 1

print(triangle_words)
