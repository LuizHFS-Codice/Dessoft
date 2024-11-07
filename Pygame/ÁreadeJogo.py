import pygame
import random
import math
from Classes import *
#from PrimeiraTela import *
from Assets import *

pygame.init()
game=True

#Configuraçoes de tela
Largura=824
Altura=596

LargNav=150
AltNav=50

LargBala=20
AltBala=10

Janela=pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('Space Flight')

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

#tela rolando para esquerda
rolagem=0
fundo=math.ceil(Largura /SkyBox.get_width()) +1

#grupo de sprites
Sprites=pygame.sprite.Group()
Balas=pygame.sprite.Group()

#Jogador
jogador = navezinha(NaveImg,Sprites,Balas,Balaimg)
Sprites.add(jogador)

FPS=30
Vx=15
Vy=9
movimento=0

while game:
    relógio.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
            
#Começar Movimento
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                jogador.speedx-=Vx
            if event.key==pygame.K_RIGHT:
                jogador.speedx+=Vx
            if event.key==pygame.K_UP:
                jogador.speedy-=Vy
            if event.key==pygame.K_DOWN:
                jogador.speedy+=Vy
            if event.key==pygame.K_SPACE:
                jogador.atirar()

#Parar Movimento
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                jogador.speedx+=Vx
            if event.key==pygame.K_RIGHT:
                jogador.speedx-=Vx
            if event.key==pygame.K_UP:
                jogador.speedy+=Vy
            if event.key==pygame.K_DOWN:
                jogador.speedy-=Vy

    Sprites.update()

    #Fundo
    movimento=0
    rolagem-=1
    Janela.fill((0,0,0))
    while movimento<fundo:
        Janela.blit(SkyBox,(SkyBox.get_width()*movimento+rolagem,0))
        movimento+=1
    rolagem-=2
    if abs(rolagem)>SkyBox.get_width():
        rolagem=0
    
    Sprites.draw(Janela)

    pygame.display.update()

pygame.quit