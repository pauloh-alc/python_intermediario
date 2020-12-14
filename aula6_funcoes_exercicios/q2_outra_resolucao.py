

def mestre(funcao, *args):
    return funcao(*args)
                # passando os argumentos desempacotados


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(mensagem, nome):
    return f'{mensagem} {nome}'


#  Passando minha função fala_oi como argumento da minha função
resultado1 = mestre(fala_oi, 'Paulo')
print(resultado1)

#  Passo saudacao como argumento, e encapsulo Hello e Paulo em args
resultado2 = mestre(saudacao, 'Hello', 'Paulo')
print(resultado2)