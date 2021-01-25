


# funcao decoradora
def master(funcao):
    
    def slave(*args, **kargs):
        print('Agora estou decorada')
        funcao(*args, **kargs)
    
    return slave


# A funcao fala_oi() agora está 'decorada'

@master # decorador
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)

outra_funcao('Ola eu sou Paulo')
















