from Inicializa import *
from Assets import *
from Config import *
#começa a rodar a tela inicial do jogo

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
    pygame.time.delay(166)
    Janela.fill((255,255,255))
    Janela.blit(Morte2,(0,0))
    pygame.display.update()
    pygame.time.delay(166)
    Janela.fill((255,255,255))
    Janela.blit(Morte3,(0,0))
    pygame.display.update()
    pygame.time.delay(166)
    Janela.fill((255,255,255))
    Janela.blit(Morte4,(0,0))
    pygame.display.update()
    pygame.time.delay(166)
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
                    pygame.quit
        if botcont3[0][0] in botcont3[1] and botcont3[0][1] in botcont3[2]:
        #Acontece nada
                if event.type==pygame.MOUSEBUTTONDOWN:
                    Morto=False
                    pygame.quit
        Janela.fill((255,255,255))
        Janela.blit(Morte5,(0,0))
        pygame.display.update()