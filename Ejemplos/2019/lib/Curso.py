from datetime import *

class Curso():
    def __init__(self, titulo, inicio, fin, dias, horas, precio):
        self.__titulo = titulo
        self.__inicio = inicio
        self.__fin = fin
        self.__dias = dias
        self.__horas = horas
        self.__precio = precio
        self.alumnosmatriculados = []
        self.numalumnosmatriculados = 0

    def buscarAlumno(self, dni):
        if len(self.alumnosmatriculados) != 0:
            for alu in self.alumnosmatriculados:
                if alu.getDNI() == dni:
                    return alu
        return None;

    def expedirTitulo(self, dni):
        if date.today() > self.__fin: # Si se ha pasado la fecha del curso
            alumno = self.buscarAlumno(dni);
            if  alumno != None: # Si el alumno figura como matriculado
                if alumno.buscarCursoRealizado(self) == None: # Si no se ha hecho expedición
                    alumno.cursosmatriculados.remove(self)
                    alumno.cursosrealizados.append(self)
                    cadena = "D/Da "+alumno.getNombre()+" ha realizado con aprovechamiento el curso "
                    cadena +=str(self.__titulo)+" en la modalidad "+str(self.__class__.__name__)+ " con una duración de "
                    cadena += str(self.__dias * self.__horas)+" horas."
                    return cadena;
        return None;


    def getTitulo(self):
        return self.__titulo

    def getPrecio(self):
        return self.__precio

    def __str__(self):
        cadena = "\nTitulo: "+str(self.__titulo)+"\nFecha inicio: "+str(self.__inicio)
        cadena +="\nFecha fin: "+str(self.__fin)+"\nDías: "+str(self.__dias)
        cadena +="\nHoras: "+str(self.__horas)+"\nPrecio: "+str(self.__precio)
        return cadena

    def listadoAlumnosOrdenado(self):
        self.alumnosmatriculados.sort()
        for i in self.alumnosmatriculados:
            print(i)

    def matricular(self, alumno):
        if alumno.__saldo >= self.getPrecio():
            if alumno.buscarCursoMatriculado(self.getTitulo()) == None:
                if self.buscarAlumno(alumno.getDNI()) == None:
                    alumno.decrementarSaldo(self.getPrecio())
                    alumno.cursosmatriculados.append(self)
                    self.alumnosmatriculados.append(alumno)
                    self.numalumnosmatriculados += 1
                    return True
        return False