from clases.Coche import Coche
from clases.Viaje import Viaje
from clases.Flexible import Flexible
from clases.Cancelable import Cancelable
from clases.Error import CustomError


coche1 = Coche('Opel Astra', 'Alberto')

viaje1 = Viaje('Arrecife - Haría', '07/03/2021', 40, 2.50, coche1)
viaje2 = Viaje('Arrecife – Playa Honda', '10/03/2021', 10, 1.50, coche1)
viaje3 = Viaje('Haría - Playa Blanca', '11/03/2021', 60, 3.00, coche1)

reserva1 = Flexible(1, 'Pedro', 2, viaje2)
reserva2 = Flexible(2, 'Juan', 2, viaje1, '12/03/2021')
reserva3 = Flexible(3, 'Ana', 1, viaje2)
reserva3.cambiarPlazas(2)
reserva4 = Cancelable(4, 'Enrique', 4, viaje3, 2)
reserva5 = Flexible(5, 'Miguel', 1, viaje2)
reserva3.cambiarPlazas(1)

reserva5 = Flexible(5, 'Miguel', 1, viaje2)
reserva4.cancelarReserva()

reserva6 = Cancelable(6, 'Beatriz', 2, viaje3, 4)
reserva6.cancelarReserva()

"""
ejercicio2
"""
print(reserva1)
print(reserva6)

coche1.mostrarViajesOrdenados()
print()
coche1.mostrarPlazasPorViajeYCancelar()