carrinho_loja = [('Produto1', 10), ('Produto2', 20), ('Produto3', 30), ('Produto4', 40)]
#               nome_produto, valor

# Forma 1:
print(carrinho_loja[0])

print(carrinho_loja[1])

print(carrinho_loja[2])

print('-' * 100)

# Forma 2:
for produto in carrinho_loja:
    print(produto)
# ........


# Forma 1:
print(carrinho_loja[0][1])
print(carrinho_loja[1][1])
print(carrinho_loja[2][1])

print('-' * 100)

# Forma 2:
for produto in carrinho_loja:
    print(produto[1])
# ........

# Desempacotamento
nome, valor = carrinho_loja[0]
print(nome, valor)
nome, valor = carrinho_loja[1]
print(nome, valor)
#.................

# Obtendo o total:
print("Obtendo total em carrinho de compra:")

# Forma 1:

total = 0

for produto in carrinho_loja:
    total = total + produto[1]
print(total)

# Forma 2:
total = []
for produto in carrinho_loja:
    total.append(produto[1])
print(sum(total))

# Forma 3:
total = [produto[1] for produto in carrinho_loja]
print(sum(total))

# Forma 4:
total = sum([produto[1] for produto in carrinho_loja])
print(total)

# Forma 5:
total = sum([valor for nome, valor in carrinho_loja])
print(total)

# Forma 6:

total = sum([float(produto[1]) for produto in carrinho_loja])
print(total)

