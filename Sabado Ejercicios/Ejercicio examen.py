"""3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
cantidad de carreras ganadas (no pueden ser números negativos)
número del vehículo (no puede ser un número negativo)
se necesita saber:
*Nacionalidad del piloto más joven.
*Cantidad de vehículos con número par.
*Nombre del piloto con menos victorias y el número de auto impar.
*Cantidad de pilotos mayores de 25 años con número de vehículo impar.
*Nombre del piloto más joven con más victorias.
*Nacionalidad del piloto más veterano con menos victorias.
*Promedio de edad de los pilotos que tiene un vehículo con número par."""

bandera_del_piloto_mas_joven = 0
contador_vehiculo_par = 0
contador_vehiculo_inpar = 0
bandera_del_piloto_con_menos_victorias = 0
contador_de_pilotos_mayores = 0
bandera_del_piloto_mas_veterano = 0
bandera_persona_mas_vieja = 0

for i in range(0,2,1):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    while edad < 18:
        edad = int(input("Eror ingrese la edad: "))
    nacionalidad = input("Ingrese su nacionalidad: ") 
    nacionalidad = nacionalidad.lower()
    while nacionalidad != "argentino" and nacionalidad != "ingles" and nacionalidad != "francés" and nacionalidad != "brasilero" and nacionalidad != "estadounidense":
        nacionalidad = input("Error, ingrese la nacionalidad correcta")
    carreras_ganadas = int(input("Ingrese cantidad de carreras ganadas: "))
    while carreras_ganadas < 0:
        carreras_ganadas = int(input("Eror, ingrese el numero adecuado "))
    numero_del_vehiculo = int(input("Ingrese el numero del vehiculo: "))
    while numero_del_vehiculo < 0:
        numero_del_vehiculo = int(input("Error,Ingrese el numero del vehiculo: "))

    if bandera_del_piloto_mas_joven == 0:
        nacionalidad_del_piloto_mas_joven = nacionalidad
        edad_del_piloto_mas_joven = edad
        bandera_del_piloto_mas_joven = 1
    elif edad < edad_del_piloto_mas_joven:
        nacionalidad_del_piloto_mas_joven = nacionalidad
        edad_del_piloto_mas_joven = edad
        
    if numero_del_vehiculo % 2 == 0:
        contador_vehiculo_par += 1
        edades_totales = edad + edades_totales
        edad_promedio = edades_totales / contador_vehiculo_par
        

       
    if bandera_del_piloto_con_menos_victorias == 0:
        nombre_del_piloto_con_menos_victorias = nombre
        menos_victorias = carreras_ganadas
        if numero_del_vehiculo % 2 != 0:
            patente = numero_del_vehiculo
        bandera_del_piloto_con_menos_victorias = 1
    elif carreras_ganadas < menos_victorias:
        nombre_del_piloto_con_menos_victorias = nombre
        menos_victorias = carreras_ganadas 
        if numero_del_vehiculo % 2 != 0:
            patente = numero_del_vehiculo
    if edad > 25:
        contador_de_pilotos_mayores += 1
        if numero_del_vehiculo % 2 != 0:
            patente_vehiculo_impar = numero_del_vehiculo
    

    if bandera_del_piloto_mas_veterano == 0:
        nacionalidad_piloto_mas_veterano = nacionalidad
        veterano_menos_victorias = carreras_ganadas
        if bandera_persona_mas_vieja == 0:
            persona_mas_vieja = nombre
            edad_persona_mas_vieja = edad
            bandera_persona_mas_vieja = 1
        elif edad > edad_persona_mas_vieja:
            persona_mas_vieja = nombre
            edad_persona_mas_vieja = edad
 
        bandera_del_piloto_con_menos_victorias = 1
    elif carreras_ganadas < veterano_menos_victorias:
        nacionalidad_piloto_mas_veterano = nacionalidad
        veterano_menos_victorias = carreras_ganadas
        if bandera_persona_mas_vieja == 0:
            persona_mas_vieja = nombre
            edad_persona_mas_vieja = edad
            bandera_persona_mas_vieja = 1
        elif edad > edad_persona_mas_vieja:
            persona_mas_vieja = nombre
            edad_persona_mas_vieja = edad


print("La nacionalidad del piloto mas joven es: ", nacionalidad_del_piloto_mas_joven )
print("La cantidad de vehiculos par es: ",contador_vehiculo_par)  
print("El nombre del pilotto con menos victorias es: ", nombre_del_piloto_con_menos_victorias , "Y el numero del auto es", patente)
print("La nacionalidad del pilotto mas joven es ", nacionalidad_piloto_mas_veterano , "con ", veterano_menos_victorias, "victorias")

