romans = open('Problem089Data.txt').read().split('\n')
current_chars = len(''.join(romans))

minimized = ["" for i in range(len(romans))]


def minimize_roman_numeral(roman):
	roman = roman.replace("DCCCC", "CM")
	roman = roman.replace("CCCC", "CD")
	roman = roman.replace("LXXXX", "XC")
	roman = roman.replace("XXXX", "XL")
	roman = roman.replace("VIIII", "IX")
	roman = roman.replace("IIII", "IV")

	return roman


for i in range(len(romans)):
	minimized[i] = minimize_roman_numeral(romans[i])

# Calculate minimized chars
minimized_chars = len(''.join(minimized))

print(current_chars - minimized_chars)
