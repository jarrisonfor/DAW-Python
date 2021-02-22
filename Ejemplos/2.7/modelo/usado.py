from modelo.coche import *


class Usado(Coche):

    def __init__(self, matricula, marca, modelo, color,  kms, propietario=None):
        super(Usado, self).__init__(matricula, marca, modelo, color, propietario)
        self._kms = kms

    def getkms(self):
        return self._kms

    def setkms(self, kms):
        self._kms = kms

    def __str__(self):
        cadena = ""
        # Código a implementar
        return cadena