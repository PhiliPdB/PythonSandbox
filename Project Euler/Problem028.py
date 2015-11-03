round = 1
sum = 1

current_number = 3
number_in_round = 1
while (current_number <= (1001 * 1001)):
	sum += current_number

	number_in_round += 1
	if number_in_round == 5:
		number_in_round = 1
		round += 1

	current_number += (2 * round)

print(sum)
