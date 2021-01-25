from dados import produtos, pessoas, lista

""" Usando lista: """

# Com filter
nova_lista = filter(lambda x: x > 5, lista)
print(lista)
print(list(nova_lista))

# Com list-comprehestion
lista_nova = [x for x in lista if x > 5]
print(lista_nova)



""" Usando lista com dic 'produtos' """

# Com filter
novo_dic = filter(lambda p: p['preco'] > 50, produtos)
for produto in novo_dic:
    print(produto)

print()

# Com list-comprehension
novos_produtos = [p for p in produtos if p['preco'] > 50]
for produto in novos_produtos:
    print(produto)

print()

""" Usando lista com dic 'pessoas' """

def myfilter(pessoas):
    if pessoas['idade'] > 25:
        return True
    else:
        return False

novas_pessoas = filter(myfilter, pessoas)
for pessoa in novas_pessoas:
    print(pessoa)
