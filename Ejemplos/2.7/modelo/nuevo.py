from modelo.coche import *

class Nuevo(Coche):
    def __init__(self, matricula, marca, modelo, color, km0, propietario = None):
        super(Nuevo, self).__init__(matricula, marca, modelo, color, propietario)
        self._km0 = km0

    def getkm0(self):
        return self._km0

    def setkm0(self, km0):
        self._km0 = km0

    def __str__(self):
        cadena = ""
        # Código a implementar
        return cadena