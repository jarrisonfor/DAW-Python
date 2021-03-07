
"""
Donde se usa:
2.11.py
"""
from datetime import datetime

class AgendaCarnaval:
    __fecha = ''
    __lugar = ''
    __nombre = ''
    __descripcion = ''
    __imagen = ''

    def __init__(self, nombre='', descripcion='', imagen='', lugar='Recinto Ferial', fecha=datetime.now()):
        self.setLugar(lugar)
        self.setNombre(nombre)
        self.setDescripcion(descripcion)
        self.setImagen(imagen)
        self.setFecha(fecha)

    def getLugar(self):
        return self.__lugar
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def getImagen(self):
        return self.__imagen
    def getFecha(self):
        return self.__fecha

    def setLugar(self, lugar):
        self.__lugar = lugar
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setDescripcion(self, descripcion):
        self.limitarCaracteres(descripcion)
    def setImagen(self, imagen):
        self.__imagen = imagen
    def setFecha(self, fecha):
        self.__fecha = fecha

    def __str__(self):
        return f'{self.getLugar()}, {self.getNombre()}, {self.getDescripcion()}, {self.getImagen()}, {self.getFecha()}'

    def calcularFecha(self, fecha):
        return f'La diferencia de fechas es de: {fecha - self.__fecha}'

    def limitarCaracteres(self, descripcion):
        if len(descripcion) > 50:
            self.__descripcion = descripcion[0:50]
            print('tas pasao')
        else:
            self.__descripcion = descripcion
