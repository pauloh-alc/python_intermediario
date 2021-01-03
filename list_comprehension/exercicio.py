
string = '0123456789012345678901234567890123456789012345678901234567890123456789'
#
# n = 10
#
# lista = [string[i:i+10] for i in range(0, len(string), n)]
# print(lista)



lista = [string[i:i+10] for i in range(0, len(string), 10)]
print(lista)

bits = "0101010101010010000000111011100100101010111111011011111110101"

bytes = [bits[i:i+8] for i in range(0, len(bits), 8)]
print(bytes)





