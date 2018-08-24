class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar(self):
        print(f"-{self.nombre}: Trabajo muy duro!" + \
              " Como un esclavo!")


class Jubilado(Trabajador):
    """Hereda de trabajador y sobreescribe trabajar()"""
    def trabajar(self):
        print(f"-{self.nombre}: Ya no trabajo! Soy JUBILADO!!")


class Menor(Trabajador):
    def trabajar(self):
        print(f"-{self.nombre}: EXPLOTADOR!!!!")