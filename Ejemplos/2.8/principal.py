from lib.interfaz import *
from lib.banco import *
from lib.cuenta import *
from lib.cliente import *

#try:
fachada = Interfaz()
while True:
    print("\n**********************************")
    print("0. Salir *************************")
    print("1. Crear banco *******************")
    print("2. Eliminar banco ****************")
    print("3. Buscar banco ******************")
    print("4. Mostrar todos los bancos ******")
    print("5. Crear cliente *****************")
    print("6. Mostrar todos los clientes ****")
    print("7. Eliminar un cliente ***********")
    print("8. Crear cuenta ******************")
    print("9. Mostrar todas las cuentas *****")
    print("10. Buscar cliente ***************")
    print("11. Buscar cuenta ****************")
    print("12. Ingresar dinero en cuenta ****")
    print("13. Retirar dinero de cuenta *****")
    print("14. Cargar datos de fichero ******")
    print("**********************************")
    opcion = int(input("Introduce una opción: "))
    if opcion == 0: break;
    if opcion == 1:
        nombre = input("Dime un nombre: ")
        capital = int(input("Dime un capital: "))
        fachada.crearBanco(nombre, capital)
    if opcion == 2:
        nombre = input("Dime un nombre: ")
        fachada.eliminarBanco(nombre)

    if opcion == 3:
        nombre = input("Dime un nombre: ")
        bancobuscado = fachada.buscarBanco(nombre)
        if bancobuscado != None:
            print(bancobuscado)
            print(bancobuscado.mostrarCuentas())
        else:
            print("El banco no ha podido ser encontrado.")
    if opcion == 4:
        fachada.imprimirBancos()

    if opcion == 5:
        dni = input("Dime un DNI: ")
        nombre = input("Dime un nombre: ")
        apellido = input("Dime un apellido: ")
        fachada.crearCliente(dni, nombre, apellido)

    if opcion == 6:
        fachada.imprimirClientes()

    if opcion == 7:
        dni = input("Dime el DNI: ")
        fachada.eliminarCliente(dni)

    if opcion == 8:
        ncc = input("Dime un NCC: ")
        saldoini = int(input("Dime un saldo inicial: "))
        dnicliente = input("Dime un DNI de cliente: ")
        nombrebanco = input("Dime un nombre del banco: ")
        fachada.crearCuenta(ncc, saldoini, dnicliente, nombrebanco)

    if opcion == 9:
        fachada.imprimirCuentas()

    if opcion == 10:
        dni = input("Dime un DNI de cliente: ")
        clientebuscado = fachada.buscarCliente(dni)
        if clientebuscado != None:
            print(clientebuscado)
            print(clientebuscado.mostrarCuentas())
        else:
            print("El banco no ha podido ser encontrado.")

    if opcion == 11:
        ncc = input("Dime un numero de cuenta corriente: ")
        cuentabuscada = fachada.buscarCuenta(ncc)
        if cuentabuscada != None:
            print(cuentabuscada)
        else:
            print("La cuenta no ha podido ser encontrada.")

    if opcion == 12:
        ncc = input("Dime un numero de cuenta corriente: ")
        cuentabuscada = fachada.buscarCuenta(ncc)
        if cuentabuscada != None:
            print(cuentabuscada)
            dinero = input("Dime el dinero a ingresar: ")
            fachada.ingresarDinero(ncc, dinero)
        else:
            print("La cuenta no ha podido ser encontrada.")

    if opcion == 13:
        ncc = input("Dime un numero de cuenta corriente: ")
        cuentabuscada = fachada.buscarCuenta(ncc)
        if cuentabuscada != None:
            print(cuentabuscada)
            dinero = input("Dime el dinero a retirar: ")
            fachada.retirarDinero(ncc, dinero)
        else:
            print("La cuenta no ha podido ser encontrada.")

    if opcion == 14:
        bancos = fachada.cargarDatosBancos("lib/bancos.txt")
        clientes = fachada.cargarDatosClientes("lib/clientes.txt")
        if (bancos and clientes):
            cuentas = fachada.cargarDatosCuentas("lib/cuentas.txt")
            if cuentas:
                print("Se han cargado todos los datos satisfactoriamente")
        else:
            print("Por problemas de integridad, no se han cargado los ficheros");

#except:
    # Comentar la excepción para poder depurar errores
    #print("\nSe ha producido un error desconocido\n")