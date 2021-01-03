"""
zip - Unindo iteráveis
zip_longest - Itertools
"""

from itertools import zip_longest, count

indice  = count() 

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Russas']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip (indice, estados, cidades)

# cidades_estados = list(cidades_estados)
# print(list(cidades_estados))
# dicionario = {key: value for key, value in cidades_estados}
# print(dicionario)

# print(next(cidades_estados))
# print(next(cidades_estados))


# desempacotando
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)



teste = [('nome1', 10), ('nome2', 20), ('nome3', 30)]

nome, idade = teste[0]
print(nome, idade)

nome, idade = teste[1]
print(nome, idade)

nome, idade = teste[2]
print(nome, idade)


