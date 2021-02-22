from modelo.persona import *


class Cliente(Persona):
    def __init__(self, dni, nombre, apellido, direccion, telefono):
        super(Cliente, self).__init__(dni, nombre, apellido)
        self._direccion = direccion
        self._telefono = telefono
        self._listacoches = [] # Lista de mis coches

    def getdireccion(self):
        return self._direccion

    def setdireccion(self, direccion):
        self._direccion = direccion

    def gettelefono(self):
        return self._telefono

    def settelefono(self, telefono):
        self._telefono = telefono

    def getcoches(self):
        return self._listacoches

    def setcoche(self, coche): # Añadimos un nuevo coche al cliente
        self._listacoches.append(coche)

    def __str__(self):
        cadena = super(Cliente, self).__str__()
        cadena += "Dirección: " + self._direccion + ", "
        cadena += "Teléfono: " + self._telefono + " "
        return cadena