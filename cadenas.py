variable = "s"
variable.strip() #elimina todos los caracteres vacios que pueda contener la variable
#cadena = " hola mundo     "
# cadena = cadena.strip()
# print(cadena) = hola mundo

variable.lower() # convierte las letras en minusculas

variable.upper() # convierte las letras en mayusculas

variable.capitalize() # convierte a mayuscula solo la primer letra en mayuscula
# y el resto en minuscula

variable.replace() #remplaza un conjunto de caracteres por otro
#cadena = "hola mundo"
#cadena = cadena.replace("la","@")
#print(cadena) ho@ mundo

variable.split() #divide una cadedna en subcadenas y las devuelve en una lista
#cadena = "python, java, c"
#print(cadena.split(","))
#['python', 'java', 'c']

variable.join() #devuelve la primera cadena unida a cada uno de los elementos de la lista
#que se le pase como parametro
# cadena = "+"
# cadena = cadena.join(["A", "B", "C"])
#print(cadena) A+B+C

variable.zfill() #rellena la cadena con ceros a la izquierda hasta llegar a la longitud
#pasada como parametro
#cadena = "314"
#print(cadena.zfill(6))
#000314

variable.isalpha() #devuelve true si todos los caracteres son alfabeticos, sino devuelve false
#cadena = "hola mundo"
#print(cadena.isalpha())
#false -> por el espacio

#cadena = "holamundo"
#print(cadena.isalpha())
#true

variable.isalnum() #devuelve true si todos los caracteres son alfanumericos, sino false
#cadena = "hola mundo 123"
#print(cadena.isalnum())
#false -> por el espacio

#cadena = "holamundo123"
#print(cadena.isalnum())
#true

variable.isdigit() #devuelve true si todos los caracteres son SOLO numeros

variable.count() #permite contar las veces que otra cadena se encuentra dentro de la primera
#cadena = "hola mundo hola"
#print(cadena.count("la")) # 2
variable.format() #las llaves, llamadas campos de formato son reemplazadas con los valores de
#las variables pasadas

#nombre_usuario = "JUAN"
#edad_usuario = 35
#cadena = "nombre: {1}, edad: {0}"
#print(cadena.format(edad_usuario,nombre_usuario))
#nombre: JUAN, edad: 35

len() # indica la longitud de la cadena de texto dentro de la variable en ese momento
#cadena = "hola mundo"
#print(len(cadena)) #10

slice #el primer numero es donde comienza(inclusivo) y el segundo indica donde termina(exclusivo)
#cadena = "hola mundo"
#print(cadena[5:10]) #mundo
#print(cadena[5:]) #mundo
#print(cadena[:10]) #hola

#del mi_dict["valor"] se encarga de eliminar el valor del diccionario elegido