# Input
name = str(input())

name_array = name.split()

character_one = name_array[len(name_array) - 1][0]
character_two = name_array[len(name_array) - 1][-1:]
character_three = name_array[0][0]

output = character_one + character_two + character_three

print(output.upper())