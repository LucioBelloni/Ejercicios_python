import pygame
"""COLOR_CELESTE = (24,211,211)
COLOR_AMARILLO = (255,255,0)
COLOR_ROJO = (255,0,0)
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
RADIO = 80
pygame.init()
posicion_circulo = [100,100]
# horizontal, vertital,ancho,alto
posicion_rectangulo = (100,5,100,200)
# TIMER 
timer_segundos = pygame.USEREVENT #este es un evento que creo yo 
pygame.time.set_timer(timer_segundos,100) #1000 es 1 segundo

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.USEREVENT:
            #print(evento.pos)
            # posicion_circulo = list(evento.pos)
            if evento.type == timer_segundos:
                if posicion_circulo[0] < ANCHO_VENTANA + RADIO :
                    posicion_circulo[0] = posicion_circulo[0] + 10
                else:
                    posicion_circulo[0] = 0

    pantalla.fill(COLOR_CELESTE)
    # pygame.draw.rect(pantalla,COLOR_ROJO,posicion_rectangulo)
    pygame.draw.circle(pantalla,COLOR_AMARILLO,posicion_circulo,RADIO)#80 es el radio 

    # mostrar los cambios de la pantalla 
    pygame.display.flip()
pygame.quit()"""


COLOR_CELESTE = (24,211,211)
COLOR_AMARILLO = (255,255,0)
COLOR_ROJO = (255,0,0)
COLOR_NEGRO =(0,0,0)
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
RADIO = 80
pygame.init()
posicion_circulo = [100,100]
# horizontal, vertital,ancho,alto
posicion_rectangulo = (100,5,100,200)
posicion_torreto = [30,100]
#imagen 
imagen_torreto = pygame.image.load("torreto.jpg")
imagen_torreto = pygame.transform.scale(imagen_torreto,(200,200))
#texto 
fuente = pygame.font.SysFont("Arial",30)
texto = fuente.render("The family is first",True,COLOR_NEGRO)


pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            posicion_torreto = evento.pos


    pantalla.fill(COLOR_CELESTE)
    pantalla.blit(texto,(150,10))
    pantalla.blit(imagen_torreto,(posicion_torreto)) #fundir la imagen en la ventana
    
    # pygame.draw.rect(pantalla,COLOR_ROJO,posicion_rectangulo)
    #pygame.draw.circle(pantalla,COLOR_AMARILLO,posicion_circulo,RADIO)#80 es el radio 

    # mostrar los cambios de la pantalla 
    pygame.display.flip()
pygame.quit()


"""        
            mover con las flechas de derechar izquierda arriba abajo 
            if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                posicion_circulo[0] = posicion_circulo[0] + 20
            if evento.key == pygame.K_LEFT:
                posicion_circulo[0] = posicion_circulo[0] - 20
            if evento.key == pygame.K_UP:
                posicion_circulo[1] = posicion_circulo[1] - 20
            if evento.key == pygame.K_DOWN:
                posicion_circulo[1] = posicion_circulo[1] + 20
"""

"""  mover con las flechas de derechar izquierda arriba abajo  manteniuendo 
    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            posicion_circulo[0] = posicion_circulo[0] + 0.05
        if lista_teclas[pygame.K_LEFT]:
            posicion_circulo[0] = posicion_circulo[0] - 0.05
        if lista_teclas[pygame.K_UP]:
            posicion_circulo[1] = posicion_circulo[1] - 0.05
        if lista_teclas[pygame.K_DOWN]:
            posicion_circulo[1] = posicion_circulo[1] + 0.05

"""