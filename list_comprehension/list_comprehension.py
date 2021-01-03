l1 = [1, 2, 3, 4, 5]
exemplo1 = [variavel for variavel in l1]
exemplo2 = [variavel * 2 for variavel in l1]
exemplo3 = [(x, y) for x in l1 for y in range(3)]

print(l1)

print(exemplo1)
print(exemplo2)
print(exemplo3)

l2 = ['Luiz', 'Mauro', 'Maria']
exemplo4 = [nome.replace('a', '@') for nome in l2]
print(exemplo4)


tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)


lista = [
    [1, 2],
    [3, 4]
]

lista = dict(lista)
print(lista)


listinha = list(range(100))
listinha_updating = [v if v % 2 == 0 else 0 for v in listinha]
print(listinha_updating)




