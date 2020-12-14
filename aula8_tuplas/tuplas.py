"""
Tuplas - imultável, depois que eu criei, não posso mais modificar
"""

tupla1 = (1, 2, 3, 'a', 'Luíz Otávio')
tupla2 = 1, 2, 3, 4
print(type(tupla1))

print(tupla1[-1])

print(tupla1[2:])

print(tupla2)


t = tupla1 + tupla2
print(t)