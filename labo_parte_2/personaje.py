import pygame
import colores

def crear(x,y,ancho,alto):
    dict_personaje = {}

    dict_personaje["surface"] = pygame.image.load("pngwing.com.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_pos"] = pygame.Rect(x,y,200,200)
    dict_personaje["rect"] = pygame.Rect(x+ancho/2-90,y+115,100,45)
    dict_personaje["score"] = 0  

    return dict_personaje

def actualizar_pantalla(personaje,ventana_principal):
    ventana_principal.blit(personaje["surface"],personaje["rect_pos"])
    #pygame.draw.rect(ventana_principal,colores.ROJO,personaje["rect"])

def update(personaje,incremenrto_x):
    nueva_x = personaje["rect_pos"].x + incremenrto_x
    if nueva_x > 0 and nueva_x < 600:
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremenrto_x
        personaje["rect"].x = personaje["rect"].x + incremenrto_x
 







    