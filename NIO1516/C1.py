word = input()
N = len(word)

for G in range(N, 1, -1):
	if N % G == 0:
		for i in range(0, int(N/G)):
			location = (i + 1) * G + int(N/G) - (i + 1)
			word = word[1:location] + word[0] + word[location:]

print(word)