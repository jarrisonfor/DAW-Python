"""
A-1.9 - Sentencias condiciones (III) - Calcular edad a partir de la fecha de nacimiento
Desarrollar un programa que calcule la edad a partir de una fecha de nacimiento.

AYUDA:

La edad la calculamos como la diferencia entre el año actual y el año de nacimiento.
Si el mes actual es menor que el mes de nacimiento, entonces todavía no hemos cumplido.
Si el mes actual es igual al mes de nacimiento y el día actual es menor que el día de nacimiento, entonces todavía no hemos cumplido.
"""

from datetime import date
fecha = input('Fecha Nacimiento en formato 1/1/1990: ').split('/')

diaNacimiento = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))
hoy = date.today()
edad = hoy.year - diaNacimiento.year
if diaNacimiento.month >= hoy.month and diaNacimiento.day > hoy.day:
    edad -= 1

print(edad)
