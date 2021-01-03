

carrinho = []

carrinho.append(('Produto_1', 30))
carrinho.append(('Produto_2', 20))
carrinho.append(('Produto_3', 50))

# Forma 1:
total = 0
for produto in carrinho:
    total = total + produto[1]

print(f'total = {total}')


# Forma 2:
total = []
for produto in carrinho:
    total.append(produto[1])

print(total)
print(sum(total))

# Forma 3:
total = [produto[1] for produto in carrinho]
print(sum(total))
