from TrabajosPracticos.data import lista_bzrp

# print(lista_bzrp[0]['title'])

# for e_lista in lista_bzrp:
    # print(e_lista["title"])

"""
maximo = lista_bzrp[0]["views"]
maximo_titulo = lista_bzrp[0]["title"]

for e_lista in lista_bzrp:
    if maximo < e_lista["views"]:
        maximo = e_lista["views"]
        maximo_titulo = e_lista["title"] 

print(maximo, maximo_titulo)"""

dic_maximo = lista_bzrp[0]

for e_lista in lista_bzrp:
    if e_lista['views'] > dic_maximo['views']:
        dic_maximo = e_lista

print(dic_maximo)

