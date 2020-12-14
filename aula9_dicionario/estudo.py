
dicionario = {'chave1': 1, 'chave2': 2, 'chave3': 3}
# d1 = {
#     'str': "Valor",
#     123: "Outro valor",
#     (1, 2, 3, 4, 5): "Tupla"
# }
#
# print(dicionario['chave2'])
#
# print(1 in dicionario.values())
# print('chave1' in dicionario.keys())
# print(len(dicionario))


for key, value in dicionario.items():
    print(key, value)



d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1
v[1] = 'Luiz'

print(d1)
print(v)
print(v == d1)

v1 = d1.copy()
v1[1] = 'Paulão'
print(v1)
print(d1)
d1.pop(3)
print(d1)