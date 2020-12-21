"""
A-1.2 - Operaciones aritméticas (I). Convertidor a segundos
Escriba un programa que pida un número de días, horas, minutos y segundos y calcule cuántos segundos son en total.

Convertidor a segundos
Dígame un número de días: 365
Dígame un número de horas: 5
Dígame un número de minutos: 48
Dígame un número de segundos: 45
365 días, 5 horas, 48 minutos y 45 segundos son 31556925 segundos
"""



dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
calculado = segundos + (minutos * 60) + (horas * 3600) + ((dias * 24) * 3600)

print('Convertidor a segundos')
print(f'Dígame un número de días: {dias}')
print(f'Dígame un número de horas: {horas}')
print(f'Dígame un número de minutos: {minutos}')
print(f'Dígame un número de segundos: {segundos}')
print(f'{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos son {calculado} segundos')
