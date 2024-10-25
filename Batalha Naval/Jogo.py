#Jogo
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida

from pprint import pprint
import numpy as np

Tam=4 #Tamanho do Navio
Embarcações=['Submarino','Contratorpedeiro','Navio-Tanque','Porta-Aviões']#Lista de Embarcações
Pos=0
Lin=0
Col=0
Ori=0
while Tam!=0:#Contagem usando o tamanho como diferenciador
    print(f'Insira as informações referentes ao navio {Embarcações[Tam-1]} que possui o tamanho {Tam}')
    Embarc=Embarcações[Tam-1]#Embaracação do ciclo atual
#-------------------------------------------------------------------------------------------------------
    frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }
#-------------------------------------------------------------------------------------------------------   
    Lin=int(input("Linha escolhida> "))
    Col=int(input("Coluna Escolhida> "))
    if Tam>1:
        Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
        if Ori==1:
            Ori='vertical'
        else:
            Ori='horizontal'
    Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
#--------------------------------------------------------------------------------------------------------
    while Check1 != True:#Caso não seja uma posição valida
        print('Esta posição não está válida!')
        Lin=int(input("Linha escolhida> "))
        Col=int(input("Coluna Escolhida> "))
        if Tam>1:
            Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
            if Ori==1:
                Ori='vertical'
            else:
                Ori='horizontal'
        Check1=posicao_valida(frota,Lin,Col,Ori,Tam)
#--------------------------------------------------------------------------------------------------------
    Pos=
    


Frota=preenche_frota(Frota,Embarc,Lin,Col,Ori,Tam)
print(Frota)
Tabuleiro=posiciona_frota(Frota)
pprint(Tabuleiro)