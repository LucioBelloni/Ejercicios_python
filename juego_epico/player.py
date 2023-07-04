import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path,columnas,filas):
    lista = []
    surface_imagen = pygame.image.load(path)
    fotograma_ancho = int(surface_imagen.get_width()/columnas)
    fotograma_alto = int(surface_imagen.get_height()/filas)
    x = 0
    for columna in range(columnas):
        for fila in range(filas):
            x = columna  * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            lista.append(surface_fotograma)
    return lista

class Player:
    def __init__(self) -> None:
        self.walk = getSurfaceFromSpriteSheet(r"C:\Users\lucio\Documents\programacion_i\caracters\stink\walk.png",15,1)
        self.stay = getSurfaceFromSpriteSheet(r"C:\Users\lucio\Documents\programacion_i\caracters\stink\idle.png",16,1)
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
    def update(self):
        if self.frame <  len(self.animation) -1:
            self.frame += 1
        else:
            self.frame = 0
    def draw(self,screen):
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        screen.blit(self.image,self.rect)
