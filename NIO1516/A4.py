
total_photos = int(input()) # First line input
photos = []
output = []
lastRound = False

for i in range(total_photos):
	photos.append(int(input()))


def photo_round():
	global lastRound

	photopick = photos[0:10]

	output.append(max(photopick))

	position = photopick.index(max(photopick))

	del photos[0:position+1]

	if len(photos) <= 10 and not lastRound:
		lastRound = True
		photo_round()
	
	if not lastRound:
		photo_round()

photo_round()

for i in output:
	print(i)