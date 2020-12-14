"""
Questão 10 -
"""

def split(lista, n):
    nova_lista = []

    for i in range(0, n):
        if lista[i] < lista[0]:
            nova_lista.append(lista[i])

    nova_lista.append(lista[0])

    for i in range(0, n):
        if lista[i] > lista[0]:
            nova_lista.append(lista[i])
    return nova_lista


def main():
    v = []
    qtd_elementos = int(input('Quantos elementos você quer em sua lista? '))
    for i in range(0, qtd_elementos):
        v.append(int(input(f'v[{i}]: ')))


    lista = split(v, qtd_elementos)
    print(f'Lista: {lista}.')


if __name__ == '__main__':
    main()