"""
Questão 6 -
"""


# Calcula a média de salário entre os habitantes:
def media_dos_salarios(lista_salarios):
    return sum(lista_salarios) / 5


# Função: devolve a menor idade encontrada na lista junto com sua posição
def menor_idade(lista_idades):
    idade_menor = min(lista_idades)
    pos_menor   = lista_idades.index(idade_menor)
    return idade_menor, pos_menor


# Função: devolve a maior idade encontrada na lista junto com sua posição
def maior_idade(lista_idades):
    idade_maior = max(lista_idades)
    pos_maior   = lista_idades.index(idade_maior)
    return idade_maior, pos_maior


# Função: responsável por retornar a quantidade de mulheres com três filhos que recebem até R$ 500,00
def qtd_mulheres(lista_sexos, lista_numero_filhos, lista_salarios):
    i   = 0
    qtd = 0
    while i < 15:
        if lista_sexos[i] == 'f' and lista_numero_filhos[i] == 3 and lista_salarios[i] <= 500:
            qtd += 1
        i += 1
    return qtd


# Função: principal
def main():

    lista_nomes = []
    lista_idades = []
    lista_sexo = []
    lista_salarios = []
    lista_numero_filhos = []

    for i in range(0, 2):
        nome = input(f"P{i + 1}.Nome: ")
        idade = int(input(f"P{i + 1}.Idade: "))
        sexo = input(f"P{i + 1}.Sexo (m ou f): ")
        salario = float(input(f"P{i + 1}.Salário: "))
        numero_filhos = int(input(f"P{i + 1}.Número de Filhos: "))
        print(end='\n')

        lista_nomes.append(nome)
        lista_idades.append(idade)
        lista_sexo.append(sexo.lower())
        lista_salarios.append(salario)
        lista_numero_filhos.append(numero_filhos)

    media             = media_dos_salarios(lista_salarios)
    informacoes_maior = maior_idade(lista_idades)
    informacoes_menor = menor_idade(lista_idades)

    idade_maior = informacoes_maior[0]
    pos_maior   = informacoes_maior[1]

    idade_menor = informacoes_menor[0]
    pos_menor   = informacoes_menor[1]

    print(f'A média de salário entre os habitantes é: {media}')
    print(f'A maior idade pertence a (nome: {lista_nomes[pos_maior]}, sexo: {lista_sexo[pos_maior]}, idade: {lista_idades[pos_maior]})')
    print(f'A menor idade pertence a (nome: {lista_nomes[pos_menor]}, sexo: {lista_sexo[pos_menor]}, idade: {lista_idades[pos_menor]})')


if __name__ == '__main__':
    main()
