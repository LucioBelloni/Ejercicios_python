"""
Belloni Lucio
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven"""
bandera_edades = 0
posicion = 0
lista_edades = [25,36,18,23,45]
lista_nombre = ["Juan","Ana","Sol","Mario","Sonia"]

for e_edades in lista_edades:
    if bandera_edades == 0:
        edad_mas_joven = e_edades
        bandera_edades = 1
    elif e_edades < edad_mas_joven:
        edad_mas_joven = e_edades
        posicion = lista_edades.index(edad_mas_joven)

print("la edad mas joven es: ", edad_mas_joven, "y su nombre es:" , lista_nombre[posicion])


    
