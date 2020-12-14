def funcao(n="Usuário", i=0, a=0.0):
    print(f'Nome: {n}\nIdade: {i}\nAltura: {a}')
    return [n, str(i), str(a)]

def main():
    nome = "Paulo"
    idade = 20
    altura = 1.90

    retorno = funcao(nome, idade, altura)
    print(retorno)  # Retorno agora é uma lista
    var = ' '.join(retorno)
    print(var)


if __name__ == '__main__':
    main()

