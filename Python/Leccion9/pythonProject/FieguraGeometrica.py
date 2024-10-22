from Leccion6.pythonProject1.Cubo import ancho


class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0  # Corregido: debe ser self._ancho
            print(f"Valor erróneo para el ancho: {ancho}")

        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0  # Corregido: debe ser self._alto
            print(f"Valor erróneo para el alto: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
    else:
        print(f"Valor erroneo ancho: {ancho}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):  # Corregido: debería validar alto, no ancho
            self._alto = alto
        else:
            print(f"Valor erroneo ancho: {ancho}")

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"

    def _validar_valores(self, valor):  # Método encapsulado
        return True if 0 < valor < 10 else False  # Corregido: 'True' en lugar de 'true'


