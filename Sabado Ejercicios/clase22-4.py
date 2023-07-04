# pasaje por valor
# pasaje por referencia 
from data_pj import lista_personajes
import re
"""
def sumar(numero: int):
    numero = numero +1
    return numero

a = 3 
b = sumar(a)
print("Este es el valor de a:" ,a)
print("Este es el valor de b:", b)

def agregar_personas(lista:list,nombre:str):
    lista.append(nombre)

lista_nombres = ["Marina","Pedro"]
print(lista_nombres)

agregar_personas(lista_nombres,"juan")
print(lista_nombres)

def listar_por_caracteres(lista:list[dict],caracteristica:str)-> None:
    for element in lista:
        print(element[caracteristica])

listar_por_caracteres(lista_personajes,"nombre")
"""

"""
def pedir_datos(texto: str)-> int:
    numero = input(texto)
    numero = int(numero)
    return numero


def sumar()-> int:
    primer_numero = pedir_datos("Ingrese la edad")
    segundo_numero = pedir_datos("Ingrese la edad")
    resultado = primer_numero + segundo_numero
    return resultado

resultado = sumar()

print(resultado)
"""
""""
nombre = "Lucio"

nombre = nombre + " Belloni"

ejemplo = len(nombre)
print(ejemplo)

print(nombre.upper())

print(nombre.lower())

saludo = "                hola           "
prueba = saludo.strip()
print(prueba)

prueba = nombre.split()
print(prueba)

prueba_dos = " ".join(prueba)
print(prueba_dos)

# [inicio:fin:paso]  slicing  

print(nombre[0])

print(nombre[:6:2])

nombre[0] = 'F'
print(nombre)

"""

def contar_cadenas(cadena:str):
    print(len(cadena))

contar_cadenas("hola")


def eliminar_caracter(cadena:str, caracter: str):
    caracter = cadena.replace(caracter, "")
    print(caracter)

eliminar_caracter("hola mundo", "la")


def contar_palabras(cadena:str, caracter: str):
    caracter = cadena.split(" ")
    print(caracter)

contar_palabras("hola mundo", "")

def remplazar_palabras(cadena: str, palabra: str, palabra_dos: str):
    cadena = cadena.replace(palabra,palabra_dos)
    print(cadena)

remplazar_palabras("hola mundo", "a", "b")

def buscar_patron(cadena:str, patron:str):
    cadena = cadena 
    patron = patron

    index = cadena.split(patron)
    print(index)

# buscar_patron("Hola mundo", 

lista1 = [1,2,3]
lista2 = ['a','b','c']

for e_lista1 in lista1:
    for e_lista2 in lista2:
        print(e_lista1,e_lista2)