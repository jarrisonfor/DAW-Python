"""
1. (2,5 puntos) Desarrolla un programa en Python que permita introducir n palabras por teclado hasta introducir “salir”. Posteriormente, concatenará las n palabras en una frase separadas por guión bajo “_”. Finalmente, el programa mostrará por pantalla la frase final convertida completamente a mayúsculas.
Ejemplo:
    Introduzca palabra 1: Hola
    Introduzca palabra 2: cómo
    Introduzca palabra 3: estás
    Introduzca palabra 4: salir
    El resultado es: HOLA_CÓMO_ESTÁS_

2. (2,5 puntos) Una tienda ofrece un descuento del 5% o del 15% sobre el total de las compras realizadas dependiendo del tipo de cliente. Realizar un programa que solicite al usuario un tipo de cliente (identificado por 1 o 2), cantidad de productos comprados, e importe de cada uno. El funcionamiento del algoritmo es el que se detalla a continuación:
    • Se le solicitará al usuario el tipo de cliente.
    • Se le solicitará al usuario la cantidad de productos a calcular.
    • Se le solicitará al usuario que introduzca el importe de cada uno de los productos, hasta tener el precio de todos los productos acumulado.

Finalmente, se mostrará por pantalla la suma total de los productos que llamaremos subtotal y el total de la venta después de aplicar el descuento dependiendo del tipo de cliente.

3. (2,5 puntos) Diseñar un programa para una caja de un supermercado que lea un precio desde el teclado y una cantidad entregada. Se debe comprobar que tanto la cantidad como el precio deben estar por debajo de los 500 euros y obviamente, cantidad debe ser mayor o igual que precio. El programa imprimirá por pantalla el número de billetes y monedas que se deben entregar de cambio, empleando para ello y por simplicidad los siguientes billetes y monedas: 100, 20, 10, 2, 1, 0.20, 0.10 y 0.01 euros.

4. (2,5 puntos) Programar una función recursiva con el siguiente pseudocódigo que permita sumar todos los elementos de un vector.

def sumar (vector, i = ultimaposicion) :
    Si i == 0: # Primera posición
        return (vector[i]) #Caso base cuando llegamos al primer elemento y no podemos continuar.
    Sino:
        return (vector [i] + sumar (vector, i - 1));
"""


def primera():
    texto = []
    i = 1
    respuesta = input('Introduzca palabra 1: ')
    while respuesta != 'salir':
        i += 1
        texto.append(respuesta.upper())
        respuesta = input(f'Introduzca palabra {i}: ')
    print("_".join(texto))


def segunda():
    suma = []
    tipo = int(input('Introduzca tipo cliente: '))
    cantidad = int(input('Introduzca cantidad de productos: '))
    for i in range(cantidad):
        suma.append(int(input(f'Introduzca importe {i + 1}: ')))
    print(f'subtotal: {sum(suma)}€')
    if tipo == 1:
        print(f'total: {sum(suma) * 0.95}€')
    else:
        print(f'total: {sum(suma) * 0.85}€')


def tercera():
    dinero = [100, 20, 10, 2, 1, 0.20, 0.10, 0.01]
    cantidad = int(input('Introduzca cantidad de productos: '))
    importe = float(input(f'Introduzca importe: '))
    total = cantidad * importe
    print('___________________________')
    print(f'Total: {"{:,.2f}".format(total)}€')
    if total >= 500 or cantidad < importe:
        print('___________________________')
        print('Cantidad o importe incorrectos')
        return
    aDevolver = 500 - total
    print(f'Total a devolver: {"{:,.2f}".format(aDevolver)}€')
    print('___________________________')
    aDevolver = round(aDevolver, 2)
    cambio = []
    j = 0
    for i in dinero:
        cambio.append(0)
        while aDevolver >= i:
            cambio[j] += 1
            aDevolver = round(aDevolver - i, 2)
        if cambio[j] > 0:
            if i <= 2:
                print(f'{cambio[j]} moneda/s de {"{:,.2f}".format(i)}€')
            else:
                print(f'{cambio[j]} billete/s de {"{:,.2f}".format(i)}€')
        j += 1


tercera()


def cuarta(vector, i):
    if i == 0:
        return (vector[i])
    else:
        return (vector[i] + cuarta(vector, i - 1))


# otra posibilidad
"""
def cuarta(vector, i=''):
    if i == '':
        i = len(vector) - 1
    if i == 0:
        return (vector[i])
    else:
        return (vector[i] + cuarta(vector, i - 1))
"""
