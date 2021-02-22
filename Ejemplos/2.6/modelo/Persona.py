from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, dni, nombre, apellido, direccion, telefono):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono

    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        self._dni = dni

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def mostrar(self):
        cadena = ""
        cadena += "DNI:"+str(self._dni)+"\n"
        cadena += "Nombre:"+str(self._nombre)+"\n"
        cadena += "Apellido:"+str(self._apellido)+"\n"
        cadena += "Dirección:"+str(self._direccion)+"\n"
        cadena += "Teléfono:"+str(self._telefono)+"\n"
        return cadena

    @abstractmethod
    def __str__(self):
        alinea = '{:<10s}{:<10s}{:<15s}{:<20s}{:<10s}'
        cadena = alinea.format(self._dni, self._nombre, self._apellido, self._direccion, self._telefono)
        return cadena