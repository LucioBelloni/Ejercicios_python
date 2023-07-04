# Expresiones regulares
import re

"""ingreso = input("Ingrese una edad: ") #strong str

if ingreso.isdigit():
    edad = int(ingreso)
    print(f"La edad es: {edad}")
else:
    print("No es un numero lo ingresado")
"""
"""
    "Marina"
    ()  ---
    []  ---> CONJUNTO [aeiou] [a-z] [A-Z] [0-9]
    {4} ---> cuantas veces

    +
    ^
    $

    \d --> todos los digitos
    \w --> alfa numerico           no es muy seguro 
    \s --> todos los seperados 


"""
"""
texto = "Ihola 123"

texto = "hola . mundo .. crual"

print(re.split(' \.{1,2} ',texto))

name = "Marina anabe11a Cardozo"
print(re.sub('[0-9]','',name))
"""
"""
texto = 'Chola 1234'  #primera letra mayuscula hola 4 4 digitos
                      # ^ empieza con PRIMER LETRA MAYUSCULA

if re.match('(^[A-Z][a-z]{4}) ([0-9]{4})',texto):
    print("se cumple")
else:
    print("No se cumple") 
"""


saludo = "¡Hola! ¿como estas? "

print(re.findall('[a-z]{4} [a-z]{5}',saludo))


fecha = "hoy es 2023/04/09 y son los 10:04:00, 12:04:00"

print(re.findall("[0-9]{4}",fecha))
print(re.findall("[0-9]{4}/[0-9]{2}/[0-9]{2}",fecha))
print(re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}",fecha))
