"""
Dicionário:
"""

d1 = {'chave1': 1, 'chave2': 'valor 2', 'chave3': 'valor 3'}
print(d1)

d1['chave1'] = 'Paulo'  #  Alterando o valor
print(d1)


d2 = {1: 'valor1', 2: 'valor2', 3: 'valor3'}
print(d2)

print(d2[3]) # Acessando valores

dicionario = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}

dicionario['chaveNaoExiste'] = 4

if 'chaveNaoExiste' in dicionario:
    print(dicionario['chaveNaoExiste'])

print(dicionario[(1, 2, 3, 4)])

if dicionario.get('chaveNaoExiste') is not None:
    print(dicionario['chaveNaoExiste'])

