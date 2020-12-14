"""
Questão 9 -
"""


# Função: ordena uma linha de maneira crescente
def ordenar(lista, limite):
    for i in range(0, limite):
        menor = lista[i]
        pos_menor = i
        for j in range(i, limite):
            if lista[j] < menor:
                menor = lista[j]
                pos_menor = j
        lista[pos_menor] = lista[i]
        lista[i] = menor


# Função: principal
def main():
    v = []
    w = []
    # Preenchendo lista 'v'
    for i in range(0, 4):
        valor_v = int(input(f'v[{i}]: '))
        v.append(valor_v)

    ordenar(v, 4)

    print()

    # Preenchendo lista 'w'
    for i in range(0, 5):
        valor_w = int(input(f'w[{i}]: '))
        w.append(valor_w)

    ordenar(w, 5)

    combinado = v + w
    ordenar(combinado, 4 + 5)
    print(combinado)


if __name__ == '__main__':
    main()
