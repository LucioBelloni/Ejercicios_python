"""edad = 21
nombre = "Lucio"

print("Su nombre es: {} y tiene {} años ".format(nombre,edad)) # argumentos posicionales

print("Su nombre es: {0} y tiene {1} años ".format(nombre,edad)) # argumentos posicionales
 
print("Su nombre es: {nom} y tiene {anios} años".format(nom="ana", anios="23")) #argumentos nombrados

print("su nombre es: {0} y tiene {anios} años ".format(nombre, anios= 12)) #mixto"""

# dic_test = {"a":22 ,"b":"hola", "c":3.41231231312412}

# print("Elemento a {0[a]:.2f} y el elemente b es: {0[b]:s} y el elemento c es: {0[c]:.2f}".format(dic_test))  #entre corchetes para buscar el value


"""from data import lista_bzrp
def tema_mas_visto():
    dic_maximo = lista_bzrp[0]
    for e_lista in lista_bzrp:
        if e_lista["views"] > dic_maximo["views"]:
            dic_maximo = e_lista
    print("Tema mas visto: titulo: {0} vistas: {1}".format(dic_maximo["title"], dic_maximo["views"]))
def temas_menos_vistos():
    dic_minimo = lista_bzrp[0]
    for e_lista in lista_bzrp:
        if e_lista["views"] < dic_minimo["views"]:
            dic_minimo = e_lista
    print("Tema manos visto: titulo: {0} vistas: {1}".format(dic_minimo["title"], dic_minimo["views"]))

"""

"""""
    1- Tema mas visto
    2- Tema menos visto
    3- Modificacion
    4- Salir
"""
# while True:
    # print("\n1-Tema mas visto\n2-Tema menos visto\n3-Salir\n")
    # opcion = int(input("Opcion: "))
    # if opcion == 1:
        # tema_mas_visto()
    # elif opcion == 2:
        # temas_menos_vistos()
    # elif opcion == 3:
        # break
# print("Finde del probrama ")
"""

"""