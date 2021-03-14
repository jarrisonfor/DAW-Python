"""
Donde se usa:
2.9.py
"""
from controllers.Director import Director
import os
import TableIt


class Pelicula:
    director = ''
    ejemplares = []
    participaciones = []

    def __init__(self, titulo, nacionalidad, productora, fecha, director):
        self.titulo = titulo
        self.nacionalidad = nacionalidad
        self.productora = productora
        self.fecha = fecha
        self.director = director
        director.addPelicula(self)

    def addParticipacion(self, participacion):
        self.participaciones.append(participacion)

    def addEjemplar(self, ejemplar):
        self.ejemplares.append(ejemplar)

    def getTitulo(self):
        return self.titulo

    def getNacionalidad(self):
        return self.nacionalidad

    def getProductora(self):
        return self.productora

    def getFecha(self):
        return self.fecha

    def getDirector(self):
        return self.director

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setProductora(self, productora):
        self.productora = productora

    def setFecha(self, fecha):
        self.fecha = fecha

    def setDirector(self, director):
        self.director = director

    def __str__(self):
        string = f'{self.titulo};{self.nacionalidad};{self.productora};{self.fecha}'
        if isinstance(self.director, Director):
            string += f';{self.director.getDni()}'
        else:
            string += f';{self.director}'
        return string

    @staticmethod
    def savePeliculaDb(pelicula, databasePath):
        with open(f'{databasePath}/Pelicula.csv', 'a+') as db:
            db.write(f'{pelicula.__str__()}\n')

    @staticmethod
    def resetPeliculaDb(databasePath):
        try:
            os.remove(f'{databasePath}/Pelicula.csv')
        except:
            pass

    @staticmethod
    def mostrarPeliculaDb(databasePath, filtro=''):
        print('\nTabla Pelicula')
        dataTable = []
        dataTable.append(
            ['Titulo', 'Nacionalidad', 'Productora', 'Fecha', 'Director'])
        with open(f'{databasePath}/Pelicula.csv', 'r') as db:
            for linea in db.readlines():
                if linea.strip().find(filtro) > -1:
                    dataTable.append(linea.strip().split(';'))
            TableIt.printTable(dataTable, useFieldNames=True)
