"""Belloni Lucio"""

lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

bandera_mayor = 0 

for elemento_lista in lista:
      if  bandera_mayor == 0:
            numero_mayor = elemento_lista 
            bandera_mayor = 1 
      elif elemento_lista > numero_mayor:
            numero_mayor = elemento_lista

       
print("El numero mayor es ", numero_mayor)