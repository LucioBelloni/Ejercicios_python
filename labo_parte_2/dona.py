import pygame
import colores
import random
                

def crear(x,y,ancho,alto):
    imagen_dona = pygame.image.load("donaxd.png")
    imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rect_dona = imagen_dona.get_rect()
    rect_dona.x = x
    rect_dona.y = y
    dict_dona = {}
    dict_dona["surface"] = imagen_dona
    dict_dona["rect"] = rect_dona
    dict_dona["visible"] = True
    dict_dona["speed"] = random.randrange(10,20,1)

    return dict_dona

def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y = rect_dona.y + dona["speed"]


def actualizar_pantalla(lista_donas,personaje,ventana_principal):
    for dona in lista_donas:
        if(dona["visible"] and personaje["rect"].colliderect(dona["rect"])):
            dona["visible"] = False
            personaje["score"] = personaje["score"] + 100
        if(dona["visible"]):
            #pygame.draw.rect(ventana_principal,colores.VERDE ,dona["rect"])
            ventana_principal.blit(dona["surface"],dona["rect"])
    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]),True,(255,0,0))
    ventana_principal.blit(text,(0,0))     

def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        y = random.randrange(-1000,0,10)
        x = random.randrange(0,740,70)
        lista_donas.append(crear(x,y,60,60))
    return lista_donas


def rastar_dona(dona):
    dona["rect"].x = random.randrange(0,740,70)
    dona["rect"].y = random.randrange(-1000,0,10)
