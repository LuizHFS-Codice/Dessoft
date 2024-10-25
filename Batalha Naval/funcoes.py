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

# Questão 4 (Começada dia 24/10, terminada 25/10)

#   1) iniciar o tabuleiro como uma lista de 10 por 10, sendo todos os valores 0
#       2) para cada navio no dicionário da minha frota eu tenho que percorrer esse dicionário onde está suas posições e marcar como 1 no tabuleiro 
#           3) Dar um return para ter esse tabuleiro preenchido

def posiciona_frota(frota):
    # entender como usar "place holder"
    tabuleiro = [([0]*10) for _ in range(10)] # Listas de Listas 0 para posicionar as frotas (diferente de uma multiplicação de listas de listas, desse jeito, cada lista se torna um elemento independente)

    #para conseguir percorrer o dicionario com a minha frota 

    for posicoes in frota.values():#Acesso ao dicionário
        for posicao in posicoes:#Primeira Camada de Lista
            for Coords in posicao: #Segunda Camada de Lista
                tabuleiro[Coords[0]][Coords[1]]=1 #Coordenadas das embarcações
    
    return tabuleiro 
#--------------------------------------------------------------------------
#Questão 4 Idéia substituida do primeiro tabuleiro
# def posiciona_frota(Frota):
#     Tab=[
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),
#         ([0]*10),        
#     ]
#     return Tab
#Teste-----------------------------------------------------------------
# frota = {
#     "porta-aviões":[
#       [[1,5],[1,6],[1,7],[1,8]]
#     ],
#     "navio-tanque":[
#       [[6,1],[6,2],[6,3]],
#       [[4,7],[5,7],[6,7]]
#     ],
#     "contratorpedeiro":[
#       [[1,1],[2,1]],
#       [[2,3],[3,3]],
#       [[9,1],[9,2]]
#     ],
#     "submarino": [
#       [[0,3]],
#       [[4,5]],
#       [[8,9]],
#       [[8,4]]
#     ],
# }
# resultado = posiciona_frota(frota)
# print(resultado)
#Teste-----------------------------------------------------------------
# Questão 5 (Começada em 25/10)
def afundados (frota,Tabuleiro):
    Afundados=0#Afundados
    Cont=0
    for Embarcação,Lista1 in frota.items():
        for Lista2 in Lista1:
            for Lista3 in Lista2:
                if Tabuleiro[Lista3[0]][Lista3[1]] == 'X':
                    Cont+=1
                if Cont==len(Lista2):
                    Afundados+=1
            Cont=0
    return Afundados

# frota = {
#     "porta-aviões":[
#       [[1,5],[1,6],[1,7],[1,8]]
#     ],
#     "navio-tanque":[
#       [[6,1],[6,2],[6,3]],
#       [[4,7],[5,7],[6,7]]
#     ],
#     "contratorpedeiro":[
#       [[1,1],[2,1]],
#       [[2,3],[3,3]],
#       [[9,1],[9,2]]
#     ],
#     "submarino": [
#       [[0,3]],
#       [[4,5]],
#       [[8,9]],
#       [[8,4]]
#     ],
# }
# tabuleiro = [
#   [0, '-', '-', 1, 0, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
#   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, '-', '-', '-', '-', 0, 0],
#   [0, '-', 0, 0, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, '-', 0, 0, 1, 0, 0],
#   [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 'X', 0, 0, 0, 0, 1],
#   [0, 1, 1, '-', '-', '-', '-', '-', '-', '-']
# ]
# resultado = afundados(frota, tabuleiro)
# print(resultado)



# ------------------------------------------------------------------------------------------------------
# Questão 6 (Começada em 25/10) Feita por Antonio


#  a aposicao devem estar dentro dos limites do tabuileiro que é 10 x 10
#  o lugar que um novo navio ocipar não pode ser o mesmo que as já ocupadas pelos outros navios 
def posicao_valida(frota,Lin, Col, orientacao, tamanho):

    # saber onde os navios já estão
    posicoes = define_posicoes(Lin, Col, orientacao, tamanho)

    for posicao in posicoes  :

        Lin, Col = posicao
        
        #lembrando que tem que tá dentro do intervalo de 10 por 10

        if Lin < 0 or Lin >= 10 or Col < 0 or Col >= 10:
            return False

    
    for navio, posicoes_ocupadas in frota.items():
        for lista_posicoes in posicoes_ocupadas:
            for pos_ocupada in lista_posicoes:
                if pos_ocupada in posicoes:
                    return False         #Piramide de for kkkkkkkk (anotar isso, deu certo)
    
    return True


# # teste 

# frota = {
#     "navio-tanque":[
#       [[6,1],[6,2],[6,3]],
#       [[4,7],[5,7],[6,7]]
#     ],
#     "contratorpedeiro":[
#       [[1,1],[2,1]],
#       [[2,3],[3,3]],
#       [[9,1],[9,2]]
#     ],
#     "submarino": [
#       [[0,3]],
#       [[4,5]],
#       [[8,9]],
#       [[8,4]]
#     ],
# }
# linha = 6
# coluna = 2
# orientacao = 'horizontal'
# tamanho = 4
# resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
# print(resultado)

# frota = {
#     "navio-tanque":[
#       [[6,1],[6,2],[6,3]],
#       [[4,7],[5,7],[6,7]]
#     ],
#     "contratorpedeiro":[
#       [[1,1],[2,1]],
#       [[2,3],[3,3]],
#       [[9,1],[9,2]]
#     ],
#     "submarino": [
#       [[0,3]],
#       [[4,5]],
#       [[8,9]],
#       [[8,4]]
#     ],
# }
# linha = 1
# coluna = 5
# orientacao = 'horizontal'
# tamanho = 4
# resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
# print(resultado)


# frota = {
#     "navio-tanque":[
#       [[6,1],[6,2],[6,3]],
#       [[4,7],[5,7],[6,7]]
#     ],
#     "contratorpedeiro":[
#       [[1,1],[2,1]],
#       [[2,3],[3,3]],
#       [[9,1],[9,2]]
#     ],
#     "submarino": [
#       [[0,3]],
#       [[4,5]],
#       [[8,9]],
#       [[8,4]]
#     ],
# }
# linha = 8
# coluna = 8
# orientacao = 'horizontal'
# tamanho = 4
# resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
# print(resultado)



# ------------------------------------------------------------------------------------------------------