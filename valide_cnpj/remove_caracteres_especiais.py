def remover_caracteres_especiais(cnpj):
    cnpj = cnpj.replace('.','');
    cnpj = cnpj.replace('-','');
    cnpj = cnpj.replace('/','');
    return cnpj

def remover_caracteres(cnpj):
    cnpj = cnpj[:-2]
    return cnpj
