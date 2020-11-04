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
