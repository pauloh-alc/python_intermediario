import vendas.cal_precos
# ou
# from vendas import cal_precos
# ou
# from vendas.cal_precos import aumento, reducao
from vendas.formata import preco as preco2

preco = 49.90
preco_com_aumento = vendas.cal_precos.aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = vendas.cal_precos.reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)


print(preco2.real(30))
print(preco2.real(40))
