"""
Questão 1 -
"""

def dobro(numero):
    return numero * 2


numero = input("Entre com um número: ")
numero = int(numero)

resultado = dobro(numero)
print(f'O dobro do número {numero} é: {resultado}')