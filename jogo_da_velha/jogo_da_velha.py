
def menu():
    print('\n[J] Jogar')
    print('[S] Sair')

# Função: responsável por desenhar o tabuleiro do jogo da velha
def desenhar_tabuleiro(tabueiro):
    print('    0    1   2')
    print(f'0:  {tabueiro[0][0]} | {tabueiro[0][1]}  | {tabueiro[0][2]}')
    print('   ---+----+---')
    print(f'1:  {tabueiro[1][0]} | {tabueiro[1][1]}  | {tabueiro[1][2]}')
    print('   ---+----+---')
    print(f'2:  {tabueiro[2][0]} | {tabueiro[2][1]}  | {tabueiro[2][2]}')

# Função: reponsável por verificar linhas, colunas, diagonal principal e  diagonal secundária
# em busca de um ganhador
def verificando_ganhador(tabuleiro):

    diagonal_p_x = 0
    diagonal_p_o = 0
    diagonal_s_x = 0
    diagonal_s_o = 0

    for i in range(0, 3):
        linha_x = 0
        linha_o = 0

        coluna_x = 0
        coluna_o = 0
        for j in range(0, 3):
            # Verificando linhas:
            if tabuleiro[i][j] == 'X':
                linha_x += 1
            elif tabuleiro[i][j] == 'O':
                linha_o += 1

            # Verificando colunas:
            if tabuleiro[j][i] == 'X':
                coluna_x += 1
            elif tabuleiro[j][i] == 'O':
                coluna_o += 1

            # Verificando diagonal principal
            if i == j:
                if tabuleiro[i][j] == 'X':
                    diagonal_p_x += 1
                elif tabuleiro[i][j] == 'O':
                    diagonal_p_o += 1

            # Verificando diagonal secundária
            if i + j == 2:
                if tabuleiro[i][j] == 'X':
                    diagonal_s_x += 1
                elif tabuleiro[i][j] == 'O':
                    diagonal_s_o += 1

        if linha_x == 3 or coluna_x == 3 or diagonal_p_x == 3 or diagonal_s_x == 3:
            return 1 # Jogador 1 [X] ganhador
        elif linha_o == 3 or coluna_o == 3 or diagonal_p_o == 3 or diagonal_s_o == 3:
            return 2 # Jogador 2 [O] ganhador


# Função principal
def main():
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    print('Jogo da velha', end='\n')
    desenhar_tabuleiro(tabuleiro)
    qtd_jogadas = 0
    jogador = '1 [X]'
    while True:
        if qtd_jogadas == 0:
            menu()
            opcao = input('Entre com um opção: ')
            if opcao.lower() == 's':
                break

        # Entrado com a coordenada
        x, y = input(f'Jogador {jogador} entre com coordenada (x,y): ').split(',')
        x = int(x)
        y = int(y)

        if jogador == '1 [X]':
            if x < 0 or x >= 3 or y < 0 or y >= 3:
                continue
            if tabuleiro[x][y] == 'X' or tabuleiro[x][y] == 'O':
                continue
            tabuleiro[x][y] = 'X'
            desenhar_tabuleiro(tabuleiro)
        # jogador 2
        else:
            if x < 0 or x >= 3 or y < 0 or y >= 3:
                continue
            if tabuleiro[x][y] == 'X' or tabuleiro[x][y] == 'O':
                continue
            tabuleiro[x][y] = 'O'
            desenhar_tabuleiro(tabuleiro)

        retorno = verificando_ganhador(tabuleiro)

        if retorno == 1:
            print('Jogador 1 [X] ganhou !!')
            break
        elif retorno == 2:
            print('Jogador 2 [O] ganhou !!')
            break

        # Alterna os jogadores
        if jogador == '1 [X]':
            jogador = '2 [O]'
        else:
            jogador = '1 [X]'

        qtd_jogadas += 1

        if qtd_jogadas == 9:
            print('Deu velha !!')
            qtd_jogadas = 0
            break


if __name__ == '__main__':
    main()


# def desenhar_tabuleiro(tabuleiro):
#     for i in range(0, 3):
#         for j in range(0, 3):
#             print(f' {tabuleiro[i][j]} ', end='')
#             if j == 0 or j == 1:
#                 print('|', end='')
#         print(end='\n')
#         if i != 2:
#             print('---+---+---', end='\n')