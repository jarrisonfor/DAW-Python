"""
Donde se usa:
2.9.py
"""

from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nacionalidad, nombre, apellido, direccion, dni, telefono, sexo):
        self.nacionalidad = nacionalidad
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.dni = dni
        self.telefono = telefono
        self.sexo = sexo

    def getNacionalidad(self):
        return self.nacionalidad

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDireccion(self):
        return self.direccion

    def getDni(self):
        return self.dni

    def getTelefono(self):
        return self.telefono

    def getSexo(self):
        return self.sexo

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setDni(self, dni):
        self.dni = dni

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setSexo(self, sexo):
        self.sexo = sexo

    @abstractmethod
    def __str__(self):
        return f'{self.nacionalidad};{self.nombre};{self.apellido};{self.direccion};{self.dni};{self.telefono};{self.sexo}'
