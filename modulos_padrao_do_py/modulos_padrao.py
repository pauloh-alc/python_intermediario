# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidade padrão da linguagem.



# import random
# ou
from random import randint as randint_original

def randint(*args):
    print(args[0])
    return "Hahaha"

for i in range(10):
    print(randint_original(0,10))


print(randint(2,3,4,5))


# para instalar algum módulo:

no terminal execute: pip install <nome_do_modulo>
