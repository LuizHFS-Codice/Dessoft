import pygame
import random
from math import *
from Classes import *
from Config import *
#from PrimeiraTela import *
from Assets import *

pygame.init()

game=True

Janela=pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('Space Flight')

#           Imagens

#imagem da nave
NaveImg=pygame.image.load('Assets/Imagens/Nave.png').convert_alpha()
NaveImg=pygame.transform.scale(NaveImg,(LargNav,AltNav))

#imagem da tela de fundo
SkyBox = pygame.image.load('Assets/Imagens/Skybox.png').convert()
SkyBox = pygame.transform.scale(SkyBox,(Largura,Altura))

#imagem da bala
Balaimg=pygame.image.load('Assets/Imagens/Bala.png').convert_alpha()
Balaimg=pygame.transform.scale(Balaimg,(LargBala,AltBala))

#Imagem do Inimigo Voador
IniVoaImg=pygame.image.load('Assets/Imagens/InimigoVoa.png').convert_alpha()
IniVoaImg=pygame.transform.scale(IniVoaImg,(LargNav,AltNav))

#tela rolando para esquerda
rolagem=0
fundo=ceil(Largura/SkyBox.get_width()) +1

#grupo de sprites
Sprites=pygame.sprite.Group()
Balas=pygame.sprite.Group()
Inimigos_Voadores=pygame.sprite.Group()

#Jogador
jogador = navezinha(NaveImg,Sprites,Balas,Balaimg)
Sprites.add(jogador)

#Inimigo Voador
for i in range(3):
    InimigoVoador=InimigoVoa(IniVoaImg,Sprites,Balas,Balaimg)
    Inimigos_Voadores.add(InimigoVoador)
Sprites.add(Inimigos_Voadores)

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
#Movimento do Inimigo Voador:
    for cada_um in Inimigos_Voadores:
        movinivoa=random.randint(0,5)
        if movinivoa==0:
            cada_um.rect.x-=Vx*10
        if movinivoa==1:
            cada_um.rect.y-=Vy*5
        if movinivoa==2:
            cada_um.rect.x+=Vx*10
        if movinivoa==3:
            cada_um.rect.y+=Vy*5
        if movinivoa==4:
            cada_um.atirar()

    #Danos
    # if 

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