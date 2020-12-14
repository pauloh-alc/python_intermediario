print('Texto explicativo')
print()
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}

repostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'\t[{rk}]{rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Ehhhhh !! Você acertou')
        repostas_certas += 1
    else:
        print('Ixiiii !! Você errou')
    print()
qtd_perguntas = len(perguntas)
porcentagem_acerto = repostas_certas * 100 / qtd_perguntas

print(f'Você acertou {porcentagem_acerto} %')