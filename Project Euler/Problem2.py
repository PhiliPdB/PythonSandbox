answer = 0

# Logic
# 0, 1, 1, 2, 3, 5
# x  y  z
#    x  y  z
#       x  y  z
#          x  y  z

x = 0
y = 1
z = 0

while y <= 4000000:
	z = x + y
	x = y
	y = z

	if y % 2 == 0:
		answer += y

print(answer)