"""
 Dicionário de alunos:
"""


# alunos = {
#     1: {
#         'Nome': "Paulo",
#         'Sobrenome': "Alencar",
#         'Matrícula': 494837,
#         'coeficiente': 9.6,
#     },
#     2: {
#         'Nome': "Paulo",
#         'Sobrenome': "Alencar",
#         'Matrícula': 494837,
#         'coeficiente': 9.6,
#     },
#     3: {
#         'Nome': "Paulo",
#         'Sobrenome': "Alencar",
#         'Matrícula': 494837,
#         'coeficiente': 9.6,
#     },
#     4: {
#         'Nome': "Paulo",
#         'Sobrenome': "Alencar",
#         'Matrícula': 494837,
#         'coeficiente': 9.6,
#     },
# }
#
# print(alunos[1]['Nome'])
#
#
# for i, dados in alunos.items():
#     print(i)
#     for j, informacoes in dados.items():
#         print(f'\t{j}: {informacoes}')

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': "Paulo",
        'sobrenome': "Alencar",
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}: {dados_v}')