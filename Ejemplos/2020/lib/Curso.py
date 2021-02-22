from datetime import *

class Curso():
    def __init__(self, codigo, titulo, inicio, fin, dias, horas, precio):
        self.__codigo = int(codigo)
        self.__titulo = titulo
        self.__inicio = inicio
        self.__fin = fin
        self.__dias = int(dias)
        self.__horas = int(horas)
        self.__precio = int(precio)
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
                if alumno.buscarCursoRealizado(self.__codigo) == None: # Si no se ha hecho expedición
                    alumno.cursosmatriculados.remove(self)
                    alumno.cursosrealizados.append(self)
                    cadena = "\n**********************************************\nD/Da "+alumno.getNombre()+" ha realizado con aprovechamiento el curso "
                    cadena +=str(self.__titulo)+" en la modalidad "+str(self.__class__.__name__)+ " con una duración de "
                    cadena += str(self.__dias * self.__horas)+" horas.\n*************************************************************"
                    return cadena;
        return None;

    def getCodigo(self):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo

    def getPrecio(self):
        return int(self.__precio)

    def __str__(self):
        cadena = str(self.__codigo)+"\t\t\t"+str(self.__titulo)+"\t\t\t"+str(self.__inicio)+"\t\t\t"+str(self.__fin)+"\t\t\t"+str(self.__dias)+"\t\t\t"+str(self.__horas)+"\t\t\t"+str(self.__precio)
        return cadena

    def imprimirMatriculados(self):
        cadena = ""
        for i in range(len(self.alumnosmatriculados)):
            cadena += self.alumnosmatriculados[i].getNombre()+" "+self.alumnosmatriculados[i].getDNI()+" "+str(self.alumnosmatriculados[i].getSaldo())
            if i != len(self.alumnosmatriculados)-1:
                cadena +=", "
        return cadena

    def listadoAlumnosOrdenado(self):
        self.alumnosmatriculados.sort()
        for i in self.alumnosmatriculados:
            print(i)

    def matricular(self, alumno):
        if alumno.getSaldo() >= self.getPrecio():
            if alumno.buscarCursoMatriculado(self.getCodigo()) == None:
                if self.buscarAlumno(alumno.getDNI()) == None:
                    alumno.decrementarSaldo(self.getPrecio())
                    alumno.cursosmatriculados.append(self)
                    self.alumnosmatriculados.append(alumno)
                    self.numalumnosmatriculados += 1
                    return True
        return False
