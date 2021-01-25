# modos --> a+ (append) w-write, r-read
# w+ write and read, 
# r+ read and write

with open('abc3.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    for linha in file:
        print(linha, end='')
