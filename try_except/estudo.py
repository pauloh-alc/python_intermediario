

#def divide(n1, n2):
#    if n2 == 0:
#        raise ValueError("n2 não pode ser 0")
#    return n1 / n2
#
#
#try:
#    print(divide(4,0))
#except ValueError as messageError:
#    print(messageError)


def converter(numero):
    try:
        numero = int(numero)
        return numero
    except ValueError:
        try:
            numero = float(numero)
            return numero
        except ValueError:
            return None

x, y = input().split();


x = converter(x)
y = converter(y)

if x is not None and y is not None:
    resultado = x * y
    print(resultado)
else:
    print("Error: you typed something wrong !!")
