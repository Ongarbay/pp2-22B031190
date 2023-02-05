import itertools
s = input()
elements = list(s)
permutations = list(itertools.permutations(elements))
print([''.join(permutations) for permutations in permutations])
