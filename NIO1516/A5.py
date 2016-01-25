LINES_OF_INPUT = 10
board = []
total = 0

for i in range(LINES_OF_INPUT):
	row = input()
	row_list = []
	for col in row:
		row_list.append(int(col))

	board.append(row_list)

# Processing
for y in range(len(board)):
	for x in range(len(board[y])):
		if board[y][x] is 0:
			# If row above was 0
			if board[y-1][x] and board[y-1][x] is not 1:
				board[y][x] = board[y-1][x]

				if board[y][x-1] and board[y][x-1] is not 1 and board[y][x-1] is not board[y][x]:
					i = x - 1
					total -= 1
					while board[y][i] and board[y][i] is not 1:
						board[y][i] = board[y][x]
						
						if not i - 1 < 0: i -= 1
						else: break

				continue
			# If previous was 0
			elif board[y][x-1] and board[y][x-1] is not 1:
				board[y][x] = board[y][x-1]
				continue
			else:
				board[y][x] = total + 2
				total += 1

print(total)
