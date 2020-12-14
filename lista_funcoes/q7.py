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
def cadastrar():
    pass


# Função: retorna a media do número de filhos
def calcula_media_numero_de_filhos():
    pass

# Função: retorna a média
def calcula_media_de_salario():
    pass


# Função: encontra o maior salário a partir de uma lista passada como argumento
def maior_salario():
    pass


# Função: calcula o percentual de pessoas com salário inferior a R$ 380,00
def calcula_percentual_de_pessoas():
    pass


def main():
    while True:
        menu()

        opcao = input('Entre com um opcao: ')
        opcao = int(opcao)

        if opcao   == 0:
            pass
        elif opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            break

if __name__ == '__main__':
    main()
