from datetime import datetime, date

class Viaje:
    __codviaje = 0
    __ruta = ''
    __fechasalida = ''
    __duracion = 0
    __precioplaza = 0.0
    __plazasdispo = 4
    __reservas = []
    __cerrado = False
    __cocheasociado = ''

    def __init__(self, ruta, fechasalida, duracion, precioplaza, cocheasociado):
        self.__ruta = ruta
        if isinstance(fechasalida, datetime):
            self.__fechasalida = fechasalida
        else:
            fecha = fechasalida.split('/')
            self.__fechasalida = datetime(
                int(fecha[2]), int(fecha[1]), int(fecha[0]))
        self.__duracion = duracion
        self.__precioplaza = precioplaza
        self.__cocheasociado = cocheasociado
        self.__cocheasociado.addViaje(self)
        self.__plazasdispo = self.__cocheasociado.getTotalplazas()

    def addReserva(self, reserva):
        self.__reservas.append(reserva)

    def getCodviaje(self):
        return self.__codviaje
    def getRuta(self):
        return self.__ruta
    def getFechaSalida(self):
        return self.__fechasalida
    def getDuracion(self):
        return self.__duracion
    def getPrecioPlaza(self):
        return self.__precioplaza
    def getPlazasDispo(self):
        return self.__plazasdispo
    def getReservas(self):
        return self.__reservas
    def getCerrado(self):
        return self.__cerrado
    def getCocheAsociado(self):
        return self.__cocheasociado

    def substractPlazas(self, nPlazas):
        self.__plazasdispo -= nPlazas
        if self.__plazasdispo <= 0:
            self.__cerrado = True


    def addPlazas(self, nPlazas):
        self.__plazasdispo += nPlazas
        self.__cerrado = False

    def quitarReserva(self, reserva):
        self.__reservas.remove(reserva)

    def __lt__(self, viaje):
        if self.__fechasalida < viaje.getFechaSalida():
            return True
        return False