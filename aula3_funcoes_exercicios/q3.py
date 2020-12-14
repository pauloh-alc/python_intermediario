"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo
um percentual (ex. 10%). Retorne (return) o valor do primeiro número somado do aumento
do percentual do mesmo
"""


def calcula_aumento(v, p):
    v = v + v * p / 100
    return v


valor = int(input("Entre com um valor: "))
porcentagem = int(input("Entre com a porcentagem de aumento: "))

resultado = calcula_aumento(valor, porcentagem)

print(f'Valor antes: {valor}.')
print(f'Após o aumento de {porcentagem}%: {resultado}')