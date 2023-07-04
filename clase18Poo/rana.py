import pygame
import colores
import elementos
pygame.init()
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
score = 0
#pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego ")

imagen_rana = pygame.image.load("pngwing.com.png")
imagen_rana = pygame.transform.scale(imagen_rana,(100,100))
rect_rana = pygame.Rect(30,100,101,101)

#creo la lista de moscas 
lista_moscas = elementos.crear_lista_moscas(10)


#mosca1 = elementos.crear_moscas(200,200,50,50)
#mosca2 = elementos.crear_moscas(320,320,50,50)
mosca = elementos.crear_lista_moscas(10)
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list(evento.pos)

            rect_rana[0] = lista_posicion[0] #modificando el left del rect de mi imagen 
            rect_rana[1] = lista_posicion[1] #modificando el top del rect de mi imagen 

    pantalla.fill(colores.LIGHTBLUE1)
    pygame.draw.rect(pantalla,colores.RED1,rect_rana)
    pantalla.blit(imagen_rana,rect_rana)
    
    #fundis imagen
    
    score = elementos.actualizar_pantalla_mosca(lista_moscas,pantalla,rect_rana,score)

    font = pygame.font.SysFont("Arial",50)
    texto = font.render("SCORE:{0}".format(score),True,colores.BLACK)
    pantalla.blit(texto,(100,100))
    pygame.display.flip()

pygame.quit()

"""
            contador_vueltas_reinicio +=1
            lista_aceite = []
            if auto_bots.visible == False:
                lista_bots = []
                movimiento_de_carril_y = 0
            if contador_vueltas_reinicio == 30:
                #screen.blit(imagen_game_over())
                nitro.stop()
                JUGANDO = 0
"""