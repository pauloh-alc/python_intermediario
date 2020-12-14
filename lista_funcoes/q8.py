"""
Questão 8 -
"""

def show(lista, n):
    for i in range(0, n):
        print(f'{i} ', end='')
        for qtd in range(1, lista[i] + 1):
            print('*', end='')
        print()


def main():
    v = []
    for i in range(0, 10):
        valor = int(input(f'Entre com o {i}° valor: '))
        v.append(valor)

    n = int(input("\nEntre com um número 'n': "))

    show(v, n)


if __name__ == '__main__':
    main()
