
# Abrindo meu arquivo:......
file = open('abc.txt', 'w+') # open('<arquivo>', 'modo') , nesse caso, write + read
#...........................

# Escrevendo no arquivo --> write('o que eu quero escrever')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

# Volta para o início do meu arquivo:
file.seek(0, 0)
#....................................

# Lendo do meu arquivo -> read() ela vai ler tudo que tem no arquivo e jogar em uma string
print('Lendo linhas:')
#string = file.read()
#print(string)
print(file.read())  
#.......................

print(10 * '*')

file.seek(0, 0)

# Lendo linha a linha:........
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
#............................

print(10 * '*')

file.seek(0, 0)
lista = file.readlines()
print(lista)

for linha in lista:
    print(linha, end='')


file.close()
