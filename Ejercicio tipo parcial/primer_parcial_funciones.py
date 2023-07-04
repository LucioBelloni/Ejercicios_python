import re
import json
# Belloni Lucio

def parse_json(nombre_archivo:str)->list:
    """la funcion lee  el archivo, extrae los datos y cierra el archivo.
       recibe por parametro el path (ruta)  
       retorna una lista de diccinarios de personas """
    with open(nombre_archivo,"r") as archivo:
        lista_final_personas= []
        todo_texto = archivo.read()
        nombre = re.findall(r'"name": "([ a-zA-Z0-9\-]+)',todo_texto)
        altura = re.findall(r'"height": "([0-9]+)',todo_texto)
        masas = re.findall(r'"mass": "([0-9]+)',todo_texto)
        genero = re.findall(r'"gender": "([a-zA-Z/]+)', todo_texto)
           
        for i in range(len(nombre)):
            personas = {}
            personas["name"] = nombre[i]
            personas["height"] = altura[i]
            personas["mass"] = masas[i]
            personas["gender"] = genero[i]
            lista_final_personas.append(personas)
            
    return lista_final_personas

def copiar_lista(lista:list)-> list:
    """la funcion copia la lista original de personas
        recibe por parametros la lista original
        retorna la lista copiada 
    """
    lista = parse_json("data.json")
    lista_copiada = lista.copy()
    return lista_copiada

lista_copiada = copiar_lista(parse_json("data.json"))
# print(lista_copiada)

def normalizar_datos(lista:list):
    """La funcion normaliza los datos que son numericos a su tipo de dato(int,float)  
        recibe por parametro la lista 
    """
    bandera = False
    if len(lista)> 0 and type(lista) == type([]):
        for e_lista in lista:
            if e_lista["height"] != int:
                e_lista["height"] = int(e_lista["height"])
                bandera = True
            if e_lista["mass"] != int:
                e_lista["mass"] = int(e_lista["mass"])
                bandera = True
        if bandera == True:
            print("datos normalizados")
    else:
        print("la lista esta vacia")        
       

def mostrar_dato_usuario(lista:list,asc_desc:str):
    """la funcion busca coincidencia (asc / desc) y si las hay retorna el valor
        recibe por parametros la lista y un str
        retorna el valor buscado
    """
    while True:
        if type(lista) == type(list()) and len(lista) > 0: 
            if re.search('asc',asc_desc) != None or re.search('desc',asc_desc) != None:
                return asc_desc
            else:
                break
        else:
            print("Error... la lista esta vacia")

# mostrar_dato_usuario(lista_copiada,"asc")

# 1-3
def listar_personas_por_altura_peso(lista:list,clave:str,tipo_orden:str)->list:
    """la funcion  ordena de manera ascendente o descendente  por la clave ingresada
        recibe por parametro la lista con la clave(srt) y el tipo de orden que queres hacer(str)
        retorna la lista ordenada cambiar
    """
    bandera_swap = True
    mostrar_dato_usuario(lista,tipo_orden)
    normalizar_datos(lista)
    if tipo_orden == "asc" or tipo_orden == "desc":
        while bandera_swap == True:
            bandera_swap = False
            for i in range(len(lista)-1):
                if (lista[i][clave] > lista[i+1][clave] and tipo_orden == "asc") or (lista[i][clave] < lista[i+1][clave] 
                and tipo_orden == "desc"):
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
        for e_lista in lista:
            print(e_lista["name"],"altura:",e_lista[clave])

        return lista      
    else:
        return False
    
#mass height
# listar_personas_por_altura(lista_copiada,"height","ascendente")

# 2
def buscar_primer_genero(lista:list,genero:str)->dict:
    """la funcion busca el primer genero 
        recibe por parametros la lista y el genero(str)
        retorna el diccionario 
    """
    primer_personaje = {}
    for e_lista in lista:
        if genero == e_lista["gender"]:
            primer_personaje = e_lista
            break
    return primer_personaje

