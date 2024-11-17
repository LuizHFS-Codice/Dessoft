#Teste de features

from Config import *
from Classes import *
import pygame
from Inicializa import *
from Assets import *
from Telas import *

pygame.init
Janela=pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('Teste')

movimento=0
Inv=0 #Invulnerabilidade
ContVoadores=0
ContTrimpots=0
Pontuação=0

    #tela rolando para esquerda
rolagem=0
fundo=ceil(Largura/SkyBox.get_width()) +1

    #       Fase 2
    #coloca inimigo novo
BossImg1=BornBoss1(LargBoss1,AltBoss1)
BossImg2=BornBoss2(LargBoss2,AltBoss2)
BossImg3=BornBoss3(LargBoss3,AltBoss3)
ColocaBoss(BossImg1,BossImg2,BossImg3)


game=True
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
            if event.key==pygame.K_z:
                jogador.atirar()
            if event.key==pygame.K_x:
                jogador.bomba()

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
pygame.quit()
