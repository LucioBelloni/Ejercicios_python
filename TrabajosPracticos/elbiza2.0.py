
# Belloni Lucio
"""
B. Recorrer la lista imprimiendo por consola el título de cada video
C. Recorrer la lista imprimiendo por consola el título de cada video junto a la
cantidad de reproducciones del mismo
D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones
(MÁXIMO)
E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones
(MÍNIMO)
F. Recorrer la lista y determinar la cantidad total de reproducciones del canal
(ACUMULADOR)
G. Recorrer la lista y determinar la cantidad promedio de reproducciones que
tiene un video (PROMEDIO)
H. Informar cual es el Título del vídeo asociado a cada uno de los indicadores
anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)
I. Calcular e informar cual es el video que más y el que menos dura.
J. Ordenar el código implementando una función para cada uno de los valores
informados
K. Construir un menú que permita elegir qué dato obtener"""

from data import lista_bzrp

def mostrar_tema(tema:dict):
     print("Tema - titulo:{0} vistas:{1}".format(tema["title"], tema["views"]))

def calcular_maximo(lista:list, clave:str)-> dict:
    """
    calcula un maximo en  base a una clave de un diccionario recibida
    racibe:una lista de deiccionarios y un string que representa una clave (key) del diccionario
    retorna: El diccionario maximo para la clave(key)recibida 
             -1 en caso de error 
    """ 
    retorno = -1
    # verificar parametros
    if type(lista) == type(list()) and type(clave) == type(str()) and len(lista) > 0:
        max = lista[0]
        for e_lista in lista:
              if e_lista[clave] > max[clave]:
                   max = e_lista
        retorno = max
    return retorno
     
     

def mostrar_todos_los_titulos():
     for e_lista in lista_bzrp:
            print(e_lista["title"])
def mostrar_video_cantidad_de_reproducciones():
    for e_lista in lista_bzrp:
            print(e_lista["title"])
            print(e_lista["views"])
def mostras_maxima_reproduccion():
    maximo = lista_bzrp[0]["views"]
    maximo_titulo = lista_bzrp[0]["title"]

    for e_lista in lista_bzrp:
            if maximo < e_lista["views"]:
                maximo = e_lista["views"]
                maximo_titulo = e_lista["title"] 
    print("La cantidad maxima de reproduccion es: ", maximo_titulo)
def mostrar_minima_de_reproducciones():
    minimo = lista_bzrp[0]["views"]
    minimo_titulo = lista_bzrp[0]["title"]

    for e_lista in lista_bzrp:
            if minimo > e_lista["views"]:
                minimo = e_lista["views"]
                minimo_titulo = e_lista["title"] 
    print("La cantidad minima de reproduccion es: ", minimo_titulo)
def mostrar_cantidad_total_de_reproducciones():
    acumulador_total = 0

    for e_lista in lista_bzrp:
        acumulador_total = e_lista["views"] + acumulador_total

    print("el total de reproduccion es: ", acumulador_total )      
def mostrar_cantidad_de_promedio_de_reproducciones(lista:list, clave:str):
    total_de_videos = lista[0][clave]
    acumulador_reproducciones = 0
    total_repordicciones = 0

    for e_lista in lista_bzrp:
        acumulador_reproducciones += 1
        total_repordicciones = e_lista[clave] + total_repordicciones
        promedio_reproducciones = total_repordicciones / acumulador_reproducciones

    print("El promedio es: ", promedio_reproducciones)   
def mostrar_video_que_dura_y_menos_dura():
    mas_durabilidad = lista_bzrp[0]["length"]
    video_mas_durabilidad = lista_bzrp[0]["title"]
    video_que_dura_mas = lista_bzrp[0]["length"]

    for e_lista in lista_bzrp:
        if mas_durabilidad < e_lista["length"]:
            mas_durabilidad = e_lista["length"]
            video_mas_durabilidad = e_lista["title"]
            video_que_dura_mas = e_lista["length"]

    print("El video que mas  dura es: ", video_mas_durabilidad, "y dura: ", video_que_dura_mas, "segundos")

    menos_durabilidad = lista_bzrp[0]["length"]
    video_menos_durabilidad = lista_bzrp[0]["title"]
    video_que_dura_manos = lista_bzrp[0]["length"]

    for e_lista in lista_bzrp:
        if menos_durabilidad > e_lista["length"]:
            menos_durabilidad = e_lista["length"]
            video_menos_durabilidad = e_lista["title"]
            video_que_dura_manos = e_lista["length"]

    print("El video que menos dura es:", video_menos_durabilidad, "y dura: ", video_que_dura_manos, "segundos")
     
while True:
    print("1-Titulo de cada video")
    print("2-Título de cada video junto a la cantidad de reproducciones del mismo")
    print("3-Cantidad máxima de reproducciones")
    print("4-Cantidad minima de reproducciones ")
    print("5-La cantidad promedio de reproducciones de los video")
    print("6-Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO y MÍNIMO)")
    print("7-Calcular e informar cual es el video que más y el que menos dura")
    print("8-Salir")

    opcion = int(input("Ingrese una de las opcion: "))
    if opcion == 1:
        mostrar_todos_los_titulos()
    elif opcion == 2:
        mostrar_video_cantidad_de_reproducciones()
    elif opcion == 3:
        mostras_maxima_reproduccion()
    elif opcion == 4:
        mostrar_minima_de_reproducciones()
    elif opcion == 5:
        mostrar_cantidad_total_de_reproducciones()
    elif opcion == 6:
        mostrar_cantidad_de_promedio_de_reproducciones()
    elif opcion == 7:
        mostrar_video_que_dura_y_menos_dura()
    elif opcion == 8:            
        break

    
print("Finde del probrama ")








    