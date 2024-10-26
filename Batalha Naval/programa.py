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
        ListNavios=[]
        print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
        Lin=int(input("Linha escolhida> "))
        Col=int(input("Coluna Escolhida> "))
        Ori='vertical'
        Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
#----------------------------------------------------------------------------------------------------
        if Check1 == False: 
                while Check1 != True: #Caso não seja uma posição valida
                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
                    Lin=int(input("Linha escolhida> "))
                    Col=int(input("Coluna Escolhida> "))
                    Ori='vertical'
                    Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
        else:
            Pos=define_posicoes(Lin,Col,Ori,tamanho) #Posição da Embarcação
            ListNavios.append(Pos)
#---------------------------------------------------------------------------------------------------------
        frota[Embarc]+=ListNavios #Colocando a posição da embarcação dentro da Frota
    if tamanho>1:
        ListNavios=[]
        print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
        Lin=int(input("Linha escolhida> "))
        Col=int(input("Coluna Escolhida> "))
        Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
        if Ori==1:
            Ori='vertical'
        else:
            Ori='horizontal'
        Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
#----------------------------------------------------------------------------------------------------------
        if Check1 == False: 
            while Check1 != True: #Caso não seja uma posição valida
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {tamanho}')
                Lin=int(input("Linha escolhida> "))
                Col=int(input("Coluna Escolhida> "))
                Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                if Ori==1:
                    Ori='vertical'
                else:
                    Ori='horizontal'
                Check1=posicao_valida(frota,Lin,Col,Ori,tamanho)
        else:
            Pos=define_posicoes(Lin,Col,Ori,tamanho) #Posição da Embarcação
            ListNavios.append(Pos)
            frota[Embarc]+=ListNavios #Colocando a posição da embarcação dentro da Frota
#-----------------------------------------------------------------------------------------------------------
print(frota)