answer = 0
below_what = 1000

for i in range(1, below_what):
	if i % 3 == 0 or i % 5 == 0:
		answer += i

print(answer)