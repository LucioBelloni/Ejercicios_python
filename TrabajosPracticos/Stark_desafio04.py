from data_pj import lista_personajes
import re
# Belloni Lucio
# 1.1
def extraer_iniciales(nombre_heroe: str)-> str:

    if len(nombre_heroe) > 0 and type(nombre_heroe) == type(str()):
        nombre_modificado = nombre_heroe
        if "the" in nombre_heroe:
            nombre_modificado = nombre_heroe.replace("the","")
        if "-" in nombre_heroe:
            nombre_modificado = nombre_heroe.replace('-'," ")
        
        iniciales = re.findall("[A-Z]+",nombre_modificado)

        seperador = "."
        iniciales_separada = seperador.join(iniciales) + "."

        return iniciales_separada
    else:
        return "N/A"
    
# inicial_extraida = extraer_iniciales("Howard the Duck:")
# print(inicial_extraida)

# 1.2 

def definir_iniciales_nombre(heroe: dict):
    if type(heroe) == type(dict()) and "nombre" in heroe:
        iniciales = extraer_iniciales(heroe["nombre"])
        heroe["iniciales"] = iniciales
        print(heroe)
        return True
    else:
        return False

# definir_iniciales_nombre(lista_personajes[1])

# 1.3

def agregar_iniciales_nombre(lista:list):
   if len(lista) > 0 and  type(lista) == type(list()):
        for e_lista in lista:
            iniciales = definir_iniciales_nombre(e_lista) 
            if iniciales == False:
                print("El origen de datos no contiene el formato correcto")
                return False       
        return True
   
# agregar_iniciales_nombre(lista_personajes)

#1.3

def stark_imprimir_nombres_con_iniciales(lista: list):
    if len(lista) > 0 and  type(lista) == type(list()):
        agregar_iniciales_nombre(lista)
        for e_lista in lista:
            print(e_lista["nombre"],'(',e_lista["iniciales"],')')

    
# stark_imprimir_nombres_con_iniciales(lista_personajes)

# 2.1
def generar_codigo_heroe(id_nombre:int, genero_heroe:str):
    if type(id_nombre) == type(int) and len(genero_heroe)> 0  or  genero_heroe == 'F' or genero_heroe == 'M' or genero_heroe == "NB" :
        id_nombre = str(id_nombre)
        if len(id_nombre) > 0 and len(id_nombre) < 9:
            if genero_heroe == 'F' or genero_heroe == 'M':
                id_nombre = str(id_nombre)
                id_nombre = id_nombre.zfill(8)
            else:
                id_nombre = str(id_nombre)
                id_nombre = id_nombre.zfill(7)
            retorno = genero_heroe + "-" + id_nombre
            return retorno
        else:
            return "validacion incorrecta"
    else:
        return "N/A"
# asd = generar_codigo_heroe(123,'F')
# print(asd)

# 2.2

def agregar_codigo_heroe(heroe: dict, id_heroe: int):
    if type(heroe) == type(dict()): #and len(generar_codigo_heroe(id_heroe,heroe["genero"])) == 10:
        codigo = generar_codigo_heroe(id_heroe,heroe["genero"])
        heroe["codigo_heroe"] = codigo
        return True
    else:
        return False

#print(agregar_codigo_heroe(lista_personajes[1],123))

#2.3

def stark_generar_codigos_heroes(lista:list):
    if len(lista) > 0 :
        contador_heroes = 0
        for e_lista in lista:
            if type(e_lista) == type(dict()) and "genero" in e_lista:
                contador_heroes+= 1
                agregar_codigo_heroe(e_lista,contador_heroes)
                #print(e_lista["codigo_heroe"])
            else:
                mensaje = "El origen de datos no contiene el formato correcto"
        mensaje = "Se asignaron:{0}\nEl código del primer héroe es: {1}\nEl código del del último héroe es: {2}".format(contador_heroes,lista[0]["codigo_heroe"],lista[23]["codigo_heroe"])  
        print(mensaje)
