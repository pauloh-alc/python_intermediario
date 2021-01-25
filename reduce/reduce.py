from dados import produtos, pessoas, lista
from functools import reduce

# Sem reduce........
acumula = 0 
for item in lista:
    acumula = acumula + item

print(acumula)
#...................

# Com reduce........
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)
#...................


# Quero somar os preços de todos produtos da lista de 
# dictionary 'produtos'

# Forma tradicional:
soma = 0
for produto in produtos:
    soma = soma + produto['preco']

print(soma)

# Com reduce:
soma_precos = reduce(lambda soma, produto: soma + produto['preco'], produtos, 0)
print(soma_precos)

# Se eu quisesse a média:
print(soma_precos / len(produtos))


# Quero obter a media das idades:

# Forma tradicional:

soma = 0
for pessoa in pessoas:
    soma = soma + pessoa['idade']

media = soma / len(pessoas) 
print(f'media das idade: {media}')
#...................


# Com reduce:

media_idades = reduce(lambda soma, pessoa: soma + pessoa['idade'], pessoas, 0) / len(pessoas)
print(f'media das idade: {media_idades}')
#...................
