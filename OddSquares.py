
output = 0

# Max input is 100 numbers
for i in range(100):
	n = int(input("Give a number "))

	# Stop when n is 0
	if n is 0:
		break

	# You only have to sum the odd squares
	if n % 2 != 0:
		output = output + (n ** 2)

print(output)