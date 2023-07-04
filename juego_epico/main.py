import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_1.update()
    player_1.draw(screen)
    # player update -- verificar como el player interactua con todo el nivel 
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    
    pygame.display.flip()
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    delta_ms = clock.tick(FPS)
