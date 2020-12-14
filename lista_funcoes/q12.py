"""
Questão 12 -
"""

def pot(base, exp):
    if exp == 0:
        return 1
    return base * pot(base, exp - 1)

"""
    2^3 = 2 * 2 * 2 = 8
    2^4 = 2^3 * 2
    2^5 = 2^4 * 2 
    2^6 = 2^5 * 2 --> pot(base,exp-1) * 2
"""
def main():
    k = int(input("Entre com um número k para a base: "))
    n = int(input("Entre com um número n para o expoente: "))

    resultado = pot(k, n)
    print(f'{k} elevado a {n} é: {resultado}')
if __name__ == '__main__':
    main()