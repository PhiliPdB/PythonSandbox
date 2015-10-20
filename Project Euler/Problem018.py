triangle = [[int(i) for i in line.split()] for line in open('Problem018Data.txt').readlines()]

def maxPathSum():
	# Go from bottom to top
	for row in range(len(triangle)-1, 0, -1):
		for col in range(0, row):
			# Save the sum in the row above
			triangle[row-1][col] += max(triangle[row][col], triangle[row][col+1])
	return triangle[0][0]

print(maxPathSum())