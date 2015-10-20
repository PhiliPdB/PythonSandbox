from datetime import date

sundays = 0

for year in range(1901, 2000 + 1):
	for month in range(1, 12 + 1):
		if date(year, month, 1).weekday() == 6:
			sundays += 1

print(sundays)