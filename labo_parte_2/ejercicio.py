
import pygame
# import colores

def getSuperficies(path,filas, columnas):
    lista=[]
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            # un pedacito de la imagen del sprite
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            lista.append(superficie_fotograma)

    return lista

class Personaje:
    def __init__(self) -> None:
        self.caminar = getSuperficies("oso_caminando.png",1,3)
        self.paso1 = 0
        self.score = 0
        self.animacion = self.caminar
        self.imagen = self.animacion[self.paso1]
        self.rect = self.imagen.get_rect()
        self.rect.y = 500

    def actualizar(self):
        #paso los fotogramas del movimiento caminar
        if(self.paso1 < len(self.animacion)-1):
            self.paso1 += 1 
        else:
            self.paso1 = 0

    def dibujar(self, pantalla):
        self.imagen = self.animacion[self.paso1]
        pantalla.blit(self.imagen, self.rect)