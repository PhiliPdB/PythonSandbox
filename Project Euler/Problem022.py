names = sorted(open('Problem022Data.txt').read().replace('"', '').split(','))
name_scores = []

for name in names:
	name_scores.append(sum([ord(letter.lower()) - 96 for letter in name]) * (names.index(name) + 1))

print(sum(name_scores))
