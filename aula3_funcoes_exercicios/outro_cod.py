def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'Fizz, {n} é divisível por 3 e 5'
    elif n % 5 == 0:
        return f'Buzz, {n} é divisível por 5'
    elif n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    return n


# Do módulo random, importei randint
from random import randint
for i in range(0, 100):
    aleatorio = randint(0, 100)  # Números aleátórios entre [0 - 100]
    print(fb(aleatorio))
