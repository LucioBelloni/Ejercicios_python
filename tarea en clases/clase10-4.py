"""def restar(var_a:int, var_b:int =5)-> int:
    return var_a - var_b

resultado = restar(10,3)
print(resultado)"""

# Pedir 2 numeros y mostrar la suma
# No tiene parametros/argumentos no tiene retorno 

"""def calcular_suma():
    num1 = int(input("Ingrese un numero"))
    num2 = int(input("Ingrese un numero"))
    resultado = num1 + num2
    print("La suma es:{0}".format(resultado))

calcular_suma()"""

"""
# Si tiene paramostros/argumentos no tiene retorno
def calcular_suma(numero1:int, numero2:int):
    resultado = numero1 + numero2
    print("La suma es:{0}".format(resultado))

num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese un numero"))

calcular_suma(num1,num2)
"""

# Si tiene paramostros/argumentos si tiene retorno

def calcular_suma(numero1:int, numero2:int):
    resultado = numero1 + numero2
    return resultado

# Programa principal 
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese un numero"))
suma = calcular_suma(num1,num2)

print("La suma es:{0}".format(suma))


