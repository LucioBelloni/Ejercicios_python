
"""edad = input("ingrese su edad")

edad = int(edad)

if edad > 17:
    print("usted ya es mayor de edad")
elif edad < 13:
    print("usted es un niño")
elif edad >= 13:
    print("adolescente")"""

""""
i = 0
contador_impares = 0
contador_pares = 0

bandera_menor_numero = 0
numero_mas_chico = 0

mayor_numero_par = 0
bandera_mayor_numero_par = 0

suma_positivos = 0

producto_de_negativos = 1

while(i < 5):
    i = i + 1

    entero = int(input("ingresa cualquier numero entero. "))
    while(entero == 0):
        entero = int(input("ingreso el numero 0, vuelva a intentar "))

    if entero % 2 == 0:
        contador_pares += 1

        if bandera_mayor_numero_par == 0:
            mayor_numero_par = entero
            bandera_mayor_numero_par = 1
        elif entero > mayor_numero_par:
            mayor_numero_par = entero

    else:
        contador_impares += 1

    if bandera_menor_numero == 0:
        numero_mas_chico = entero
        bandera_menor_numero = 1
    elif entero < numero_mas_chico:
        numero_mas_chico = entero

    if entero > 0:
        suma_positivos += entero
    else:
        producto_de_negativos *= entero

print("la cantidad de numeros pares es de: ", contador_pares)
print("la cantidad de numeros impares es de: ", contador_impares)
print("el numero mas chico es : ", numero_mas_chico)
print("el numero par mas grande ingresado es el: ", mayor_numero_par)
print("la suma de todos los numeros positivos es de: ", suma_positivos)
print("el producto de los negativos es de: ", producto_de_negativos)   
"""

"""
edad = int(input("ingrese su edad: "))
estado_civil = input("ingrese su estado civil.  CASADO/SOLTERO: ")

if edad < 18:
    estado_civil = estado_civil.lower()
    if estado_civil == "casado":
        print("es muy pequeño para NO ser soltero")
    else:
        print("muy bien")
"""






""""
tarifa_base = 15000
estacion = input("ingrese una estacion del año. INVIERNO/VERANO/OTOÑO/PRIMAVERA: ")
estacion = estacion.lower()
while estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera":
    estacion = input("ingreso algo distinto a las estaciones mostradas, vuelva a intentar. INVIERNO/VERANO/OTOÑO/PIMAVERA: ")
    estacion = estacion.lower()

localidad = input("ingrese una localidad. BARILOCHE/CATARATAS/MAR DEL PLATA/CORDOBA: ")
localidad = localidad.lower()
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
    localidad = input("ERROR, ingreso mal la localidad vuelva a intentar. BARILOCHE/CATARATAS/MAR DEL PLATA/CORDOBA: ")

match estacion:
    case "invierno":
        tarifa_bariloche = tarifa_base * 1.2
        tarifa_cataratas = tarifa_base * 1.1
        tarifa_cordoba = tarifa_base * 1.1
        tarifa_mar_del_plata = tarifa_base * 0.80
    case "verano":
        tarifa_bariloche = tarifa_base * 0.80
        tarifa_cataratas = tarifa_base * 1.1
        tarifa_cordoba = tarifa_base * 1.1
        tarifa_mar_del_plata = tarifa_base * 1.2
    case "otoño":
        tarifa_bariloche = tarifa_base * 1.1
        tarifa_cataratas = tarifa_base * 1.1
        tarifa_cordoba = tarifa_base
        tarifa_mar_del_plata = tarifa_base * 1.1
    case "primavera":
        tarifa_bariloche = tarifa_base * 1.1
        tarifa_cataratas = tarifa_base * 1.1
        tarifa_cordoba = tarifa_base
        tarifa_mar_del_plata = tarifa_base * 1.1

match localidad:
    case "bariloche":
        print("el precio final de bariloche es de: ", tarifa_bariloche)
    case "cataratas":
        print("el precio final de cataratas es de: ", tarifa_cataratas)
    case "cordoba":
        print("el precio final de cordoba es de: ", tarifa_cordoba)
    case "mar del plata":
        print("el precio final de mar del plata es de: ", tarifa_mar_del_plata)
"""

###############################  29/3 ############################################################

"""restultado = 17 //  2 
print(restultado)"""

# restultado = 10 != 2 
# print("El resultado es " , restultado)
# print(type(restultado))

# resultado = 10 != 2 and 10 > 2 
# print(resultado) 
# print(not(resultado)) el not se usa con precauison 

# lista = [8 , 'a' , 3.14 , "Hola mundo"]
# print(lista[0])
# print(lista[1])
# print(lista[3])
# lista[3] = "Hola Yanina"
# print(lista[0])
# print(lista[1])
# print(lista[3])
# type(lista[2])

# lista = [0,1,2,3,4] 
# lista = list(range(10 , 100 ))

# for e_lista in lista :
    # print(e_lista)

# for i in range(5):
    # print(i)

"""lista1 = [1,2,3]
lista2 = ['a','b','c']
lista3 = ["Palabra1", "Palabra2", "Palabra3"]

# FOR ANINADOS

for e_lista1 in lista1:
    print(e_lista1)
    for e_lista2 in lista2:
        print("   " ,e_lista2)
        for e_listta3 in lista3:
            print(e_listta3)
"""



