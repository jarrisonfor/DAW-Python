from lib.Curso import *

class Presencial(Curso):
    def __init__(self, titulo, inicio, fin, dias, horas, precio, cupo):
        super(Presencial, self).__init__(titulo, inicio, fin, dias, horas, precio)
        self.cupo = cupo
        self.plazaslibres = cupo

    def matricular(self, alumno):
        if self.plazaslibres > 0:
            if super(Presencial, self).matricular(alumno):
                self.plazaslibres -= 1
            else:
                print("El alumno no se ha podido matricular")
        else:
            print("No hay plazas libres")