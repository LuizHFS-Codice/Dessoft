import pygame
from Config import *
from Assets import *
from Classes import *

import random
from math import *

pygame.init()

#       tamanho de janela
Janela=pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('Space Flight')

#           Imagens

#imagem da tela de creditos
telacreditos=pygame.image.load('Assets/Imagens/Creditos.png').convert_alpha()
telacreditos=pygame.transform.scale(telacreditos,(824,596))

#imagem da fase2
telafase2=pygame.image.load('Assets/Imagens/Fase2.png').convert_alpha()
telafase2=pygame.transform.scale(telafase2,(824,596))

#animacao
#imagem de morte
Morte1=pygame.image.load('Assets/Imagens/Morte1.png').convert_alpha()
Morte1=pygame.transform.scale(Morte1,(824,596))#imagem da Morte

Morte2=pygame.image.load('Assets/Imagens/Morte2.png').convert_alpha()
Morte2=pygame.transform.scale(Morte2,(824,596))#imagem da Morte

Morte3=pygame.image.load('Assets/Imagens/Morte3.png').convert_alpha()
Morte3=pygame.transform.scale(Morte3,(824,596))#imagem da Morte

Morte4=pygame.image.load('Assets/Imagens/Morte4.png').convert_alpha()
Morte4=pygame.transform.scale(Morte4,(824,596))#imagem da Morte

Morte5=pygame.image.load('Assets/Imagens/Morte5.png').convert_alpha()
Morte5=pygame.transform.scale(Morte5,(824,596))

#imagem da tela de preparação do do boss
telaboss=pygame.image.load('Assets/Imagens/TelaBoss.png').convert_alpha()
telaboss=pygame.transform.scale(telaboss,(824,596))

Historia1=pygame.image.load('Assets/Imagens/Historia1.png').convert_alpha()
Historia1=pygame.transform.scale(Historia1,(824,596))

Historia2=pygame.image.load('Assets/Imagens/Historia2.png').convert_alpha()
Historia2=pygame.transform.scale(Historia2,(824,596))

Historia3=pygame.image.load('Assets/Imagens/Historia3.png').convert_alpha()
Historia3=pygame.transform.scale(Historia3,(824,596))

Aviso=pygame.image.load('Assets/Imagens/Aviso.png').convert_alpha()
Aviso=pygame.transform.scale(Aviso,(824,596))
'''
telacreditos=pygame.image.load('Assets/Imagens/Creditos.png').convert_alpha()
telacreditos=pygame.transform.scale(telacreditos,(824,596))'''

#imagem da tela inicial
telainicial=pygame.image.load('Assets/Imagens/Capa.png').convert_alpha()
telainicial=pygame.transform.scale(telainicial,(824,596))

#imagem da nave
NaveImg=pygame.image.load('Assets/Imagens/Nave.png').convert_alpha()
NaveImg=pygame.transform.scale(NaveImg,(LargNav,AltNav))

#imagem da tela de fundo
SkyBox = pygame.image.load('Assets/Imagens/Skybox.png').convert()
SkyBox = pygame.transform.scale(SkyBox,(Largura,Altura))

#imagem tela de fundo inicial
Skyboxini = pygame.image.load('Assets/Imagens/Skyboxini.png').convert()
Skyboxini = pygame.transform.scale(Skyboxini,(Largura,Altura))

#imagem da bala
Balaimg=pygame.image.load('Assets/Imagens/Bala.png').convert_alpha()
Balaimg=pygame.transform.scale(Balaimg,(LargBala,AltBala))

BalaIniimg=pygame.image.load('Assets/Imagens/BalaIni.png').convert_alpha()
BalaIniimg=pygame.transform.scale(BalaIniimg,(LargBala,AltBala))

#Imagem da bomba
Bombasimg=pygame.image.load('Assets/Imagens/Bomba.png').convert_alpha()
Bombasimg=pygame.transform.scale(Bombasimg,(Bomb,Bomb))

#Imagem do Inimigo Voador
IniVoaImg=pygame.image.load('Assets/Imagens/InimigoVoa.png').convert_alpha()
IniVoaImg=pygame.transform.scale(IniVoaImg,(LargNavm,AltNavm))

