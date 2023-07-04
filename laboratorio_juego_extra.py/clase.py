class Personaje:
    '''
    Documentar la clase
    '''
    tipo = "x"

    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.lista = ["HOLA","PEPE","JUAN"]

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def __str__(self) -> str:
        return  self.__nombre + " HOLA"
    
    def __len__(self):
        return 8
    def __getitem__(self,index):
        if index == "nombre":
            return self.__nombre
        else:
            return ""
    def __setitem__(self,index,valor):
        if index == "nombre":
            self.__nombre = valor
    
    def __iter__(self):
        for i in self.lista:
            yield i
            
            

aux = Personaje("Vero")
aux["nombre"] = "juan"
print(aux["nombre"])
print(aux.nombre)

contador = 0
for elemento in aux:
    contador += 1
    print(elemento)
print(contador)

"""aux_personaje1 = Personaje("PEPE")
aux_personaje2 = Personaje("JUANA")
aux_personaje2.mostrar()
aux_personaje1.mostrar()

print(aux_personaje1.tipo)
print(aux_personaje2.tipo)
print(Personaje.tipo)"""



