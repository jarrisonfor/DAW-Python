
class reparacion(object):

    def __init__(self, fecha, horas, coche, mecanico):
        self.__fecha = fecha
        self.__horas = horas
        self.__coche = coche # Coche implicado en reparación
        self.__mecanico = mecanico # Mecánico que atiende la reparación

    def sethoras(self, horas):
        self._horas = horas

    def gethoras(self):
        return self.__fecha

    def setfecha(self, fecha):
        self._fecha = fecha

    def getfecha(self):
        return self.__fecha

    def setcoche(self, coche):
        self._fecha = coche

    def getcoche(self):
        return self.__coche

    def setmecanico(self, mecanico):
        self._mecanico = mecanico

    def getmecanico(self):
        return self.__mecanico