import pygame
from Telas import *

frameinicio()
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
ColocaVoadores(IniVoaImg)
TrimpotImg = BornTrimpot(LargNavt,AltNavt)
ColocaTrimpot(TrimpotImg)
BossImg1=BornBoss1(LargBoss1,AltBoss1)
ColocaBoss1(BossImg1)

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

#Movimento do Inimigo Voador:
        if event.type==andaiv:
            for cada_um in Inimigos_Voadores:
                movinivoa=random.randint(0,30)
                if movinivoa in range(0,5):
                    cada_um.speedx-=Vx 
                if movinivoa in range(5,10):
                    cada_um.speedy-=Vy
                if movinivoa in range(10,15):
                    cada_um.speedx+=Vx
                if movinivoa in range(15,20):
                    cada_um.speedy+=Vy
        if event.type==timertiroiv:
            for cada_um in Inimigos_Voadores:
                moviatira=random.randint(0,30)
                if moviatira%2!=0:
                    cada_um.atirar()
    #Movimento do Trimpod
        if event.type==andat:
            for cada in Trimpots:
                moviTrimpot=random.randint(0,30)
                if moviTrimpot in range(0,4):
                    cada.speedx-=Vx/2
                if moviTrimpot in range(4,9):
                    cada.speedx+=Vx
        if event.type==timertirot:
            for cada in Trimpots:
                moviatirat=random.randint(0,30)
                if moviatirat%2!=0:
                    cada.atirar()

    #Danos
    Dano=[]
    if Inv==0:
        Dano=pygame.sprite.spritecollide(jogador,Balas_Voadores,1)
        if len(Dano)>0:
            jogador.vida-=Dano_inimigo_Voa
            Inv=FPS*T_Inv
            Pontuação-=10
        Dano=pygame.sprite.spritecollide(jogador,Missils,1)
        if len(Dano)>0:
            jogador.vida-=Dano_Missil_Inimigo
            Inv=FPS*T_Inv
            Pontuação-=10
        Dano=pygame.sprite.spritecollide(jogador,Trimpots,0)
        if len(Dano)>0:
            jogador.vida-=Dano_Colisão
            Inv=FPS*T_Inv
            Pontuação-=10
        Dano=pygame.sprite.spritecollide(jogador,Inimigos_Voadores,0)
        if len(Dano)>0:
            jogador.vida-=Dano_Colisão
            Inv=FPS*T_Inv
            Pontuação-=10

    else:
        Inv-=1
    if jogador.vida<=0:
        game=False
        animacaomorte()
    #Colisão Tiro-Inimigo Voador
    Dano=[]
    Dano=pygame.sprite.groupcollide(Trimpots,Balas,0,1)
    for Tripod in Dano:
        Tripod.vida-=Dano_Tiro_Jogador
        Pontuação+=50
        if Tripod.vida<=0:
            Tripod.kill()
            ContTrimpots+=1
            Pontuação+=250
    #Colisão Tiro-Tripod
    Dano=[]
    Dano=pygame.sprite.groupcollide(Inimigos_Voadores,Balas,0,1)
    for Inimigos in Dano:
        Inimigos.vida-=Dano_Tiro_Jogador
        Pontuação+=10
        if Inimigos.vida<=0:
            Inimigos.kill()
            ContVoadores+=1
            Pontuação+=250
    #Colisão Bomba-Tripod
    Dano=[]
    Dano=pygame.sprite.groupcollide(Trimpots,Bombas,0,1)
    for Trimpod in Dano:
        Trimpod.vida-=Dano_Bomba_Jogador
        Pontuação+=10
        if Trimpod.vida<=0:
            Trimpod.kill()
            ContTrimpots+=1
            Pontuação+=150
    #Colisão Bomba-Inimigo Voador
    Dano=[]
    Dano=pygame.sprite.groupcollide(Inimigos_Voadores,Bombas,0,1)
    for Inimigos in Dano:
        Inimigos.vida-=Dano_Bomba_Jogador
        Pontuação+=25
        if Inimigos.vida<=0:
            Inimigos.kill()
            ContVoadores+=1
            Pontuação+=150
            
    #Repawn dos inimigos
    if ContTrimpots==3:
        for i in range(3):
            Trimpot=InimigoBaixo(TrimpotImg,Sprites,Missils,MisselImg)
            Sprites.add(Trimpot)
            Trimpots.add(Trimpot)
            ContTrimpots=0
    if ContVoadores==3:
        for i in range(3):
            InimigoVoador=InimigoVoa(IniVoaImg,Sprites,Balas_Voadores,Balaimg)
            Sprites.add(InimigoVoador)
            Inimigos_Voadores.add(InimigoVoador)
            ContVoadores=0
    
    vida_tela=font.render(f'{jogador.vida}', False, (255, 255, 255))
    Pontuação_Tela=font.render(f'{Pontuação}', False, (255, 255, 255))

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
    Janela.blit(vida_tela,(0,0))
    Janela.blit(Pontuação_Tela,(Largura-100,0))

    Sprites.draw(Janela)

    pygame.display.update()

pygame.quit

#Codar o Boss aqui
