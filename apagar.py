
from itertools import combinations, permutations

notas = ['n1', 'n2', 'n3', 'n4']

i = 1
for grupo in permutations(notas, 4):
    print(f'{i} - {grupo}')
    i += 1
