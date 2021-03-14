from abc import ABC, abstractmethod
from datetime import datetime, date
from clases.Error import CustomError

class Reserva(ABC):
    __codigo = 0
    __usuario = ''
    __numplazas = 0
    __fechareserva = ''
    __viajeasociado = ''

    def __init__(self, codigo, usuario, numplazas, viajeasociado, fechareserva=datetime.now(), ):
        if isinstance(fechareserva, datetime):
            self.__fechareserva = fechareserva
        else:
            fecha = fechareserva.split('/')
            self.__fechareserva = datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
        try:
            if usuario == viajeasociado.getCocheAsociado().getPropietario():
                raise CustomError('el usuario no puede ser el mismo que el propietario')
            if viajeasociado.getCerrado():
                raise CustomError('El viaje esta cerrado')
            if viajeasociado.getFechaSalida() < self.__fechareserva:
                raise CustomError('la fecha de reserva no puede ser posterior a la de salida')
            if viajeasociado.getPlazasDispo() - numplazas < 0:
                raise CustomError('numero de plazas excedido')
        except CustomError as v:
            print(v.getMessage())
            return

        self.__viajeasociado = viajeasociado
        self.__codigo = codigo
        self.__usuario = usuario
        self.__numplazas = numplazas
        self.__viajeasociado.substractPlazas(self.__numplazas)
        self.__viajeasociado.addReserva(self)

    def cambiarPlazas(self, nPlazas):
        self.__viajeasociado.addPlazas(self.__numplazas)
        self.__viajeasociado.substractPlazas(nPlazas)
        self.__numplazas = nPlazas

    def getCodigo(self):
        return self.__codigo
    def getUsuario(self):
        return self.__usuario
    def getNumPlazas(self):
        return self.__numplazas
    def getFechaReserva(self):
        return self.__fechareserva
    def getViajeAsociado(self):
        return self.__viajeasociado

    def cancelarReserva(self):
        self.__viajeasociado.addPlazas(self.__numplazas)
        self.__viajeasociado.quitarReserva(self)

    def __str__(self):
        return f'{self.getCodigo()}, {self.getUsuario()}, {self.getNumPlazas()}, {self.getFechaReserva()}, {self.getViajeAsociado().getRuta()}'