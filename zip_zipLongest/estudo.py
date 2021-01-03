
lista1 = list(range(0,50,2))
lista2 = list(range(0,50,3))

print(lista1)
print(lista2)

#print(list(zip(lista1, lista2)))

#lista_r = []
#for e1, e2 in zip(lista1, lista2):
#    if e1 % 2 == 0 and e1 % 3 == 0:
#        lista_r.append(e1)
#    elif e2 % 2 == 0 and e2 % 3 == 0:
#        lista_r.append(e2)

#lista_r = set(lista_r)
#print(list(lista_r))



lista_r = [(e1, e2) for e1, e2 in zip(lista1, lista2) if e1 % 2 == 0 and e1 % 3 == 0 if e2 % 2 == 0 and e2 % 3 == 0]
print(lista_r)


lista_n = []
for a, b in lista_r:
    lista_n.append(a)
    lista_n.append(b)

print(lista_n)
