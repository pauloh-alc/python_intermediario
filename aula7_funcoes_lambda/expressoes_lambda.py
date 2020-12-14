"""
Funções Lambada ou expressoes anônimas
"""

lista = [
    ['P1', 13],
    ['P2', 15],
    ['P3', 8],
    ['P4', 13],
    ['P5', 17],
]

# Ordena lista baseado
def func(item):
    return item[1]


lista.sort(key=func, reverse=True)
print(lista)