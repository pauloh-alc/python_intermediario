
""" 
    Count - Itertool --> vai me gerar um iterador infinito
"""

from itertools import count

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2))
    if round(valor,2) >= 10.0:
        break



index = count()
lista_nome = ["Paulo", "Luara", "Davi", "Valério", "Rilda", "Luan"]
lista_indexada = zip(index, lista_nome)
print(list(lista_indexada))

