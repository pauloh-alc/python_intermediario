from dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)
# ou
# nova_lista = [x*2 for x in lista]
# print(lista)
# print(list(nova_lista))



#def aumenta_preco(produto):
#    produto['preco'] = round(produto['preco'] * 1.05, 2)
#    return produto

#novos_produtos = map(aumenta_preco, produtos)

#for produto in novos_produtos:
#    print(produto)


# com list-comprehetion
lista_nomes = [dic['nome'] for dic in pessoas]
print(lista_nomes)

lista_idades = [dic['idade'] for dic in pessoas]
print(lista_idades)

# com map
nomes = map(lambda p: p['nome'], pessoas)
print(list(nomes))

idades = map(lambda p: p['idade'], pessoas)
print(list(idades))



def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p

pessoas_novas = map(aumenta_idade, pessoas)

for pessoa in pessoas_novas:
    print(pessoa)






