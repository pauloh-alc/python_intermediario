



def imprimir(msg):
    print(msg)


def retornando_outra_funcao():
    return imprimir('Hello World !!')


retornando_outra_funcao()



def retorna():
    return imprimir


new_funcao = retorna()

new_funcao('Olá Paulo !!')
new_funcao('Seja bem vindo !!')
