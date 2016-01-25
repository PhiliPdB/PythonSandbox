from copy import deepcopy
import sys

length = input()
numbers = [int(x) for x in input().split(" ")]
saved_numbers = deepcopy(numbers)
turns_1 = []
turns_2 = []
turns_3 = []

def omkeren(x, y, turns):
	turns.append([x, y])
	while (x < y and x != y):
		numbers[x-1], numbers[y-1] = numbers[y-1], numbers[x-1]
		x += 1
		y -= 1

def sort():
	tmp_numbers = numbers
	while True:
		if numbers.index(max(tmp_numbers)) + 1 is not len(tmp_numbers):
			omkeren(numbers.index(max(tmp_numbers)) + 1, len(tmp_numbers), turns_1)

		if sorted(numbers) == numbers:
			break
		tmp_numbers.remove(max(tmp_numbers))

def selection_sort():
	for i in range(0, len(numbers)):
		minimal = i
		for j in range(i + 1, len(numbers)):
			if numbers[j] < numbers[minimal]:
				minimal = j
		if minimal is not i:
			omkeren(i + 1, minimal + 1, turns_2)

def quick_sort():
	quick_sort_helper(0, len(numbers) - 1)

def quick_sort_helper(first, last):
	if first < last:
		splitpoint = partition(first, last)

		quick_sort_helper(first, splitpoint - 1)
		quick_sort_helper(splitpoint + 1, last)

def partition(first, last):
	pivotvalue = numbers[first]

	leftmark = first + 1
	rightmark = last

	done = False
	while not done:

		while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		while numbers[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1

		if rightmark < leftmark:
			done = True
		elif leftmark is not rightmark:
			omkeren(leftmark + 1, rightmark + 1, turns_3)

	if first is not rightmark:
		omkeren(first + 1, rightmark + 1, turns_3)

	return rightmark

sort()
numbers = deepcopy(saved_numbers)
selection_sort()
numbers = deepcopy(saved_numbers)
quick_sort()

min_turns = min(len(turns_1), len(turns_2), len(turns_3))
if min_turns is len(turns_1):
	print(len(turns_1))
	for turn in turns_1:
		print(str(turn[0]) + " " + str(turn[1]))
elif min_turns is len(turns_2):
	print(len(turns_2))
	for turn in turns_2:
		print(str(turn[0]) + " " + str(turn[1]))
elif min_turns is len(turns_3):
	print(len(turns_3))
	for turn in turns_3:
		print(str(turn[0]) + " " + str(turn[1]))

print(numbers, file=sys.stderr)
print(turns_1, file=sys.stderr)
print(turns_2, file=sys.stderr)
print(turns_3, file=sys.stderr)