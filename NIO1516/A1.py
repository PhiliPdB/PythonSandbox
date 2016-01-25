# Input
n = int(input())

class Halter:

	def __init__(self, number):
		self.number = number
		self.line_length = 2 * number - 1

	def create_line(self, line_number):
		
		if line_number >=  self.number:
			line_number = 2 * self.number - line_number

		dash_length = line_number - 1
		star_length = self.line_length - (2 * dash_length)

		return self.multiple("-", dash_length) + self.multiple("*", star_length) + self.multiple("-", dash_length)

	def multiple(self, what, times):
		string = ""
		for i in range(times):
			string = string + what
		return string

	# Prints the halter
	def print(self):
		total_lines = self.line_length

		for i in range(1, total_lines + 1):
			print(self.create_line(i))


Halter(n).print()

