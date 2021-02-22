from modelo.persona import *


class Mecanico(Persona):
    def __init__(self, dni, nombre, apellido, fechac, salario):
        super(Mecanico, self).__init__(dni, nombre, apellido)
        self._fechac = fechac
        self._salario = salario
        self._listareparaciones = [] # Lista de reparaciones que atiende

    def getfechac(self):
        return self._fechac

    def setfechac(self, fechac):
        self._direccion = fechac

    def getsalario(self):
        return self._salario

    def setsalario(self, salario):
        self._salario = salario

    def getreparaciones(self):
        return self._listareparaciones

    def setreparaciones(self, coche):  # Añadimos un nuevo coche al cliente
        self._listareparaciones.append(coche)

    def __str__(self):
        cadena = super(Mecanico, self).__str__()
        cadena += "Fecha contratación: " + self._fechac.strftime("%d/%m/%Y") + ", "
        cadena += "Salario: " + str(self._salario) + " "
        return cadena