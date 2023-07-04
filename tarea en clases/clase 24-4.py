def parse_csv(nombre_archivo:str)->list:
    lista = []
    with open(nombre_archivo,"r") as archivo:
        for e_linea in archivo:
            lista_linea = e_linea.split(",")
        # creamos un diccionario 
            tema = {}
            tema["title"] = lista_linea[0]
            tema["views"] = lista_linea[1]
            tema["length"] = lista_linea[2]
            tema["img_url"] = lista_linea[3]
            tema["url"] = lista_linea[4]
            tema["data"] = lista_linea[5]
            lista.append(tema)
    # archivo.close()
    return lista

def generar_csv(lista:list, nombre_archivo:str):

    with open(nombre_archivo, "w") as archivo:
        for e_tema in lista:
            #printeamos
            mensaje = "{0},{1},{2},{3},{4},{5}"
            mensaje = mensaje.format(
                                    e_tema["title"],
                                    e_tema["views"],
                                    e_tema["length"],
                                    e_tema["img_url"],
                                    e_tema["url"],
                                    e_tema["data"])
            print(mensaje)
            archivo.write(mensaje)



lista = parse_csv("data.csv")
# print(lista)
generar_csv(lista,"data_salida.csv")



