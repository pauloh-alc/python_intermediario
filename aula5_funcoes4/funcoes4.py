var_global = 'valor_global'  # GLOBAL


def funcao():
    print(var_global)



def funcao2():
    print(var_global)


def funcao3(): 
    var_local = 'valor_local'  # LOCAL


funcao()
print(var_local)  # Gera Erro. Pois var_local só é vista no escopo da funcao3()