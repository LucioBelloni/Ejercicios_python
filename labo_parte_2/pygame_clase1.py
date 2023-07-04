import pygame
import colores
import dona
import personaje


ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")
# print(type(ventana_principal)) # <class 'pygame.surface.Surface'>


pos_circulo = [30,60]

#TIMER
timer_segundos = pygame.USEREVENT + 0
pygame.time.set_timer(timer_segundos,100)


player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200 )
lista_donas = dona.crear_lista_donas(100)

#Crear un texto 
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("HOLA HOMERO",True,colores.ROJO)


flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:
                dona.update(lista_donas)
    
    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player,-2)   
    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player,2)
    ventana_principal.fill(colores.NEGRO)
    
    personaje.actualizar_pantalla(player,ventana_principal)
    dona.actualizar_pantalla(lista_donas,player,ventana_principal)

    pygame.display.flip()
pygame.quit()