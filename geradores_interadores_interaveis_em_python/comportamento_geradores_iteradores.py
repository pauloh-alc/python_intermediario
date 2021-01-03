# listas, tuples, str --> sequences --> Interável

nome = "Paulo Alencar"
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(iterador))
print(next(iterador))

print("Teremos o for")

for letra in iterador:
    print(letra)

print('#' * 100)

try:

    print(next(iterador))

except:
    pass
