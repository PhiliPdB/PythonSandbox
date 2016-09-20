from itertools import permutations

total = 0

numbers = list(permutations(range(10)))

for n in numbers:
	d = ''.join([str(i) for i in n])

	if int(d[1] + d[2] + d[3]) % 2 is 0 and int(d[2] + d[3] + d[4]) % 3 is 0 and int(d[3] + d[4] + d[5]) % 5 is 0 and int(d[4] + d[5] + d[6]) % 7 is 0 \
			and int(d[5] + d[6] + d[7]) % 11 is 0 and int(d[6] + d[7] + d[8]) % 13 is 0 and int(d[7] + d[8] + d[9]) % 17 is 0:
		total += int(d)

print(total)
