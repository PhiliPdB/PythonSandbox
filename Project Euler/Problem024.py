from itertools import permutations

perms = sorted(set([int(''.join(i)) for i in permutations('0123456789')]))

print(perms[1000000 - 1])