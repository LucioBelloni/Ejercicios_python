import json
import re
# Belloni Lucio

def parse_json(nombre_archivo:str)->list:
    with open(nombre_archivo,"r") as archivo:
        lista_final_heroes = []
        todo_texto = archivo.read()
        nombre = re.findall(r'"nombre": "([ a-zA-Z-]+)',todo_texto)
        identidad = re.findall(r'"identidad": "([ \(\)a-zA-Z]+)',todo_texto)
        altura = re.findall(r'"altura": ([0-9\.0-9]+)',todo_texto)
        peso = re.findall(r'"peso": ([0-9\.0-9]+)',todo_texto)
        fuerza = re.findall(r'"fuerza": ([0-9]+)', todo_texto)
        inteligencia = re.findall(r'"inteligencia": "([""a-z]+)', todo_texto)
        
        for i in range(len(nombre)):
            heroes = {}
            heroes["nombre"] = nombre[i]
            heroes["identidad"] = identidad[i]
            heroes["altura"] = altura[i]
            heroes["peso"] = peso[i]
            heroes["fuerza"] = fuerza[i]
            heroes["inteligencia"] = inteligencia[i]
            lista_final_heroes.append(heroes)
            i+=1
    return lista_final_heroes



def copiar_lista(lista:list)-> list:
    lista = parse_json("data_stark.json")
    lista_copiada = lista.copy()
    return lista_copiada

lista_copiada = copiar_lista(parse_json("data_stark.json"))

def listar_heroes(lista:list):
    respuesta = "s"
    while respuesta:
        if respuesta == "s": 
            numero_ingresado = input("¿Cuantos numeros desea ingesar?..")
            if numero_ingresado.isdigit() == True:
                numero_ingresado = int(numero_ingresado)
                if numero_ingresado > 0 and numero_ingresado < 25:
                    for i in range(numero_ingresado):
                        print(lista[i]["nombre"])
                    break
                            
                else:
                    print("Error... Ingrese un numero del 1 al 24")
            else:
                print("Error..ingreso un numero")

            respuesta = input("desea seguir ingresando s/n")
       
        else:
            break    
        
# listar_heroes(lista_copiada)
def listar_heroes_por_altura(lista:list):
    respuesta = "s"
    while respuesta:
        if respuesta == "s":
            ordenar_asc_desc = input("Ingrese la manera como lo quiere ordenar... asc o desc")
            if ordenar_asc_desc.isdigit() == False:
                if ordenar_asc_desc == "asc":
                    bandera_swap = True
                    while bandera_swap == True:
                        bandera_swap = False
                        for i in range(len(lista)-1):
                            if float(lista[i]["altura"]) > float(lista[i+1]["altura"]):
                                auxiliar = lista[i]
                                lista[i] = lista[i+1]
                                lista[i+1] = auxiliar
                                bandera_swap = True
                    for e_lista in lista:
                        print(e_lista["nombre"],e_lista["altura"])
                    break        
                elif ordenar_asc_desc == "desc":
                    bandera_swap = True
                    while bandera_swap == True:
                        bandera_swap = False
                        for i in  range(len(lista)-1):
                            if float(lista[i]["altura"]) < float(lista[i+1]["altura"]):
                                auxiliar = lista[i]
                                lista[i] = lista[i+1]
                                lista[i+1] = auxiliar
                                bandera_swap = True
                    for e_lista in lista:
                        print(e_lista["nombre"],e_lista["altura"])
                    
                else:
                    print("ingrese la palabra correctta")    
            else:
                print("Error,ingrese lo adecuada")

            respuesta = input("desea seguir ingresando s/n")

        else:
            break                

# listar_heroes_por_altura(lista_copiada)

