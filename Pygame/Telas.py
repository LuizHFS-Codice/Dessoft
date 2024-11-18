import pygame
from Inicializa import *

#começa a rodar a tela inicial do jogo
def fase2():
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
    TrimpotImg = BornTrimpot(LargNavt,AltNavt)
    ColocaTrimpot(TrimpotImg)

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

def fase1():

    ColocaVoadores(IniVoaImg)

    movimento=0
    Inv=0 #Invulnerabilidade
    Ação=FPS//4
    ContVoadores=0
    ContTrimpots=0
    Pontuação=0

    #tela rolando para esquerda
    rolagem=0
    fundo=ceil(Largura/SkyBox.get_width()) +1

    #       Tela inicial
    framepadrao(Historia1)
    framepadrao1(Historia2)
    framepadrao(Historia3)

    #começar a fase 1
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
        #Danos
        Dano=[]
        if Inv==0:
            Dano=pygame.sprite.spritecollide(jogador,Balas_Voadores,1)
            if len(Dano)>0:
                jogador.vida-=Dano_inimigo_Voa
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
        Dano=pygame.sprite.groupcollide(Inimigos_Voadores,Balas,0,1)
        for Inimigos in Dano:
            Inimigos.vida-=Dano_Tiro_Jogador
            Pontuação+=10
            if Inimigos.vida<=0:
                Inimigos.kill()
                ContVoadores+=1
                Pontuação+=250
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
            Janela.blit(Skyboxini,(Skyboxini.get_width()*movimento+rolagem,0))
            movimento+=1
        rolagem-=2
        if abs(rolagem)>SkyBox.get_width():
            rolagem=0
        Janela.blit(vida_tela,(0,0))
        Janela.blit(Pontuação_Tela,(Largura-100,0))

        Sprites.draw(Janela)

        pygame.display.update()

        #passando de fase
        if Pontuação > 1500:
            game=False
            framefase2() 
#função que traduz get_pos e transforma em dados para usar na lógica dos botões
def verificabotao(bx,by,bt,ba):
    #pega a area do botão
    xb = range(bx,bx+bt+1)
    yb = range(by,by+ba+1)
    #usa a funçao get_pos e traduz
    pos = (f'{pygame.mouse.get_pos()}')
    pos = pos.replace('(','',)
    pos = pos.replace(')','',)
    pos = pos.split(', ')
    #transforma os dados em valores numericos
    pos[1] = int(pos[1])
    pos[0] = int(pos[0])
    #retorna os dados importantes para comparar
    return pos, xb, yb

def frameinicio():
    framepadrao(Aviso)
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                inicio = False
                pygame.quit
            #usa a funcao de traducao
            botcom = verificabotao(bxcom,bycom,btv,bav)
            botcred = verificabotao(bxcom,bycred,btv,bav)
            botsair = verificabotao(bxcom,bysair,btv,bav)
            #compara se a posiçao do mouse está na area do botao
            if botcom[0][0] in botcom[1] and botcom[0][1] in botcom[2]:
                #começa o jogo
                if event.type==pygame.MOUSEBUTTONDOWN:
                    inicio = False
                    fase1()
            if botcred[0][0] in botcred[1] and botcred[0][1] in botcred[2]:
                #apresenta os creditos
                if event.type==pygame.MOUSEBUTTONDOWN:
                    inicio = False
                    framecreditos()
            if botsair[0][0] in botsair[1] and botsair[0][1] in botsair[2]:
                #sai do jogo
                if event.type==pygame.MOUSEBUTTONDOWN:
                    inicio = False
                    pygame.quit
            Janela.fill((255,255,255))
            Janela.blit(telainicial,(0,0))
            pygame.display.update()


def framecreditos():
    credit=True
    while credit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                credit = False
                pygame.quit
        botvolt = verificabotao(bxvol,byvol,btv,bav)
        if botvolt[0][0] in botvolt[1] and botvolt[0][1] in botvolt[2]:
                #volta pro incio
                if event.type==pygame.MOUSEBUTTONDOWN:
                    credit=False
                    frameinicio()
        Janela.fill((255,255,255))
        Janela.blit(telacreditos,(0,0))
        pygame.display.update()

def framefase2():
    Fase2=True
    while Fase2:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Fase2 = False
                pygame.quit
        botcont = verificabotao(bxcont,bycont,btv,bav)
        if botcont[0][0] in botcont[1] and botcont[0][1] in botcont[2]:
        #Continua o games
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Fase2=False
                    fase2()
        Janela.fill((255,255,255))
        Janela.blit(telafase2,(0,0))
        pygame.display.update()

def frametelaboss():
    BossFight=True
    while BossFight:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                BossFight = False
                pygame.quit
        botcont = verificabotao(bxcont,bycont,btv,bav)
        if botcont[0][0] in botcont[1] and botcont[0][1] in botcont[2]:
        #Continua o games
                if event.type==pygame.MOUSEBUTTONDOWN:
                    BossFight=False
        Janela.fill((255,255,255))
        Janela.blit(telaboss,(0,0))
        pygame.display.update()

def framepadrao(img):
    BossFight=True
    while BossFight:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                BossFight = False
                pygame.quit
        botcont = verificabotao(bxcont,bycont,btv,bav)
        if botcont[0][0] in botcont[1] and botcont[0][1] in botcont[2]:
        #Continua o games
                if event.type==pygame.MOUSEBUTTONDOWN:
                    BossFight=False
        Janela.fill((255,255,255))
        Janela.blit(img,(0,0))
        pygame.display.update()

def framepadrao1(img):
    BossFight=True
    while BossFight:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                BossFight = False
                pygame.quit
        botcont2 = verificabotao(bxcont2,bycont2,btv,bav)
        if botcont2[0][0] in botcont2[1] and botcont2[0][1] in botcont2[2]:
        #Continua o games
                if event.type==pygame.MOUSEBUTTONDOWN:
                    BossFight=False
        Janela.fill((255,255,255))
        Janela.blit(img,(0,0))
        pygame.display.update()

def animacaomorte():
    Janela.fill((255,255,255))
    Janela.blit(Morte1,(0,0))
    pygame.display.update()
    pygame.time.delay(350)
    Janela.fill((255,255,255))
    Janela.blit(Morte2,(0,0))
    pygame.display.update()
    pygame.time.delay(350)
    Janela.fill((255,255,255))
    Janela.blit(Morte3,(0,0))
    pygame.display.update()
    pygame.time.delay(350)
    Janela.fill((255,255,255 ))
    Janela.blit(Morte4,(0,0))
    pygame.display.update()
    pygame.time.delay(400)
    Janela.fill((255,255,255))
    Morto=True
    while Morto:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Morto = False
                pygame.quit
        botcont2 = verificabotao(bmx,brmy,brmt,brma)
        botcont3 = verificabotao(bmx,bvmy,bvmt,bvma)
        if botcont2[0][0] in botcont2[1] and botcont2[0][1] in botcont2[2]:
        #Acontece nada
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Morto=False
                    fase1()
        if botcont3[0][0] in botcont3[1] and botcont3[0][1] in botcont3[2]:
        #Acontece nada
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Morto=False
                    frameinicio()
        Janela.fill((255,255,255))
        Janela.blit(Morte5,(0,0))
        pygame.display.update()