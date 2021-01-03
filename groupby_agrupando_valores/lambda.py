
# function = lambda argumentos : expressão

# Exemplo 1:
x = lambda a: a + 10
print(f'{x(10)}\n')


# Exemplo 2:

x = lambda a, b : a + b

print(f'{x(30, 20)}\n')


# Exemplo 3:

x = lambda a, b, c: a + b + c

print(f'{x(10,10,10)}\n')


# Exemplo 4:

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(f'{mydoubler(11)}\n')

# Exemplo 5:

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))



