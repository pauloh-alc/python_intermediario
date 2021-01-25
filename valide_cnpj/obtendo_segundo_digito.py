def segundo_digito(cnpj):
    cont1 = 6
    cont2 = 9
    soma = 0
    for i, j in enumerate(cnpj):
        if i < 5:
            soma = soma + cont1 * int(j)
            cont1 -= 1
        else:
            soma = soma + cont2 * int(j)
            cont2 -= 1

    formula = 11 - (soma % 11)

    if formula <= 9:
        return formula
    else:
        return 0


