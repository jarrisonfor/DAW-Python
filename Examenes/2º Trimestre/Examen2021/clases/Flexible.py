from clases.Reserva import Reserva
from clases.Error import CustomError
from datetime import datetime
class Flexible(Reserva):
    def __init__(self, codigo, usuario, numplazas, viajeasociado, fechareserva=datetime.now()):
        super().__init__(codigo, usuario, numplazas, viajeasociado, fechareserva)

    def cambiarPlazas(self, nPlazas):
        super().cambiarPlazas(nPlazas)

    def __str__(self):
        string = super().__str__()
        return string