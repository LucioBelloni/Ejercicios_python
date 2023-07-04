import json
import re

def parse_json(nombre_arcivos:str)->list:

    with open(nombre_arcivos,"r") as archivo:
        lista_final=[]
        todo_texto = archivo.read()
        #print(todo_texto)
        titulo = re.findall(r'"nombre": "([ a-zA-Z0-9\|  #-\\ ]+)',todo_texto)
        vistas = re.findall(r'"vie')
        print(titulo)

    return lista_final

lista = parse_json("data_stark.json")
