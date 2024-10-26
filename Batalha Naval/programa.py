#Jogo
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida

Tam=4 #Tamanho do Navio
Embarcacoes=['submarino','contratorpedeiro','navio-tanque','porta-aviões']#Lista de Embarcações
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
contagem=0
ListNavios=[]

 # nosso loop pra posicionar as embarcações do jogo ( todas elas)
while Tam!=0:#Contagem usando o tamanho como diferenciador
    Embarc=Embarcacoes[Tam-1]#Embarcação do ciclo atual
#-------------------------------------------------------------------------------------------------------   
    if Tam==4:  #Porta-Aviões
        print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
        Lin=int(input("Linha escolhida> "))
        Col=int(input("Coluna Escolhida> "))
        if Tam>1:
            Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
            if Ori==1:
                Ori='vertical'
            else:
                Ori='horizontal'
        Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
        if Check1 ==False: 
#--------------------------------------------------------------------------------------------------------
            while Check1 != True:#Caso não seja uma posição valida
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
                Lin=int(input("Linha escolhida> "))
                Col=int(input("Coluna Escolhida> "))
                if Tam>1:
                    Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                    if Ori==1:
                        Ori='vertical'
                    else:
                        Ori='horizontal'
                Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
        else:
#--------------------------------------------------------------------------------------------------------
            Pos=[define_posicoes(Lin,Col,Ori,Tam)]#Posição da Embarcação
            frota[Embarc]+=Pos#Colocando a posição da embarcação dentro da Frota
#-------------------------------------------------------------------------------------------------------- 
    elif Tam==3: #Navio_tanque
        while contagem<2:
            print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
            Lin=int(input("Linha escolhida> "))
            Col=int(input("Coluna Escolhida> "))
            Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
            if Ori==1:
                Ori='vertical'
            else:
                Ori='horizontal'
            Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            if Check1 == False: 
#-------    ---------------------------------------------------------------------------------------------
                while Check1 != True:#Caso não seja uma posição valida
                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
                    Lin=int(input("Linha escolhida> "))
                    Col=int(input("Coluna Escolhida> "))
                    Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                    if Ori==1:
                        Ori='vertical'
                    else:
                        Ori='horizontal'
                    Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            else:
                Pos=define_posicoes(Lin,Col,Ori,Tam)#Posição da Embarcação
                ListNavios.append(Pos)
                contagem+=1
#---------------------------------------------------------------------------------------------------------
        frota[Embarc]+=ListNavios#Colocando a posição da embarcação dentro da Frota
#-------------------------------------------------------------------------------------------------------- 
    elif Tam==2: #Contra-Torpedeiro
        while contagem<3:
            print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
            Lin=int(input("Linha escolhida> "))
            Col=int(input("Coluna Escolhida> "))
            Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
            if Ori==1:
                Ori='vertical'
            else:
                Ori='horizontal'
            Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            if Check1 == False: 
#-------    ---------------------------------------------------------------------------------------------
                while Check1 != True:#Caso não seja uma posição valida
                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
                    Lin=int(input("Linha escolhida> "))
                    Col=int(input("Coluna Escolhida> "))
                    Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
                    if Ori==1:
                        Ori='vertical'
                    else:
                        Ori='horizontal'
                    Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            else:
                Pos=define_posicoes(Lin,Col,Ori,Tam)#Posição da Embarcação
                ListNavios.append(Pos)
                contagem+=1
#---------------------------------------------------------------------------------------------------------
        frota[Embarc]+=ListNavios#Colocando a posição da embarcação dentro da Frota
#-------------------------------------------------------------------------------------------------------- 
    elif Tam==1: #submarino
        while contagem<4:
            print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
            Lin=int(input("Linha escolhida> "))
            Col=int(input("Coluna Escolhida> "))
            Ori='vertical'
            Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            if Check1 == False: 
#-------    ---------------------------------------------------------------------------------------------
                while Check1 != True:#Caso não seja uma posição valida
                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {Embarc} que possui tamanho {Tam}')
                    Lin=int(input("Linha escolhida> "))
                    Col=int(input("Coluna Escolhida> "))
                    Ori='vertical'
                    Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
            else:
                Pos=define_posicoes(Lin,Col,Ori,Tam)#Posição da Embarcação
                ListNavios.append(Pos)
                contagem+=1
#---------------------------------------------------------------------------------------------------------
        frota[Embarc]+=ListNavios#Colocando a posição da embarcação dentro da Frota
#---------------------------------------------------------------------------------------------------------
    contagem=0
    ListNavios=[]
    Tam-=1
print(frota)