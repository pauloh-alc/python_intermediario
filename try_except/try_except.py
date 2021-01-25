
try: # Tenta executar, se por acaso tivermos algum erro, vamos para --> except
    a = {}
    print(a)
    a / 0
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave');    
except Exception as erro:
    print('Ocorre um erro inesparado.')
else: # Só executa se não encontrar nenhum erro
    print("Seu bloco foi executado com sucesso")
finally: # Sempre é executada
    print('Finalmente')










print("Vamos continuar")
