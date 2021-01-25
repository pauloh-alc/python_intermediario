
def master():

    def slave():
        print('Oi')
    
    # slave()
    return slave

variavel = master() # Agora variável é uma função
variavel()


#.....................................

# Essa é uma função decoradora
def master2(funcao):

    def slave():
        print('Agora eu estou decorada')
        funcao()
    
    return slave
    
#variavel = master2(fala_oi)
#variavel()


@master2
def fala_oi():
    print('Oi')


fala_oi()

# fala_oi()
# ou 
# variavel = fala_oi # Agora variável é uma função
#variavel()

# print(type(variavel))

#......................................



