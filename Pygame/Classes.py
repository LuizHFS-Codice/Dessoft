import pygame
from ÁreadeJogo import *
import random

class Nave(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Assets/Imagens/Nave.png').convert_alpha()
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
        self.rect.x+=self.speedx#Movimento no Eixo X
        self.rect.y+=self.speedy#Movimento no Eixo Y
#Limites
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura

class InimigoVoa(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.img=pygame.transform.scale(self.image,(LargNav,AltNav))
        self.rect=self.image.get_rect()
        self.rect.left=0
        self.rect.right=Largura+200 #Começar fora da tela, para entrar dentro
        self.rect.top=0
        self.rect.bottom=0
        self.rect.centery=random.randint(0,Altura) #Posição Aleatória de Spawn na Altura
        self.speedx=0
        self.speedy=0
        self.life=3

    def update(self):
        #Movimento do inimigo voador
        while self.rect.right>Largura:
            self.speedx-=Vx
        movimento=random.randint(1,3)
        if movimento==1:
            self.rect.x+=random.randint(-Vx,Vx)
        if movimento==2:
            self.rect.y+=random.randint(-Vy,Vy)
        #Limites do inimigo Voador
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura


