#Jogo
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida

from pprint import pprint
import numpy as np

Tam=4 #Tamanho do Navio
Embarcações=['Submarino','Contratorpedeiro','Navio-Tanque','Porta-Aviões']
while Tam!=0:
    print(f'Insira as informações referentes ao navio {Embarcações[Tam]} que possui o tamanho {Tam}')
    Embarc=Embarcações[Tam]
    frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }     
    Lin=int(input("Linha escolhida> "))
    Col=int(input("Coluna Escolhida> "))
    if Tam>1:
        Ori=int(input("Rotação da Embarcação (1 (Vertical) ou 2 (Horizontal))> "))
        if Ori==1:
            Ori='vertical'
        else:
            Ori='horizontal'
    Check1=posicao_valida()
    
    
    


Frota=preenche_frota(Frota,Embarc,Lin,Col,Ori,Tam)
print(Frota)
Tabuleiro=posiciona_frota(Frota)
pprint(Tabuleiro)