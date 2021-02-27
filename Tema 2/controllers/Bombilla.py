"""
Donde se usa:
2.10.py
"""
import datetime

class Bombilla:
    __encendido = False
    __intensidad = 'alta'

    def getEncendido(self):
        return self.__encendido

    def getIntensidad(self):
        return self.__intensidad

    def switchEncendido(self):
        self.__encendido = not self.__encendido
        if self.__encendido:
            self.__intensidad = 'alta'

    def bajarIntensidad(self):
        if self.__intensidad == 'alta':
            self.__intensidad = 'media'
        elif self.__intensidad == 'media':
            self.__intensidad = 'baja'

    def subirIntensidad(self):
        if self.__intensidad == 'baja':
            self.__intensidad = 'media'
        elif self.__intensidad == 'media':
            self.__intensidad = 'alta'

    def __str__(self):
        string = f"Estado: {self.__encendido}"
        if self.__encendido:
            string += f", Intensidad: {self.__intensidad}"
        return string
