import pygame
from ÁreadeJogo import *
#from PrimeiraTela import *
import random

Largura=824
Altura=596

LargNav=150
AltNav=50

class navezinha(pygame.sprite.Sprite):
    def __init__(self,NaveImg,Sprites,Balas,Balaimg):
        pygame.sprite.Sprite.__init__(self)

        self.image = NaveImg
        self.Sprites = Sprites
        self.Balas = Balas

        #coordenada inicial
        self.rect=self.image.get_rect()
        self.rect.left= 0
        self.rect.right= 0
        self.rect.top= 0
        self.rect.bottom= 0
        self.rect.centery=Altura/2

        #velocidade inicial
        self.speedx=0
        self.speedy=0
        
        #Carregando balas
        self.Balas = Balas
        self.Balaimg = Balaimg

    #Atualiza as coordenadas
    def update(self):
        self.rect.x+=self.speedx#Movimento no Eixo X
        self.rect.y+=self.speedy#Movimento no Eixo Y

        #Carrega a ação de atirar
    def atirar(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        atiro = Tiro(self.Balaimg, self.rect.x, self.rect.y)
        self.Balas.add(atiro)
        self.Sprites.add(atiro)

#Limites
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura

#Classe parar os tiros
class Tiro(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x = x+125
        self.rect.y = y+22.5

        #cordenadas do tiro

        #velocidade do tiro na horizontal
        self.speedx = 25

    def update(self):
        #atualiza a bala no eixo x
        self.rect.x += self.speedx

        #se for maior que a largura da tela, apaga o tiro
        if self.rect.bottom > Largura:
            self.kill()

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


