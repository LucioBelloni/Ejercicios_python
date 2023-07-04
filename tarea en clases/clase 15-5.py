"""x = 43 
if x == 42:
    result = "es la respuesta"
else:
    result = "anduviste cerca"

print(result)"""

# expresion condicional 

"""x = 43 
resultado = "es la respuesta" if x == 42 else "anduviste cerca"

print(resultado)"""

"""def idenificar(num)-> str:
    result = "es par" if num % 2 == 0 else "no es par"
    return result

respuesta = idenificar(4)
print(respuesta)

con lambda
"""

# print((lambda num : "es par" if num % 2 == 0 else "no es par")(2))
"""
lista = [10,20,30,40]
print(lista)
copia_lista = lista.copy()  # shallow copy
copia_lista[3] = "Roberto"

print(copia_lista)
print(lista)
"""
from copy import deepcopy

"""lista = [
    {"nombre": "Ana", "edad":25,"nota":9},
    {"nombre": "Jose", "edad":34,"nota":8},
]  
    
lista1 = [
    {"nombre": "Sol", "edad":46,"nota":7},
    {"nombre": "Beto", "edad":28,"nota":6},
]

lista2 = []

print("LISTA", lista)
print("LISTA1", lista1)

lista2.extend(lista)
print("lista 2 extendida - parte1", lista2)
lista2.extend(lista1)
print("lista 2 extendida parte 2", lista2)

"""


"""print("LISTA ORIGINAL", lista)
copia_lista = deepcopy(lista) #deepcopy 
copia_lista[3]["nombre"] = "Roberto"""

# print("LISTA ORIGINAL", lista)
""""
lista = [
    {"nombre": "Ana", "edad":25,"nota":9},
    {"nombre": "Jose", "edad":34,"nota":8},
    {"nombre": "Sol", "edad":46,"nota":7},
    {"nombre": "Beto", "edad":28,"nota":6},
]  

print(lista)

for i,elemento in enumerate(lista):
    print(i,elemento)

nombres = [
    {"nombre": "Ana", "edad":25,"nota":9},
    {"nombre": "Jose", "edad":34,"nota":8},
    {"nombre": "Sol", "edad":46,"nota":7},
    {"nombre": "Beto", "edad":28,"nota":6},
]  

print(lista)

for i,elemento in enumerate(lista):
    print(i,elemento)

"""

"""from functools import reduce

lista = [2,4,6,8]

print(reduce(lambda a,b: a*b ,lista))"""



"""lista = [{"nombre": "Ana", "edad": 25, "nota": 9},
         {"nombre": "Jose", "edad": 34, "nota": 8},
         {"nombre": "Ana", "edad": 46, "nota": 7},
         {"nombre": "Beto", "edad": 28, "nota": 6},]

lista.sort( key =lambda alumno: alumno["nota"]  , reverse=True)
print(lista)"""

# Diccionarios 

lista = [
        {"edad": 25, "nota": 9},
         {"nombre": "Jose", "edad": 34, "nota": 8},
         {"nombre": "Sol", "edad": 46, "nota": 7},
         {"nombre": "Beto","edad": 28, "nota": 6},]

for i, e_nombre in enumerate(lista):
    nom = e_nombre.get("nombre", "No hay nombre")
    if nom == "No hay nombre":
        vacio = i
        #print("Posiciones sin key: ", i )

dic_cero = dict(lista[1])
# valor_eliminado = dic_cero.pop("nombre","Sin nombre")
# print("Valor eliminado: ", valor_eliminado)
dic_cero.update({"nombre":"Lucio"})
lista[1] = dic_cero
print(lista)