#Jogo
#Funções para rodar o jogo-----------
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida
#------------------------------------
#Condições Iniciais------------------
tamanhos=[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
Embarcacoes=['submarino','contratorpedeiro','navio-tanque','porta-aviões'] #Lista de Embarcações
Pos=0
Lin=0
Col=0
Ori=0
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }
ListNavios=[]
#-----------------------------------
#loop de for para cada tamanho
for tamanho in tamanhos:
    if tamanho==4:
        Embarc=Embarcacoes[3] #Porta Avião
    elif tamanho==3:
        Embarc=Embarcacoes[2] #Navio Tanque
    elif tamanho==2:
        Embarc=Embarcacoes[1] #Contra Torpedeiro
    elif tamanho==1:
        Embarc=Embarcacoes[0] #Submarino
#Posição X,Y
#---------------------------------------------------------------------------------------------------------
    ListNavios=[]
    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
    Lin=int(input("Linha escolhida> "))
    Col=int(input("Coluna Escolhida> "))
#Orientação
#---------------------------------------------------------------------------------------------------------
    if tamanho>1:
        Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
        if Ori==1:
            Ori='vertical'
        else:
            Ori='horizontal'
    else:
        Ori='vertical'
    Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
#Checagem
#----------------------------------------------------------------------------------------------------------
    if Check1 == False: 
        while Check1 != True: #Caso não seja uma posição valida
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
            Lin=int(input("Linha escolhida> "))
            Col=int(input("Coluna Escolhida> "))
            if tamanho>1:
                Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                if Ori==1:
                    Ori='vertical'
                else:
                    Ori='horizontal'
            else:
                Ori='vertical'
            Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
    else:
        Pos=define_posicoes(Lin,Col,Ori,tamanho) #Posição da Embarcação
        ListNavios.append(Pos)
        frota[Embarc]+=ListNavios #Colocando a posição da embarcação dentro da Frota
#-----------------------------------------------------------------------------------------------------------
print(frota)

# sugestão de melhora pra simplificar de forma que ao invés de ter um bloco só 
# pro submarino, usar um if dentro do bloco que já temos para determinar a orientacao

# Tentativa 1:

# def obter_input_valido(Embarc, tamnho):
#     while True:

#         print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')

#         Lin = int(input("Linha escolhida>"))
#         Col = int(input('Coluna Escolhida>'))

#         # automaticamnte saber a orientacao para o submarino

#         if tamnho == 1:
#             Ori = "vertical"

#         else:

#             Ori = int(input('Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> '))
#             Ori = "vertical" if Ori == 1 else "horizontal"

#         if posicao_valida(frota, Lin, Col, Ori, tamnho):
#             return Lin, Col, Ori
        
#         else:

#             print("Esta posição não está válida!")


