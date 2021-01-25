"""
Exercício:........................................

Faça uma lista de 'tarefas' com as seguintes opções:
    # adicionar tarefa
    # listar tarefas
    # opção de desfazer tarefa (a cada vez que chamarmos, desfaz a última ação)
    # opção de refazer  tarefa (a cada vez que chamarmos, refaz a útima ação)

    Ex:

    ['t1', 't2', 't3', ] --> ativo a opcao 'desfazer', fica -->  ['t1', 't2'] --> ativo a opcao 'refazer', fica: ['t1', 't2', 't3']


#................................................
"""

# Função: exibe menu de opções.
def menu():
    print('\n[1] adicionar tarefa\n'
          '[2] listar tarefas  \n'
          '[3] desfazer tarefa \n'
          '[4] refazer tarefa  \n'
          '[5] sair            \n')


# Função: adiciona tarefa específica na lista. 
def adicionar_tarefa(lista):
    tarefa = input('tarefa: ')
    lista.append(tarefa)

# Função: lista todas as tarefas da lista
def listar_tarefas(lista):
    if bool(lista) != False:
        print(lista)
        print()
        for tarefa in lista:
            print(tarefa)
    else:
        print("\nVocê 'desfez' muitas vezes, sua lista está vazia. Você pode 'refazer' !!")


# Função: desfazer a última ação.
def desfazer(lista, lista_copia, qtd):
    if qtd == 0:
        lista_copia.clear()
        for i in lista:
            lista_copia.append(i)
     
    if bool(lista) != False:
        lista.pop()
        qtd += 1
        listar_tarefas(lista)
        return qtd
    return qtd


# Função: reponsávl por refazer a última ação.
def refazer(lista, lista_copia, qtd):
    
    if qtd == 0:
        lista_copia.clear()
        for i in lista:
            lista_copia.append(i)

    tamanho = len(lista)
    if tamanho != len(lista_copia):
        lista.append(lista_copia[tamanho])
        listar_tarefas(lista)
    else:
        print("\nLimite para 'refazer' alcançado !! Mas você pode 'desfazer'")
        listar_tarefas(lista)
    

# Função: principal
def main():
    
    # Dicionário de dados:
    lista = []
    lista_copia = []
    qtd = 0
    
    while True:
        menu()
        op1 = input('opção: ')
        
        # Escolha de opções:
        if op1 == '5':
           op2 = input('sair [s/n]: ')
           if op2 == 's':
               break
        
        if op1 == '1':
            adicionar_tarefa(lista)
            #qtd = 0
        elif op1 == '2':
            listar_tarefas(lista)

        elif op1 == '3':
            qtd = desfazer(lista, lista_copia, qtd)
        
        elif op1 == '4':
            refazer(lista, lista_copia, qtd)


if __name__ == '__main__':
    main()

