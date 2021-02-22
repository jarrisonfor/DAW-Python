from abc import ABC, abstractmethod


class Coche(ABC):

    def __init__(self, matricula, marca, modelo, color, propietario=None):
        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._propietario = propietario # Almacenaremos un objeto de tipo cliente

    def getpropietario(self):
        return self._propietario

    def setpropietario(self, propietario):
        self._propietario = propietario

    def getmatricula(self):
        return self._matricula

    def setmatricula(self, matricula):
        self._matricula = matricula

    def getmarca(self):
        return self._marca

    def setmarca(self, marca):
        self._marca = marca

    def getmodelo(self):
        return self._modelo

    def setmodelo(self, modelo):
        self._modelo = modelo

    def getcolor(self):
        return self._color

    def setcolor(self, color):
        self._color = color

    @abstractmethod
    def __str__(self):
        cadena = ""
        # Código a implementar
        return cadena