""" while True:
    tipo = input("Ingrese la contrasenia: ")
    if tipo in("utn", "UTN"):
        break """ 


"""respuesta = 's'

while(respuesta == 's'):
    respuesta = input("¿Desea continuar? s/n ")"""

"""i = 0
while(i < 5):
    i = i + 1 
    print(i)"""

"""destino = "Bariloche"

 
match destino:       
    case "Bariloche":
        print("Hace frio")
    case "Cataratas":
        print("Hace calor")
    case _: 
        print("Selecciono Otro")"""

"""numero = 7 
if numero > 8:
    print("No imprimio")
elif numero > 5:
    print("Voy a imprimir")
elif numero > 6:
    print("No voy a imprimir")
else:
    print("No imprimo ni loco ")


nombre = input("Ingrese su nombre")
sueldo = input("Ingrese su sueldo")
aumento = float(sueldo) * 1.10
print()"""



"""dic_test = {"a": 22, "b": "Hola" , "c": 3 }
print(dic_test)
print(dic_test["a"])

dic_test["a"] = 28
print(dic_test["a"])
dic_test['d'] = 4
print(dic_test)

print(dic_test.items())
print(dic_test.values())"""


"""""""""-----------------------------------------------------------"""

"""dic_test = {"a": 22, "b": "Hola" , "c": 3 }

lista = list (dic_test.values())

for e_lista in lista:
    print(e_lista)"""

dic_test = {"a": 22, "b": "Hola" , "c": 3 }
lista = [{"a": 22, "b": "Hola" , "c": 3 }]

print(lista)
print(lista[0] ['a'])

"""for item in lista: 
    print(item["key"])"""