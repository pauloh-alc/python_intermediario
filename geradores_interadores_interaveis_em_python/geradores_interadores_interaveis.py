import sys
import time

def preenche_lista():
    r = []
    for i in range(100):
        yield i
        time.sleep(0.1)
    return r


lista = preenche_lista()

for valor in lista:
    print(valor)


l1 = [x for x in range(1000)] # Gerado lista
l2 = (x for x in range(1000)) # Gerando lista com gerador, bem menos memória

print(l1)
print(l2)

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

for i in l2:
    print(i)
