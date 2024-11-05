import pygame
import random
import math

pygame.init()

Largura=824
Altura=596

LargNav=100
AltNav=50

Janela=pygame.display.set_mode((Largura,Altura))
pygame.display.set_caption('Space Flight')

NaveImg=pygame.image.load('Assets/Imagens/Nave.png').convert()
relógio=pygame.time.Clock()

SkyBox=pygame.image.load('Assets/Imagens/Skybox.png').convert()
rolagem=0
fundo=math.ceil(Largura /SkyBox.get_width()) +1

class Nave(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Assets/Imagens/Nave.png').convert()
        self.image=pygame.transform.scale(self.image,(LargNav,AltNav))
        self.rect=self.image.get_rect()
        self.rect.left=0
        self.rect.right=0
        self.rect.top=0
        self.rect.bottom=0
        self.rect.centery=Altura/2
        self.speedx=0
        self.speedy=0

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura


Sprites=pygame.sprite.Group()
jogador=Nave(NaveImg)
Sprites.add(jogador)

FPS=30
game=True


while game:
    relógio.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    Sprites.update()

    rolagem=-6
    Janela.fill((0,0,0))
    Janela.blit(SkyBox,(0,0))
    Sprites.draw(Janela)

    pygame.display.update()
pygame.quit