from itertools import permutations

def is_permutation(m, n):
	p = list(permutations([x for x in str(m)]))
	final_p = []
	for x in p:
		final_p.append(int(''.join([y for y in x])))

	permutation = True
	for x in n:
		if not x in final_p:
			permutation = False
			break
	return permutation

for i in range(2, int(1e6)):
	if is_permutation(i, [i * x for x in range(2, 6 + 1)]):
		print(i)
		break
