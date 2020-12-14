"""
Funções (def) em python - return
"""

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2


def dumb():
    return [1, 2, 3, 4, 5, 6]



#---------------------------

resultado = divisao(8, 2)

if resultado:
    print(resultado)
else:
    print('Conta inválida')

print(dumb(), type(dumb()))