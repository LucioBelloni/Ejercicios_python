import re 
#metodos del tipo str
"""cad = "QUEVEDO || BZRP Music Sessions #52"
lista = cad.split("||")
lista2 = lista[1].split("#")
artista = lista[0]
tipo = lista2[0]
numero = lista2[1]
print("Artista: {0}\ntipo: {1}\nnumero: {2}".format(artista,tipo,numero))"""

"""cad = "QUEVEDO || BZRP Music Sessions #52"
lista = re.split("[\|#]+",cad)
artisa = lista[0]
tipo = lista[1]
numero = lista[2]
print("Artista: {0}\ntipo: {1}\nnumero: {2}".format(artisa,tipo,numero))"""

"""cad = "2022-07-06 00:00:00"
lista = re.split("[-: ]+",cad)
print(lista)

anio = lista[0]
mes = lista[1]
dia = lista[2]
hora = lista[3]
minutos = lista[4]
segundos = lista[5]

print("anio: {0}\nmes: {1}\ndia:{2}\nhora:{3}\nminutos:{4}\nsegundos{5}".format(anio,mes,dia,hora,minutos,segundos))
"""

cad = "2022-07-06 00:00:00"
mes = re.findall("([0-9]{1,2}):([0-9]{2}):([0-9]{2})",cad)
print(mes)
