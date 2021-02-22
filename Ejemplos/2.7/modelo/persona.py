from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self, dni, nombre, apellido):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido

    def getdni(self):
        return self._dni

    def setdni(self, dni):
        self._dni = dni

    def getdni(self):
        return self._dni

    def setdni(self, dni):
        self._dni = dni

    def getapellido(self):
        return self._apellido

    def setapellido(self, apellido):
        self._apellido = apellido

    @abstractmethod
    def __str__(self):
        cadena=""
        cadena+= "DNI: "+ self._dni+ ", "
        cadena += "Nombre: "+ self._nombre+", "
        cadena += "Apellido: "+ self._apellido+", "
        return cadena