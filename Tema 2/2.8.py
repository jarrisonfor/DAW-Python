"""
UT3-AEA8 Diagrama de clases UML - Proyecto Gestión Bancaria
Diseñar la clase CuentaCorriente, sabiendo que los datos necesarios son: saldo, límite de descubierto (dinero que se permite sacar de una cuenta que ya está a cero), nombre y DNI del titular. Las operaciones típicas con una cuenta corriente son:

Crear la cuenta: se necesita el nombre y DNI del titular.
El saldo inicial será 0 y el límite de descubierto será de -50 euros.
Sacar dinero: solo se podrá sacar dinero hasta el límite de descubierto. El método debe indicar si ha sido posible llevar a cabo la operación.
Ingresar dinero: se incrementa el saldo.
Mostrar información: muestra la información disponible de la cuenta corriente.
1º Sobrecarga el constructor de la clase CuentaCorriente para que permita:

Crear un constructor que sólo se le pase por parámetro el saldo inicial, no serán necesarios los datos del titular. Por defecto el límite de descubierto será 0 euros.
Crear un constructor con un saldo inicial, con un límite de descubierto y con el DNI del titular de la cuenta. Muestra en el programa principal la llamada a cada uno de los constructores y muestra la información que contiene cada uno de los objetos.
2º Modificar la visibilidad de la clase CuentaCorriente para que sea visible desde clases externas y la visibilidad de sus atributos para que:

Saldo y limite no sean visibles para otras clases (privado).
Nombre sea público para cualquier clase.
Dni sea privado para cualquier clase.
Realizar modificaciones en el programa principal para comprobar la visibilidad de los atributos.
3º Todas las cuentas corrientes con las que vamos a trabajar pertenecen al mismo banco. Añadir un atributo que almacene el nombre del banco (que es único) en la clase CuentaCorriente. Diseñar un método que permita modificar el nombre del banco (al que pertenecen todas las cuentas corrientes.

4º Modifica la clase CuentaCorriente para añadir un nuevo atributo que nos indique la fecha y hora del último movimiento de dinero que realizamos, tanto si es una entrada, como si es una salida de dinero. Modifica además el método mostrarInformacion() para comprobar la fecha y hora.

5º Diseñar la clase Banca de la que interesa guardar su nombre, capital y la dirección central. Los bancos tienen las siguientes restricciones:

Siempre tienen que tener un nombre, que no pueda ser modificado.
Si no se especifica, todos los bancos tienen un capital por defecto de 5.2 millones de euros al crearse.
El capital y la dirección de un banco son modificables. Modifica la clase CuentaCorriente para que cada una esté vinculada a un objeto de tipo Banca. Escribir los métodos necesarios en la clase CuentaCorriente para gestionar el banco al que pertenece. Existe la posibilidad de que una cuenta corriente no esté vinculada a ningún banco.

"""

