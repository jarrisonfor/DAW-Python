"""
Donde se usa:
2.9.py
"""

from controllers.Persona import Persona
import os

class Actor(Persona):
    participaciones = []
    def __init__(self, nacionalidad, nombre, apellido, direccion, dni, telefono, sexo, nombreArtistico):
        super().__init__(nacionalidad, nombre, apellido, direccion, dni, telefono, sexo)
        self.nombreArtistico = nombreArtistico

    def addParticipacion(self, participacion):
        self.participaciones.append(participacion)


    def getNombreArtistico(self):
        return self.nombreArtistico

    def setNombreArtistico(self, nombreArtistico):
        self.nombreArtistico = nombreArtistico

    def __str__(self):
        string = f'{super().__str__()}'
        string += f';{self.nombreArtistico}'
        return string


    @staticmethod
    def saveActorDb(actor, databasePath):
        with open (f'{databasePath}/Actor.csv','a+') as db:
            db.write(f'{actor.__str__()}')

    @staticmethod
    def resetActorDb(databasePath):
        try:
            os.remove(f'{databasePath}/Actor.csv')
        except:
            pass