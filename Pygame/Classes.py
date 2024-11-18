

import pygame
import random
import math
from Config import *


class navezinha(pygame.sprite.Sprite):
    '''As principais funções da classe nave estão armazenadas aqui.'''
    def __init__(self,NaveImg,sprites,Balas,Balaimg,Bombas,Bombasimg):
        '''Função __init__: Onde suas condições iniciais estão armazenadas.
        Como onde ela nasce, o seu retângulo e onde é carregado as balas.'''
        pygame.sprite.Sprite.__init__(self)

        self.image = NaveImg
        self.sprites = sprites
        self.Balas = Balas
        self.Bombas=Bombas

        #coordenada inicial
        self.rect=self.image.get_rect()
        self.rect.left= 0
        self.rect.right= 0
        self.rect.top= 0
        self.rect.bottom= 0
        self.rect.centery=Altura/2

        #vida
        self.vida=Vida_Jogador

        #velocidade inicial
        self.speedx=0
        self.speedy=0
        
        #Carregando balas
        self.Balas = Balas
        self.Balaimg = Balaimg

        #Carregando Bombas
        self.Bombas=Bombas
        self.Bombasimg=Bombasimg

    #Atualiza as coordenadas
    def update(self):
        '''Função update: Onde seus limites são delimitados e o movimento da nave
        é realizado.'''
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
        
        # # Melhoria na lógica de limites:
        # def limitar_movimentos(self):
        #     self.rect.left  = max(0, self.rect.left)
        #     self.rect.right = min(Largura, self.rect.right)
        #     self.rect.top = max(0, self.rect.top)
        #     self.rect.bottom = min(Altura, self.rect.bottom)

        # def update(self):

        #     self.rect.x  += self.speedx
        #     self.rect.y += self.speedy
        #     self.limitar_movimento()

        #Carrega a ação de atirar
    def atirar(self):
        '''Função Atirar: Permite o ataque, utilizando a classe "Tiro".'''
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        atiro = Tiro(self.Balaimg, self.rect.x, self.rect.y)
        self.Balas.add(atiro)
        self.sprites.add(atiro)

        #Carrega o bombardeio
    def bomba(self):
        boom=Bombardeio(self.Bombasimg, self.rect.x,self.rect.y)
        self.Bombas.add(boom)
        self.sprites.add(boom)



#Classe para os tiros
class Tiro(pygame.sprite.Sprite):
    '''Classe "Tiro" que será utilizada pela nave.'''
    def __init__(self, img, x, y):
        '''Função __init__: Estabelecimento de onde a bala nascerá,
        E a velocidade horizontal inicial.'''
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x = x+LargNav
        self.rect.y = y+(AltNav/2)

        #cordenadas do tiro

        #velocidade do tiro na horizontal
        self.speedx = 25

    def update(self):
        '''Função Update: A velocidade continua constante por cada atualização.
        Se a Bala passar da largura, ela será apagada automaticamente.'''
        #atualiza a bala no eixo x
        self.rect.x += self.speedx

        #se for maior que a largura da tela, apaga o tiro
        if self.rect.bottom > Largura:
            self.kill()



# Classe da Bomba
class Bombardeio(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)

            self.image=img
            self.rect=self.image.get_rect()

            self.rect.x=x+LargNav/2
            self.rect.y=y+AltNav

            #cordenadas do Missil

            #velocidade do tiro na vertical
            self.speedy=10

        def update(self):
            #atualiza a bala no eixo x
            self.rect.y+=self.speedy*1.1

            #se for maior que a largura da tela, apaga o tiro
            if self.rect.bottom==Altura:
                self.kill()

