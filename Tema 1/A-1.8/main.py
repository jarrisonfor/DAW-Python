"""
A-1.8 - Sentencias condiciones (II) - Un segundo después
Desarrollar un programa que solicite la hora, los minutos y los segundos y calcule la hora exactamente un segundo después.

AYUDA:

Si los segundos son menores que 59, entonces incrementamos en 1 el valor de los segundos.
Si estamos en el segundo 59 y los minutos son menores que 59, entonces establecemos el valor de los segundos a 0 e incrementamos en 1 los minutos.
Si estamos en el segundo 59 y en el minuto 59 puede ocurrir dos cosas:
Si estamos en la hora 23, entonces establecemos horas, minutos y segundo a cero.
Si la hora es menor que 23, entonces pondríamos los minutos y los segundos a 0 e incrementaríamos en 1 las horas.
EJECUCIÓN:

--------------------------------

Introduzca la hora: 23

Introduzca los minutos: 59

Introduzca los segundos: 59

---------------------------------
"""

horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

segundos = segundos + 1
if segundos == 60:
    segundos = 0
    minutos = minutos + 1
if minutos == 60:
    minutos = 0
    horas = horas + 1
if horas == 24:
    horas = 0

print(
    f'Serían las {horas}:{minutos}:{segundos} exactamente un segundo después.')
