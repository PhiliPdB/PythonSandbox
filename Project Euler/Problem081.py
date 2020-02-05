
# Read matrix
lines = open('./Problem081Data.txt').readlines()
matrix = [[int(n) for n in line.split(',')] for line in lines]

# Work from bottom-right to top-left
# Thus in a backwards fashion

size = len(matrix)

# Calculate bottom and right side
for i in reversed(range(0, size - 1)):
	matrix[size - 1][i] += matrix[size - 1][i + 1]
	matrix[i][size - 1] += matrix[i + 1][size - 1]

for i in reversed(range(0, size - 1)):
	for j in reversed(range(0, size - 1)):
		matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

print(matrix[0][0])
