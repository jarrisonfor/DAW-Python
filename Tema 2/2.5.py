"""
UT3-AEA5 Manejo de Fechas y Horas
1. Escribir un programa que lea por teclado una hora cualquiera y un número n que represente una cantidad en segundos. El programa mostrará la hora que será dentro de los n segundos siguientes. Para ello, hemos de diseñar previamente la clase Hora que dispone de los atributos horas, minutos y segundos. Los valores de los atributos se controlarán mediante métodos. La clase debe disponer de los siguientes métodos:

getHora().
setHora(int hora).
getMinuto().
setMinuto(int minuto).
getSegundo().
setSegundo(int segundo).
void incrementaSegundo().

2. Diseñar una clase Calendario que representa una fecha concreta (año, mes y día). La clase debe disponer de los métodos que se detallan a continuación:

Calendario (int anho, int mes, int dia): que crea un objeto con los datos pasados como parámetros, siempre y cuando, la fecha que representen sea correcta.
incrementarDia(int cantidad): que incrementa la fecha del calendario en el número de días especificados.
incrementarMes(int cantidad): que incrementa la fecha del calendario en el número de meses especificados.
incrementarAnho(int cantidad): que incrementa la fecha del calendario en el número de años especificados, salvo que el año resultante sea el 0 (que no existió).
Mostrar la fecha por consola sobreescribiendo el correspondiente método.
Sobrecargar el operador de comparación "==" para determinar si la fecha invocante y la que se pasa como parámetro son iguales o distintas.
"""

from controllers.Hora import Hora
from controllers.Calendario import Calendario

""" hora = input('Dime una hora con formato <23:59:59> : ')
segundos = int(input('Dime los segundos: ')) """

hora = '23:59:59'
segundos = '1'

ora = Hora(hora, segundos)
print(ora)
ora.setHora(23)
print(ora.getHora())
ora.setMinuto(59)
print(ora.getMinuto())
ora.setSegundo(58)
print(ora.getSegundo())
ora.incrementaSegundo(segundos)
print(ora)

print("\n")

muda = Calendario()
mudada = muda.Calendario()
print(muda)
print(mudada)
muda.incrementarDia(1)
muda.incrementarMes(1)
muda.incrementarAnho(1)
print(muda == mudada)
mudada.incrementarDia(1)
mudada.incrementarMes(1)
mudada.incrementarAnho(1)
print(muda == mudada)