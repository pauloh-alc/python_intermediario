"""
2 - Crie uma função que receba 3 número como parâmetros e exiba a soma entre eles
"""

def soma(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

while True:
    i = 1
    numero1 = input("Entre com o número {}: ".format(i))
    numero2 = input("Entre com o número {}: ".format(i + 1))
    numero3 = input("Entre com o número {}: ".format(i + 2))

    if not numero1.isdecimal() or not numero2.isdecimal() or not numero3.isdecimal():
        print('Erro: você só pode entrar com número positivos !!')
        continue

    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)

    resultado = soma(numero1, numero2, numero3)

    print(f'A soma entre {numero1}, {numero2} e {numero3} é = {resultado}')
