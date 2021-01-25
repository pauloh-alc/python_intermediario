from remove_caracteres_especiais import remover_caracteres_especiais, remover_caracteres
from obtendo_primeiro_digito import primeiro_digito
from obtendo_segundo_digito import segundo_digito
from verifica_sequencia import verifica_se_e_sequencia

cnpj_original = '71.506.168/0001-11'
cnpj = cnpj_original


cnpj = remover_caracteres_especiais(cnpj)


retorno = verifica_se_e_sequencia(cnpj)
if retorno:
    print("cpnj não pode ser uma sequência, entre com outro");
else:

    cnpj = remover_caracteres(cnpj)

    # Gerando primeiro dígito:
    digito1 = primeiro_digito(cnpj)
    cnpj = cnpj + str(digito1);

    # Gerando segundo dígito:
    digito2 = segundo_digito(cnpj)
    cnpj = cnpj + str(digito2)

    # Verificação:
    if cnpj == remover_caracteres_especiais(cnpj_original):
        print('Válido')
    else:
        print('Inválido')

