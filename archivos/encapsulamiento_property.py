class Encapsulamiento:
    """ Esta clase tiene 3 atributos y 3 métodos propios.

        >>> # El atributo privado es accesible a través de una Propiedad.
        >>> x = Encapsulamiento()
        >>> x.atributo_publico
        este atributo es privado.
        >>> x._atributo_semi_privado
        este atributo es 'casi' privado.
        >>> x.atributo_privado
        este atributo es privado.
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

    @property
    def atributo_privado(self):
        return self.__atributo_privado

    @atributo_privado.setter
    def atributo_privado(self, valor):
        self.__atributo_privado = valor
