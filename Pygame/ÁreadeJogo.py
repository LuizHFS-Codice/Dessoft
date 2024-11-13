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

#Imagem do Inimigo Trimpot
TrimpotImg=pygame.image.load('Assets/Imagens/Trimpot.png').convert_alpha()
TrimpotImg=pygame.transform.scale(TrimpotImg,(LargNav/3,AltNav*2))

#Imagem do Missil do Trimpot
MisselImg=pygame.image.load('Assets/Imagens/Missil.png')
MisselImg=pygame.transform.scale(MisselImg,(LargMissil,AltMissil))

#tela rolando para esquerda
rolagem=0
fundo=ceil(Largura/SkyBox.get_width()) +1

#grupo de sprites
Sprites=pygame.sprite.Group()
Balas=pygame.sprite.Group()
Balas_Voadores=pygame.sprite.Group()
Inimigos_Voadores=pygame.sprite.Group()
Trimpots=pygame.sprite.Group()
Missils=pygame.sprite.Group()

#Jogador
jogador = navezinha(NaveImg,Sprites,Balas,Balaimg)
Sprites.add(jogador)

#Inimigo Voador
for i in range(3):
    InimigoVoador=InimigoVoa(IniVoaImg,Sprites,Balas_Voadores,Balaimg)
    Sprites.add(InimigoVoador)
    Inimigos_Voadores.add(InimigoVoador)
    Trimpot=InimigoBaixo(TrimpotImg,Sprites,Missils,MisselImg)
    Sprites.add(Trimpot)
    Trimpots.add(Trimpot)
Sprites.add(Inimigos_Voadores)
Sprites.add(Trimpots)

movimento=0
Inv=0 #Invulnerabilidade

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
        movinivoa=random.randint(0,30)
        if movinivoa in range(0,5):
            cada_um.speedx-=Vx/5
        if movinivoa in range(5,10):
            cada_um.speedy-=Vy/2.5
        if movinivoa in range(10,15):
            cada_um.speedx+=Vx/5
        if movinivoa in range(15,20):
            cada_um.speedy+=Vy/2.5
        if movinivoa in range(29,31):
            cada_um.atirar()
    #Movimento do Trimpod
    for cada in Trimpots:
        moviTrimpot=random.randint(0,30)
        if moviTrimpot in range(0,5):
            cada.speedx-=Vx/10
        if moviTrimpot in range(10,15):
            cada.speedx+=Vx/10
        if moviTrimpot in range(24,25):
            cada.atirar()
    
    #Danos
    Dano=[]
    if Inv==0:
        Dano=pygame.sprite.spritecollide(jogador,Balas_Voadores,1)
        if len(Dano)>0:
            Inv=FPS*T_Inv
        Dano=pygame.sprite.spritecollide(jogador,Missils,1)
        if len(Dano)>0:
            Inv=FPS*T_Inv
    else:
        Inv-=1
    Dano=[]
    Dano=pygame.sprite.groupcollide(Inimigos_Voadores,Balas,0,1)


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