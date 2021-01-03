"""
    Considerando duas listas de inteiros ou floats (lista A e lista B)
    Some os valores nas listas retornando uma nova lista com os valores somados:

    Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor lista.

    Exemplo:

    lista_a    = [1,2,3,4,5,6,7]
    lista_b    = [1,2,3,4]
    resultado:
    lista_soma = [2,3,6,6]
"""

# Resolução:


lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

# Forma 1: forma mais geral

print("Forma 1:")
lista_soma = []

if len(lista_b) < len(lista_a):
    for i in range(len(lista_b)):
        lista_soma.append(lista_a[i] + lista_b[i])

    print(lista_soma)
else:
    for i in range(len(lista_a)):
        lista_soma.append(lista_a[i] + lista_b[i])
    print(lista_soma)

# Forma 2: 
print("Forma 2:")
lista_soma = []

if len(lista_b) < len(lista_a):
    for i, _ in enumerate(lista_b):
        lista_soma.append(lista_a[i] + lista_b[i])
    print(lista_soma)
else:
    for i, _ in enumerate(lista_a):
        lista_soma.append(lista_a[i] + lista_b[i])
    print(lista_soma)

# Forma 3: com list comprehention
lista_soma = []

print("Forma 3:")
if len(lista_a) < len(lista_b):
    lista_soma = [lista_a[i] + lista_b[i] for i in range(len(lista_a))]
    print(lista_soma)
else:
    lista_soma = [lista_a[i] + lista_b[i] for i in range(len(lista_b))]
    print(lista_soma)

# Forma 4: 

# print(list(zip(lista_a,lista_b)))
print("Forma 4:")
lista_soma = [a + b for a, b in zip(lista_a, lista_b)]
print(lista_soma)


