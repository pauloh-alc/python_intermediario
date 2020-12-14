#funcao2
def ola_mundo():
    return 'Olá mundo'


#funcao1
def mestre(funcao2):
    return funcao2()


retorno = mestre(ola_mundo)
print(retorno)
