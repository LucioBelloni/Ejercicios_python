"""class Persona:
    tipo = "Persona"

    def __init__(self,nombre,apellido,edad,genero = "") -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero 

def presentarse(self):
    print(f"!Hola! Mi nombre es{self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")
"""


class Auto:
    def __init__(self,p_marca,p_color_,p_numero,p_velocidad_max) -> None:
        self.marca = p_marca
        self.color = p_color_
        self.numero = p_numero
        self.velocida_max = p_velocidad_max

    def acelerar(self):
        return "soy muy rapido {0}".format(self.velocida_max)
    
auto_uno = Auto("toyota","rojo",10,180)
auto_dos = Auto("fiat","azul",25,300)

print(auto_uno.acelerar())
print(auto_dos.acelerar())
