from modelo.Alumno import Alumno
class Matricula:

    def __init__(self, codigo, anioacad, alum):
        self._codigo = codigo
        self._anioacad = anioacad
        self._detalle_matricula = []
        if isinstance(alum, Alumno):
            self._alumno = alum
            self._alumno.incluir_matricula(self)
        else:
            raise Exception("Esta intentando pasar un objeto que no es un alumno")

    def incluir_detalle(self, d):
        self._detalle_matricula.append(d)

    def imprimirDetallesMatriculas(self):
        cadena = ""
        for detalle in self._detalle_matricula:
            cadena += str(detalle.get_modulo().get_nombre())+" "+str(detalle.get_calificacion())+" ("+str(detalle.get_modulo().get_profesor().get_nombre())+")\n"
        return cadena

    def __str__(self):
        cadena = ""
        cadena += "Código:" + str(self._codigo) + "\n"
        cadena += "Curso:" + str(self._anioacad) + "\n"
        cadena += "Alumno:" + str(self._alumno.get_nombre()+" "+self._alumno.get_apellido()+ "\n")
        cadena += self.imprimirDetallesMatriculas()
        return cadena


class DetalleMatricula(object):
    def __init__(self, calificacion, matricula, modulo):
        self._calificacion = calificacion
        if isinstance(matricula, Matricula):
            self._matricula = matricula # Pertenece a una matrícula
            self._matricula.incluir_detalle(self) # Yo como detalle de matrícula se lo asigno a la matrícula
        else:
            raise Exception("No estás pasando una matrícula válida")
        self._modulo = modulo

    def get_calificacion(self):
        return self._calificacion

    def get_modulo(self):
        return self._modulo

    def __str__(self):
        cadena = ""
        cadena += "Calificación:" + str(self._calificacion) + "\n"
        cadena += "Matrícula:" + str(self._matricula) + "\n"
        cadena += "Módulo:" + str(self._modulo) + "\n"
        return cadena