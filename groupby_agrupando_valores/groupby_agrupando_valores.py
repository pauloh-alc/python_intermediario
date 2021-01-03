from itertools import groupby

alunos = [
        {'nome': 'Luiz',     'nota': 'A'},
        {'nome': 'Letícia',  'nota': 'B'},
        {'nome': 'Fabrício', 'nota': 'A'},
        {'nome': 'Rosemary', 'nota': 'C'},
        {'nome': 'Joana',    'nota': 'A'},
        {'nome': 'João',     'nota': 'A'},
        {'nome': 'Eduardo',  'nota': 'C'},
        {'nome': 'André',    'nota': 'C'},
        {'nome': 'Anderson', 'nota': 'B'},
        {'nome': 'José',     'nota': 'A'},
]



ordena = lambda item: item['nota']
alunos.sort(key=ordena)

alunos_agrupados = groupby(alunos, ordena)


for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for alunos in valores_agrupados:
        for nome, nota in alunos.items():
            print(f'{nome} | {nota}')

    print()
            
        
