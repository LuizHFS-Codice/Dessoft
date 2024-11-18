from math import *
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
#           Medições
Largura=824
Altura=596

LargNav=235/1.8
AltNav=110/1.8
LargNavm=130/1.3
AltNavm=83/1.3
LargNavt=50/1.1
AltNavt=100/1.1

LargBoss1=LargNav*2.5
AltBoss1=AltNav*2.5
LargBoss2=LargNav*2
AltBoss2=AltNav*2
LargBoss3=LargNavt*3
AltBoss3=AltNavt*3

LargBala=20
AltBala=10

LargMissil=10
AltMissil=20

Bomb=20

#Botão tamanho vermelho e Botão altura vermelho
btv = 224
bav = 46

#botão cordenada x para todos os botões do começo
bxcom = 569

#botão cordenada y para o botão de começar
bycom = 364

#botão y, de créditos
bycred = 430

#botão y, de sair
bysair = 495

#botão x e botão y de voltar
bxvol = 560
byvol = 492

#botao de continuar telas
bxcont = bxvol
bycont = byvol

#botao de continuar tela historia 2
bxcont2 = 46
bycont2 = 502

#tamanho do botao da tela de morte
brmt = 126
brma = 103

bvmt = 126
bvma = 39

#botao da tela de morte
bmx = 665

brmy = 443
bvmy = 549

#Frames
FPS=30

#Velocidade nave
Vx=15
Vy=9

#Variaveis de vida
Vida_Jogador=50
T_Inv=1#Tempo de Invulnerabilidade em segundos
Vida_Inimigo_Voa=10
Vida_Tripod=15
Vida_Boss=200
#Variáveis de dano
Dano_Tiro_Jogador=1
Dano_Bomba_Jogador=2
Dano_inimigo_Voa=2.5
Dano_Missil_Inimigo=5
Dano_Colisão=10
Dano_Laser=7.5

#sons
shot=pygame.mixer.Sound('Assets\Sons_efeitos\shot.wav')
shotinim=pygame.mixer.Sound('Assets\Sons_efeitos\shotinim.wav')