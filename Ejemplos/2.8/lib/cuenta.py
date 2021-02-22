import datetime
from lib.error import *
class Cuenta():
    def __init__(self, ncc, saldo, cliente, banco):
        self.__ncc = ncc
        self.__saldo = int(saldo)
        self.__cliente = cliente
        self.__banco = banco
        self.__fechaultmov = datetime.datetime.now()

    def actualizarSaldo(self, saldo):
        try:
            if self.__saldo + int(saldo) < -50:
                raise Error("Límite de descubierto. No se ha realizado la operación.")
        except Error as e:
            print("ERROR: ",e.mensaje)
        else:
                self.__saldo += int(saldo)
                self.__fechaultmov = datetime.datetime.now()
                print("Operación realizada correctamente")

    def getNCC(self):
        return self.__ncc

    def getSaldo(self):
        return self.__saldo

    def getUltimoMovimiento(self):
        return self.__fechaultmov

    def getCliente(self):
        return self.__cliente

    def getBanco(self):
        return self.__banco

    def __str__(self):
        return "\nNúmero cuenta: "+str(self.__ncc)+"\nSaldo: "+str(self.__saldo)+"\nCliente: "+str(self.__cliente)+"\nBanco: "+str(self.__banco)+"\nUltimo movimiento: "+str(self.__fechaultmov)