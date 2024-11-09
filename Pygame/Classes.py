
import pygame
import random
from Config import *

class navezinha(pygame.sprite.Sprite):
    def __init__(self,NaveImg,sprites,Balas,Balaimg):
        pygame.sprite.Sprite.__init__(self)

        self.image = NaveImg
        self.sprites = sprites
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
        #Limites
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura
            
        #Carrega a ação de atirar
    def atirar(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        atiro = Tiro(self.Balaimg, self.rect.x, self.rect.y)
        self.Balas.add(atiro)
        self.sprites.add(atiro)



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

#Classe do Inimigo Voador
class InimigoVoa(pygame.sprite.Sprite):
    def __init__(self,img,Sprites,Balas,Balaimg):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.Sprites = Sprites
        self.Balas = Balas
        self.img=pygame.transform.scale(self.image,(LargNav,AltNav))
        #Spawns
        self.rect=self.image.get_rect()
        self.rect.x=Largura
        self.rect.y=random.randint(0,Altura-100) #Posição Aleatória de Spawn na Altura
        #Carregando balas
        self.Balas = Balas
        self.Balaimg = Balaimg

    def update(self):
        # while self.rect.x>Largura:
        #     self.speedx-=Vx/10
        #     self.rect.x+=self.speedx
        #     self.speedx+=Vx/10
        #     self.rect.x+=self.speedx
        
        #Limites do inimigo Voador
        
        if self.rect.left<Largura/2:
            self.rect.left=Largura/2
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura-100:
            self.rect.bottom=Altura-100

    def atirar(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        atiro = TiroInimigo(self.Balaimg, self.rect.x, self.rect.y)
        self.Balas.add(atiro)
        self.Sprites.add(atiro)

class TiroInimigo(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.image=pygame.transform.flip(self.image,1,0)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y+AltNav/2

        #cordenadas do tiro

        #velocidade do tiro na horizontal
        self.speedx = 25/2

    def update(self):
        #atualiza a bala no eixo x
        self.rect.x -= self.speedx

        #se for maior que a largura da tela, apaga o tiro
        if self.rect.bottom < 0:
            self.kill()

