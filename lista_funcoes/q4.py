"""
Questão 4 -
"""


# Função: exibe os erros
def erros(mensagem):
    print(f"Erro: {mensagem} !!")


# Função: determina se os valores passados como argumentos formam um triângulo
def define_se_e_triangulo(lado1, lado2, lado3):
    if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado2 + lado1:
        return 0
    return 1


# Função: determina qual o triângulo formado pelos valores passados como argumento
def determina_o_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return 0
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return 1
    else:
        return 2


# Início:
while True:
    l1 = input("L1: ")
    l2 = input("L2: ")
    l3 = input("L3: ")

    if not l1.isdecimal() or not l2.isdecimal() or not l3.isdecimal():
        erros("proibido digitar letras ou caracteres especiais, você precisa degitar valores número positivos")
        continue
    if l1 == 0 or l2 == 0 or l3 == 0:
        continue

    l1 = int(l1)
    l2 = int(l2)
    l3 = int(l3)

    if define_se_e_triangulo(l1, l2, l3):
        retorno = determina_o_triangulo(l1, l2, l3)

        if retorno == 0:
            print('Triângulo Equilátero !!')
        elif retorno == 1:
            print('Triângulo Escaleno !!')
        else:
            print('Triângulo Isosceles !!')
    else:
        erros("Números digitados não corresponde a um triângulo")
