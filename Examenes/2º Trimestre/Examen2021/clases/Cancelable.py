from clases.Reserva import Reserva
from clases.Error import CustomError
from datetime import datetime


class Cancelable(Reserva):
    diasantes = 0

    def __init__(self, codigo, usuario, numplazas, viajeasociado, diasantes, fechareserva=datetime.now()):
        super().__init__(codigo, usuario, numplazas, viajeasociado, fechareserva)
        self.diasantes = diasantes

    def cancelarReserva(self):
        try:
            if self.diasantes >= (self.getViajeAsociado().getFechaSalida().day - datetime.now().day):
                raise CustomError('no puedes cancelar una reserva a unos pocos dias de la salida')
        except CustomError as v:
            print(v.getMessage())
            return False
        super().cancelarReserva()
        return True

    def __str__(self):
        string = super().__str__()
        string += f', {self.diasantes}'
        return string

    def getDiasantes(self):
        return self.diasantes