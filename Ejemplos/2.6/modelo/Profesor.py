from modelo.Persona import *

class Profesor(Persona):
    def __init__(self, dni, nombre, apellido, direccion, telefono, vinculo, especialidad):
        super(Profesor, self).__init__(dni, nombre, apellido, direccion, telefono)
        self._vinculo = vinculo
        self._especialidad = especialidad
        self._lista_modulos = [] # Lista de módulos de ese profesor en cuestión

    def asignar_modulo(self, modulo):
            self._lista_modulos.append(modulo)
            modulo.set_profesor(self)

    def get_vinculo(self):
        return self._vinculo

    def set_vinculo(self, v):
        self._vinculo = v

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, e):
        self._especialidad = e

    def imprimirModulos(self):
        cadena = ""
        for modulo in self._lista_modulos:
            cadena += str(modulo.get_nombre())+", "
        return cadena

    def mostrarProfesor(self):
        cadena = super(Profesor, self).__str__()
        cadena += "Vínculo: "+str(self._vinculo)+"\n"
        cadena += "Especialidad: "+str(self._especialidad)+"\n"
        cadena += "Módulos: " + str(self.imprimirModulos()) + "\n"
        return cadena

    def __str__(self):
        cadena = super(Profesor, self).__str__()
        alinea = '{:<15s}{:<20s}{:<60s}'
        cadena += alinea.format(self._vinculo, self._especialidad, self.imprimirModulos())
        return cadena