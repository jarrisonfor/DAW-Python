class Banco():
    def __init__(self, nombre, capital=5200000, direccion=None):
        self.__nombre = nombre
        self.__capital = capital
        self.__direccion = direccion
        self.__listacuentas = []

    def incluir(self, cuentanueva):
        self.__listacuentas.append(cuentanueva)

    def getCapital(self):
        return self.__capital

    def getCuentas(self):
        return self.__listacuentas;

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def __str__(self):
        cadena = "\nNombre: "+str(self.__nombre) + "| Capital: " + str(self.__capital) + "| Dirección: " + str(self.__direccion)
        return cadena

    def mostrarCuentas(self):
        cadena="\n*************************************************"
        for i in range(len(self.__listacuentas)):
            cadena += "\n\t Número CC "+str(i)+": "+str(self.__listacuentas[i].getNCC());
            cadena += "\n\t Saldo: "+str(i)+" "+str(self.__listacuentas[i].getSaldo());
            cadena += "\n\t Cliente: " + str(i) + " " + str(self.__listacuentas[i].getCliente());
            cadena +="\n*************************************************"
        return cadena


