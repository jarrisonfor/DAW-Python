from lib.Alumno import *
from lib.Curso import *
from lib.Online import *
from lib.Presencial import *

from datetime import date

alu = Alumno("Francisco Atoche",55555555)
alu2 = Alumno("Pepito Pérez",55555551)
print(alu)
cur = Presencial("Prueba1", date(2015,12,1), date(2015,12,20), 10, 30, 20, 10)
cur2 = Online("PruebaOnline", date(2015,12,1), date(2015,12,20), 10, 30, 20)
cur2.listacursosprevios.append(cur)

print(cur)
alu.matricular(cur)
alu2.matricular(cur)

#print(alu)

#print(cur.expedirTitulo(55555555))


#alu.matricular(cur2)
print(alu)
print("\n\nListado de alumnos matriculados de forma ordenada")
cur.listadoAlumnosOrdenado()