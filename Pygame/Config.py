import pygame
from Assets import *
from math import *

#           Medições

Largura=824
Altura=596

LargNav=150
AltNav=50

LargBala=20
AltBala=10


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
T_Inv=3#Tempo de Invulnerabilidade em segundos
Vida_Inimigo_Voa=2
Dano_Jogador=1
Dano_inimigo_Voa=2
