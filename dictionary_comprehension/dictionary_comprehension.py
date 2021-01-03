
lista = [ 
        ('chave1', 1),
        ('chave2', 2),
        ]

dic = {x.upper() : y for x, y in lista}
print(dic)


conjunto = {x for x in range(5)}
print(conjunto)


dicionario = {f'chave_{x}': x**2 for x in range(5)}
print(dicionario)
