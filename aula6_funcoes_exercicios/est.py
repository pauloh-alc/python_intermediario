

def soma(*args):
    qtd_args = len(args)
    if qtd_args == 2:
        return n1 + n2
    elif qtd_args == 3:
        return n1 + n2 + n3
    elif bool(args) is False:
        print('A função foi chamada sem argumentos')

n1 = 1
n2 = 2
n3 = 3

soma()
print(soma(n1, n2))
print(soma(n1, n2, n3))

