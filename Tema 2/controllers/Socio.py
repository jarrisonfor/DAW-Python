"""
Donde se usa:
2.9.py
"""

from controllers.Persona import Persona
import os
class Socio(Persona):
    alquileres = []
    avalados = []
    aval = ''
    def __init__(self, nacionalidad, nombre, apellido, direccion, dni, telefono, sexo):
        super().__init__(nacionalidad, nombre, apellido, direccion, dni, telefono, sexo)

    def addAlquiler(self, alquiler, aval):
        self.alquileres.append(alquiler)
        self.setAval(aval)
        aval.addAvalado(self)

    def addAvalado(self, avalado):
        self.avalados.append(avalado)

    def getAval(self):
        return self.aval

    def setAval(self, aval):
        self.aval = aval

    def __str__(self):
        string = f'{super().__str__()}'
        if isinstance(self.aval, Socio):
            string += f';{self.aval.getDni()}'
        else:
            string += f';{self.aval}'
        return string

    @staticmethod
    def saveSocioDb(socio, databasePath):
        with open (f'{databasePath}/Socio.csv','a+') as db:
            db.write(f'{socio.__str__()}')

    @staticmethod
    def resetSocioDb(databasePath):
        try:
            os.remove(f'{databasePath}/Socio.csv')
        except:
            pass