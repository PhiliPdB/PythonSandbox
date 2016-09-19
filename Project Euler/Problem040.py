def d(n):
	number = ''.join([str(i) for i in range(1, n + 1)])
	return int(number[n - 1])

print(d(1) * d(int(10)) * d(int(100)) * d(int(1e3)) * d(int(1e4)) * d(int(1e5)) * d(int(1e6)))