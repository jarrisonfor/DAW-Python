from lib.Curso import *

class Presencial(Curso):
    def __init__(self, codigo, titulo, inicio, fin, dias, horas, precio, cupo):
        super(Presencial, self).__init__(codigo, titulo, inicio, fin, dias, horas, precio)
        self.cupo = int(cupo)
        self.plazaslibres = int(cupo)

    def matricular(self, alumno):
        if self.plazaslibres > 0:
            if super(Presencial, self).matricular(alumno):
                self.plazaslibres -= 1
            else:
                print("El alumno no se ha podido matricular")
        else:
            print("No hay plazas libres")

    def __str__(self):
        print("\nCodigo\t\t\tTítulo\t\t\tFecha inicio\t\t\tFecha fin\t\t\tDías\t\t\tHoras\t\tPrecio\t\t\tCupo\t\t\tPlazas\t\t\tTipo\t\t\tMatriculados")
        cadena = super(Presencial, self).__str__() +"\t\t\t"+str(self.cupo)+"\t\t\t"+str(self.plazaslibres)+"\t\t\t"+"Presencial"+"\t\t\t"
        cadena +=  super(Presencial, self).imprimirMatriculados()
        return cadena
