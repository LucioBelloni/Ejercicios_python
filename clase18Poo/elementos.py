import pygame
import colores

def crear_moscas(x,y,ancho,alto):
    imagen_mosca = pygame.image.load("mosca.png")
    imagen_mosca = pygame.transform.scale(imagen_mosca,(ancho,alto))
    rect_mosca = imagen_mosca.get_rect()
    rect_mosca.x = x
    rect_mosca.y = y
    #guardar la imagen y el rect en un diccionario 
    dic_moscas = {}
    dic_moscas["image"] = imagen_mosca
    dic_moscas["rect"] = rect_mosca
    dic_moscas["visible"] = True
    return dic_moscas

def crear_lista_moscas(cantidad):
    lista_moscas = []
    for i in range(cantidad):
        lista_moscas.append(crear_moscas(0+(i*50),230,30,30))
    return lista_moscas

def actualizar_pantalla_mosca(lista_moscas,pantalla,rect_rana,score):
    for e_mosca in lista_moscas:
        if e_mosca["visible"] == True and rect_rana.colliderect(e_mosca["rect"]):
            e_mosca["visible"] = False
            score = score + 100
        if e_mosca["visible"] == True:
            pygame.draw.rect(pantalla,colores.RED1,e_mosca["rect"])
            pantalla.blit(e_mosca["image"],e_mosca["rect"])  
    return score
    