from lib.Curso import *


class Online(Curso):
    def __init__(self, titulo, inicio, fin, dias, horas, precio):
        super(Online, self).__init__(titulo, inicio, fin, dias, horas, precio)
        self.listacursosprevios = []

    def comprobarprerrequisitos(self, alumno):
        cont = 0
        for cursosprevios in self.listacursosprevios:
            for cursosalumnorealizado in alumno.cursosrealizados:
                if cursosprevios.getTitulo() == cursosalumnorealizado.getTitulo():
                    cont += 1;
                    if cont == len(self.listacursosprevios):
                        return True
        return False

    def matricular(self, alumno):
        if self.comprobarprerrequisitos(alumno):
            if super(Online, self).matricular(alumno):
                print("Se ha matriculado correctamente")
            else:
                print("El alumno no se ha podido matricular")
        else:
            print("No hay plazas libres")
