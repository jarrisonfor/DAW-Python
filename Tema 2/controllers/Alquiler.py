"""
Donde se usa:
2.9.py
"""

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
        return f'Alquiler: {self.socio.getDni()} alquilo el ejemplar nº {self.ejemplar.getNumeroEjemplar()}'


    @staticmethod
    def saveAlquilerDb(self):
        pass