def verifica_se_e_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    
    if cnpj == sequencia:
        return 1
    else:
        return 0


