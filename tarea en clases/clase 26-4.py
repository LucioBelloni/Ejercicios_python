# por valor: hago una copia del contenido de la varraible del main dentro de la funcion
# por referencia: manejo directamente la variable 

# simples: por valor  int bool 
# Compuestos: por referencia list dict 



# def doblar_valor(numero):
    # return numero * 2

# n = 10


# print(doblar_valor(n))

"""lista = [2,4,1,6]

def copiar_lista(lista_recibida: list)-> list:
    #shallow copy 
    lista_duplicada = lista_recibida.copy()
    lista_duplicada[0] = 99
    return lista_duplicada

print(lista)
lista_retorno = copiar_lista(lista)
print(lista)
print(lista_retorno)"""
"""
menor = 23 
mayor = 56 
aux = 0
print("menor: ", menor)
print("menor: ", mayor)
print("")
#  intercambiar los valores de mayor x menor y vicerversa 
# swap 
aux = menor
menor = mayor
mayor = aux

print("menor: ", menor)
print("menor: ", mayor)
print("")
bandera_swap = True

lista = [2,6,8,3,9,1]
print(lista)

while bandera_swap == True:
    bandera_swap = False
    for i in range( len(lista)-1):
        if lista[i] > lista[i+1]:
            auxiliar = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = auxiliar
            bandera_swap = True
print(lista)
"""

lista = [{"nombre": "Ana","edad":25, "nota":9},
         {"nombre": "Jose","edad":34, "nota":8},
         {"nombre": "Ana","edad":46, "nota":7},
         {"nombre": "Beto","edad":28, "nota":6},
         ]

bandera_swap = True
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

while bandera_swap == True:
    bandera_swap = False
    for i in  range(len(lista)-1):
        if lista[i]["nombre"] > lista[i+1]["nombre"]:
            auxiliar = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = auxiliar
            bandera_swap = True
        if lista[i]["nombre"]  == lista[i+1]["nombre"]:
            if lista[i]["nota"] > lista[i+1]["nota"]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                bandera_swap = True

print("lista ordenada" )
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

