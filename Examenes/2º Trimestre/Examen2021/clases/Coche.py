from clases.Flexible import Flexible

class Coche:
    __marca = ''
    __totalplazas = 0
    __propietario = ''
    __viajes = []

    def __init__(self, marca, propietario, totalplazas=4):
        self.__marca = marca
        self.__propietario = propietario
        self.__totalplazas = totalplazas

    def addViaje(self, viaje):
        self.__viajes.append(viaje)

    def reducirPlazas(self, nPlazas):
        self.__totalplazas -= nPlazas


    def getMarca(self):
        return self.__marca
    def getTotalplazas(self):
        return self.__totalplazas
    def getPropietario(self):
        return self.__propietario

    def mostrarViajesOrdenados(self):
        self.__viajes.sort()
        for i in self.__viajes:
            print(i.getFechaSalida())

    def mostrarPlazasPorViajeYCancelar(self):
        for i in self.__viajes:
            print(f'{i.getRuta()}: {i.getPlazasDispo()}')
            for x in i.getReservas():
                if isinstance(x, Flexible):
                    x.cancelarReserva()