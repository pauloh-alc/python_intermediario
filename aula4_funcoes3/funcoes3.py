"""
Funções (def) em python - *args **kwargs
"""


def func(*args):  # Os argumentos estão empacotados
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    # Não posso alterar  elemento de uma tupla

    args = list(args)
    args[0] = 100
    print(args)

func(1, 2, 3, 4, 5)

lista = [1, 2, 3, 4, 5]
print(*lista)  # desempacotando lista


def funcao(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Argumento idade não passado')

listinha = [1, 2, 3, 4, 5]
funcao(listinha)

funcao(*listinha, 6, 7, 8, 9, nome='Paulo', sobrenome='Alencar')