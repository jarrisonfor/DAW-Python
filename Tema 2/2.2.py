"""
UT2-AEA2 Saldo Cuenta Corriente
Diseñar la clase CuentaCorriente, sabiendo que los datos necesarios son:

saldo
límite de descubierto (dinero que se permite sacar de una cuenta que ya está a cero)
nombre
DNI del titular.

Las operaciones típicas con una cuenta corriente son:

Crear la cuenta: se necesita el nombre y DNI del titular.
El saldo inicial será 0 y el límite de descubierto será de -50 euros.
Sacar dinero: solo se podrá sacar dinero hasta el límite de descubierto. El método debe indicar si ha sido posible llevar a cabo la operación.
Ingresar dinero: se incrementa el saldo.
Mostrar información: muestra la información disponible de la cuenta corriente.


1º Sobrecarga el constructor de la clase CuentaCorriente para que permita:

Crear un constructor que sólo se le pase por parámetro el saldo inicial, no serán necesarios los datos del titular.
Por defecto el límite de descubierto será 0 euros.
Crear un constructor con un saldo inicial, con un límite de descubierto y con el DNI del titular de la cuenta.

Muestra en el programa principal la llamada a cada uno de los constructores y muestra la información que contiene cada uno de los objetos.

2º Modificar la visibilidad  de los atributos de la clase CuentaCorriente para que:

Saldo y limite no sean visibles para otras clases (privado).
Nombre sea público para cualquier clase.
Dni sea privado para cualquier clase.
Realizar modificaciones en el programa principal para comprobar la visibilidad de los atributos.

3º Añadir un atributo que almacene el nombre del banco (que es único) en la clase CuentaCorriente. Diseñar un método que permita modificar el nombre del banco (al que pertenecen todas las cuentas corrientes).

4º Modifica la clase CuentaCorriente para añadir un nuevo atributo que nos indique la fecha y hora del último movimiento de dinero que realizamos, tanto si es una entrada, como si es una salida de dinero. Modifica además el método mostrarInformacion() para comprobar la fecha y hora.
"""

from controllers.CuentaCorriente import CuentaCorriente

cuenta1 = CuentaCorriente(100)
cuenta2 = CuentaCorriente(100, -50, '', '12345678Z')

cuenta2.setBanco('imaginBank')

print(cuenta1)
print('\n')
print(cuenta2)
print('\n')

cuenta1.retirar(100)
cuenta1.ingresar(150)
cuenta1.mostrar()

print('\n')
