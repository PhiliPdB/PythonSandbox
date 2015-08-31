# When you input your name, you get some information about it

name = input("What is your name? ")

def count_letters(word):
    return str(len(word) - word.count(' '))

def count_capital_letters(word):
	return str(sum(1 for c in word if c.isupper()))

def count_characters(word):
	return str(len(set(word) - set(' ')))

# Now print all information
print("Total length: " + count_letters(name))
print("Total capital characters: " + count_capital_letters(name))
print("Total different characters: " + count_characters(name))
print("Inversed: " + name[::-1])
