from lib.Presencial import *
from lib.Online import *
from lib.Error import *

class Alumno():
    def __init__(self, nombre, dni, saldo=100):
        self.__nombre = nombre
        self.__dni = dni
        self.__saldo = saldo
        self.cursosrealizados = []
        self.cursosmatriculados = []

    def getNombre(self):
        return self.__nombre

    def getDNI(self):
        return self.__dni

    def buscarCursoRealizado(self, titulo):
        if len(self.cursosrealizados) != 0:
            for curso in self.cursosrealizados:
                if curso.getTitulo() == titulo:
                    return curso
        return None;

    def buscarCursoMatriculado(self, titulo):
        if len(self.cursosmatriculados) != 0:
            for curso in self.cursosmatriculados:
                if curso.getTitulo() == titulo:
                    return curso
        return None;

    def incrementarSaldo(self, cantidad):
        self.__saldo += cantidad

    def decrementarSaldo(self, cantidad):
        self.__saldo -= cantidad

    def comprobarmatricula(self, curso):
        if self.__saldo >= curso.getPrecio():
            if self.buscarCursoMatriculado(curso.getTitulo()) == None:
                if curso.buscarAlumno(self.getDNI()) == None:
                    self.__saldo -= curso.getPrecio()
                    self.cursosmatriculados.append(curso)
                    curso.alumnosmatriculados.append(self)
                    curso.numalumnosmatriculados += 1
                    return True
        return False

    def comprobarprerrequisitos(self, curso):
        cont = 0
        for cursosprevios in curso.listacursosprevios:
            for cursosalumnorealizado in self.cursosrealizados:
                if cursosprevios.getTitulo() == cursosalumnorealizado.getTitulo():
                    cont += 1;
                    if cont == len(curso.listacursosprevios):
                        return True
        return False

    def matricular(self, curso):
        if isinstance(curso, Presencial):
            try:
                if curso.plazaslibres > 0 and self.comprobarmatricula(curso):
                    curso.plazaslibres -= 1
                    print("El alumno se ha matriculado satisfactoriamente")
                else:
                    raise Error("No hay plazas libres")
            except Error as err:
                print("ERROR: ", err.mensaje)

        elif isinstance(curso, Online):
            try:
                if self.comprobarprerrequisitos(curso) and self.comprobarmatricula(curso):
                    print("El alumno se ha matriculado satisfactoriamente")
                else:
                    raise Error("No se cumple con los prerrequisitos del curso")
            except Error as err:
                print("ERROR: ", err.mensaje)
        else:
            print("El tipo de dato no es un curso Presencial u Online")

    def __str__(self):
        cadena = "\nDNI: "+str(self.__dni)+"\nNombre: "+str(self.__nombre)
        cadena +="\nSaldo: "+str(self.__saldo)
        return cadena

    def __gt__(self, alumno):  # Mayor que
        return self.__dni > alumno.getDNI()

    def __lt__(self, alumno):  # Menor que
        return self.__dni < alumno.getDNI()

    def __ge__(self, alumno):  # Mayor o igual
        return self.__dni >= alumno.getDNI()

    def __le__(self, alumno):  # Menor o igual
        return self.__dni <= alumno.getDNI()