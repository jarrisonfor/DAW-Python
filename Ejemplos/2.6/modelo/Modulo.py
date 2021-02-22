from modelo.Profesor import *

class Modulo(object):
    def __init__(self, codigo, nombre, prof):
        self._codigo = codigo
        self._nombre = nombre
        if isinstance(prof, Profesor):
            self._profesor = prof
            self._profesor.asignar_modulo(self) # Añado a la lista del profesor el módulo
        else:
            raise Exception("No es un objeto de tipo profesor")


    def get_codigo(self):
        return self._codigo

    def asignar_profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self._profesor = profesor
            self._profesor.asignar_modulo(self)
        else:
            print("No estás pasando un objeto de tipo profesor")

    def get_nombre(self):
        return self._nombre

    def get_profesor(self):
        return self._profesor

    def set_codigo(self, c):
        self._codigo = c

    def set_nombre(self, c):
        self._nombre = c

    def set_profesor(self, c):
        self._profesor = c

    def __str__(self):
        cadena=""
        cadena +='{:<25s}{:<25s}{:<60s}'.format(str(self._codigo), str(self._nombre), str(self._profesor.get_nombre()))
        return cadena
