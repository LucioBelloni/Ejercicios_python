"Belloni Lucio"

from data_pj import lista_personajes
acumulador_altura = 0
total_altura = 0

def Mostrar_los_nombres_de_cada_superhéroe():
    for e_lista in lista_personajes:
        print(e_lista["nombre"])
def Mostrar_nombres_y_altura():
    for e_lista in lista_personajes:
        print(e_lista["nombre"])
        print(e_lista["altura"])
def Mostrar_superhéroe_mas_alto():
    maximo = float(lista_personajes[0]["altura"])
    superhéroe_mas_alto = lista_personajes[0]["nombre"]

    for e_lista in lista_personajes:
        e_lista["altura"] = float(e_lista["altura"])
        if maximo < e_lista["altura"]:
            maximo = e_lista["altura"]
            superhéroe_mas_alto = e_lista["nombre"] 
    print("El superhéroe mas alto es:", superhéroe_mas_alto)
def Mostrar_superhéroe_mas_bajo():
    minimo = float(lista_personajes[0]["altura"])
    superhéroe_mas_bajo = lista_personajes[0]["nombre"]

    for e_lista in lista_personajes:
        e_lista["altura"] = float(e_lista["altura"])
        if minimo > e_lista["altura"]:
            minimo = e_lista["altura"]
            superhéroe_mas_bajo = e_lista["nombre"] 
    print("El superhéroe mas bajo es:", superhéroe_mas_bajo)
def Mostrar_total_promedio():
    acumulador_altura = 0 
    for e_lista in lista_personajes:
            e_lista["altura"] = float(e_lista["altura"])
            acumulador_altura += 1
            total_altura = float(e_lista["altura"]) + total_altura
            promedio_reproducciones = total_altura / acumulador_altura
    print("El promedio total de la altura de los superhéroes: ", promedio_reproducciones)
def Mostrar_superhéroe_mas_y_menos_pesado():
    mas_pesado = float(lista_personajes[0]["peso"])
    nombre_del_superhéroe_mas_pesado = lista_personajes[0]["nombre"]

    for e_lista in lista_personajes:
        e_lista["peso"] = float(e_lista["peso"])
        if mas_pesado < e_lista["peso"]:
            mas_pesado = e_lista["peso"]
            nombre_del_superhéroe_mas_pesado = e_lista["nombre"]

    print("El superhéroe mas pesado es: ", nombre_del_superhéroe_mas_pesado)

    menos_pesado = float(lista_personajes[0]["peso"])
    nombre_del_superhéroe_manos_pesado = lista_personajes[0]["nombre"]
    
    for e_lista in lista_personajes:
        e_lista["peso"] = float(e_lista["peso"])
        if menos_pesado > e_lista["peso"]:
            menos_pesado = e_lista["peso"]
            nombre_del_superhéroe_manos_pesado = e_lista["nombre"]

    print("El superhéroe menos pesado es: ", nombre_del_superhéroe_manos_pesado)

while True:
    print("1-Mostrar los nombres de cada superhéroe")
    print("2-Mostrar los nombres de cada superhéroe junto a la altura del mismo")
    print("3-Mostrar superhéroe mas alto")
    print("4-Mostrar superhéroe mas bajo")
    print("5-Mostrar promedio de los superhéroes")
    print("6-Mostrar cual de los superhéroe es más y menos pesado.")
    print("7-Salir")

    opcion = int(input("Ingrese una de las opcion: "))
    if opcion == 1:
        Mostrar_los_nombres_de_cada_superhéroe()
    elif opcion == 2:
        Mostrar_nombres_y_altura()
    elif opcion == 3:
        Mostrar_superhéroe_mas_alto()
    elif opcion == 4:
        Mostrar_superhéroe_mas_bajo()
    elif opcion == 5:
        Mostrar_total_promedio()
    elif opcion == 6:
        Mostrar_superhéroe_mas_y_menos_pesado()
    elif opcion == 7:
        print("Finalizo el programa xd lol")
        break



          

