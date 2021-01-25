
def lista_de_clientes(clientes_interavel, lista=None):
    if lista is None:
        lista = []
    
    lista.extend(clientes_interavel)
    return lista

lista_clientes1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes1)
clientes2 = lista_de_clientes(['Luara', 'Davi', 'Pedro'], ['Zico', 'Ronaldinho'])
clientes3 = lista_de_clientes(['Rilda', 'Valério'])


# Output
print(clientes1)
print(clientes2)
print(clientes3)
