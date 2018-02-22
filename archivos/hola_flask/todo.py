from datetime import datetime

class TodoItem:
    """
        Clase que modela los 'quehaceres' de la lista.
    """
    ESTADOS = ('nueva', 'en proceso', 'completada')

    def __init__(self, nombre, estado='nueva'):
        self.nombre = nombre
        if estado not in self.ESTADOS:
            raise ValueError('El estado tiene que ser alguno de ', self.ESTADOS)
        self.estado = estado
        self.fechahora = datetime.utcnow()

    def avanzar_estado(self):
        indice_estado_actual = self.ESTADOS.index(self.estado)
        if indice_estado_actual + 1 < len(self.ESTADOS):
            self.estado = self.ESTADOS[indice_estado_actual + 1]
            self.fechahora = datetime.utcnow()
            return True
        return False

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS:
            raise ValueError('El estado tiene que ser alguno de ', self.ESTADOS)
        self.estado = nuevo_estado
        self.fechahora = datetime.utcnow()

    def esta_completa(self):
        if self.estado == 'completada':
            return True
        return False

    def __repr__(self):
        return '<ToDoItem {}>'.format(self.nombre)

    def __str__(self):
        return '<ToDoItem {} {} {}>'.format(self.nombre, self.estado, self.fechahora) 