#guarda o inimigo trimpot para nascer depois
def BornTrimpot(LargNavt,AltNavt):
    #Imagem do Inimigo Trimpot
    TrimpotImg=pygame.image.load('Assets/Imagens/Trimpot.png').convert_alpha()
    TrimpotImg=pygame.transform.scale(TrimpotImg,(LargNavt,AltNavt))
    return TrimpotImg

#Imagem do Missil do Trimpot
MisselImg=pygame.image.load('Assets/Imagens/Missil.png').convert_alpha()
MisselImg=pygame.transform.scale(MisselImg,(LargMissil,AltMissil))

andando=pygame.image.load('Assets/Imagens/Andando.png').convert_alpha()
andando=pygame.transform.scale(MisselImg,(LargNav,AltNav))

#Imagem do Laser
LaserImg=pygame.image.load('Assets/Imagens/Laser.png').convert_alpha()
andando=pygame.transform.scale(LaserImg,(Largura,AltNavt))

#Guarda as Partes do Boss para spawnar depois
def BornBoss1(Largura,Altura):
    BossImg=pygame.image.load('Assets/Imagens/Tax_1.png').convert_alpha()
    BossImg=pygame.transform.scale(BossImg,(Largura,Altura))
    return BossImg

def BornBoss2(Largura,Altura):
    BossImg=pygame.image.load('Assets/Imagens/Tax_2.png').convert_alpha()
    BossImg=pygame.transform.scale(BossImg,(Largura,Altura))
    return BossImg


def BornBoss3(Largura,Altura):
    BossImg=pygame.image.load('Assets/Imagens/Tax_3.png').convert_alpha()
    BossImg=pygame.transform.scale(BossImg,(Largura,Altura))
    return BossImg



'''#imagem do boss
BossImg=pygame.image.load('Assets/Imagens/Boss.png').convert_alpha()
BossImg=pygame.transform.scale(BossImg,(824,596))'''

#           Configurações Jogo

#definindo espaço de tempo para atirar
timertiroiv = pygame.USEREVENT + 1
pygame.time.set_timer(timertiroiv,500)

timertirot = pygame.USEREVENT + 2
pygame.time.set_timer(timertirot,900)

#definindo espaço de tempo para andar
andaiv = pygame.USEREVENT + 3
pygame.time.set_timer(andaiv,100)

andat = pygame.USEREVENT + 4
pygame.time.set_timer(andat,500)

#espaçoparanimação
animacao = pygame.USEREVENT + 5
pygame.time.set_timer(animacao, 166)

#tempo no jogo
relógio=pygame.time.Clock()
#Fonte
font = pygame.font.SysFont(None, 48)

#grupo de sprites
Sprites=pygame.sprite.Group()
Balas=pygame.sprite.Group()
Balas_Voadores=pygame.sprite.Group()
Inimigos_Voadores=pygame.sprite.Group()
Trimpots=pygame.sprite.Group()
Missils=pygame.sprite.Group()
Bombas=pygame.sprite.Group()
Lasers=pygame.sprite.Group()


#Jogador
jogador = navezinha(NaveImg,Sprites,Balas,Balaimg,Bombas,Bombasimg)
Sprites.add(jogador)

#Inimigo Voador
def ColocaVoadores(IniVoaImg):
    for i in range(3):
        InimigoVoador=InimigoVoa(IniVoaImg,Sprites,Balas_Voadores,BalaIniimg)
        Sprites.add(InimigoVoador)
        Inimigos_Voadores.add(InimigoVoador)
    Sprites.add(Inimigos_Voadores)

def ColocaTrimpot(TrimpotImg):
    for i in range(3):
        Trimpot=InimigoBaixo(TrimpotImg,Sprites,Missils,MisselImg)
        Trimpots.add(Trimpot)
        Sprites.add(Trimpot)
    Sprites.add(Trimpot)
    Trimpots.add(Trimpot)

def ColocaBoss(BossImg1,BossImg2,BossImg3):
    time=0
    Chefao1=Boss1(BossImg1,Sprites,Lasers,LaserImg,time)
    Sprites.add(Chefao1)

    Chefao2=Boss2(BossImg2,Sprites,Balas_Voadores,BalaIniimg)
    Sprites.add(Chefao2)

    Chefao3=Boss3(BossImg3,Sprites,Missils,MisselImg)
    Sprites.add(Chefao3)
