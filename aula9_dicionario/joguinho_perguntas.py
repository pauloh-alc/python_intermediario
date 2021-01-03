"""
Joguinho de perguntas e respostas
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 3 * 7?',
        'respostas': {
            'a': '14',
            'b': '20',
            'c': '21',
        },
        'resposta_correta': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 40 * 4?',
        'respostas': {
            'a': '160',
            'b': '140',
            'c': '120',
        },
        'resposta_correta': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 12 * 3?',
        'respostas': {
            'a': '123',
            'b': '36',
            'c': '32',
        },
        'resposta_correta': 'b'
    },
}

acertos = 0
porcentagem = 0
for perguntas_k, perguntas_v in perguntas.items():
    print(perguntas_k)
    print(f'\t{perguntas_v["pergunta"]}')
    for dados_pergunta_k, dados_perguntas_v in perguntas_v["respostas"].items():
        print(f'({dados_pergunta_k}): {dados_perguntas_v}')

    resposta = input('Digite a letra correspondente a sua resposta: ')
    if resposta == perguntas_v['resposta_correta']:
        print('Você acertou!')
        acertos += 1
    else:
        print('Você errou!')

    qtd_total = len(perguntas)
    porcentagem = acertos * 100 / qtd_total
print(f'Você acertou {porcentagem} %')






