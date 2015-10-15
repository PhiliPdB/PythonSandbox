import math

abc_list = []

for x in range(1, 1000):
	for y in range(1, 1000):
		if math.sqrt(x ** 2 + y ** 2) % 1 == 0:
			abc_list.append([x, y, int(math.sqrt(x ** 2 + y ** 2))])

def check(number):
	for i in abc_list:
		if sum(i) == number:
			return i

def product(list):
	p = 1
	for i in list:
		p *= i
	return p

print(product(check(1000)))