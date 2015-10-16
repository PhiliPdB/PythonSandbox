to_what = 20
number = to_what
found = False

while True:
	for i in range(1, to_what + 1):
		if number % i == 0:
			if i == len(range(1, to_what + 1)):
				found = True
			continue
		else:
			break

	if found:
		break
	else:
		number += to_what

print(number)
