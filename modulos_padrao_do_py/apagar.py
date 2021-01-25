# gera 'n' numeros primos:

def gera_primos(n):
    numeros_primos = []
    cont = 0
    x = 1
    while cont < n:
        div = 0
        for i in range(1, x + 1):
            if x % i == 0:
                div += 1
        if div == 2:
            numeros_primos.append(x)
            cont += 1
        x += 1

    return numeros_primos


