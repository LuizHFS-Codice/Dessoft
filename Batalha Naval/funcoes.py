# Questão 1 (feita dia 21/10)
def define_posicoes(Lin,Col,Ori,Tam):
    lf=[]
    Cont=0
    Lis_Pos=0
    #
    if Ori=='horizontal':
        for i in range(Tam):
            Cont=Col+i
            Lis_Pos=[Lin,Cont]
            lf.append(Lis_Pos)
        Cont=0
        #######################
    else:
        Lis_Cont=range(Lin,Tam+1)
        for i in range(Tam):
            Cont=Lin+i
            Lis_Pos=[Cont,Col]
            lf.append(Lis_Pos)
        ###
    return lf

#------------------------------------------------------------------------------------
# Questão 2 (feita dia 22/10)
def preenche_frota(frota, nome_navio, Lin, Col, Ori,Tam):

    posicoes_navio = define_posicoes(Lin,Col, Ori, Tam)


    if nome_navio in frota:
        frota[nome_navio].append(posicoes_navio)
    else: 
        frota[nome_navio] = [posicoes_navio]
    
    return frota 

# frota = {}
# nome_navio = "navio-tanque"
# Lin = 6
# Col = 1
# Ori = "horizontal"
# Tam = 3

# resultado = preenche_frota(frota,nome_navio, Lin, Col, Ori, Tam)
# print(resultado)
#---------------------------------------------------------------------------------

# Questão 3 (feita dia 23/10)


def faz_jogada(tabuleiro, Lin, Col):

    # verificando  a posicao no tabuleiro com condiconais 
    if tabuleiro[Lin][Col] == 1:
        tabuleiro[Lin][Col] = 'X' #Ou seja, acertou alguma coisa (obs : usar "X")
    else:
         tabuleiro[Lin][Col] = '-' #errou e não acertou ninguém 
    
    return tabuleiro

# # teste:

# from pprint import  pprint

# tabuleiro = [
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
#   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#   [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# ]

# linha = 1
# coluna = 1
# # resultado = faz_jogada(tabuleiro, linha, coluna)
# # print(resultado)

# tabuleiro = faz_jogada(tabuleiro, 1, 1)

# pprint(tabuleiro)

# Questão 4 (feita dia 24/10)

#   1) iniciar o tabuleiro como uma lista de 10 por 10, sendo todos os valores 0
#       2) para cada navio no dicionário da minha frota eu tenho que percorrer esse dicionário onde está suas posições e marcar como 1 no tabuleiro 
#           3) Dar um return para ter esse tabuleiro preenchido

def posiciona_frota(frota):
    # entender como usar "place holder"
    tabuleiro = [] # começar vazio pq meu tabuleiro está somente com "0"

    for i in range (10):
        linha = [0*10] # são 10 
        tabuleiro.append(linha)

    #para conseguir percorrer o dicionario com a minha frota 

    for posicoes in frota.values():
        for posicao in posicoes:
            for linha, coluna in posicoes:
                tabuleiro[linha][coluna] =1
    
    return tabuleiro 