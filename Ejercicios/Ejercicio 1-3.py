"""
Belloni Lucio
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos."""

contador_pares = 0
contador_impares = 0
bandera_del_menor_numero = 0
bandera_numero_par = 0
suma_de_positivos = 0
producto_de_negativos = 0

for i in range(0,3,1):
    numero = int(input("Ingrese un numero"))
    while numero <= 0:
        numero = int(input("Eror,Ingrese un numero"))

    if numero % 2 == 0:
        contador_pares += 1
        if bandera_numero_par == 0:
            numero_mayor_ingresado = numero
            bandera_numero_par = 1
        elif numero > numero_mayor_ingresado:
               numero_mayor_ingresado = numero 

    else:
        contador_impares += 1
    
    if bandera_del_menor_numero == 0:
        menor_numero_ingresado = numero
        bandera_del_menor_numero = 1
    elif numero < menor_numero_ingresado:
        menor_numero_ingresado = numero

    if numero > 0:
        suma_de_positivos = numero + suma_de_positivos
    else:
        producto_de_negativos = numero * producto_de_negativos 



print("la cantidad de  numeros pares es:", contador_pares, "La cantidad de numeros impares es:", contador_impares)
print("EL menor numero es: ", menor_numero_ingresado)
print("El mayor numero ingresado de los pares es", numero_mayor_ingresado )
print("Suma de positivos", suma_de_positivos )
print("El producto de los negativos es: ", producto_de_negativos)

