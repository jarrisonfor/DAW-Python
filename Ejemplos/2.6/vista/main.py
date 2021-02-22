
from modelo.Matricula import *
from modelo.Modulo import *
from datetime import date

a1 = Alumno("12344456H", "Pedro", "Gómez", "Calle Fajardo 1", "111111111", "1", date(1994,12,20))
p = Profesor("54053560h", "Francisco", "Atoche", "Calle Fajardo 1", "111111111", "Funcionario", "Informática")
m1 = Modulo("01", "Programación", p)
m2 = Modulo("02", "Bases de Datos", p) # Al módulo le paso el profesor
m3 = Modulo("03", "Sistemas informáticos", p)

mat1 = Matricula("MAT1", "2020-21", a1)
mat2 = Matricula("MAT2", "2019-20", a1)
mat3 = Matricula("MAT3", "2018-19", a1)

dt1mat1 = DetalleMatricula(9,mat1,m1)
dt2mat1 = DetalleMatricula(8,mat1,m2)
dt3mat1 = DetalleMatricula(7,mat1,m3)

print(a1)
print(a1.imprimirMatriculas())
#print(mat1)