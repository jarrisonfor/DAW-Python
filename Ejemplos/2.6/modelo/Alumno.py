from modelo.Persona import *
from datetime import date

class Alumno(Persona):
    def __init__(self, dni, nombre, apellido, direccion, telefono, n_exp, fecha_nac):
        super(Alumno, self).__init__(dni, nombre, apellido, direccion, telefono)
        self._n_exp = n_exp
        self._fecha_nac = fecha_nac
        self._listamatriculas = [] # Lista de matrículas en diferentes cursos académicos

    def incluir_matricula(self, matricula):
        self._listamatriculas.append(matricula)

    def get_fecha(self):
        return self._fecha_nac

    def set_fecha(self, f):
        self._fecha_nac = f

    def get_exp(self):
        return self._n_exp

    def set_exp(self, e):
        self._n_exp = e

    def imprimirMatriculas(self):
        cadena = ""
        for matricula in self._listamatriculas:
            cadena += str(matricula)
        return cadena

    def mostrarAlumno(self):
        cadena = super(Alumno, self).mostrar()
        cadena += "Expediente:" + str(self._n_exp) + "\n"
        cadena += "Fecha nacimiento:" + str(self._fecha_nac) + "\n"
        return cadena

    def __str__(self):
        cadena = super(Alumno, self).__str__()
        alinea = '{:<15s}{:<12s}'
        cadena += alinea.format(self._n_exp, self._fecha_nac.strftime("%d/%m/%Y"))
        return cadena