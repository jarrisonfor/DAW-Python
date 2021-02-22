from lib.Curso import *
from lib.Alumno import *
from datetime import date

class Fachada():

    def __init__(self):
        self.listaalumnos = []
        self.listacursos = []

    def buscarAlumno(self, dni):
        if len(self.listaalumnos) != 0:
            for alu in self.listaalumnos:
                if alu.getDNI() == dni:
                    return alu
        return None;

    def buscarCurso(self, codigo):
        if len(self.listacursos) != 0:
            for cur in self.listacursos:
                if cur.getCodigo() == codigo:
                    return cur
        return None;

    def matricularAlumnoCurso(self):
        codigo = input("Código del curso: ")
        cursobuscado = self.buscarCurso(int(codigo))
        if cursobuscado != None:
            print(cursobuscado)
            dni = input("DNI del alumno: ")
            alumnobuscado = self.buscarAlumno(dni)
            if alumnobuscado != None:
                print(alumnobuscado)
                cursobuscado.matricular(alumnobuscado)

    def matricularCursoAlumno(self):
        codigo = input("Código del curso: ")
        cursobuscado = self.buscarCurso(int(codigo))
        if cursobuscado != None:
            print(cursobuscado)
            dni = input("DNI del alumno: ")
            alumnobuscado = self.buscarAlumno(dni)
            if alumnobuscado != None:
                print(alumnobuscado)
                alumnobuscado.matricular(cursobuscado)

    def expedirTitulo(self):
        codigo = input("Código del curso: ")
        cursobuscado = self.buscarCurso(int(codigo))
        if cursobuscado != None:
            print(cursobuscado)
            dni = input("DNI del alumno: ")
            alumnobuscado = self.buscarAlumno(dni)
            if alumnobuscado != None:
                print(alumnobuscado)
                certifica = cursobuscado.expedirTitulo(dni)
                if certifica != None:
                    print(certifica)

    def mostrarAlumnos(self):
        if len(self.listaalumnos) != 0:
            for alu in self.listaalumnos:
                print(alu)

    def mostrarCursos(self):
        if len(self.listacursos) != 0:
            for cur in self.listacursos:
                print(cur)

    def crearAlumno(self, nombre, dni, saldo):
        alumnobuscado = self.buscarAlumno(dni)
        if alumnobuscado == None:
            alumnobuscado = Alumno(nombre, dni, saldo)
            self.listaalumnos.append(alumnobuscado)
        else:
            print("\nYa existe un alumno con ese DNI:")
        return alumnobuscado

    def crearCursoPresencial(self, codigo, titulo, fechainicio, fechafin, dias, horas, precio, cupo):

        cursobuscado = self.buscarCurso(codigo)
        inicio = fechainicio.split("/")
        fin = fechafin.split("/")
        i = date(int(inicio[2]),int(inicio[1]),int(inicio[0]))
        f = date(int(fin[2]), int(fin[1]), int(fin[0]))

        if cursobuscado == None:
            cursobuscado = Presencial(codigo, titulo, i, f, dias, horas, precio, cupo)
            self.listacursos.append(cursobuscado)
        else:
            print("\nYa existe un curso con ese Título:")
        return cursobuscado

    def crearCursoOnline(self, codigo, titulo, fechainicio, fechafin, dias, horas, precio):
        cursobuscado = self.buscarCurso(codigo)
        inicio = fechainicio.split("/")
        fin = fechafin.split("/")
        i = date(int(inicio[2]),int(inicio[1]),int(inicio[0]))
        f = date(int(fin[2]), int(fin[1]), int(fin[0]))

        if cursobuscado == None:
            cursobuscado = Online(codigo, titulo, i, f, dias, horas, precio)
            self.listacursos.append(cursobuscado)
        else:
            print("\nYa existe un curso con ese Título:")
        return cursobuscado

    def cargarDatosAlumnos(self, rutafichero):
        correcto = False
        try:
            fd = open(rutafichero, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de libros")
        else:
            for linea in fd:
                divide = linea.split(',')
                self.crearAlumno(divide[0].lstrip(), divide[1].lstrip(), divide[2].lstrip())
            fd.close()
            correcto = True
        return correcto

    def cargarDatosCursosPresenciales(self, rutafichero):
        correcto = False
        try:
            fd = open(rutafichero, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de libros")
        else:
            for linea in fd:
                divide = linea.split(',')
                self.crearCursoPresencial(divide[0].lstrip(), divide[1].lstrip(), divide[2].lstrip(),divide[3].lstrip(), divide[4].lstrip(), divide[5].lstrip(), divide[6].lstrip(), divide[7].lstrip())
            fd.close()
            correcto = True
        return correcto

    def cargarDatosCursosOnline(self, rutafichero):
        correcto = False
        try:
            fd = open(rutafichero, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de libros")
        else:
            for linea in fd:
                divide = linea.split(',')
                nuevocurso = self.crearCursoOnline(divide[0].lstrip(), divide[1].lstrip(), divide[2].lstrip(),divide[3].lstrip(), divide[4].lstrip(), divide[5].lstrip(), divide[6].lstrip())
                for i in range(7,len(divide)):
                    cursoprevio = self.buscarCurso(int(divide[i].lstrip()))
                    if cursoprevio != None:
                        nuevocurso.listacursosprevios.append(cursoprevio)
                    else:
                        print ("No se ha encontrado el curso que es prerrequisito "+divide[i].lstrip())
            fd.close()
            correcto = True
        return correcto

