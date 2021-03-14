"""
Donde se usa:
2.9.py
"""

import os
import TableIt
from controllers.Pelicula import Pelicula


class Ejemplar:
    alquileres = []

    def __init__(self, numeroEjemplar, estado, pelicula):
        self.estado = estado
        self.numeroEjemplar = numeroEjemplar
        self.pelicula = pelicula
        pelicula.addEjemplar(self)

    def addAlquiler(self, alquiler):
        self.alquileres.append(alquiler)

    def getEstado(self):
        return self.estado

    def getNumeroEjemplar(self):
        return self.numeroEjemplar

    def getPelicula(self):
        return self.pelicula

    def setEstado(self, estado):
        self.estado = estado

    def setNumeroEjemplar(self, numeroEjemplar):
        self.numeroEjemplar = numeroEjemplar

    def setPelicula(self, pelicula):
        self.pelicula = pelicula

    def __str__(self):
        string = f'{self.numeroEjemplar};{self.estado}'
        if isinstance(self.pelicula, Pelicula):
            string += f';{self.pelicula.getTitulo()}'
        else:
            string += f';{self.pelicula}'
        return string

    @staticmethod
    def saveEjemplarDb(ejemplar, databasePath):
        with open(f'{databasePath}/Ejemplar.csv', 'a+') as db:
            db.write(f'{ejemplar.__str__()}\n')

    @staticmethod
    def resetEjemplarDb(databasePath):
        try:
            os.remove(f'{databasePath}/Ejemplar.csv')
        except:
            pass

    @staticmethod
    def mostrarEjemplarDb(databasePath, filtro=''):
        print('\nTabla Ejemplar')
        dataTable = []
        dataTable.append(['Ejemplar', 'Estado', 'Pelicula'])
        with open(f'{databasePath}/Ejemplar.csv', 'r') as db:
            for linea in db.readlines():
                if linea.strip().find(filtro) > -1:
                    dataTable.append(linea.strip().split(';'))
            TableIt.printTable(dataTable, useFieldNames=True)
