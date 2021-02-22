from lib.banco import *
from lib.cliente import *
from lib.cuenta import *
import math

class Interfaz():
    def __init__(self):
        self.__listabancos = []
        self.__listaclientes = []

    def imprimirBancos(self):
        for i in self.__listabancos:
            print(i)

    def imprimirClientes(self):
        for j in self.__listaclientes:
            print(j)

    def buscarBanco(self, nombre):
        if len(self.__listabancos)!= 0:
            for i in range(len(self.__listabancos)):
                if (self.__listabancos[i].getNombre()== nombre):
                    return self.__listabancos[i]
            return None;

    def buscarCliente(self, dni):
        if len(self.__listaclientes)!= 0:
            for i in range(len(self.__listaclientes)):
                if (self.__listaclientes[i].getDNI()== dni):
                    return self.__listaclientes[i]
            return None;

    def buscarCuenta(self, ncc):
        for i in range(len(self.__listabancos)):
            for j in range(len(self.__listabancos[i].getCuentas())):
                if self.__listabancos[i].getCuentas()[j].getNCC() == ncc:
                    return self.__listabancos[i].getCuentas()[j]
        return None;

    def buscarBancoPosicion(self, nombre):
        if len(self.__listabancos)!= 0:
            for i in range(len(self.__listabancos)):
                if (self.__listabancos[i].getNombre()== nombre):
                    return i
            return -1;

    def buscarClientePosicion(self, dni):
        if len(self.__listaclientes)!= 0:
            for i in range(len(self.__listaclientes)):
                if (self.__listaclientes[i].getDNI()== dni):
                    return i
            return -1;

    def eliminarBanco(self, nombre):
        if len(self.__listabancos)!= 0:
            posicion = self.buscarBancoPosicion(nombre)
            if  posicion != -1:
                self.__listabancos.pop(posicion)
            else:
                print ("No se ha encontrado el banco")
        else:
            print ("La lista de bancos está vacia")

    def eliminarCliente(self, dni):
        if len(self.__listaclientes) != 0:
            posicion = self.buscarClientePosicion(dni)
            if posicion != -1:
                self.__listaclientes.pop(posicion)
            else:
                print("No se ha encontrado el cliente")
        else:
            print("La lista de clientes está vacia")


    def crearBanco(self, nombre, capital=5200000, direccion=None):
        try:
            if self.buscarBanco(nombre) == None:
                nuevobanco = Banco(nombre, capital, direccion)
                if (nuevobanco != None):
                    self.__listabancos.append(nuevobanco)
                else:
                    raise Error("El banco no se ha podido crear.")
            else:
                raise Error("El banco no se puede crear porque ya existe.")

        except Error as err:
            print("ERROR: ", err.mensaje)

    def crearCliente(self, dni, nombre, apellidos):
        try:
            if self.buscarCliente(dni) == None:
                nuevocliente = Cliente(dni, nombre, apellidos)
                if (nuevocliente != None):
                    self.__listaclientes.append(nuevocliente)
                else:
                    raise Error("El cliente no se ha podido crear.")
            else:
                raise Error("El cliente no se puede crear porque ya existe.")

        except Error as err:
            print("ERROR: ", err.mensaje)

    def crearCuenta(self, ncc, saldo, dnicliente, nombrebanco):
        try:
            bancobuscado = self.buscarBanco(nombrebanco)
            clientebuscado = self.buscarCliente(dnicliente)
            if bancobuscado == None or clientebuscado == None:
                raise Error("Error. No se ha encontrado el banco o el cliente")
            else:
                cuentabuscada = self.buscarCuenta(ncc)
                if cuentabuscada != None:
                    raise Error("La cuenta ya existía")
                else:
                    nuevacuenta = Cuenta(ncc, saldo, clientebuscado, bancobuscado)
                    clientebuscado.incluir(nuevacuenta)
                    bancobuscado.incluir(nuevacuenta)
        except Error as err:
            print("ERROR: ", err.mensaje)

    def imprimirCuentas(self):
        for i in range(len(self.__listabancos)):
            for j in range(len(self.__listabancos[i].getCuentas())):
                print(self.__listabancos[i].getCuentas()[j])

    def ingresarDinero(self, ncc, dinero):
        cuentabuscada = self.buscarCuenta(ncc)
        if cuentabuscada == None:
            print("La cuenta no existe")
        else:
            cuentabuscada.actualizarSaldo(math.fabs(int(dinero)))

    def retirarDinero(self, ncc, dinero):
        cuentabuscada = self.buscarCuenta(ncc)
        if cuentabuscada == None:
            print("La cuenta no existe")
        else:
            cuentabuscada.actualizarSaldo(-math.fabs(int(dinero)))

    def cargarDatosBancos(self, ruta):
        correcto = False
        try:
            fd = open(ruta, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de bancos")
        else:
            for linea in fd:
                dir = ""
                divide = linea.split()
                for i in range(2,len(divide)):
                    dir +=(divide[i]+" ")
                self.crearBanco(divide[0],divide[1], dir)
            fd.close()
            correcto = True
        return correcto

    def cargarDatosClientes(self, ruta):
        correcto = False
        try:
            fd = open(ruta, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de clientes")
        else:
            for linea in fd:
                apellidos = ""
                divide = linea.split()
                for i in range(2,len(divide)):
                    apellidos +=(divide[i]+" ")
                self.crearCliente(divide[0],divide[1],apellidos)
            fd.close()
            correcto = True
        return correcto

    def cargarDatosCuentas(self, ruta):
        correcto = False
        try:
            fd = open(ruta, "r")
        except IOError as io:
            print("Error de Entrada/Salida. No se encuentra el fichero de cuentas")
        else:
            for linea in fd:
                divide = linea.split()
                self.crearCuenta(divide[0],divide[1],divide[2],divide[3])
            fd.close()
            correcto = True
        return correcto