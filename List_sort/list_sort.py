# Escolhendo critério de ordenação:

# Esse programa ordena a lista baseado num critério (comprimento das palavras)

lista_nomes = ['kikomaniocozinhado', 'Paulo', 'Lua', 'Rildinha', 'Paraibaninho']

def comprimento(x):
    return len(x)

print('Ordenada de forma crescente')
lista_nomes.sort(key=comprimento)
print(lista_nomes)



print('Ordenada de forma decrescente')
lista_nomes.sort(key=comprimento, reverse=True)
print(lista_nomes)


