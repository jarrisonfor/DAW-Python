"""
Donde se usa:
2.9.py
"""

import os
import TableIt
from controllers.Actor import Actor
from controllers.Pelicula import Pelicula


class Participacion:
    def __init__(self, actor, pelicula, papelPrincipal):
        self.actor = actor
        self.pelicula = pelicula
        self.papelPrincipal = papelPrincipal
        actor.addParticipacion(self)
        pelicula.addParticipacion(self)

    def getActor(self):
        return self.actor

    def getPelicula(self):
        return self.pelicula

    def setActor(self, actor):
        self.actor = actor

    def setPelicula(self, pelicula):
        self.pelicula = pelicula

    def __str__(self):
        string = ''

        if isinstance(self.actor, Actor):
            string += f'{self.actor.getDni()}'
        else:
            string += f'{self.actor}'

        if isinstance(self.pelicula, Pelicula):
            string += f';{self.pelicula.getTitulo()}'
        else:
            string += f';{self.pelicula}'

        string += f';{self.papelPrincipal}'

        return string

    @staticmethod
    def saveParticipacionDb(participacion, databasePath):
        with open(f'{databasePath}/Participacion.csv', 'a+') as db:
            db.write(f'{participacion.__str__()}\n')

    @staticmethod
    def resetParticipacionDb(databasePath):
        try:
            os.remove(f'{databasePath}/Participacion.csv')
        except:
            pass

    @staticmethod
    def mostrarParticipacionDb(databasePath, filtro=''):
        print('\nTabla Participacion')
        dataTable = []
        dataTable.append(['Actor', 'Pelicula', 'Papel Principal'])
        with open(f'{databasePath}/Participacion.csv', 'r') as db:
            for linea in db.readlines():
                if linea.strip().find(filtro) > -1:
                    dataTable.append(linea.strip().split(';'))
            TableIt.printTable(dataTable, useFieldNames=True)
