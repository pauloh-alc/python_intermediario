"""
Questão 11
"""


def somatorio(n):
    if n == 0:
        return 0
    return n + somatorio(n-1)


"""
    main() --> somatorio(5)
               somatorio(4)
               somatorio(3)
               somatorio(2)
               somatorio(1)
               somatorio(0) return 0

"""

def main():
    n = int(input("Entre com um número n > 0: "))
    soma = somatorio(n)
    print(f'A soma dos números de 1 até {n} é: {soma}')


if __name__ == '__main__':
    main()
