from datetime import date
fecha = input('Fecha Nacimiento en formato 1/1/1990: ').split('/')

diaNacimiento = date(int(fecha[2]), int(fecha[1]), int(fecha[0]))
hoy = date.today()
edad = hoy.year - diaNacimiento.year
if diaNacimiento.month >= hoy.month and diaNacimiento.day > hoy.day:
    edad -= 1

print(edad)
