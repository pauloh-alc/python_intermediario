"""
    Coloca o menor elemento da lista na posicao lista[0] e
    colocar o lista[0] na posicao do menor elemento
"""

lista = []

i = 0
# Inserindo valores:
while i < 5:
    valor = int(input(f"Entre com um número {i}: "))
    lista.append(valor)
    i += 1


menor = min(lista)
i = 0
pos_menor = 0
while i < 5:
    if lista[i] == menor:
        pos_menor = i
    i += 1

print(f"Lista original: {lista}")

aux = menor
lista[pos_menor] = lista[0]
lista[0] = aux

print(f"lista nova: {lista}")
