# Logic
# 0, 1, 1, 2, 3, 5
# x  y  z
#    x  y  z
#       x  y  z
#          x  y  z

index = 1
x = 0
y = 1
z = 0

while len(str(x)) < 1000:
	z = x + y
	x = y
	y = z
	index += 1

print(index)