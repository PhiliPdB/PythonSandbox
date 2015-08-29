
n = int(input("Type a number "))

# The full line width is 		2n - 1
# The total amount of lines is	n + 1
# The dash length is			n - 1

# Set the same character multiple times in a string
def multiple(what, times):
	position = 1
	string = ""
	for i in range(times):
		string = string + what
	return string

def print_christmas_tree(lines):
	# Create the line
	def create_line(line_number):
		dash_length = n - line_number

		# line_number	tree_width
		# 1				1
		# 2				3
		# 3				5

		tree_width = (2 * line_number) - 1

		return multiple("-", dash_length) + multiple("*", tree_width) + multiple("-", dash_length)

	# Loop through the tree
	for i in range(1, n + 1):
		print(create_line(i))
	# Print the base
	print(create_line(1))

# Print the whole tree
print_christmas_tree(n)
