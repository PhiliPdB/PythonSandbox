from math import factorial

def nCr(n, r):
	return int(factorial(n) / (factorial(r) * factorial(n - r)))

print(nCr(40, 20)) # 40 is total of moves	20 is total of moves in one direction