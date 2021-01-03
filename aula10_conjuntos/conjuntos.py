"""
Sets - conjuntos:

add (adicionar), update (atualiza), clear, discard
union | ( une )

# intersection & (Todos os elementos presentes nos dois sets)
# difference - elementos apenas no set da esquerda
# symmetric_difference ^(elementos que estão nos dois sets, mas não em ambos)
"""

s1 = {1, 2, 3, 4, 5, 6}  # suportam somente elementos imutáveis
print(s1)
for v in s1:
    print(v)

s2 = set()
s2.add(1)
s2.add(2)
print(s2)
s2.discard(2)
print(s2)
s2.update([1, 2, 3, 4, 5, 6, 7])
print(s2)


conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8}
# União:
conjunto_uniao = conjunto1 | conjunto2
print(conjunto_uniao)

# Intersection
conjunto_int = conjunto1 & conjunto2
print(conjunto_int)