# stark_generar_codigos_heroes(lista_personajes)

# 3.1
def sanitizar_entero(numero_str: str):
    numero_str = numero_str.strip()
    if type(numero_str) == type(str()) and numero_str.isdigit():
        numero_str = int(numero_str)
        return numero_str
    elif re.findall("[A-Za-z]+",numero_str):
        return "-1" 
    elif numero_str < "0" and numero_str.isdigit() == True:
        return "-2"
    else:
        return "-3"
    
# print(sanitizar_entero("123"))


# 3.2 
def sanitizar_flotante(numero_str: str):
    retorno = "-3"
    numero_flotante_str = numero_str.strip()
    if re.findall("[a-zA-Z]+",numero_flotante_str):
        retorno = "-1"
    if re.findall("[0-9]",numero_flotante_str):
        numero_flotante_str = float(numero_flotante_str)
        retorno = numero_flotante_str
        if numero_flotante_str < 0:
            retorno = "-2"
    return retorno
# print(sanitizar_flotante("/"))

# 3.3
def sanitizar_string(valor_str:str,valor_por_defecto = '-'):
    retorno = "N/A"
    valor_str = valor_str.strip()

    if type(valor_str) == type(str()):
        if valor_str != "":
            if re.findall("[a-zA-Z]+",valor_str):
                valor_str = valor_str.replace("/"," ")
                retorno = valor_str.lower()
        else:
            retorno = valor_por_defecto.lower()
    return retorno

# print(sanitizar_string("Hasda","a"))

# 3.4

def sanitizar_dato(heroe: dict,clave:str,tipo_dato:str):
    
    tipo_dato = tipo_dato.lower()
    if tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante":
        if clave in heroe:
            if tipo_dato == "entero":
                heroe[clave] = sanitizar_entero(heroe[clave])
                return True
            elif tipo_dato == "flotante":
                heroe[clave] = sanitizar_flotante(heroe[clave])
                return True
            elif tipo_dato == "string":
                heroe[clave] = sanitizar_string(heroe[clave])
                return True
            else:
                return False  
        else:
            print("La clave especificada no existe en el héroe")    
    else:
        print("Tipo de dato no reconocido")
# print(sanitizar_dato(lista_personajes[0],"altura","flotante"))

#3.5
def stark_normalizar_datos(lista:list):
    if type(lista) == type(list()):
        for e_lista in lista:
            (e_lista,"altura","flotante")
            (e_lista,"peso","flotante")
            (e_lista,"color_ojos","string")
            (e_lista,"color_pelo","string")
            (e_lista,"fuerza","entero")
            (e_lista,"inteligencia","string")
        print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía") 

# stark_normalizar_datos(lista_personajes)

# 4.1
def generar_indice_nombres(lista:list):
    acumulador_de_nombres = []
    
    if len(lista) > 0 :
        for e_lista in lista:
            if type(e_lista) == type(dict()) and "nombre" in e_lista:
                e_lista["nombre"] = str(e_lista["nombre"])
                e_lista["nombre"] = e_lista["nombre"].replace("-",",")
                nombre = e_lista["nombre"]
                nombre = re.split(" ",e_lista["nombre"])
                acumulador_de_nombres  += nombre
        return acumulador_de_nombres
    else:
        print("El origen de datos no contiene el formato correcto ")   

# generar_indice_nombres(lista_personajes)

# 4.2
def stark_imprimir_indice_nombre(lista:list):
    nombres = generar_indice_nombres(lista)
    indice = '-'.join(nombres)
    print(indice)

#stark_imprimir_indice_nombre(lista_personajes)

def convertir_cm_a_mtrs(valor_cm: int):
        if valor_cm > 0:
            return valor_cm / 100
        else:
            return -1  

print(convertir_cm_a_mtrs(50600))