def listar_heroes_por_fuerza(lista:list):
    respuesta = "s"
    while respuesta:
        if respuesta == "s":
            ordenar_asc_desc = input("Ingrese la manera como lo quiere ordenar... asc o desc")
            if ordenar_asc_desc.isdigit() == False:
                if ordenar_asc_desc == "asc":
                    bandera_swap = True
                    while bandera_swap == True:
                        bandera_swap = False
                        for i in range(len(lista)-1):
                            if float(lista[i]["fuerza"]) > float(lista[i+1]["fuerza"]):
                                auxiliar = lista[i]
                                lista[i] = lista[i+1]
                                lista[i+1] = auxiliar
                                bandera_swap = True
                    for e_lista in lista:
                        print(e_lista["nombre"],e_lista["fuerza"])
                            
                elif ordenar_asc_desc == "desc":
                    bandera_swap = True
                    while bandera_swap == True:
                        bandera_swap = False
                        for i in  range(len(lista)-1):
                            if float(lista[i]["fuerza"]) < float(lista[i+1]["fuerza"]):
                                auxiliar = lista[i]
                                lista[i] = lista[i+1]
                                lista[i+1] = auxiliar
                                bandera_swap = True
                    for e_lista in lista:
                        print(e_lista["nombre"],e_lista["fuerza"])
                else:
                    print("ingrese la palabra correctta")    
            else:
                print("Error,ingrese lo adecuada")    
            respuesta = input("desea seguir ingresando s/n")
        else:
            break
# listar_heroes_por_fuerza(lista_copiada)

def calcular_promedio(lista: list, clave:str):
        
    suma = 0

    for e_lista in lista:
        suma += float(e_lista[clave])
    promedio = suma / 24
    mayor_menor = input("Ingrese el mayor o el menor")
    mayor_menor = mayor_menor.lower()   
    if mayor_menor == "mayor":
        for e_lista in lista:
            if float(e_lista[clave]) > promedio:
                print(e_lista["nombre"]) 
    elif mayor_menor == "menor":
        for e_lista in lista:
            if float(e_lista[clave]) < promedio:
                print(e_lista["nombre"])
    else:
        print("Error ingrese el mayor o minimo ")
           
# calcular_promedio(lista_copiada,"peso")

def buscar_heroes_inteligencia(lista:list, clave:str):
    for e_lista in lista:
        if re.search(clave,e_lista["inteligencia"])!= None:
                print(e_lista["nombre"])
           
# buscar_heroes_inteligencia(lista_copiada,"good")

def generar_csv(lista:list, nombre_archivo:str):
    with open(nombre_archivo, "w") as archivo:
        for e_lista in lista:
            #printeamos
            mensaje = "{0},{1},{2},{3},{4},{5}"
            mensaje = mensaje.format(
                                    e_lista["nombre"],
                                    e_lista["identidad"],
                                    e_lista["altura"],
                                    e_lista["peso"],
                                    e_lista["fuerza"],
                                    e_lista["inteligencia"])
            print(mensaje)
            archivo.write(mensaje)

# generar_csv(lista_copiada,"data_starkasd.csv")

def mostrar_menu():
    while True:
        print("\n1- Listar los primeros N héroes."
              "\n2- Ordenar y Listar héroes por altura."
              "\n3- Ordenar y Listar héroes por fuerza."
              "\n4- Calcular promedio de cualquier key"
              "\n5- Buscar héroes por inteligencia"
              "\n6- Exportar a CSV la lista de héroes"
              "\n7- Salir"
            )
        respuesta = input("Ingrese una opcion")
        # re.findall('[0-9]+',respuesta)
        match respuesta:
            case"1":
                listar_heroes(lista_copiada)
            case"2":
                listar_heroes_por_altura(lista_copiada)
            case"3":
                listar_heroes_por_fuerza(lista_copiada)
            case"4":
                print("\n1- altura"
                      "\n2- peso"
                      "\n3- fuerza")
                sub_menu= input("Ingrese una opcion")
                re.findall('[0-9]+',sub_menu)
                match sub_menu:
                    case"1":
                        calcular_promedio(lista_copiada,"altura")
                    case"2":
                        calcular_promedio(lista_copiada,"peso")
                    case"2":
                        calcular_promedio(lista_copiada,"fuerza")
            case"5":
                print("\n1- good"
                      "\n2- average"
                      "\n3- high")
                sub_menu_dos= input("Ingrese una opcion")
                re.findall('[0-9]+',sub_menu_dos)                
                match sub_menu_dos:
                    case"1":
                        buscar_heroes_inteligencia(lista_copiada,"good")
                    case"2":
                        buscar_heroes_inteligencia(lista_copiada,"average")
                    case"3":
                        buscar_heroes_inteligencia(lista_copiada,"high")
            case"6":
                generar_csv(lista_copiada,"data_stark1.csv")
            case"7":
                break

print(lista_copiada)              
mostrar_menu()



    


