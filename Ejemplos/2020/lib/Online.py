from lib.Curso import *


class Online(Curso):
    def __init__(self, codigo, titulo, inicio, fin, dias, horas, precio):
        super(Online, self).__init__(codigo, titulo, inicio, fin, dias, horas, precio)
        self.listacursosprevios = []

    def comprobarprerrequisitos(self, alumno):
        cont = 0
        for cursosprevios in self.listacursosprevios:
            for cursosalumnorealizado in alumno.cursosrealizados:
                if cursosprevios.getCodigo() == cursosalumnorealizado.getCodigo():
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


    def imprimirPrerrequisitos(self):
        cad =""
        for i in range(len(self.listacursosprevios)):
            cad += self.listacursosprevios[i].getTitulo()
            if i != len(self.listacursosprevios)-1:
                cad +=", "
        return cad

    def __str__(self):
        print("\nCodigo\t\t\tTítulo\t\t\tFecha inicio\t\t\tFecha fin\t\t\tDías\t\t\tHoras\t\tPrecio\t\t\tTipo\t\t\tMatriculados\t\t\tCursos prerrequisitos")
        cadena = super(Online, self).__str__()+"\t\t\t"+"Online"+"\t\t\t"
        cadena += super(Online, self).imprimirMatriculados() + "\t\t\t"+self.imprimirPrerrequisitos()
        return cadena
