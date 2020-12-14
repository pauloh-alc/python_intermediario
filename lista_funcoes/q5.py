"""
Questão 5 -
"""


def main():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    temperaturas = []
    i = 0
    while i < 12:
        temp = input(f"Temperatura do mês {i + 1}:")
        temp = float(temp)
        temperaturas.append(temp)
        i += 1

    posicao_maior = maior_temperatura(temperaturas)
    print(f'Maior temperatura ocorreu no mês de {meses[posicao_maior]} com {temperaturas[posicao_maior]} °C')
    posicao_menor = menor_temperatura(temperaturas)
    print(f'Menor temperatura ocorreu no mês de {meses[posicao_menor]} com {temperaturas[posicao_menor]} °C')


def maior_temperatura(lista_temp):
    i = 0
    maior = lista_temp[0]
    pos_maior = 0
    while i < 12:
        if lista_temp[i] > maior:
            maior = lista_temp[i]
            pos_maior = i
        i += 1
    return pos_maior


def menor_temperatura(lista_temp):
    i = 0
    menor = lista_temp[0]
    pos_menor = 0
    while i < 12:
        if lista_temp[i] < menor:
            menor = lista_temp[i]
            pos_menor = i
        i += 1
    return pos_menor


if __name__ == '__main__':
    main()
