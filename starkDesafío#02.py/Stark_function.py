#  Belloni Lucio



# 0
def stark_normalizar_datos(lista:list)->list:
    """normalizar los datos de la lista y retornar la lista con los datos cambiados a entero o a float 
       parametros que recicibe una lista y verifica que sea de tipo lista y que no este vacia
       retorna la lista modificada 
    """
    bandera = False
    if len(lista)> 0 and type(lista) == type([]):
        for e_lista in lista:
            if e_lista["altura"] != float:
                e_lista["altura"] = float(e_lista["altura"])
                bandera = True
            if e_lista["peso"] != float:
                e_lista["peso"] =  float(e_lista["peso"])
                bandera = True
            if e_lista["fuerza"] != int:
                e_lista["fuerza"] = int(e_lista["fuerza"])
                bandera = True
        if bandera == True:
            print("datos normalizados")
    else:
        print("la lista esta vacia")        
    return lista
# 1.1
def obtener_nombre(diccionario: dict)->str:
        """recibe por parametro todo el diccionario y busca en el la clave. En este caso es "nombre"
        y retorna el nombre con su dicha clave 
        """
        nombrepj= diccionario
        return ("Nombre: {0}".format(nombrepj["nombre"]))
# 1.2
def imprimir_dato(dato:str):
    """imprime un dato de tipo str """
    print(dato)
# 1.3
def stark_imprimir_nombres_heroes(lista:list):
    """imprime todos los nombres de los heroes. recibe una lista """
    stark_normalizar_datos(lista)
    for e_nombre in lista:
        imprimir_dato(obtener_nombre(e_nombre))
#2   
def obtener_nombre_y_dato(diccionario:dict, clave:str)->str:
    """obtiene el nombre y el dato(clave/key) de los heroes 
     esta funcion recibe 2 paremetros el diccionario y su clave
     retorna el dato(clave) y el nombre """
    nombre_heroe = diccionario["nombre"]
    dato = diccionario[clave]
    retorno = "Nombre: {0}    |  {2}:{1}  ".format(nombre_heroe,dato,clave)
    
    return retorno 
#3 
def stark_imprimir_nombres_alturas(lista:list, clave: str):
    """normaliza los datos,recorre la lista con  for y guarda el nombre y su clave luego los imprime.
       recibe como parametros una lista y su clave"""
    stark_normalizar_datos(lista)
    for e_lista in lista:
        nombre_dato_heroes = obtener_nombre_y_dato(e_lista,clave)
        print(nombre_dato_heroes)
# 4.1/4.2/4.3
def calcular_max_min_dato(lista:list, clave:str, estado: str)-> dict:
    """normaliza los datos. Calcula el maximo y el minimo dependiendo del estado en el que este 
    recibe como parametros una lista con su clave y el estado (maximo,minimo)
    me retorna el diccionario"""
    minimo_maximo = lista[0]
    stark_normalizar_datos(lista)
    for e_lista in lista:
        if estado == "maximo":
            if e_lista[clave] > minimo_maximo[clave]:
                minimo_maximo = e_lista
        elif estado == "minimo":
            if e_lista[clave] < minimo_maximo[clave]:
                minimo_maximo = e_lista
                
    return minimo_maximo , clave , estado
# 4.4
def stark_calcular_imprimir_heroe(lista:list,clave: str, estado: str):
    """recibe la funcion maximo minimo y te busca su maximo y minimo dependiendo de su estado 
    recime como parametros una lista con su clave y el estado en el que quiere buscar"""
    heroe_var,clave_var, estado_var = calcular_max_min_dato(lista, clave,estado)
    imprimir_dato("El super heroe con el {0} {1} es  {2}  el valor es: {3:.2f}".format(estado_var,clave_var, heroe_var["nombre"], heroe_var[clave])) 
# 5.1
def sumar_dato_heroe(lista:list,clave:str)-> float:
    """suma y acumala todos los datos dependiendo de su clave(key)
    recibe por parametros una lista con su clave 
    retorna  la suma con un float """
    suma_total = 0
    stark_normalizar_datos(lista)
    
    for e_lista in lista:
        if type(e_lista) == type(dict()) and len(e_lista) > 0:    
            suma_total +=  e_lista[clave]    
    return suma_total
# 5. 2
def dividir(dividiendo: float, divisor: float)-> float:
    """recibe 2 parametros un divisor y el dividiendo. en una variable guarda la division y la retorna la cuenta 
    como float"""
    if divisor == 0:
        return  0
    else:
        cuenta = dividiendo / divisor
        return cuenta 
# 5.3 
def calcular_promedio(lista:list,clave:str)-> float:
    """usa la funcion creadas anteriormente con el len obtenemos la cantidad y con la funcion dividir hacemos el promedio
    recibe como parametros la lista con su clave y retorna su promedio """
    suma_total= sumar_dato_heroe(lista, clave)
    cantidad_de_veces = len(lista)
    promedio = dividir(suma_total,cantidad_de_veces)
    return promedio 
