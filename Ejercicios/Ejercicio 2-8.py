"""
Belloni Lucio
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido"""

lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

for e_lista in lista:
    contador_rep = 0
    for segunda_e_lista in lista:
        if e_lista == segunda_e_lista:
            contador_rep += 1
        if contador_rep == 2:
            numero_repetido = e_lista

print("El numero repetido es: ", numero_repetido)




    
