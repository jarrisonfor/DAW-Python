from modelo.Alumno import *
from modelo.Modulo import *
from datetime import date

class Controlador(object):
    def __init__(self):
        self.listaalumnos = [] # Almacenamos los alumnos
        self.listaprofesores = [] # Lista global de profesores
        self.listamodulos = []  # Lista global de módulos

    def cargarDatosAlumnos(self):
        try:
            fd = open("../ficheros/alumnos.txt", encoding="utf8")
        except(FileNotFoundError) as err:
            print("No se ha podido cargar el fichero: ", err)
        else:
            for linea in fd:
                divide = linea.replace("\n", "").split(",")
                fechan = divide[6].lstrip()
                dividefecha = fechan.split("/")
                self.listaalumnos.append(
                    Alumno(divide[0].lstrip(), divide[1].lstrip(), divide[2].lstrip(), divide[3].lstrip(), \
                           divide[4].lstrip(), divide[5].lstrip(), date(int(dividefecha[2]),int(dividefecha[1]),int(dividefecha[0]))))
            fd.close()

    def cargarDatosProfesores(self):
        try:
            fd = open("../ficheros/profesores.txt", encoding="utf8")
        except(FileNotFoundError) as err:
            print("No se ha podido cargar el fichero: ", err)
        else:
            for linea in fd:
                divide = linea.replace("\n", "").split(",")
                self.listaprofesores.append(
                    Profesor(divide[0].lstrip(), divide[1].lstrip(), divide[2].lstrip(), divide[3].lstrip(), \
                           divide[4].lstrip(), divide[5].lstrip(), divide[6].lstrip()))
            fd.close()

    def cargarDatosModulos(self):
        try:
            fd = open("../ficheros/modulos.txt", encoding="utf8")
        except(FileNotFoundError) as err:
            print("No se ha podido cargar el fichero: ", err)
        else:
            for linea in fd:
                divide = linea.replace("\n", "").split(",")
                profesorencontrado = self.buscarProfesorDNI(divide[2].lstrip())
                if profesorencontrado:
                    m = Modulo(divide[0].lstrip(), divide[1].lstrip(), profesorencontrado)
                    self.listamodulos.append(m)
                else:
                    print("No se ha encontrado el profesor. El módulo no se creará")
            fd.close()

    def CrearAlumno(self, dni, nexp, nombre, apellidos, direccion, telefono, fecha_n):
        try:
            dividefecha = fecha_n.split("/")
            a = Alumno(dni, nexp, nombre, apellidos, direccion, telefono, date(int(dividefecha[2]),int(dividefecha[1]),int(dividefecha[0])))
            self.listaalumnos.append(a) # Añadimos el alumno a la lista
        except:
            print("Ha ocurrido un error con alguno de los datos")
            return False
        else:
            return True

    def CrearProfesor(self, dni, nombre, apellidos, direccion, telefono, vinculo, especialidad):
        try:
            p = Profesor(dni, nombre, apellidos, direccion, telefono, vinculo, especialidad)
            self.listaprofesores.append(p) # Añadimos el profesor a la lista
        except:
            print("Ha ocurrido un error con alguno de los datos")
            return False
        else:
            return True

    def CrearModulo(self, codigo, nombre, dniprofesor):
        p = self.buscarProfesorDNI(dniprofesor)
        if p == None:
            print("No existe profesor con ese DNI")
        else:
            m = Modulo(codigo, nombre, p)
            self.listamodulos.append(m)

    def mostrarAlumnos(self):
        alinea = '{:<10s}{:<10s}{:<15s}{:<20s}{:<10s}{:<15s}{:<12s}'
        print(alinea.format("DNI", "Nombre", "Apellidos", "Dirección", "Teléfono", "Expediente", "Fecha de nacimiento"))
        for alumno in self.listaalumnos:
            print(alumno)

    def mostrarProfesores(self):
        alinea = '{:<10s}{:<10s}{:<15s}{:<20s}{:<10s}{:<15s}{:<20s}{:<60s}'
        print(alinea.format("DNI", "Nombre", "Apellidos", "Dirección", "Teléfono", "Vínculo", "Especialidad", "Módulos"))
        for profesor in self.listaprofesores:
            print(profesor)

    def mostrarModulos(self):
        alinea = '{:<25s}{:<25s}{:<60s}'
        print(alinea.format("Código", "Nombre", "Profesor"))
        for modulo in self.listamodulos:
            print(modulo)

    def listarAlumnos(self):
        for alumno in self.listaalumnos:
            print(alumno.get_dni()+" "+alumno.get_exp()+" "+alumno.get_nombre()+" "+alumno.get_apellido())

    def listarProfesores(self):
        for profesor in self.listaprofesores:
            print(profesor.get_dni()+" "+profesor.get_nombre()+" "+profesor.get_apellido())

    def buscarAlumnoDNI(self, dni):
        for alumno in self.listaalumnos:
            if alumno.get_dni() == dni:
                return alumno
        return None

    def buscarProfesorDNI(self, dni):
        for profesor in self.listaprofesores:
            if profesor.get_dni() == dni:
                return profesor
        return None

    def buscarModulo(self, codigo):
        for modulo in self.listamodulos:
            if modulo.get_codigo() == codigo:
                return modulo
        return None

    def buscarAlumnoEXP(self, exp):
        for alumno in self.listaalumnos:
            if alumno.get_exp() == exp:
                return alumno
        return None