import pygame
from Assets import *
from math import *

#           Medições

Largura=824
Altura=596

LargNav=212/1.8
AltNav=110/1.8
LargNavm=130/1.3
AltNavm=83/1.3
LargNavt=50/1.1
AltNavt=100/1.1

LargBala=20
AltBala=10

LargMissil=10
AltMissil=20

Bomb=20

#           Configurações Jogo


#tempo no jogo
relógio=pygame.time.Clock()

#Frames
FPS=30

#Velocidade nave
Vx=15
Vy=9

#Variaveis de dano
Vida_Jogador=10
T_Inv=5#Tempo de Invulnerabilidade em segundos
Vida_Inimigo_Voa=2
Dano_Tiro_Jogador=1
Dano_Bomba_Jogador=2
Dano_inimigo_Voa=2
Dano_Missil_Inimigo=2
