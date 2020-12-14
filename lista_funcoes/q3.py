"""
Questão 3 -
"""
lista_div = []


def soma_dos_divisores(valor):
    soma = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            lista_div.append(i)
            soma = soma + i
    return soma


valor = int(input("Entre com um valor: "))

somatorio = soma_dos_divisores(valor)
print(f'O divisores de {valor} são: {lista_div}')
print(f'A soma dos divisores de {valor} é: {somatorio}')