tabuleiro = [['*', 'A', 'B', 'C'], ['1', ' ', ' ', ' '], ['2', ' ', ' ', ' '], ['3', ' ', ' ', ' ']]
dicionario = {'A' : 1, 'B' : 2, 'C' : 3}
vetor_X = ['X', 'X', 'X']
vetor_Y = ['O', 'O', 'O']

def imprime_tabuleiro():
    """Imprime o tabuleiro 
    """
    print('-' * 30)
    for linha in range(0, 4):
        for coluna in range(0,4):
            print(f'[{tabuleiro[linha][coluna]}] | ', end=' ')
        print()
    print('-' * 30)

def regras (linha, coluna, peca):
    """Define as regras do jogo, retornando false caso a jogada esteja contra as regras
       Atualiza o tabuleiro poscionando a peça
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

def verifica_vitoria():
    """ Função que verifica se algum jogador venceu, retorna verdadeiro caso tenha vencido
    """
    #verificando linha e coluna
    for linha in range(1, 4):
        vetor_aux = [' ', ' ', ' ']
        vetor_aux_coluna = [' ', ' ', ' ']
        for coluna in range(1, 4):
            vetor_aux[coluna-1] = tabuleiro[linha][coluna]
            vetor_aux_coluna[coluna-1] = tabuleiro[coluna][linha]
        if vetor_aux == vetor_X or vetor_aux == vetor_Y:
            print("Vitória!")
            return True
        if vetor_aux_coluna == vetor_X or vetor_aux_coluna == vetor_Y:
            print("Vitória!")
            return True
    #verificando diagonais
    if tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != ' ':
        print("Vitória!")
        return True
    if tabuleiro[1][3] == tabuleiro[2][2] == tabuleiro[3][1] != ' ':
        print("Vitória!")
        return True

def infomacoes():
    """Informações acerca do jogo
    """
    print('*' * 30)
    print('Versão: 1.0', end='\n')
    print('Autor: Mauro Fidelis Santana Pontes', end='\n')
    print('Data da última atualização: 03/07/2020', end='\n')
    print('Mais informações: https://github.com/maurofidelis/jogo_da_velha')
    print('*' * 30)

def game():
    #Tabuleiro Vazio
    imprime_tabuleiro()
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
            imprime_tabuleiro()
            #O contador define quando é X ou O e so é atualizado qdo a jogada for válida
            if (verifica_vitoria()):
                return False
            cont = cont + 1
        else:
            print("Jogada Inválida")

def main():
    #Menu
    print('*' * 30)
    print('0 - Informações')
    print('1 - Novo Jogo')
    print('2 - Sair')
    print('*' * 30)
    opc = int(input('Selecione a opção desejada: '))   
    
    #Condições do menu
    if opc == 0:
        infomacoes()
    elif opc == 1:
        game()
    elif opc == 2:
        exit()
    else:
        print("Comando Inválido")
        return False
    
main()

    

        





