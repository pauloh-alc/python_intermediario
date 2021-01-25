from time import time
from time import sleep



# Função: decoradora
def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time   = time()
        tempo = (end_time - start_time) * 1000
        lista.append(tempo)
        print(f'A função {funcao.__name__} levou {tempo}ms para executar.')
        return resultado

    return interna



@velocidade # <--- decorador, estou decorando demora()
def demora_On(lista):
    for i in range(10):
        pass   
        
lista = []
demora_On(lista) # chamando funcao decorada

@velocidade
def demora_On_n(lista):
    for i in range(10):
        for j in range(10):
            pass

demora_On_n(lista)
print(lista)
print(f'Diferenca = {lista[1] - lista[0]}')
