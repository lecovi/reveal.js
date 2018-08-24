class Persona:
    """Abstracción de los objetos Persona"""
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Acabo de ser creado y me llamo {self.nombre}")

    def avanzar(self):
        print(f"Soy {self.nombre} y estoy caminando hacia adelante!")
