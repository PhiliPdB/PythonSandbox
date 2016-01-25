
global_output = 0

def read_input():
	global global_output
	n = int(input())

	if n == 0:
		print(global_output)
		return
	elif n % 7 == 0 or '7' in str(n):
		global_output += 1

	read_input()

read_input()