def calcular_max_dato(lista:list,clave:str,genero:str):
    """la funcion busca el mayor de cada genero
        recibe por parametros la  lista, clave(str) y el genero(str)
        retorna el personaje mas alto de cada genero 
    """
    normalizar_datos(lista)
    primer_personaje = buscar_primer_genero(lista,genero)
    for e_lista in lista:
        if e_lista["gender"] == genero:
            if e_lista[clave] > primer_personaje[clave]:
                primer_personaje = e_lista
                      
    return primer_personaje
# n/a male female
# 4
def buscador_de_personajes(lista:list):
    """esta funcion busca a los personajes de derecha a izquierda 
        recibe por parametros la lista
    """
    indice_actual = 0
    valor = 0
    print(lista[indice_actual])
    while valor != "1" or valor != "2" or valor != "3":
        valor = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir\n")
        match valor:
            case"1":
                indice_actual = (indice_actual - 1 ) % len(lista)
                print(lista[indice_actual])
            case"2":
                indice_actual = (indice_actual + 1) % len(lista)
                print(lista[indice_actual])
            case"3":
                break

# buscador_de_personajes(lista_copiada)

# 5
def generar_csv(lista:list, nombre_archivo:str):
    """la funcion escribe  el archivo, extrae los datos y cierra el archivo.
        recibe por parametro la lista y  el path (ruta) 
    """
    with open(nombre_archivo, "w") as archivo:
            for e_lista in lista:
                #printeamos
                mensaje = "{0},{1},{2},{3}\n"
                mensaje = mensaje.format(
                                        e_lista["name"],
                                        e_lista["height"],
                                        e_lista["mass"],
                                        e_lista["gender"],
                )
                archivo.write(mensaje)    
    
def imprimir_menu():
    print("\n1- Listar los personajes ordenados por altura."
          "\n2- Mostrar el personaje más alto de cada genero"
          "\n3- Ordenar y listar los personajes por peso."
          "\n4- buscador de personajes"
          "\n5- Exportar a CSV la lista de personajes ordenada"
          "\n6- Salir\n"
            )

def validar_entero(numero_str:str):
    """valida que el numero_str no contenga palabras en el caso que lo haya retorna false
    recibe como parametros un numero en formato str"""
    if numero_str.isdigit():
        return True
    else:
        return False
    
def mostrar_menu():
    while True:
        imprimir_menu()
        opcion = input("Ingrese la opcion..")
        if validar_entero(opcion) == True:
            opcion = int(opcion)
        else:
            print("Error...ingrese la opcion correcta")
        return opcion

def menu_app(lista:list):
    lista_persona_uno = []
    while True:
        opcion = mostrar_menu()
        match opcion:
            case 1:
                asc_desc = "mal"
                while asc_desc != "asc" and asc_desc != "desc":
                    asc_desc = input("Ingrese la manera como lo quiere ordenar... asc o desc\n")  
                    lista_persona_uno = listar_personas_por_altura_peso(lista,"height",asc_desc)

            case 2:
                print("1-n/a\n"
                      "2-male\n"
                      "3-female\n")
                opcion_sub_menu = input("Ingrese una opcion")
                match opcion_sub_menu:
                    case "1":
                        max_altura = calcular_max_dato(lista,"height","n/a")
                        print(max_altura)
                    case "2":
                        max_altura = calcular_max_dato(lista,"height","male")
                        print(max_altura)
                    case "3":
                        max_altura = calcular_max_dato(lista,"height","female")
                        print(max_altura)
            case 3:
                asc_desc = "mal"
                while asc_desc != "asc" and asc_desc != "desc":
                    asc_desc = input("Ingrese la manera como lo quiere ordenar... asc o desc\n")
                    listar_personas_por_altura_peso(lista,"mass",asc_desc)
            case 4:
                buscador_de_personajes(lista)
            case 5:
                if len(lista_persona_uno) > 0:
                    generar_csv(lista_persona_uno,"Exportar_parcial_labo.csv")
                    print("El csv se exporto con exito..")
                else:
                    print("tiene que ingresar la opcion 1 para exportar el csv")
            case 6:
                break
