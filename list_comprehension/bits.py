"""

Objetivo:
Dada uma cadeia de bits, separe em bloquinhos de 8 bits = 1byte, convertendo cada
bloquinho para seu respectivo número em decimal.

"""

# Função: pega uma cadeia de bits e retorna uma lista onde cada elemento
# é um bloquinho de 8 bits = 1 byte.
def separa_bits_em_1_byte(bits):
    lista_de_bytes = []
    aux = 0
    for i in range(8, len(bits), 8):
        lista_de_bytes.append(bits[aux:i])
        aux = i

    return lista_de_bytes

# Função: converte cada elemento da lista de bytes para seu
# respectivo número em decimal.
def converte_bytes_para_decimal(lista_de_bytes):
    lista_de_decimais = []
    for byte in lista_de_bytes:
        byte = byte[7::-1]

        base2 = 1
        decimal = 0
        for bit in byte:
            if bit == '1':
                decimal = decimal + base2

            base2 = base2 * 2
        lista_de_decimais.append(decimal)

    return lista_de_decimais

# Função: principal
def main():

    bits = '010010100111010101010101110101010000101100111101010100101111010101010100010101010100110101'
    lista_de_bytes = separa_bits_em_1_byte(bits)
    lista_de_decimais = converte_bytes_para_decimal(lista_de_bytes)
    print(lista_de_decimais)


if __name__ == '__main__':
    main()
