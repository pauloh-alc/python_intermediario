"""
Questão 7 -
"""

# Função: exibe do menu
def menu():
    print('[0] Cadastrar pessoa')
    print('[1] Média de salário da população')
    print('[2] Média do número de filhos')
    print('[3] O maior salário')
    print('[4] O percentual de pessoas com salário inferior a R$ 380,00')
    print('[5] SAIR')


# Função: responsável por realizar o cadastro de pessoas de uma determinada cidade
def cadastrar(lista_nomes, lista_salarios, lista_numero_filhos, n):
    lista_nomes.append(input(f'\nEntre com o nome da pessoa {n}: '))
    lista_salarios.append(float(input(f'Entre com o salário da pessoa {n}: ')))
    lista_numero_filhos.append(int(input(f'Entre com o número de filhos da pessoas {n}: ')))
    n += 1
    return n


# Função: retorna a média de saário da população
def calcula_media_de_salario(lista_salarios, n):
    return sum(lista_salarios) / n


# Função: retorna a media do número de filhos
def calcula_media_numero_de_filhos(lista_numero_filhos, n):
    return sum(lista_numero_filhos) / n


# Função: encontra o maior salário a partir de uma lista passada como argumento
def maior_salario(lista_salarios):
    maior = max(lista_salarios)
    pos_maior = lista_salarios.index(maior)
    return maior, pos_maior


# Função: calcula o percentual de pessoas com salário inferior a R$ 380,00
def calcula_percentual_de_pessoas(lista_salarios, n):
    qtd = 0
    for salario in lista_salarios:
        if salario < 380:
            qtd += 1
    return qtd * 100 / n


# Função principal
def main():
    # Dicionário de dados:
    nomes = []
    salarios = []
    numero_filhos = []
    n = 0

    while True:
        menu()

        opcao = input('Entre com um opcao: ')
        opcao = int(opcao)

        if opcao   == 0:
            n = cadastrar(nomes, salarios, numero_filhos, n)
        elif opcao == 1:
            media = calcula_media_de_salario(salarios, n)
            print(f'Média do salário da população é: {media}.\n')
        elif opcao == 2:
            media = calcula_media_numero_de_filhos(numero_filhos, n)
            print(f'Média do número de filhos é: {media}.\n')
        elif opcao == 3:
            salario_maior = maior_salario(salarios)
            print(f'Maior salário é: {salario_maior[0]} da pessoa -> {nomes[salario_maior[1]]}\n')
        elif opcao == 4:
             percentual = calcula_percentual_de_pessoas(salarios, n)
             print(f'Percentual de pessoas com salário inferior a R$ 380,00 é: {percentual} %\n')
        elif opcao == 5:
            break


if __name__ == '__main__':
    main()


