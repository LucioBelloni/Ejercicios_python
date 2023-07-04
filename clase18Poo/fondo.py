import pygame
import colores
from personaje import Personaje 

ANCHO_VENTANA = 600
ALTO_VENTANA = 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mi primer bosque")
reloj = pygame.time.Clock()

imagen_bosque = pygame.image.load("bosque.png")
imagen_bosque = pygame.transform.scale(imagen_bosque,(ANCHO_VENTANA,ALTO_VENTANA))

#crear de mi persona (constructor)
persona1 = Personaje()

flag_correr = True

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            persona1.rect.x = persona1.rect.x + 20
            persona1.actualizar()
        if keys[pygame.K_LEFT]:
            persona1.rect.x = persona1.rect.x - 20
            persona1.actualizar()
        if keys[pygame.K_DOWN]:
            persona1.rect.y = persona1.rect.y + 20
            persona1.actualizar()    
        if keys[pygame.K_UP]:
            persona1.rect.y = persona1.rect.y - 20
            persona1.actualizar()                            

    milis = reloj.tick(60) #cada 8 milis da una vuelta al while 60fps
    pantalla.blit(imagen_bosque,imagen_bosque.get_rect())
    #dibujar personaje 
    persona1.dibujar(pantalla)
    
    pygame.display.flip()

pygame.quit