# 5.4  
def stark_calcular_imprimir_promedio_altura(lista:list):
    promedio = calcular_promedio(lista, "altura")
    imprimir_dato("El promedio de la altura es: {0:.2f}".format(promedio))
# 5.4 reutilizable
def stark_calcular_imprimir_promedio(lista:list, clave:str):
    """recibe como paremetros una lista y su clave. 
    Con la funcion 5.3 hace su promedio y luego imprime el promedio dado """
    promedio = calcular_promedio(lista, clave)
    imprimir_dato("El promedio de la altura es: {0:.2f}".format(promedio))
#  6.1
def imprimir_menu():
        """Imprime un menu de opciones"""
        imprimir_dato("\n"
                      "1- Mostrar todos los  nombres de los heroes"
                    "\n2- Mostrar nombres con su altura,fuerza o peso"
                    "\n3- Mostrar MAXIMO peso,altura o fuerza"
                    "\n4- Mostrar MINIMO peso,altura o fuerza"
                    "\n5- Mostrar total dato de heroe: peso,altura o fuerza "
                    "\n6- Mostrar promedio altura,peso o fuerza"
                    "\n7- Salir"
                    )
# 6.2
def validar_entero(numero_str:str):
    """valida que el numero_str no contenga palabras en el caso que lo haya retorna false
    recibe como parametros un numero en formato str"""
    if numero_str.isdigit():
        return True
    else:
        return False
# 6.3
def stark_menu_principal():
    """imprime el menu, solicita al usuario que ingrese una opcion y valida que se haya ingresado
      un numero y que sea menor a 8 y mayor a 0 en caso contario repetira el bucle hasta que ingrese lo correcto"""
    while True:
        imprimir_menu()
        opcion = input(" Ingrese una opcion: ")
        if validar_entero(opcion) == True:
            opcion = int(opcion)
        if type(opcion) == type(int()) and opcion < 8 and opcion > 0:
            break
    return opcion
#sub menu
def stark_menu_principal_sub_menu():
    while True:
        opcion_sub_menu = input(" Ingrese una opcion:  ")
        if validar_entero(opcion_sub_menu) == True:
            opcion_sub_menu = int(opcion_sub_menu)
        if type(opcion_sub_menu) == type(int()) and opcion_sub_menu < 4 and opcion_sub_menu > 0:
            break
    return opcion_sub_menu

def stark_marvel_app(lista: list):
    """imprime todas las funciones utilizadas hasta el momento"""
    while True:
        opcion = stark_menu_principal()
        match opcion: 
            case 1:
                 imprimir_dato(stark_imprimir_nombres_heroes(lista))
            case 2:
                imprimir_dato("\n1- Altura"
                            "\n2- Fuerza"
                            "\n3- Peso")
                opcion_sub_menu = stark_menu_principal_sub_menu()
                match opcion_sub_menu:
                    case 1:
                        imprimir_dato(stark_imprimir_nombres_alturas(lista, "altura"))
                    case 2:
                        imprimir_dato(stark_imprimir_nombres_alturas(lista, "fuerza"))
                    case 3:
                        imprimir_dato(stark_imprimir_nombres_alturas(lista, "peso"))
            case 3:
                imprimir_dato("\n1- Altura"
                            "  \n2- Fuerza"
                            "  \n3- Peso")
                opcion_sub_menu = stark_menu_principal_sub_menu()
                match opcion_sub_menu:
                    case 1:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"altura","maximo"))
                    case 2:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"fuerza","maximo"))

                    case 3:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"peso","maximo"))
            case 4:
                imprimir_dato("\n1- Altura"
                            "  \n2- Fuerza"
                            "  \n3- Peso")
                opcion_sub_menu = stark_menu_principal_sub_menu()
                match opcion_sub_menu:
                    case 1:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"altura","minimo"))
                    case 2:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"fuerza","minimo"))
                    case 3:
                        imprimir_dato(stark_calcular_imprimir_heroe(lista,"peso","minimo"))
            case 5:
                imprimir_dato("\n1- Altura"
                            "  \n2- Fuerza"
                            "  \n3- Peso")
                opcion_sub_menu = stark_menu_principal_sub_menu()
                match opcion_sub_menu:
                    case 1:
                        imprimir_dato(sumar_dato_heroe(lista, "altura"))
                    case 2:
                        imprimir_dato(sumar_dato_heroe(lista, "fuerza"))
                    case 3:
                        imprimir_dato(sumar_dato_heroe(lista, "peso"))
            case 6: 
                imprimir_dato("\n1- Altura"
                            "\n2- Fuerza"
                            "\n3- Peso")
                opcion_sub_menu = stark_menu_principal_sub_menu()
                match opcion_sub_menu:
                    case 1:
                        imprimir_dato(stark_calcular_imprimir_promedio(lista,"altura"))
                    case 2:
                        imprimir_dato(stark_calcular_imprimir_promedio(lista,"fuerza"))
                    case 3:
                        imprimir_dato(stark_calcular_imprimir_promedio(lista,"peso"))
            case 7:
                break
