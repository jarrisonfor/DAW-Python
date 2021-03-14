"""
Donde se usa:
2.9.py
"""

from controllers.Persona import Persona
import os
import TableIt


class Director(Persona):
    peliculas = []

    def __init__(self, nacionalidad, nombre, apellido, direccion, dni, telefono, sexo, nombreArtistico, generoCine):
        super().__init__(nacionalidad, nombre, apellido, direccion, dni, telefono, sexo)
        self.nombreArtistico = nombreArtistico
        self.generoCine = generoCine

    def addPelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def getNombreArtistico(self):
        return self.nombreArtistico

    def getGeneroCine(self):
        return self.generoCine

    def setNombreArtistico(self, nombreArtistico):
        self.nombreArtistico

    def setGeneroCine(self, generoCine):
        self.generoCine

    def __str__(self):
        string = f'{super().__str__()}'
        string += f';{self.nombreArtistico};{self.generoCine}'
        return string

    @staticmethod
    def saveDirectorDb(director, databasePath):
        with open(f'{databasePath}/Director.csv', 'a+') as db:
            db.write(f'{director.__str__()}\n')

    @staticmethod
    def resetDirectorDb(databasePath):
        try:
            os.remove(f'{databasePath}/Director.csv')
        except:
            pass

    @staticmethod
    def mostrarDirectorDb(databasePath, filtro=''):
        print('\nTabla Director')
        dataTable = []
        dataTable.append(['Nacionalidad', 'Nombre', 'Apellido', 'Direccion',
                          'Dni', 'Telefono', 'Sexo', 'Nombre Artistico', 'Genero'])
        with open(f'{databasePath}/Director.csv', 'r') as db:
            for linea in db.readlines():
                if linea.strip().find(filtro) > -1:
                    dataTable.append(linea.strip().split(';'))
            TableIt.printTable(dataTable, useFieldNames=True)
