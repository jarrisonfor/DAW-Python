class Cliente():
    def __init__(self, DNI, Nombre, Apellido):
        self.__listacuentas = [];
        self.__DNI = DNI
        self.__Nombre = Nombre
        self.__Apellido = Apellido

    def incluir(self, cuentanueva):
        self.__listacuentas.append(cuentanueva)

    def getDNI(self):
        return self.__DNI

    def getCuentas(self):
        return self.__listacuentas

    def getNombre(self):
        return self.__Nombre

    def getApellido(self):
        return self.__Apellido

    def __str__(self):
        return " DNI: "+str(self.__DNI)+" | Nombre: "+str(self.__Nombre)+" | Apellido: "+str(self.__Apellido)

    def mostrarCuentas(self):
        cadena="\n*************************************************"
        for i in range(len(self.__listacuentas)):
            cadena += "\n Número CC: "+str(self.__listacuentas[i].getNCC());
            cadena += "\n Saldo: "+str(self.__listacuentas[i].getSaldo());
            cadena += "\n Banco: "+ str(self.__listacuentas[i].getBanco());
            cadena += "\n*************************************************"
        return cadena


