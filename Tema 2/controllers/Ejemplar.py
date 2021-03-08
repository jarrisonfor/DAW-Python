"""
Donde se usa:
2.9.py
"""

import os

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
        return f'Ejemplar: {self.numeroEjemplar}, {self.estado}'

    @staticmethod
    def saveEjemplarDb(ejemplar, databasePath):
        with open (f'{databasePath}/Ejemplar.csv','a+') as db:
            db.write(f'{ejemplar.__str__()}')

    @staticmethod
    def resetEjemplarDb(databasePath):
        try:
            os.remove(f'{databasePath}/Ejemplar.csv')
        except:
            pass