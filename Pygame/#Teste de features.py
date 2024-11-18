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

time=-1
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
        PeçasXY=3
        for Parte in Boss:
            if PeçasXY>1:
                movinivoa=random.randint(0,30)
                if movinivoa in range(0,5):
                    Parte.speedx-=Vx 
                if movinivoa in range(5,10):
                    Parte.speedy-=Vy
                if movinivoa in range(10,15):
                    Parte.speedx+=Vx
                if movinivoa in range(15,20):
                    Parte.speedy+=Vy
                if PeçasXY==3:
                    if movinivoa in range(20,30):
                            if time<0:
                                time=FPS*2
                            elif time==0:
                                Parte.disparar()
                                time-=1
                            else:
                                time-=1
                PeçasXY-=1
            else:
                MãoChão=random.randint(0,15)
                if MãoChão in range(0,5):
                    Parte.speedx-=Vx
                if MãoChão in range(5,10):
                    Parte.speedx+=Vx
                


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
