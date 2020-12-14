"""
1 - Crie uma função1 que recebe uma função2 como parâmetro
    e retorne o valor da função2 executada
"""

# funcao1
def imprime(funcao2):
    return funcao2()


#funcao2
def preenche_lista():
    lista = []
    for i in range(0, 5):
        valor = int(input(f"Valor {i}: "))
        lista.append(valor)
    return lista


def main():
    retorno = imprime(preenche_lista)
    print(retorno)


if __name__ == '__main__':
    main()



