"""
4 - Fizz Buzz - Se  o parâmetro da função for divisível por 3
    retorne fizz, se o parâmetro da função for divisível por 5
    retorne buzz. Se o parâmetro da função for divisível por 5 e por 3
    retorne FizzBuzz, caso contrário, retorne o número enviado.
"""


def verifica_divisibilidade(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"

    return num

valor = int(input("Entre com um valor: "))
resultado = verifica_divisibilidade(valor)
print(resultado)
