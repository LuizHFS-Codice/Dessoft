import pygame #Importação Pygame
pygame.init #Inicialização do Pygame

window=pygame.display.set_mode((824,596))
pygame.display.set_caption('Voando pelo espaço')

game=True

Ptela=pygame.image.load('Assets/Imagens/Capa.png').convert_alpha()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        window.fill((255,255,255))
        window.blit(Ptela,(0,0))
        pygame.display.update()
pygame.quit()