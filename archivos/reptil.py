class Reptil:
    """Abstracción de los objetos Reptiles"""
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Acabo de ser creado y me llamo {self.nombre}")

    def avanzar(self):
        print(f"Soy {self.nombre} y estoy reptando hacia adelante!")