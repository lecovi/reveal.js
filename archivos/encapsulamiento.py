class Encapsulamiento:
    """ Esta clase tiene 3 atributos y 3 métodos propios.
        
        >>> # Creamos una instancia de la clase
        >>> x = Encapsulamiento()
        >>> # Al atributo público accedemos normalmente.
        >>> x.atributo_publico
        este atributo es público.
        >>> # Lo mismo con el semi_privado. Es una convención.
        >>> x._atributo_semi_privado
        este atributo es 'casi' privado.
        >>> # El atributo privado, no es accesible de la misma manera.
        >>> x.__atributo_privado
        AttributeError: 'Encapsulamiento' object has no attribute '__atributo_privado'
        >>> # Funciona con el Name Mangling
        >>> x._Encapsulamiento__atributo_privado
        este atributo es privado.
        >>> # Lo mismo sucede con los atributos
        >>> x.publico()
        Este es un método Público
        >>> x._semi_privado()
        Este es un método Semi Privado
        >>> x.__privado()
        AttributeError: 'Encapsulamiento' object has no attribute '__privado'
        >>> x._Encapsulamiento__privado()
        Este es un método Privado
    """
    def __init__(self):
        self.__atributo_privado = "este atributo es privado."
        self._atributo_semi_privado = "este atributo es 'casi' privado."
        self.atributo_publico = "este atributo es público."

    def publico(self):
        return "Este es un método Público"

    def _semi_privado(self):
        return "Este es un método Semi Privado"

    def __privado(self):
        return "Este es un método Privado"
