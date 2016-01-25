houses = [[11, 56], [12, 59], [13, 53], [13, 57], [14, 50],
		[17, 53], [18, 52], [18, 54], [18, 58], [19, 55],
		[20, 51], [21, 54], [22, 55], [22, 56], [23, 51],
		[23, 52], [24, 57], [26, 50], [26, 52], [26, 53]]
min_distance = None
final_coord = []

def pythagoras(a, b):
	return ((a ** 2) + (b ** 2)) ** 0.5

for y in range(50, 59 + 1):
	for x in range(11, 26 + 1):
		# Cannot be on a house
		if [x, y] in houses: continue

		max_distance = None
		for coord in houses:
			a = abs(coord[0] - x)
			b = abs(coord[1] - y)
			if max_distance is None or pythagoras(a, b) > max_distance:
				max_distance = pythagoras(a, b)

		if min_distance is None or min_distance > max_distance:
			min_distance = max_distance
			final_coord = [x, y]

print(final_coord)