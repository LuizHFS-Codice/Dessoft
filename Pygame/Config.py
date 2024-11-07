import pygame

#           Medições

Largura=824
Altura=596

LargNav=150
AltNav=50

LargBala=20
AltBala=10

#           Imagens

#imagem da nave
NaveImg=pygame.image.load('Assets/Imagens/Nave.png').convert_alpha()
NaveImg=pygame.transform.scale(NaveImg,(LargNav,AltNav))

#tempo no jogo
relógio=pygame.time.Clock()

#imagem da tela de fundo
SkyBox=pygame.image.load('Assets/Imagens/Skybox.png').convert()
SkyBox=pygame.transform.scale(SkyBox,(Largura,Altura))

#iamgem da bala
Balaimg=pygame.image.load('Assets/Imagens/Bala.png').convert()
Balaimg=pygame.transform.scale(Balaimg,(LargBala,AltBala))

#           Configurações Jogo

FPS=30

Vx=15
Vy=9