#Classe do Inimigo Voador
class InimigoVoa(pygame.sprite.Sprite):
    '''Classe "Inimigo Voador", um dos oponentes.'''
    def __init__(self,img,Sprites,Balas,Balaimg):
        '''Função __init__: Determina onde o inimigo nascerá
        O inimigo necessariamente nascerá do lado direito da tela
        A função também carrega as balas do inimigo.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.Sprites = Sprites
        self.Balas = Balas
        self.img=pygame.transform.scale(self.image,(LargNav,AltNav))
        self.vida=Vida_Inimigo_Voa
        #Spawns
        self.rect=self.image.get_rect()
        self.rect.x=Largura
        self.rect.y=random.randint(0,Altura-100) #Posição Aleatória de Spawn na Altura
        #Carregando balas
        self.speedx=0
        self.speedy=0
        self.Balas = Balas
        self.Balaimg = Balaimg
        

    def update(self):
        '''Função Update: limita o espaço que a nave inimiga voadora percorre
        Junto com a velocidade que ele percorrerá.'''
        # while self.rect.x>Largura:
        #     self.speedx-=Vx/10
        #     self.rect.x+=self.speedx
        #     self.speedx+=Vx/10
        #     self.rect.x+=self.speedx

        #Velocidade do inimigo
        self.rect.x+=(math.sin(self.speedx)+math.cos(self.speedx))*2
        self.rect.y+=(math.sin(self.speedy)+math.cos(self.speedy))*2
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
        '''Função Atirar: Permite o ataque, utilizando a classe "Tiro".'''
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

class InimigoBaixo(pygame.sprite.Sprite):
    def __init__(self,img,Sprites,missel,misselimg):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.Sprites = Sprites
        self.missel = missel
        self.img=pygame.transform.scale(self.image,(LargNav/3,AltNav))
        self.vida=Vida_Tripod
        #Spawns
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(100,Largura-200)
        self.rect.y=Altura-100 #Posição Aleatória de Spawn na Altura
        #Carregando balas
        self.speedx=0
        self.missel = missel
        self.misselimg = misselimg
        
    def update(self):
        #Movimento lateral do Trimpot
        self.rect.x+=math.tan(self.speedx)*5
        #Limites Laterais
        if self.rect.left<100:
            self.rect.left=100
        if self.rect.right>Largura//1.5:
            self.rect.right=Largura//1.5
    
    def atirar(self):
        # O novo Missil vai ser criado logo acima e no centro vertical do Trimpot
        atiro = MissilInimigoBaixo(self.misselimg, self.rect.x, self.rect.y)
        self.missel.add(atiro)
        self.Sprites.add(atiro)

class MissilInimigoBaixo(pygame.sprite.Sprite):
        def __init__(self, img, x, y):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()

            self.rect.x = x+(LargNav/3)/2
            self.rect.y = y+AltNav/2

            #cordenadas do Missil

            #velocidade do tiro na vertical
            self.speedy = 10

        def update(self):
            #atualiza a bala no eixo x
            self.rect.y -= self.speedy

            #se for maior que a largura da tela, apaga o tiro
            if self.rect.bottom < 0:
                self.kill()

class Boss1(pygame.sprite.Sprite):
    def __init__(self,img,Sprites,Laser,Laserimg,time):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.Sprites = Sprites
        self.Laser = Laser

        self.img=pygame.transform.scale(self.image,(LargBoss1,AltBoss1))
        self.vida=Vida_Inimigo_Voa*20

        #Spawns

        self.rect=self.image.get_rect()
        self.rect.x=Largura
        self.rect.y=Altura/2 #Posição do Spawn

        #Carregando Laser

        self.speedx=0
        self.speedy=0
        self.Laser = Laser
        self.Laserimg = Laserimg
        self.time=time
    
    def update(self):
        '''Função Update: limita o espaço que o Boss percorre
        Junto com a velocidade que ele percorrerá.'''
        #Velocidade do Boss
        self.rect.x+=(math.sin(self.speedx)+math.cos(self.speedx))*4
        self.rect.y+=(math.sin(self.speedy)+math.cos(self.speedy))*4

        #Limites do Boss
        
        if self.rect.left<Largura/1.5:
            self.rect.left=Largura/1.5
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura-100:
            self.rect.bottom=Altura-100

    def disparar(self):
        disparo=laser((self.Laserimg, self.rect.x, self.rect.y,self.time))
        self.Laserimg.add(disparo)
        self.Sprites.add(disparo)

class Boss2(pygame.sprite.Sprite):
    def __init__(self,img,Sprites,Bala,BalaImg):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.Sprites = Sprites
        self.Bala = Bala
        self.img=pygame.transform.scale(self.image,(LargNav,AltNav))
        self.vida=Vida_Inimigo_Voa*10
        #Spawns
        self.rect=self.image.get_rect()
        self.rect.x=Largura
        self.rect.y=0 #Posição do Spawn
        #Carregando Laser
        self.speedx=0
        self.speedy=0
        self.Bala = Bala
        self.BalaImg = BalaImg
    
    def update(self):
        '''Função Update: limita o espaço que o Boss percorre
        Junto com a velocidade que ele percorrerá.'''
        #Velocidade do Boss
        self.rect.x+=(math.sin(self.speedx)+math.cos(self.speedx))*8
        self.rect.y+=(math.sin(self.speedy)+math.cos(self.speedy))*8

        #Limites do Boss
        
        if self.rect.left<Largura/1.5:
            self.rect.left=Largura/1.5
        if self.rect.right>Largura:
            self.rect.right=Largura
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>Altura-100:
            self.rect.bottom=Altura-100

    def disparar(self):
        disparo=laser((self.Bala, self.rect.x, self.rect.y))
        self.BalaImg.add(disparo)
        self.Sprites.add(disparo)

class Boss3(pygame.sprite.Sprite):
    def __init__(self,img,Sprites,missel,misselimg):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.Sprites = Sprites
        self.missel = missel
        self.img=pygame.transform.scale(self.image,(LargNav*1.5,AltNav*2))
        self.vida=Vida_Tripod*10
        #Spawns
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(100,Largura-200)
        self.rect.y=Altura-100 #Posição Aleatória de Spawn na Altura
        #Carregando balas
        self.speedx=0
        self.missel = missel
        self.misselimg = misselimg
        
    def update(self):
        #Movimento lateral do Trimpot
        self.rect.x+=math.tan(self.speedx)*5
        #Limites Laterais
        if self.rect.left<100:
            self.rect.left=100
        if self.rect.right>Largura//1.5:
            self.rect.right=Largura//1.5
        if self.rect.bottom>Altura:
            self.rect.bottom=Altura
    
    def atirar(self):
        # O novo Missil vai ser criado logo acima e no centro vertical do Trimpot
        atiro = MissilInimigoBaixo(self.misselimg, self.rect.x, self.rect.y)
        self.missel.add(atiro)
        self.Sprites.add(atiro)


    
class laser(pygame.sprite.Sprite):
    def __init__(self, img, x, y, time):
        '''Função __init__: Onde o laser aparecerá na tela
        Na frente do Boss Principal e no meio da posição y dele.'''
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        self.rect.x=x-LargBoss1
        self.rect.y=y+AltBoss1/2

        self.time=time
    def update(self):
            '''Após um tempo ser decorrido, o laser desaperecerá.'''
            if self.time==0:
                self.kill()

# Input=int(input('Escolha um número para ver a documentação de cada classe, 1=Nave, 2=Tiro, 3=Inimigo Voador, 4=Tiro Inimigo> '))
# if Input==1:
#     help(navezinha)
# if Input==2:
#     help(Tiro)
# if Input==3:
#     help(InimigoVoa)
# if Input==4:
#     help(TiroInimigo)