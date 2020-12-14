"""
Funções: - def em Python
"""

# def - estou definindo minha função

def saudacao(mensagem = "Olá", usuario = "Usuário"):
    print('{} {}'.format(mensagem, usuario))


def modifica_nome(algum_nome):
    return algum_nome.upper()


# Início:

nome = input("Entre com um nome: ")
nome_modificado = modifica_nome(nome)
print(nome_modificado)

saudacao("Hello", "Paulo")
saudacao()
