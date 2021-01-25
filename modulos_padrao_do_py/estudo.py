
import random
# ou
# from random import randint
# from random import randint as numero_pseudo_aleatorio

numero_magico = random.randint(0, 10)

numero_usuario = input("Digite um número no intervalor [0 - 10]: ")

try:
    numero_usuario = int(numero_usuario)
    if numero_usuario == numero_magico:
        print("Acertou !!")
    else:
        print("Errou !!")
except ValueError:
    print("Erro: o que você digitou não é um numero [0 - 10]")



lista = ['Paulo', 'Gabriel', 'Luan', 'Teixeira', 'Rafael', 'Manoel', 'Leonam', 'Fhelipe']

print(random.choice(lista))
