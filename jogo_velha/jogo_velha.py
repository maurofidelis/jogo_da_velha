tabuleiro = [['*', 'A', 'B', 'C'], [1, ' ', ' ', ' '], [2, ' ', ' ', ' '], [3, ' ', ' ', ' ']]

def tabuleiro_vazio():
    print('-' * 30)
    for linha in range(0, 4):
        for coluna in range(0,4):
            print(f'[{tabuleiro[linha][coluna]}] | ', end=' ')
        print()
    print('-' * 30)

def imprime_tabuleiro (lin, col, peca):
    """
    Imprime o tabuleiro e vai atualizando a cada jogada
    """
    print('-' * 30)
    for linha in range(0, 4):
        for coluna in range(0, 4):
            # Definindo a coluna que a peça vai ser posicionada
            if tabuleiro[linha][coluna] == col:
                pos_col = coluna
            #Posicionando a peça
            if linha == int(lin) and coluna == pos_col:
                tabuleiro[linha][coluna] = peca
                print(f'[{tabuleiro[linha][coluna]}] | ', end=' ')
            #Se não estiver na posição da peça continua imprimindo o tabuleiro
            else:
                print(f'[{tabuleiro[linha][coluna]}] | ', end=' ')
        print()
    print('-' * 30)

def main():
    #Menu


    #Tabuleiro Vazio
    tabuleiro_vazio()

    cont = 1
    while (True):
        if cont % 2 == 0:
            peca = 'O'
        else:
            peca = 'X'
        jogada =(input('Seleciona a jogada: ')).upper()
        lin = jogada[1]
        col = jogada[0]
        imprime_tabuleiro(lin, col, peca)
        # Definir condição de parada
        cont = cont + 1

main()
    


        





