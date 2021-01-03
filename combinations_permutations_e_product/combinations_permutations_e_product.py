"""
Combinations, permutations e product - itertools
# Combinação - Ordem não importa
# Permutação - Ordem importa
Ambos não repetem valores únicos
# Produto - ordem importa e repete valores únicos

"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']


print("Combinação: ")
# Combinação - ordem não importa
for grupo in combinations(pessoas, 2):
    print(grupo)
print('\n')


print("Permutação: ")
# Permutação - ordem importa
for grupo in permutations(pessoas, 2):
    print(grupo)
print('\n')

print("Produto")
# Produto - a ordem importa e repete valores únicos
for grupo in product(pessoas,repeat=2):
    print(grupo)

