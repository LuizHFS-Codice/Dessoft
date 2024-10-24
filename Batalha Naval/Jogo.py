#Jogo
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
import numpy as np

print(posiciona_frota(0))
Tam=0 #Tamanho do Navio
Lin=int(input("Linha escolhida> "))
Col=int(input("Coluna Escolhida> "))
Ori=input("Rotação da Embarcação (vertical ou horizontal)> ")
Embarc=input("Qual o tipo de Embarcação> ")
ListEmbarc=["porta-aviões","navio-tanque","contratorpedeiro","submarino"]
if Embarc == ListEmbarc[0]:
    Tam=4
elif Embarc==ListEmbarc[1]:
    Tam=3
elif Embarc==ListEmbarc[2]:
    Tam=2
elif Embarc==ListEmbarc[3]:
    Tam=1
Frota={}
print(preenche_frota(Frota,Embarc,Lin,Col,Ori,Tam))