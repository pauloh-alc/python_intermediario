"""
Questão 2 -
"""


def converte_em_minutos(h=0, m=0, s=0):
    h = h * 60 * 60
    m = m * 60
    segundos_total = h + m + s

    return segundos_total


hora = int(input("Entre com uma hora: "))
minutos = int(input("Entre com os minutos: "))
segundos = int(input("Entre com os segundos: "))


resultado = converte_em_minutos(hora, minutos, segundos)
print(f"O total de segundos é: {resultado}s")
