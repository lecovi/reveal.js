import trabajador

class Persona:
    def __init__(self, edad):
        self.edad = edad


class Empleado(Persona, trabajador.Trabajador):
    """Este empleado puede trabajar()"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def identidad(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")
