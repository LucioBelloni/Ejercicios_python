"""
Belloni Lucio
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'"""

edad = int(input("Ingrese una edad"))
estado_civil = input("Ingrese un estado civil ")
estado_civil = estado_civil.lower()
while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "divorsiado" :
    estado_civil = input("Error,Ingrese un estado civil correcto ")

if edad < 18 and estado_civil == "casado" and estado_civil != "divorsiado":
    print("Es muy pequeño para NO ser soltero")
else:
    print("Usteded se tiene que arrepentir de lo que dijo")
