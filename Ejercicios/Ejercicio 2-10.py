"""
Belloni Lucio
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]"""

alumnos = list([])
sexo = list([])
nota = list([])

bandera_nota_mas_baja_masculina = 0
suma_nota_mujeres = 0
nota_mas_baja_masculina = 0
indice_hombre = 0
cantidad_notas_mujeres = 0
nombre_nota_mas_baja = "no hay hombres"

for e_alumnos in range(0,3,1):
    alumnos_nombres = input("ingrese el nombre del alumno: ")
    alumnos.append(alumnos_nombres)

    alumnos_sexo = input("ingrese su sexo: M/F: ")
    alumnos_sexo = alumnos_sexo.lower()
    while(alumnos_sexo != "m" and alumnos_sexo != "f"):
        alumnos_sexo = input("ingrese su sexo: M/F: ")
        alumnos_sexo = alumnos_sexo.lower()

    sexo.append(alumnos_sexo)

    alumnos_nota = int(input("ingrese su nota: "))
    while(alumnos_nota > 10 or alumnos_nota < 1):
        alumnos_nota = int(input("Error, vuelva ingresar la nota: "))

    if alumnos_sexo == "m" and bandera_nota_mas_baja_masculina == 0:
        nota_mas_baja_masculina = alumnos_nota
        nombre_nota_mas_baja = alumnos_nombres
        bandera_nota_mas_baja_masculina = 1

    elif nota_mas_baja_masculina > alumnos_nota:
        nota_mas_baja_masculina = alumnos_nota
        nombre_nota_mas_baja = alumnos_nombres

    nota.append(alumnos_nota)

    if alumnos_sexo == "f":
       suma_nota_mujeres += alumnos_nota
       cantidad_notas_mujeres += 1
       promedio_mujeres = suma_nota_mujeres / cantidad_notas_mujeres

print("El nombre de la nota mas baja de un hombre es : ", nombre_nota_mas_baja)
print("El promedio de las notas de las mujeres es : ", promedio_mujeres)
