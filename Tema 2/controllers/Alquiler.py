"""
Donde se usa:
2.9.py
"""

from controllers.Socio import Socio
from controllers.Ejemplar import Ejemplar
import TableIt
import os


class Alquiler:
    def __init__(self, socio, ejemplar, aval, fechaSalida, fechaEntrada):
        self.socio = socio
        self.ejemplar = ejemplar
        self.fechaSalida = fechaSalida
        self.fechaEntrada = fechaEntrada
        ejemplar.addAlquiler(self)
        socio.addAlquiler(self, aval)

    def getSocio(self):
        return self.socio

    def getEjemplar(self):
        return self.ejemplar

    def getFechaSalida(self):
        return self.fechaSalida

    def getFechaEntrada(self):
        return self.fechaEntrada

    def setSocio(self, socio):
        self.socio = socio

    def setEjemplar(self, ejemplar):
        self.ejemplar = ejemplar

    def setFechaSalida(self, fechaSalida):
        self.fechaSalida = fechaSalida

    def setFechaEntrada(self, fechaEntrada):
        self.fechaEntrada = fechaEntrada

    def __str__(self):
        string = ''

        if isinstance(self.socio, Socio):
            string += f'{self.socio.getDni()}'
        else:
            string += f'{self.socio}'

        if isinstance(self.ejemplar, Ejemplar):
            string += f';{self.ejemplar.getNumeroEjemplar()}'
        else:
            string += f';{self.ejemplar}'

        string += f';{self.fechaSalida};{self.fechaEntrada}'

        return string

    @staticmethod
    def saveAlquilerDb(alquiler, databasePath):
        with open(f'{databasePath}/Alquiler.csv', 'a+') as db:
            db.write(f'{alquiler.__str__()}\n')

    @staticmethod
    def resetAlquilerDb(databasePath):
        try:
            os.remove(f'{databasePath}/Alquiler.csv')
        except:
            pass

    @staticmethod
    def mostrarAlquilerDb(databasePath, filtro=''):
        print('\nTabla Alquiler')
        dataTable = []
        dataTable.append(
            ['Socio', 'Ejemplar', 'Fecha Salida', 'Fecha Entrada'])
        with open(f'{databasePath}/Alquiler.csv', 'r') as db:
            for linea in db.readlines():
                if linea.strip().find(filtro) > -1:
                    dataTable.append(linea.strip().split(';'))
            TableIt.printTable(dataTable, useFieldNames=True)
