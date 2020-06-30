tabuleiro = [['*', 'A', 'B', 'C'], [1, ' ', ' ', ' '], [2, ' ', ' ', ' '], [3, ' ', ' ', ' ']]
dicionario = {'A' : 1, 'B' : 2, 'C' : 3}

def tabuleiro_vazio():
    print('-' * 30)
    for linha in range(0, 4):
        for coluna in range(0,4):
            print(f'[{tabuleiro[linha][coluna]}] | ', end=' ')
        print()
    print('-' * 30)

def regras (linha, coluna, peca):
    """Define as regras do jogo, retornando false caso a jogada esteja contra as regras
    >>> Selecione a jogada: a0
    False
    """
    #Coluna informada é inválida
    if coluna != 'A' and coluna != 'B' and coluna != 'C':
        return False     
    #linha informada é inválida
    elif linha != '1' and linha != '2' and linha != '3':
        return False
    #posição já tem uma peça
    elif tabuleiro[int(linha)][dicionario[coluna]] != ' ':
        return False
    else:
        #preenche tabuleiro coma peça passada
        tabuleiro[int(linha)][dicionario[coluna]] = peca
        return True

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
        if (regras(lin, col, peca)):
            tabuleiro_vazio()
            #O contador define quando é X ou O e so é atualizado qdo a jogada for válida
            cont = cont + 1
        else:
            print("Jogada Inválida")
       
main()
    

        





