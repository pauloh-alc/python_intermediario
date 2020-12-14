"""
1 - Crie uma função que exiba uma saudação com os parâmetros saudacao e nome
"""


def exibe_saudacao(saudacao='Bem-vindo', nome='usuário'):
    print(saudacao, nome)


nome_usuario = input("Entre com seu nome: ")
exibe_saudacao("Olá", nome_usuario)
