"""
Donde se usa:
A-2.2.py

"""
import datetime


class CuentaCorriente:
    __saldo = 0
    __limite = 0
    nombre = ''
    __dni = ''
    __banco = 'La Caixa'
    __fecha = ''

    def __init__(self, saldo=0, limite=0, nombre='', dni=''):
        self.__saldo = saldo
        self.__limite = limite
        self.nombre = nombre
        self.__dni = dni

    def retirar(self, cantidad):
        saldoTemp = self.__saldo
        if saldoTemp - cantidad >= self.__limite:
            self.__saldo -= cantidad
            self.__fecha = datetime.datetime.now()
            return True
        print('Cantidad de retirada sobrepasa los limites')
        return False

    def ingresar(self, cantidad):
        self.__saldo += cantidad
        self.__fecha = datetime.datetime.now()

    def mostrar(self):
        print(f"saldo: {self.__saldo}\nfecha ultimo movimiento: {self.__fecha}")

    def setBanco(self, banco):
        self.__banco = banco

    def __str__(self):
        return f"saldo: {self.__saldo}\nlimite: {self.__limite}\nnombre: {self.nombre}\ndni: {self.__dni}\nbanco: {self.__banco}\nfecha ultimo movimiento: {self.__fecha}"
