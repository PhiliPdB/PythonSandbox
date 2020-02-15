
# Read matrix
lines = open('./Problem082Data.txt').readlines()
matrix = [[int(n) for n in line.split(',')] for line in lines]

size = len(matrix)

solution = [matrix[i][size - 1] for i in range(size)]

# # Calculate for going right
# for y in range(0, size):
# 	matrix[y][size - 2] += matrix[y][size - 1]

for x in reversed(range(0, size - 1)):
	solution[0] += matrix[0][x]
	for y in range(1, size):
		solution[y] = min( matrix[y][x] + solution[y] # right
				    , matrix[y][x] + solution[y - 1]  # up
				    )

	for y in reversed(range(0, size - 1)):
		solution[y] = min( solution[y]               # change nothing
					, matrix[y][x] + solution[y + 1] # down
					)

print(min(solution))

